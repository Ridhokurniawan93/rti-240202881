"""
compile_logs.py
Compile semua JSON log hasil benchmarking menjadi CSV + analisis statistik dasar.

Usage:
    python compile_logs.py
    python compile_logs.py --input results/ --output analysis/
"""

import os
import json
import csv
import argparse
import numpy as np
from collections import defaultdict


def find_all_json_files(results_dir):
    """Cari semua file JSON hasil benchmarking."""
    json_files = []
    for root, dirs, files in os.walk(results_dir):
        for f in files:
            if f.endswith(".json") and f != "all_trials.json":
                json_files.append(os.path.join(root, f))
    return sorted(json_files)


def compile_to_csv(json_files, output_csv):
    """Compile JSON logs ke satu CSV file."""
    rows = []
    errors = 0

    for filepath in json_files:
        try:
            with open(filepath, "r") as f:
                data = json.load(f)

            if data.get("metadata", {}).get("execution_status") == "failed":
                errors += 1
                continue

            row = {
                "run_id": data["identity"]["run_id"],
                "condition_id": data["identity"]["condition_id"],
                "dbms": data["identity"]["dbms"],
                "index_type": data["identity"]["index_type"],
                "query_version": data["identity"]["query_version"],
                "operation": data["identity"]["operation"],
                "volume": data["identity"]["volume"],
                "seed": data["identity"]["seed"],
                "replication": data["identity"]["replication"],
                "response_time_ms": data["metrics"]["response_time_ms"],
                "throughput_qps": data["metrics"]["throughput_qps"],
                "rows_affected": data["metrics"]["rows_affected"],
                "cpu_usage_percent": data["metadata"].get("cpu_usage_percent", 0),
                "memory_usage_mb": data["metadata"].get("memory_usage_mb", 0),
                "status": data["metadata"]["execution_status"]
            }
            rows.append(row)
        except Exception as e:
            errors += 1
            print(f"  [WARN] Skip {filepath}: {e}")

    if not rows:
        print("Tidak ada data valid ditemukan!")
        return None

    # Write CSV
    fieldnames = list(rows[0].keys())
    with open(output_csv, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)

    print(f"  Compiled {len(rows)} trials -> {output_csv}")
    if errors:
        print(f"  Skipped {errors} error/failed entries")

    return rows


def basic_statistics(rows):
    """Hitung statistik dasar per kondisi."""
    print(f"\n{'='*70}")
    print(f"RINGKASAN STATISTIK DASAR")
    print(f"{'='*70}")

    # Group by condition + operation + volume
    groups = defaultdict(list)
    for row in rows:
        key = f"{row['condition_id']}|{row['dbms']}|{row['index_type']}|{row['query_version']}|{row['operation']}|{row['volume']}"
        groups[key].append(row["response_time_ms"])

    stats_rows = []
    for key, times in sorted(groups.items()):
        parts = key.split("|")
        arr = np.array(times)
        stats = {
            "condition_id": parts[0],
            "dbms": parts[1],
            "index_type": parts[2],
            "query_version": parts[3],
            "operation": parts[4],
            "volume": int(parts[5]),
            "n": len(arr),
            "mean_ms": round(np.mean(arr), 3),
            "std_ms": round(np.std(arr, ddof=1), 3) if len(arr) > 1 else 0,
            "min_ms": round(np.min(arr), 3),
            "max_ms": round(np.max(arr), 3),
            "cv_percent": round((np.std(arr, ddof=1) / np.mean(arr)) * 100, 2) if len(arr) > 1 and np.mean(arr) > 0 else 0,
        }
        stats_rows.append(stats)

    # Print summary table
    print(f"\n{'Condition':<6} {'DBMS':<12} {'Index':<10} {'Query':<10} {'Op':<8} {'Volume':>10} {'Mean(ms)':>10} {'Std':>8} {'CV%':>6}")
    print(f"{'-'*80}")
    for s in stats_rows:
        print(f"{s['condition_id']:<6} {s['dbms']:<12} {s['index_type']:<10} {s['query_version']:<10} {s['operation']:<8} {s['volume']:>10,} {s['mean_ms']:>10.3f} {s['std_ms']:>8.3f} {s['cv_percent']:>6.2f}")

    # Per-DBMS summary
    print(f"\n{'='*70}")
    print(f"PERBANDINGAN DBMS (rata-rata response time per operasi)")
    print(f"{'='*70}")

    dbms_ops = defaultdict(list)
    for row in rows:
        key = f"{row['dbms']}|{row['operation']}"
        dbms_ops[key].append(row["response_time_ms"])

    print(f"\n{'DBMS':<12} {'Operation':<10} {'Mean(ms)':>12} {'Std':>10} {'Count':>6}")
    print(f"{'-'*55}")
    for key, times in sorted(dbms_ops.items()):
        parts = key.split("|")
        arr = np.array(times)
        print(f"{parts[0]:<12} {parts[1]:<10} {np.mean(arr):>12.3f} {np.std(arr, ddof=1):>10.3f} {len(arr):>6}")

    # Repeatability check
    print(f"\n{'='*70}")
    print(f"REPEATABILTY CHECK (CV < 5% = PASS)")
    print(f"{'='*70}")

    pass_count = 0
    fail_count = 0
    for s in stats_rows:
        status = "PASS" if s["cv_percent"] < 5.0 else "FAIL"
        if status == "PASS":
            pass_count += 1
        else:
            fail_count += 1
            print(f"  [FAIL] {s['condition_id']} {s['operation']} vol={s['volume']:,}: CV={s['cv_percent']:.2f}%")

    print(f"\n  Result: {pass_count} PASS, {fail_count} FAIL dari {len(stats_rows)} grup")

    return stats_rows


def save_stats_csv(stats_rows, output_dir):
    """Simpan statistik ke CSV."""
    if not stats_rows:
        return

    stats_csv = os.path.join(output_dir, "summary_statistics.csv")
    fieldnames = list(stats_rows[0].keys())
    with open(stats_csv, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(stats_rows)
    print(f"\n  Statistik tersimpan di: {stats_csv}")


def main():
    parser = argparse.ArgumentParser(description="Compile benchmarking results")
    parser.add_argument("--input", type=str, default="results/", help="Results directory")
    parser.add_argument("--output", type=str, default="analysis/", help="Output directory")
    args = parser.parse_args()

    os.makedirs(args.output, exist_ok=True)

    print(f"{'='*60}")
    print(f"DBMS Benchmarking - Compile & Analyze Results")
    print(f"Input: {args.input}")
    print(f"Output: {args.output}")
    print(f"{'='*60}")

    # Find JSON files
    json_files = find_all_json_files(args.input)
    print(f"\n  Found {len(json_files)} JSON files")

    if not json_files:
        print("  Tidak ada file JSON ditemukan. Jalankan run_benchmark.py terlebih dahulu.")
        return

    # Compile to CSV
    output_csv = os.path.join(args.output, "all_trials.csv")
    rows = compile_to_csv(json_files, output_csv)

    if rows:
        # Basic statistics
        stats = basic_statistics(rows)
        save_stats_csv(stats, args.output)

    print(f"\n{'='*60}")
    print(f"ANALISIS SELESAI")
    print(f"CSV data: {os.path.join(args.output, 'all_trials.csv')}")
    print(f"CSV stats: {os.path.join(args.output, 'summary_statistics.csv')}")
    print(f"Selanjutnya: gunakan all_trials.csv untuk ANOVA di WS-12")
    print(f"{'='*60}")


if __name__ == "__main__":
    main()
