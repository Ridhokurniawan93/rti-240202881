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
- Distribusi hasil → uji statistik (ANOVA, Kruskal-Wallis)
- Variabilitas → error bar di grafik, coefficient of variation

### Execution Plan

Setiap eksperimen harus memiliki plan sebelum eksekusi:
- Daftar skenario (8 kondisi × 4 CRUD × 5 volume)
- Jumlah replikasi per skenario (minimal 5 — sesuai power analysis WS-07)
- Random seed per replikasi (pre-determined!)
- Urutan eksekusi (randomisasi/counterbalancing untuk menghindari order bias)
- Pre-execution checklist

### Data Logging Komprehensif

Setiap run menghasilkan log terstruktur:
1. **Identitas** — Run ID, timestamp, kondisi eksperimen
2. **Konfigurasi** — Semua parameter, seed, DBMS version, config version
3. **Hasil** — Response time (ms), throughput (QPS) per operasi CRUD
4. **Metadata** — CPU usage, memory usage, CPU temperature, Docker stats, warning/error

Format: JSON terstruktur — **bukan stdout yang di-copy-paste**.

### Engineering vs Research Execution

| Aspek | Engineering | Research |
|-------|-----------|---------|
| Run | Sekali (deploy) | Multiple (min 5, seed berbeda) |
| Logging | Error log, access log | Semua parameter, metrik, metadata |
| Anomali | Bug → fix → redeploy | Investigasi → dokumentasi → analisis |
| Urutan | Tidak penting | Bisa bias — perlu randomisasi |

### Anomali = Dokumentasi, Bukan Hapus

Run gagal/anomali tidak boleh dihapus tanpa dokumentasi. Bisa jadi:
- **Bug** → fix & re-run (dokumentasikan!)
- **Batas kemampuan DBMS** → OOM pada volume 1M dengan RAM 8 GB = temuan
- **Data yang bias** jika hanya simpan run "berhasil"

### Jebakan Kognitif

1. "Satu angka cukup" → tanpa distribusi, tidak bisa diuji statistik
2. "Seed tidak penting" → data generation dengan Faker bergantung pada seed
3. "Run gagal langsung hapus" → kehilangan temuan tentang limitasi DBMS
4. "Semua run harus hari ini" → thermal throttling pada laptop, fatigue hardware

---

## Template A.10 — Execution Plan & Data Log

```
EXECUTION PLAN

| Run # | Skenario | Seed | Parameter | Status | Waktu | Output File |
|-------|----------|------|-----------|--------|-------|-------------|
| 1     |          |      |           |        |       |             |
| 2     |          |      |           |        |       |             |
| ...   |          |      |           |        |       |             |

Jumlah replikasi per sel : 5
Total runs               : 800 (8 kondisi × 4 CRUD × 5 volume × 5 replikasi)

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

**8 Kondisi Eksperimen (dari WS-07):**

| ID | DBMS | Indexing | Optimization |
|----|------|----------|-------------|
| C1 | PostgreSQL | none | default |
| C2 | PostgreSQL | single | default |
| C3 | PostgreSQL | composite | default |
| C4 | PostgreSQL | composite | optimized |
| C5 | MySQL | none | default |
| C6 | MySQL | single | default |
| C7 | MySQL | composite | default |
| C8 | MySQL | composite | optimized |

**Matriks Eksekusi per Kondisi:**

| Variasi | Jumlah |
|---------|--------|
| Operasi CRUD | 4 (SELECT, INSERT, UPDATE, DELETE) |
| Volume data | 5 (50K, 100K, 250K, 500K, 1M) |
| Replikasi | 5 (seed: 42, 123, 456, 789, 1024) |

**Total per kondisi:** 4 × 5 × 5 = 100 trial
**Total keseluruhan:** 8 × 100 = **800 trial**

**Execution Plan (per batch — dikelompokkan per DBMS untuk efisiensi):**

| Batch | Kondisi | Operasi | Volume | Replikasi | Seed | Status |
|-------|---------|---------|--------|-----------|------|--------|
| B1 | C1: PG, none, default | SELECT, INSERT, UPDATE, DELETE | 50K, 100K, 250K, 500K, 1M | 5× | 42, 123, 456, 789, 1024 | Planned |
| B2 | C2: PG, single, default | SELECT, INSERT, UPDATE, DELETE | 50K, 100K, 250K, 500K, 1M | 5× | 42, 123, 456, 789, 1024 | Planned |
| B3 | C3: PG, composite, default | SELECT, INSERT, UPDATE, DELETE | 50K, 100K, 250K, 500K, 1M | 5× | 42, 123, 456, 789, 1024 | Planned |
| B4 | C4: PG, composite, optimized | SELECT, INSERT, UPDATE, DELETE | 50K, 100K, 250K, 500K, 1M | 5× | 42, 123, 456, 789, 1024 | Planned |
| B5 | C5: MySQL, none, default | SELECT, INSERT, UPDATE, DELETE | 50K, 100K, 250K, 500K, 1M | 5× | 42, 123, 456, 789, 1024 | Planned |
| B6 | C6: MySQL, single, default | SELECT, INSERT, UPDATE, DELETE | 50K, 100K, 250K, 500K, 1M | 5× | 42, 123, 456, 789, 1024 | Planned |
| B7 | C7: MySQL, composite, default | SELECT, INSERT, UPDATE, DELETE | 50K, 100K, 250K, 500K, 1M | 5× | 42, 123, 456, 789, 1024 | Planned |
| B8 | C8: MySQL, composite, optimized | SELECT, INSERT, UPDATE, DELETE | 50K, 100K, 250K, 500K, 1M | 5× | 42, 123, 456, 789, 1024 | Planned |

**Total batch:** 8
**Trial per batch:** 100 (4 CRUD × 5 volume × 5 replikasi)
**Total trial keseluruhan:** 800

**Urutan Eksekusi (untuk menghindari order bias & thermal bias):**
```
Urutan batch di-randomize antar DBMS (counterbalanced):
  Sesi 1:  B1 (PG, none, default)       → istirahat 10 menit
  Sesi 2:  B5 (MySQL, none, default)     → istirahat 10 menit
  Sesi 3:  B2 (PG, single, default)      → istirahat 10 menit
  Sesi 4:  B6 (MySQL, single, default)   → istirahat 10 menit
  Sesi 5:  B3 (PG, composite, default)   → istirahat 10 menit
  Sesi 6:  B7 (MySQL, composite, default) → istirahat 10 menit
  Sesi 7:  B4 (PG, composite, optimized) → istirahat 10 menit
  Sesi 8:  B8 (MySQL, composite, optimized) → istirahat 10 menit

  Dalam setiap batch, urutan CRUD di-randomize:
    Replikasi 1 (seed=42):   DELETE, SELECT, INSERT, UPDATE
    Replikasi 2 (seed=123):  INSERT, UPDATE, DELETE, SELECT
    Replikasi 3 (seed=456):  SELECT, DELETE, UPDATE, INSERT
    Replikasi 4 (seed=789):  UPDATE, INSERT, SELECT, DELETE
    Replikasi 5 (seed=1024): SELECT, INSERT, DELETE, UPDATE

  Volume diurutkan ascending (50K → 1M) untuk efisiensi load data.
```

**Pre-execution Checklist:**
- [ ] Docker container PostgreSQL berjalan dan healthy
- [ ] Docker container MySQL berjalan dan healthy
- [ ] Dataset tergenerate untuk semua volume (checksum terverifikasi)
- [ ] Config.yaml ter-load dan parameter sesuai batch
- [ ] DBMS cache di-clear sebelum batch baru
- [ ] Tidak ada background process (antivirus, Windows Update, Search Indexer)
- [ ] Laptop tercolok ke power adapter, power plan = "Best Performance"
- [ ] Cooling pad aktif, CPU temperature < 50°C sebelum mulai
- [ ] Hanya 1 DBMS container aktif per batch (stop yang lain untuk menghemat RAM 8 GB)

**Dataset untuk semua run:**
- Source: Dataset sintetis Faker (seed=42), skema 19 kolom (Google Playstore-like)
- Volume: 50.000, 100.000, 250.000, 500.000, 1.000.000 record
- Checksum: SHA256 per file volume (dicatat sebelum eksekusi)
- Format: CSV, di-load ke database via COPY (PostgreSQL) / LOAD DATA (MySQL)

---

## Latihan 2 — Data Log Terstruktur

Desain format data log untuk eksperimen Anda. Tentukan field apa saja yang akan dicatat.

**Identitas:**
| Field | Contoh | Tipe |
|-------|--------|------|
| Run ID | run-B1-SELECT-100K-r3 | string |
| Timestamp | 2026-06-22T10:30:00Z | datetime |
| Batch | B1 | string |
| Condition ID | C1 (PG, none, default) | string |
| Operation | SELECT / INSERT / UPDATE / DELETE | enum |
| Volume | 100000 | integer |
| Replication | 3 | integer |

**Konfigurasi:**
| Field | Contoh | Tipe |
|-------|--------|------|
| Seed | 456 | integer |
| Code version | commit-abc1234 | string |
| Config file | config-v1.0.yaml | string |
| PostgreSQL version | 16.3 | string |
| MySQL version | 8.0.38 | string |
| Dataset checksum (100K) | sha256:a1b2c3... | string |
| Index type | none / single / composite | enum |
| Query version | default / optimized | enum |

**Hasil (Metrik Utama):**
| Metrik | Tipe Data | Range Valid | Satuan |
|--------|----------|-------------|--------|
| Response time | float | > 0 | milidetik (ms) |
| Throughput | float | > 0 | queries per second (QPS) |
| Rows affected | integer | ≥ 0 | jumlah baris |
| Query plan cost | float | > 0 | cost unit (dari EXPLAIN) |

**Metadata (Resource & System):**
| Field | Contoh | Tipe |
|-------|--------|------|
| CPU usage | 45.2 | persen |
| Memory usage | 3200 | MB |
| CPU temperature | 72 | Celsius |
| Docker container memory | 1800 | MB |
| Disk I/O read | 150 | MB/s |
| Execution status | success / warning / failed | enum |
| Notes | Thermal throttling at 15:45, CPU dropped to 2.8 GHz | string |

**Format output:** [x] JSON / [ ] CSV / [ ] Database / [ ] Lainnya: ____

**Template JSON per trial:**
```json
{
  "identity": {
    "run_id": "run-B1-SELECT-100K-r3",
    "timestamp": "2026-06-22T10:30:00Z",
    "batch": "B1",
    "condition": {
      "id": "C1",
      "dbms": "postgresql",
      "index_type": "none",
      "query_version": "default"
    },
    "operation": "SELECT",
    "volume": 100000,
    "replication": 3
  },
  "configuration": {
    "seed": 456,
    "code_version": "commit-abc1234",
    "config_file": "config-v1.0.yaml",
    "dbms_version": "PostgreSQL 16.3",
    "dataset_checksum": "sha256:a1b2c3d4e5...",
    "buffer_pool_size": "128MB",
    "max_connections": 50
  },
  "metrics": {
    "response_time_ms": 245.3,
    "throughput_qps": 4076.2,
    "rows_affected": 15234,
    "explain_cost": 8432.15
  },
  "metadata": {
    "cpu_usage_percent": 45.2,
    "memory_usage_mb": 3200,
    "cpu_temperature_celsius": 72,
    "docker_memory_mb": 1800,
    "disk_io_read_mbps": 150,
    "execution_status": "success",
    "notes": "Run completed without issues"
  }
}
```

**Compilation strategy:**
- Per trial: JSON file di `results/B1/C1_pg_none_default/SELECT_100K/r3.json`
- Struktur folder: `results/{batch}/{condition}/{operation}_{volume}/r{replication}.json`
- Final analysis: Python script `compile_logs.py` → `results/all_trials.csv` untuk statistical analysis
- Expected total files: 800 JSON files

---

## Latihan 3 — Anomaly Protocol

Rencanakan bagaimana menangani anomali. Untuk setiap jenis, tentukan langkah yang diambil.

| Jenis Anomali | Contoh | Tindakan | Dokumentasi |
|---------------|--------|----------|-------------|
| **Run gagal (crash)** | OOM exception saat volume 1M record pada RAM 8 GB; Docker container killed | 1. Catat error message lengkap di log 2. Dokumentasi kondisi saat crash (memory %, swap usage) 3. Kurangi batch_size atau split query menjadi sub-batches 4. Re-run dengan parameter adjusted 5. Laporkan sebagai limitasi hardware | Log: `logs/anomalies/run-XXX-oom-crash.txt` |
| **Response time ekstrem (outlier)** | SELECT = 5000ms padahal baseline 200ms pada volume yang sama | 1. Jangan langsung hapus 2. Investigasi: cache hit? thermal throttling? background process? 3. Check CPU temp dan clock speed 4. Re-run dengan fresh cache 5. Jika konsisten ekstrem = temuan tentang worst-case scenario | Log: `logs/anomalies/run-XXX-outlier.md` |
| **Thermal throttling** | CPU temperature > 85°C, clock speed turun dari 4.3 GHz ke 2.5 GHz | 1. Pause eksekusi 2. Istirahat 10-15 menit untuk cooling 3. Catat timestamp dan durasi throttling 4. Lanjutkan setelah suhu < 70°C 5. Pertimbangkan re-run batch yang terpengaruh | Log: `logs/anomalies/thermal-events.csv` |
| **RAM exhaustion** | Docker container killed karena memory limit 2 GB terlampaui saat volume 1M | 1. Catat memory usage saat OOM 2. Restart container 3. Untuk volume 1M: jalankan query dalam sub-batches (100K per batch) 4. Laporkan sebagai limitasi RAM 8 GB | Log: `logs/anomalies/run-XXX-oom.md` |
| **Inkonsistensi antar replikasi** | CV > 5% pada 5 replikasi di kondisi yang sama | 1. Verifikasi seed di semua library (Faker, NumPy, Python random) 2. Check DBMS cache state (sudah di-clear?) 3. Verifikasi tidak ada background process 4. Re-run replikasi yang outlier 5. Jika tetap tinggi → laporkan variabilitas sebagai temuan | Log: `logs/anomalies/run-XXX-high-variance.md` |
| **Data integrity issue** | Dataset checksum tidak match setelah load ke database; jumlah record berbeda | 1. Stop eksekusi batch 2. Verifikasi CSV file (corrupted?) 3. Re-generate dataset dengan seed=42 4. Verifikasi proses LOAD DATA / COPY 5. Catat perbedaan record count | Log: `logs/anomalies/dataset-integrity.json` |
| **Docker issue** | Container restart, connection refused, port conflict | 1. Restart Docker Desktop 2. Verify containers healthy 3. Re-run affected trials 4. Catat durasi downtime | Log: `logs/anomalies/docker-issues.md` |

**Prinsip Anomaly Handling:**
```
Detect → Investigate → Document → Decide → Execute

Detect:      Monitor CPU temp, memory, response time real-time selama run
Investigate: Jangan assume — cek root cause (thermal? RAM? I/O? bug?)
Document:    Tulis lengkap di anomaly log (JANGAN DIHAPUS!)
Decide:      Re-run? Proceed dengan catatan? Report sebagai limitasi?
Execute:     Jalankan keputusan, log hasilnya
```

**Jenis anomali yang TIDAK boleh dihapus:**
- "Run OOM pada volume 1M → langsung delete log" → **SALAH!** Ini bukti limitasi RAM 8 GB
- "Response time outlier → re-run tanpa dokumentasi yang pertama" → **SALAH!** Bisa jadi DBMS behavior
- "Thermal throttling → abaikan karena hanya sebentar" → **SALAH!** Bisa memengaruhi hasil

**Semua anomali harus:**
- Dicatat di `logs/anomalies/anomaly-log.md`
- Masuk final report (bukan hidden)
- Dianalisis dampaknya ke kesimpulan
- Khusus OOM dan thermal: dilaporkan sebagai **batasan penelitian**

**Anomali spesifik untuk hardware Lenovo V14 G4 ABP (RAM 8 GB):**
| Risiko | Trigger | Mitigasi Proaktif |
|--------|---------|-------------------|
| OOM pada volume 1M | Dataset 1M record ≈ 500 MB+ di memory DBMS | Query dalam sub-batches; buffer pool 128 MB; stop container lain |
| Thermal throttling | Sustained CPU > 80% selama batch panjang | Cooling pad; istirahat 10 menit antar batch; monitor HWiNFO |
| Swap usage | RAM penuh → OS swap ke SSD → I/O bottleneck | Tutup semua app non-esensial; monitor Task Manager |
| Docker overhead | Docker Desktop di Windows makan ~2-3 GB RAM | Set Docker memory limit 4 GB total; alokasikan 2 GB per DBMS container |

---

## Refleksi

> Pernahkah Anda melaporkan hasil riset/tugas dari single run? Apa risikonya? Bagaimana multiple run mengubah kepercayaan terhadap hasil?

**Pengalaman sebelumnya:**
> Single run pada project akademis sebelumnya sering menghasilkan overconfidence — misal: "PostgreSQL response time 12ms lebih cepat dari MySQL" padahal itu hanya 1 eksekusi. Risiko: Kesimpulan tidak robust, bisa disebabkan cache state, thermal condition, atau specific data distribution pada run tersebut.

**Yang akan dilakukan berbeda:**
> Sekarang melakukan 5 replikasi per sel dengan seed berbeda (42, 123, 456, 789, 1024) untuk mendapatkan mean ± std dan confidence interval. Ini memberikan variabilitas yang lebih realistis. Jika hasil 5 replikasi konsisten (CV < 5%) → temuan lebih trustworthy. Jika ada outlier → investigasi alih-alih dihapus → menghasilkan insight tentang edge case DBMS atau limitasi hardware (thermal throttling, OOM pada RAM 8 GB).

**Rencana Dokumentasi Eksekusi:**
1. Semua 8 batch (800 trial) dijalankan sesuai execution plan dengan urutan counterbalanced (PG-MySQL bergantian)
2. Setiap trial menghasilkan JSON log terstruktur di `results/{batch}/{condition}/{operation}_{volume}/r{N}.json`
3. Semua anomali dicatat di `logs/anomalies/` (TIDAK DIHAPUS) — termasuk OOM, thermal throttling, high variance
4. Final compilation: `python compile_logs.py` → `results/all_trials.csv` (800 baris)
5. Data ready untuk WS-11 (validasi) & WS-12 (analisis statistik ANOVA)
6. Limitasi hardware (RAM 8 GB, thermal throttling) dilaporkan transparan sebagai batasan penelitian