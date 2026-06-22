# WS-10: Experiment Execution & Data Collection

> **Bab 10 — Eksekusi Eksperimen & Pengumpulan Data**

---

## Ringkasan Materi

### Experiment Execution Pipeline

```
Design → Execution Plan → Controlled Execution → Data Collection → Data Logging → Dataset for Analysis
```

### Multiple Run = Non-Negotiable

Single run **tidak pernah cukup** untuk klaim ilmiah. Minimum 5-10 run per skenario dengan seed berbeda. Multiple run menghasilkan:
- Mean, std, confidence interval
- Distribusi hasil → uji statistik
- Variabilitas → error bar di grafik

### Execution Plan

Setiap eksperimen harus memiliki plan sebelum eksekusi:
- Daftar skenario
- Jumlah run per skenario
- Random seed per run (pre-determined!)
- Urutan eksekusi (randomisasi/counterbalancing)
- Pre-execution checklist

### Data Logging Komprehensif

Setiap run menghasilkan log terstruktur:
1. **Identitas** — Run ID, timestamp, skenario
2. **Konfigurasi** — Semua parameter, seed, code version
3. **Hasil** — Semua metrik, output detail
4. **Metadata** — Waktu eksekusi, resource usage, warning/error

Format: CSV/JSON/database — **bukan stdout yang di-copy-paste**.

### Engineering vs Research Execution

| Aspek | Engineering | Research |
|-------|-----------|---------|
| Run | Sekali (deploy) | Multiple (min 5-10, seed berbeda) |
| Logging | Error log, access log | Semua parameter, metrik, metadata |
| Anomali | Bug → fix → redeploy | Investigasi → dokumentasi → analisis |
| Urutan | Tidak penting | Bisa bias — perlu randomisasi |

### Anomali = Dokumentasi, Bukan Hapus

Run gagal/anomali tidak boleh dihapus tanpa dokumentasi. Bisa jadi:
- **Bug** → fix & re-run (dokumentasikan!)
- **Batas kemampuan metode** → DNF = temuan
- **Data yang bias** jika hanya simpan run "berhasil"

### Jebakan Kognitif

1. "Satu angka cukup" → tanpa distribusi, tidak bisa diuji
2. "Seed tidak penting" → bahkan algoritma deterministik bisa dipengaruhi library stokastik
3. "Run gagal langsung hapus" → kehilangan temuan potensial
4. "Semua run harus hari ini" → thermal throttling, fatigue

---

## Template A.10 — Execution Plan & Data Log

```
EXECUTION PLAN

| Run # | Skenario | Seed | Parameter | Status | Waktu | Output File |
|-------|----------|------|-----------|--------|-------|-------------|
| 1     |          |      |           |        |       |             |
| 2     |          |      |           |        |       |             |
| 3     |          |      |           |        |       |             |
| ...   |          |      |           |        |       |             |

Jumlah runs per skenario : ____
Total runs               : ____

DATA LOG (per run):
  Run ID    : ____________________
  Timestamp : ____________________
  Skenario  : ____________________
  Input     : ____________________
  Output    : ____________________
  Anomali   : ____________________
  Catatan   : ____________________
```

---

## Latihan 1 — Execution Plan

Susun execution plan untuk eksperimen Anda. Tentukan skenario, jumlah run, dan seed sebelum eksekusi.

| Run # | Skenario | Seed | Parameter Kunci | Status |
|-------|----------|------|----------------|--------|
| 1 | Tradisional | 42 | employee_count=50, salary_components=8, deduction_types=5, seed=42 | Planned |
| 2 | Tradisional | 123 | employee_count=50, salary_components=8, deduction_types=5, seed=123 | Planned |
| 3 | Tradisional | 456 | employee_count=50, salary_components=8, deduction_types=5, seed=456 | Planned |
| 4 | XP Method | 42 | employee_count=50, salary_components=8, deduction_types=5, seed=42 | Planned |
| 5 | XP Method | 123 | employee_count=50, salary_components=8, deduction_types=5, seed=123 | Planned |
| 6 | XP Method | 456 | employee_count=50, salary_components=8, deduction_types=5, seed=456 | Planned |

**Total skenario:** 2 (Tradisional, XP)
**Run per skenario:** 3
**Total run keseluruhan:** 6

**Urutan Eksekusi (untuk menghindari order bias):**
```
Randomized execution order:
  Trial 1: Run 4 (XP, seed=42)
  Trial 2: Run 1 (Tradisional, seed=42)
  Trial 3: Run 5 (XP, seed=123)
  Trial 4: Run 2 (Tradisional, seed=123)
  Trial 5: Run 6 (XP, seed=456)
  Trial 6: Run 3 (Tradisional, seed=456)
  
  [Atau bisa alternating jika ingin konsistensi hardware thermal]
```

**Dataset untuk semua run:**
- Source: `data/employees.csv` (50 pegawai Politeknik Ganesha Guru)
- Checksum: SHA256 untuk verifikasi integritas
- Snapshot date: Januari 2024 (fixed, di-version control)
- Size: ~5-10 KB (kecil, dibaca ke memory)

---

## Latihan 2 — Data Log Terstruktur

Desain format data log untuk eksperimen Anda. Tentukan field apa saja yang akan dicatat.

**Identitas:**
| Field | Contoh | Tipe |
|-------|--------|------|
| Run ID | run-001 | string |
| Timestamp | 2026-01-15T10:30:00Z | datetime |
| Skenario | Tradisional / XP | enum |
| Trial Number | 1 / 2 / 3 | integer |

**Konfigurasi:**
| Field | Contoh | Tipe |
|-------|--------|------|
| Seed | 42 | integer |
| Code version | commit-abc1234 | string |
| Config file | config-v1.0.yaml | string |
| Database version | PostgreSQL 13.x | string |
| Dataset checksum | sha256:def456... | string |

**Hasil (Metrik Utama):**
| Metrik | Tipe Data | Range Valid | Satuan |
|--------|----------|-------------|--------|
| Processing time | float | > 0 | menit |
| Accuracy percentage | float | 0.0 - 100.0 | persen (%) |
| Error count | integer | ≥ 0 | jumlah error |
| User satisfaction score | float | 1.0 - 5.0 | skala Likert |

**Metadata (Resource & System):**
| Field | Contoh | Tipe |
|-------|--------|------|
| CPU usage | 65.3 | persen |
| Memory usage | 4.2 | GB |
| CPU temperature | 72 | Celsius |
| Execution status | success / warning / failed | enum |
| Notes | Thermal throttling detected at 15:45 | string |

**Format output:** [x] JSON / [ ] CSV / [ ] Database / [ ] Lainnya: ____

**Template JSON per run:**
```json
{
  "identity": {
    "run_id": "run-001",
    "timestamp": "2026-01-15T10:30:00Z",
    "scenario": "traditional",
    "trial_number": 1
  },
  "configuration": {
    "seed": 42,
    "code_version": "commit-abc1234",
    "config_file": "config-v1.0.yaml",
    "database_version": "PostgreSQL 13.x",
    "dataset_checksum": "sha256:def456..."
  },
  "metrics": {
    "processing_time_minutes": 12.4,
    "accuracy_percentage": 97.5,
    "error_count": 1,
    "user_satisfaction_score": 3.2
  },
  "metadata": {
    "cpu_usage_percent": 65.3,
    "memory_usage_gb": 4.2,
    "cpu_temperature_celsius": 72,
    "execution_status": "success",
    "notes": "Run completed without issues"
  }
}
```

**Compilation strategy:**
- Per run: JSON file di `logs/run-001.json`, `logs/run-002.json`, ... `logs/run-006.json`
- Final analysis: Python script `compile_logs.py` → `results/all_runs.csv` untuk statistical analysis

---

## Latihan 3 — Anomaly Protocol

Rencanakan bagaimana menangani anomali. Untuk setiap jenis, tentukan langkah yang diambil.

| Jenis Anomali | Contoh | Tindakan | Dokumentasi |
|---------------|--------|----------|-------------|
| **Run gagal (crash)** | Database connection timeout / OOM exception | 1. Catat error message lengkap di log 2. Dokumentasi kondisi saat crash (CPU%, temp, memory%) 3. Reduce parameter (misal: batch_size lebih kecil) 4. Re-run dengan parameter adjusted | Log file: `logs/run-001-crash.txt` |
| **Hasil ekstrem (outlier)** | Processing time = 2 menit padahal baseline 8+ menit | 1. Jangan langsung hapus 2. Investigasi: cache hit? thermal throttling? CPU usage? 3. Re-run dengan fresh cache 4. Jika konsisten ekstrem = finding yang valid | `logs/run-XXX-outlier-investigation.md` |
| **Waktu eksekusi anomali** | Trial 2 jauh lebih lama (15 menit vs 8 menit pada trial 1) | 1. Check CPU temperature (throttling?) 2. Check background processes (update, indexing?) 3. Monitor disk I/O 4. Catat kondisi lingkungan (cooling, room temp) | Resource log: `logs/run-XXX-resource.csv` |
| **Inkonsistensi dengan run lain** | Seed sama tapi hasil berbeda > 5% variance | 1. Verifikasi seed di kode (bukan hardcoded random) 2. Check database state (cache bersih?) 3. Verifikasi config file (sama untuk semua run?) 4. Check library version (NumPy, pandas, seed behavior) | Config verification: `logs/verify-seed-setup.txt` |
| **Data integrity issue** | Dataset checksum tidak match | 1. Stop eksekusi 2. Verifikasi dataset file (corrupted?) 3. Re-download dataset dari source 4. Catat perubahan apa saja | Integrity log: `logs/dataset-integrity-check.json` |

**Prinsip Anomaly Handling:**
```
Detect → Investigate → Document → Decide → Execute

Detect:   Monitor selama run, catat anomali real-time
Investigate: Jangan assume, cari root cause
Document: Tulis lengkap di anomaly log (bukan deleted!)
Decide:   Re-run? Proceed? Report as finding?
Execute:  Jalankan keputusan, log hasilnya
```

**Jenis anomali yang TIDAK boleh dihapus:**
- ❌ "Run gagal → langsung delete log"
- ❌ "Hasil outlier → re-run tanpa dokumentasi yang pertama"
- ❌ "Sudah banyak data, tidak perlu catat anomali kecil"

**Semua anomali harus:**
- ✅ Dicatat di `logs/anomalies.md`
- ✅ Masuk final report (bukan hidden)
- ✅ Dianalisis dampaknya ke kesimpulan

---

## Refleksi

> Pernahkah Anda melaporkan hasil riset/tugas dari single run? Apa risikonya? Bagaimana multiple run mengubah kepercayaan terhadap hasil?

**Pengalaman sebelumnya:**
> Single run pada project akademis sebelumnya sering menghasilkan overconfidence — misal: "Algoritma A accuracy 92% lebih baik dari B" padahal itu hanya 1 eksekusi. Risiko: Kesimpulan tidak robust, bisa disebabkan random seed lucky, cache state, atau specific data point.

**Yang akan dilakukan berbeda:**
> Sekarang melakukan 3 runs per skenario dengan seed berbeda untuk mendapatkan mean ± std. Ini memberikan confidence interval & variabilitas yang lebih realistis. Jika hasil 3 runs konsisten (std kecil) → temuan lebih trustworthy. Jika ada outlier → investigasi alih-alih dihapus → menghasilkan insight tambahan tentang edge case atau limitation metode.

**Rencana Dokumentasi Eksekusi:**
1. Semua 6 runs dijalan sesuai execution plan (random order untuk hindari order bias)
2. Setiap run menghasilkan JSON log terstruktur di `logs/run-XXX.json`
3. Semua anomali dicatat di `logs/anomalies.md` (TIDAK DIHAPUS)
4. Final compilation: `python compile_logs.py` → `results/all_runs.csv`
5. Data ready untuk ws-11 (validation) & ws-12 (analysis)
