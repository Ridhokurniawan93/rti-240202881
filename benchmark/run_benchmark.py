"""
run_benchmark.py
Script utama benchmarking DBMS (PostgreSQL vs MySQL).
Mengukur response time query CRUD dengan variasi indexing & optimization.

Usage:
    python run_benchmark.py                          # Run semua kondisi
    python run_benchmark.py --condition C1           # Run kondisi C1 saja
    python run_benchmark.py --condition C1 --volume 100000  # Run C1, volume 100K
"""

import os
import sys
import json
import time
import random
import argparse
import yaml
import psutil
import csv
from datetime import datetime

# ============================================================
# DATABASE CONNECTIONS
# ============================================================
def get_pg_connection(config):
    import psycopg2
    db = config["dbms"]["postgresql"]
    return psycopg2.connect(
        host=db["host"], port=db["port"],
        database=db["database"], user=db["user"], password=db["password"]
    )

def get_mysql_connection(config):
    import mysql.connector
    db = config["dbms"]["mysql"]
    return mysql.connector.connect(
        host=db["host"], port=db["port"],
        database=db["database"], user=db["user"], password=db["password"]
    )

def get_connection(dbms_name, config):
    if dbms_name == "postgresql":
        return get_pg_connection(config)
    elif dbms_name == "mysql":
        return get_mysql_connection(config)
    else:
        raise ValueError(f"DBMS tidak dikenal: {dbms_name}")


# ============================================================
# SCHEMA & DATA LOADING
# ============================================================
def setup_schema(conn, dbms_name):
    """Setup tabel app_playstore."""
    schema_file = "schema_postgres.sql" if dbms_name == "postgresql" else "schema_mysql.sql"
    with open(schema_file, "r") as f:
        schema_sql = f.read()

    cursor = conn.cursor()
    for stmt in schema_sql.split(";"):
        stmt = stmt.strip()
        if stmt and not stmt.startswith("--"):
            try:
                cursor.execute(stmt)
            except Exception as e:
                pass  # Ignore errors from comments/empty statements
    conn.commit()
    cursor.close()
    print(f"  [OK] Schema created for {dbms_name}")


def load_data(conn, dbms_name, csv_path, volume):
    """Load data dari CSV ke database."""
    print(f"  Loading {volume:,} records into {dbms_name}...")
    cursor = conn.cursor()

    with open(csv_path, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        batch = []
        count = 0
        for row in reader:
            # Convert boolean strings
            for bool_field in ["free", "ad_supported", "in_app_purchases", "editors_choice"]:
                row[bool_field] = 1 if row[bool_field] == "True" else 0

            batch.append((
                row["app_name"], row["app_id"], row["category"],
                float(row["rating"]), int(row["rating_count"]), row["installs"],
                int(row["free"]), float(row["price"]), row["currency"],
                row["size"], row["min_android"], row["developer_id"],
                row["released"], row["last_updated"], row["content_rating"],
                int(row["ad_supported"]), int(row["in_app_purchases"]),
                int(row["editors_choice"]), row["scraped_time"]
            ))
            count += 1

            if len(batch) >= 5000:
                insert_batch(conn, dbms_name, cursor, batch)
                batch = []
                if count % 100000 == 0:
                    print(f"    Loaded {count:,} records...")

        if batch:
            insert_batch(conn, dbms_name, cursor, batch)

    conn.commit()
    cursor.close()
    print(f"  [OK] {count:,} records loaded into {dbms_name}")


def insert_batch(conn, dbms_name, cursor, batch):
    """Insert batch data ke database."""
    if dbms_name == "postgresql":
        sql = """INSERT INTO app_playstore
            (app_name, app_id, category, rating, rating_count, installs,
             free, price, currency, size, min_android, developer_id,
             released, last_updated, content_rating, ad_supported,
             in_app_purchases, editors_choice, scraped_time)
            VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
    else:  # mysql
        sql = """INSERT INTO app_playstore
            (app_name, app_id, category, rating, rating_count, installs,
             free, price, currency, size, min_android, developer_id,
             released, last_updated, content_rating, ad_supported,
             in_app_purchases, editors_choice, scraped_time)
            VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
    cursor.executemany(sql, batch)
    conn.commit()


# ============================================================
# INDEX MANAGEMENT
# ============================================================
def apply_indexing(conn, dbms_name, index_type):
    """Terapkan indexing strategy."""
    cursor = conn.cursor()

    # Drop existing indexes first
    try:
        if dbms_name == "postgresql":
            cursor.execute("DROP INDEX IF EXISTS idx_app_id")
            cursor.execute("DROP INDEX IF EXISTS idx_composite")
        else:
            cursor.execute("DROP INDEX idx_app_id ON app_playstore")
    except:
        pass
    try:
        if dbms_name == "postgresql":
            cursor.execute("DROP INDEX IF EXISTS idx_composite")
        else:
            cursor.execute("DROP INDEX idx_composite ON app_playstore")
    except:
        pass
    conn.commit()

    if index_type == "none":
        print(f"  Indexing: none (primary key only)")
    elif index_type == "single":
        sql = "CREATE INDEX idx_app_id ON app_playstore (app_id)"
        cursor.execute(sql)
        conn.commit()
        print(f"  Indexing: single-column on app_id")
    elif index_type == "composite":
        sql = "CREATE INDEX idx_composite ON app_playstore (app_id, category, developer_id)"
        cursor.execute(sql)
        conn.commit()
        print(f"  Indexing: composite on (app_id, category, developer_id)")

    cursor.close()


def clear_cache(conn, dbms_name):
    """Clear DBMS cache untuk cold start."""
    cursor = conn.cursor()
    try:
        if dbms_name == "postgresql":
            cursor.execute("DISCARD ALL")
        else:
            cursor.execute("RESET QUERY CACHE")
    except:
        pass
    conn.commit()
    cursor.close()


# ============================================================
# BENCHMARK QUERIES
# ============================================================
def get_queries(dbms_name, query_version, volume):
    """Return query dict berdasarkan DBMS, versi, dan operasi."""
    limit = min(volume, 10000)

    if query_version == "default":
        return {
            "SELECT": f"SELECT * FROM app_playstore WHERE category = 'GAME' LIMIT {limit}",
            "INSERT": f"""INSERT INTO app_playstore
                (app_name, app_id, category, rating, rating_count, installs,
                 free, price, currency, size, min_android, developer_id,
                 released, last_updated, content_rating, ad_supported,
                 in_app_purchases, editors_choice, scraped_time)
                VALUES ('BenchmarkApp', 'com.bench.app.test', 'GAME', 4.5, 1000,
                        '100K+', 1, 0.0, 'USD', '10M', '8.0 and up',
                        'dev_benchmark', '2024-01-01', '2024-06-01',
                        'Everyone', 0, 0, 0, '2024-06-22 10:00:00')""",
            "UPDATE": "UPDATE app_playstore SET rating = 4.8, last_updated = '2024-06-22' WHERE category = 'GAME' AND id <= 1000",
            "DELETE": "DELETE FROM app_playstore WHERE app_id = 'com.bench.app.test'",
        }
    else:  # optimized
        return {
            "SELECT": f"SELECT app_name, rating, category FROM app_playstore WHERE category = 'GAME' AND app_id LIKE 'com.%' ORDER BY rating DESC LIMIT {limit}",
            "INSERT": f"""INSERT INTO app_playstore
                (app_name, app_id, category, rating, rating_count, installs,
                 free, price, currency, size, min_android, developer_id,
                 released, last_updated, content_rating, ad_supported,
                 in_app_purchases, editors_choice, scraped_time)
                VALUES ('OptApp1', 'com.opt.app.1', 'GAME', 4.9, 5000,
                        '1M+', 1, 0.0, 'USD', '15M', '10.0 and up',
                        'dev_optimized', '2024-01-15', '2024-06-15',
                        'Everyone', 1, 1, 0, '2024-06-22 10:00:00')
                ON CONFLICT DO NOTHING""" if dbms_name == "postgresql" else
                      f"""INSERT IGNORE INTO app_playstore
                (app_name, app_id, category, rating, rating_count, installs,
                 free, price, currency, size, min_android, developer_id,
                 released, last_updated, content_rating, ad_supported,
                 in_app_purchases, editors_choice, scraped_time)
                VALUES ('OptApp1', 'com.opt.app.1', 'GAME', 4.9, 5000,
                        '1M+', 1, 0.0, 'USD', '15M', '10.0 and up',
                        'dev_optimized', '2024-01-15', '2024-06-15',
                        'Everyone', 1, 1, 0, '2024-06-22 10:00:00')""",
            "UPDATE": "UPDATE app_playstore SET rating = 4.9 WHERE app_id IN (SELECT app_id FROM app_playstore WHERE category = 'GAME' LIMIT 100)" if dbms_name == "postgresql" else "UPDATE app_playstore SET rating = 4.9 WHERE category = 'GAME' LIMIT 100",
            "DELETE": "DELETE FROM app_playstore WHERE id IN (SELECT id FROM app_playstore WHERE rating < 1.5 LIMIT 100)" if dbms_name == "postgresql" else "DELETE FROM app_playstore WHERE rating < 1.5 LIMIT 100",
        }


def run_query(conn, dbms_name, sql, operation):
    """Eksekusi 1 query dan ukur response time."""
    cursor = conn.cursor()
    start = time.perf_counter()

    try:
        cursor.execute(sql)
        if operation == "SELECT":
            rows = cursor.fetchall()
            rows_affected = len(rows)
        else:
            rows_affected = cursor.rowcount if cursor.rowcount >= 0 else 0
            conn.commit()
    except Exception as e:
        conn.rollback()
        raise e

    end = time.perf_counter()
    elapsed_ms = (end - start) * 1000
    cursor.close()

    return elapsed_ms, rows_affected


def get_resource_usage():
    """Ambil CPU & memory usage saat ini."""
    return {
        "cpu_usage_percent": psutil.cpu_percent(interval=0.1),
        "memory_usage_mb": round(psutil.virtual_memory().used / (1024 * 1024), 1),
        "memory_percent": psutil.virtual_memory().percent
    }


# ============================================================
# MAIN BENCHMARK LOOP
# ============================================================
def run_single_trial(conn, dbms_name, condition, operation, volume, seed, replication, config):
    """Jalankan 1 trial benchmark."""
    queries = get_queries(dbms_name, condition["query_version"], volume)
    sql = queries[operation]

    # Warmup (tidak dicatat)
    warmup_count = config["experiment"]["warmup_queries"]
    for _ in range(warmup_count):
        try:
            run_query(conn, dbms_name, sql, operation)
        except:
            pass

    # Actual measurement
    resource_before = get_resource_usage()
    response_time_ms, rows_affected = run_query(conn, dbms_name, sql, operation)
    resource_after = get_resource_usage()

    # Calculate throughput
    throughput_qps = 1000.0 / response_time_ms if response_time_ms > 0 else 0

    return {
        "response_time_ms": round(response_time_ms, 3),
        "throughput_qps": round(throughput_qps, 2),
        "rows_affected": rows_affected,
        "resource_before": resource_before,
        "resource_after": resource_after,
    }


def run_experiment(config, condition_filter=None, volume_filter=None):
    """Jalankan seluruh eksperimen."""
    results_dir = config["output"]["results_dir"]
    logs_dir = config["output"]["logs_dir"]
    os.makedirs(results_dir, exist_ok=True)
    os.makedirs(logs_dir, exist_ok=True)

    conditions = config["conditions"]
    if condition_filter:
        conditions = [c for c in conditions if c["id"] == condition_filter]

    volumes = config["dataset"]["volumes"]
    if volume_filter:
        volumes = [v for v in volumes if v == volume_filter]

    operations = config["operations"]
    seeds = config["experiment"]["seeds"]

    total_trials = len(conditions) * len(volumes) * len(operations) * len(seeds)
    current = 0

    print(f"\n{'='*60}")
    print(f"DBMS BENCHMARKING EXPERIMENT")
    print(f"Total trials: {total_trials}")
    print(f"Conditions: {len(conditions)}, Volumes: {len(volumes)}, Operations: {len(operations)}, Seeds: {len(seeds)}")
    print(f"{'='*60}\n")

    all_results = []

    for condition in conditions:
        dbms_name = condition["dbms"]
        cid = condition["id"]

        print(f"\n--- Condition {cid}: {dbms_name} | index={condition['index_type']} | query={condition['query_version']} ---")

        # Connect
        conn = get_connection(dbms_name, config)
        conn.autocommit = False

        # Setup schema
        setup_schema(conn, dbms_name)

        for volume in volumes:
            # Load data
            csv_path = os.path.join(config["dataset"]["data_dir"], f"app_playstore_{volume}.csv")
            if not os.path.exists(csv_path):
                print(f"  [SKIP] Dataset {csv_path} tidak ditemukan. Jalankan generate_data.py terlebih dahulu.")
                continue

            # Reload schema + data untuk setiap volume
            setup_schema(conn, dbms_name)
            load_data(conn, dbms_name, csv_path, volume)

            # Apply indexing
            apply_indexing(conn, dbms_name, condition["index_type"])

            for operation in operations:
                for seed in seeds:
                    current += 1
                    random.seed(seed)

                    # Clear cache sebelum trial
                    clear_cache(conn, dbms_name)

                    print(f"  [{current}/{total_trials}] {cid} | {operation} | vol={volume:,} | seed={seed}", end="")

                    try:
                        result = run_single_trial(
                            conn, dbms_name, condition, operation, volume, seed,
                            seeds.index(seed) + 1, config
                        )

                        # Build log entry
                        log_entry = {
                            "identity": {
                                "run_id": f"run-{cid}-{operation}-{volume}-s{seed}",
                                "timestamp": datetime.now().isoformat(),
                                "condition_id": cid,
                                "dbms": dbms_name,
                                "index_type": condition["index_type"],
                                "query_version": condition["query_version"],
                                "operation": operation,
                                "volume": volume,
                                "seed": seed,
                                "replication": seeds.index(seed) + 1
                            },
                            "configuration": {
                                "config_file": "config.yaml",
                                "dbms_version": f"{dbms_name}",
                                "buffer_pool": "128MB"
                            },
                            "metrics": {
                                "response_time_ms": result["response_time_ms"],
                                "throughput_qps": result["throughput_qps"],
                                "rows_affected": result["rows_affected"]
                            },
                            "metadata": {
                                "cpu_usage_percent": result["resource_after"]["cpu_usage_percent"],
                                "memory_usage_mb": result["resource_after"]["memory_usage_mb"],
                                "execution_status": "success"
                            }
                        }

                        # Save individual JSON
                        trial_dir = os.path.join(results_dir, cid, f"{operation}_{volume}")
                        os.makedirs(trial_dir, exist_ok=True)
                        json_path = os.path.join(trial_dir, f"s{seed}.json")
                        with open(json_path, "w") as f:
                            json.dump(log_entry, f, indent=2)

                        print(f" -> {result['response_time_ms']:.2f} ms")
                        all_results.append(log_entry)

                    except Exception as e:
                        print(f" -> ERROR: {e}")
                        # Log error
                        error_entry = {
                            "identity": {
                                "run_id": f"run-{cid}-{operation}-{volume}-s{seed}",
                                "timestamp": datetime.now().isoformat(),
                                "condition_id": cid,
                                "dbms": dbms_name,
                                "operation": operation,
                                "volume": volume,
                                "seed": seed
                            },
                            "error": str(e),
                            "metadata": {"execution_status": "failed"}
                        }
                        all_results.append(error_entry)

                        # Save error log
                        error_dir = os.path.join(logs_dir, "errors")
                        os.makedirs(error_dir, exist_ok=True)
                        with open(os.path.join(error_dir, f"error-{cid}-{operation}-{volume}-s{seed}.json"), "w") as f:
                            json.dump(error_entry, f, indent=2)

        conn.close()

    # Save compiled results
    compiled_path = os.path.join(results_dir, "all_trials.json")
    with open(compiled_path, "w") as f:
        json.dump(all_results, f, indent=2)

    print(f"\n{'='*60}")
    print(f"EKSPERIMEN SELESAI!")
    print(f"Total trials dijalankan: {len(all_results)}")
    print(f"Hasil tersimpan di: {results_dir}")
    print(f"Compiled results: {compiled_path}")
    print(f"{'='*60}")

    return all_results


# ============================================================
# ENTRY POINT
# ============================================================
def main():
    parser = argparse.ArgumentParser(description="DBMS Benchmarking Runner")
    parser.add_argument("--config", type=str, default="config.yaml", help="Config file")
    parser.add_argument("--condition", type=str, default=None, help="Run specific condition (e.g., C1)")
    parser.add_argument("--volume", type=int, default=None, help="Run specific volume (e.g., 100000)")
    args = parser.parse_args()

    with open(args.config, "r") as f:
        config = yaml.safe_load(f)

    run_experiment(config, condition_filter=args.condition, volume_filter=args.volume)


if __name__ == "__main__":
    main()
