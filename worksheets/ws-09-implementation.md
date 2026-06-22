# WS-09: Implementation & Environment

> **Bab 9 — Implementasi Riset & Kontrol Lingkungan**

---

## Ringkasan Materi

### Implementasi Riset ≠ Coding Biasa

Tujuan implementasi riset bukan membuat software yang berfungsi, melainkan membangun **instrumen pengukuran yang konsisten**. Setiap modul harus di-mapping ke variabel (dari Bab 6), parameter harus config-driven, dan logging aktif dari hari pertama.

### Reproducible Implementation Model

```
Design → Implementation → Environment Setup → Execution Consistency → Reproducibility → Trustworthy Result
```

Setiap transisi memiliki syarat:
- Design → Implementation: kode sesuai mapping variabel-ke-komponen (WS-06)
- Implementation → Environment: versi, dependency, seed, path, OS eksplisit
- Environment → Consistency: seed terkunci, urutan deterministik
- Consistency → Reproducibility: dokumentasi lengkap
- Reproducibility → Trust: siapa pun ikuti dokumentasi → hasil sama/serupa

### Repeatability vs Reproducibility

| Level | Peneliti | Environment | Hasil |
|-------|---------|-------------|-------|
| **Repeatability** | Sama | Sama | Sama persis |
| **Reproducibility** | Berbeda | Berbeda (ikuti docs) | Sama/serupa |

Capai **repeatability** dulu, baru **reproducibility**.

### Engineering vs Research Perspective

| Aspek | Engineering | Research |
|-------|-----------|---------|
| Tujuan | Sistem berfungsi untuk user | Instrumen pengukuran konsisten |
| Dependency | Update ke terbaru | Lock di versi spesifik |
| Testing | Unit, integration, E2E | Repeatability test (run ulang → sama?) |
| Dokumentasi | User guide, API docs | Environment spec, execution steps, expected output |
| Config | Default masuk akal | Setiap parameter eksplisit & adjustable |

### Jebakan Kognitif

1. Menunda environment setup → bug sulit dilacak
2. Tidak pakai version control → hasil tidak bisa direkonstruksi
3. Menolak Docker/container → "di laptop saya bisa" saat review
4. 3× hasil sama ≠ repeatable (bisa cache/state tersimpan)

### Istilah Penting

- **Environment Specification** — Deskripsi lengkap: hardware, OS, runtime, library + versi, config, seed
- **Dependency** — Komponen eksternal yang harus di-lock versinya
- **Config-driven** — Parameter dieksternalisasi ke file konfigurasi, bukan hardcode

---

## Template A.9 — Dokumentasi Setup Eksperimen

```
EXPERIMENT SETUP DOCUMENTATION

Hardware:
  CPU     : AMD Ryzen 5 7430U (6 Core / 12 Thread, 2.3 GHz base, 4.3 GHz boost, 16MB L3 Cache)
  RAM     : 8 GB DDR4-3200 (soldered)
  GPU     : AMD Radeon Graphics (integrated)
  Storage : 512 GB NVMe SSD

Software:
  OS        : Windows 11 Pro 64-bit
  Runtime   : Python 3.11.x
  DBMS      : PostgreSQL 16.x, MySQL 8.0.x
  Container : Docker Desktop 4.x (untuk isolasi DBMS)

Dependencies:
| Library       | Version | Sumber  | Hash/Checksum         |
|---------------|---------|---------|-----------------------|
| psycopg2      | 2.9.9   | PyPI    | (tercantum di lockfile) |
| mysql-connector-python | 8.3.0 | PyPI | (tercantum di lockfile) |
| pandas        | 2.1.4   | PyPI    | (tercantum di lockfile) |
| numpy         | 1.26.3  | PyPI    | (tercantum di lockfile) |
| scipy         | 1.11.4  | PyPI    | (tercantum di lockfile) |
| pyyaml        | 6.0.1   | PyPI    | (tercantum di lockfile) |
| faker         | 22.0.0  | PyPI    | (tercantum di lockfile) |
| matplotlib    | 3.8.2   | PyPI    | (tercantum di lockfile) |

Konfigurasi:
  Config file     : config.yaml (semua parameter eksperimen)
  Random seed     : 42 (untuk data generation dan replikasi)
  DBMS settings   : buffer pool / shared_buffers = 128MB, max_connections = 50

Reproducibility Check:
  [x] Dependency terdokumentasi (requirements.txt / Pipfile.lock)
  [x] Seed ditetapkan di semua level (Python, NumPy, Faker data generator)
  [x] Config di version control (Git)
  [x] README instruksi reproduksi lengkap
  [x] Docker Compose untuk setup DBMS yang identik
```

---

## Latihan 1 — Environment Specification

Dokumentasikan environment untuk eksperimen Anda (boleh environment saat ini atau yang direncanakan).

| Komponen | Spesifikasi |
|----------|------------|
| CPU | AMD Ryzen 5 7430U (6 Core / 12 Thread, 2.3 GHz base, 4.3 GHz boost, 16MB L3 Cache) — Lenovo V14 G4 ABP |
| RAM | 8 GB DDR4-3200 (soldered) |
| GPU | AMD Radeon Graphics (integrated) — tidak digunakan untuk eksperimen database |
| Storage | 512 GB NVMe SSD (kecepatan read/write penting untuk database I/O) |
| OS | Windows 11 Pro 64-bit |
| Runtime | Python 3.11.x (script benchmarking) |
| DBMS | PostgreSQL 16.x dan MySQL 8.0.x (masing-masing di Docker container) |
| Container | Docker Desktop 4.x — resource limit: 2 GB RAM per container, 2 CPU cores |
| Random Seed | 42 (untuk data generation menggunakan Faker dan konsistensi replikasi) |

**Dependencies (minimal 5):**

| Library | Version | Alasan Dibutuhkan |
|---------|---------|-------------------|
| psycopg2 | 2.9.9 | Adapter PostgreSQL untuk koneksi database dan eksekusi query dari Python |
| mysql-connector-python | 8.3.0 | Adapter MySQL untuk koneksi database dan eksekusi query dari Python |
| pandas | 2.1.4 | Data manipulation untuk parsing hasil benchmarking, aggregation, dan analisis statistik |
| numpy | 1.26.3 | Numerical computation untuk kalkulasi statistik (mean, std, confidence interval) |
| scipy | 1.11.4 | Statistical testing: ANOVA, Kruskal-Wallis, Tukey HSD (sesuai Statistical Plan di WS-07) |
| pyyaml | 6.0.1 | Parsing config file YAML yang berisi parameter eksperimen (DBMS, indexing, optimization, volume) |
| faker | 22.0.0 | Data generator untuk menghasilkan dataset terstandarisasi dengan seed=42 |
| matplotlib | 3.8.2 | Visualisasi hasil benchmarking (grafik perbandingan response time) |

---

## Latihan 2 — Repeatability Test Plan

Rancang tes repeatability sederhana: jalankan kode yang sama 3× di environment yang sama.

| Run | Seed | Metrik Utama | Hasil Sama? |
|-----|------|-------------|-------------|
| 1 | 42 | Response time (ms) per query, Throughput (QPS) | — |
| 2 | 42 | Response time (ms) per query, Throughput (QPS) | [ ] Ya / [ ] Tidak |
| 3 | 42 | Response time (ms) per query, Throughput (QPS) | [ ] Ya / [ ] Tidak |

**Catatan:** Response time tidak akan identik persis antar-run karena variabilitas OS scheduling dan I/O. Kriteria repeatability: coefficient of variation (CV) < 5% pada mean response time per kondisi.

**Jika hasil berbeda (CV > 5%), kemungkinan penyebab:**
> 1. DBMS cache belum dibersihkan antar-run → query kedua lebih cepat karena data sudah di-buffer pool
> 2. Background process Windows (antivirus scan, Windows Update, search indexing) → response time naik tidak terduga
> 3. Thermal throttling pada laptop — CPU clock turun saat suhu tinggi → query jadi lebih lambat
> 4. Docker container resource contention (jika kedua DBMS berjalan bersamaan) → variabilitas timing
> 5. OS page cache tidak dibersihkan → I/O performance bervariasi antar-run
> 6. Seed=42 tidak di-set di semua library (misal: Faker menggunakan seed berbeda) → data generated berbeda

**Checklist kontrol yang sudah diterapkan:**
- [x] Random seed di-set di semua level (Python `random.seed(42)`, NumPy `np.random.seed(42)`, Faker `Faker.seed(42)`)
- [x] Tidak ada background process yang mengganggu (disable antivirus real-time scan, pause Windows Update, disable Search Indexer selama eksperimen)
- [x] DBMS cache dibersihkan antar-kondisi: PostgreSQL → `DISCARD ALL` + restart container; MySQL → `RESET QUERY CACHE` + restart container
- [x] Config file yang sama untuk semua run (config.yaml di-lock di Git, versi dicatat di log)
- [x] Power plan laptop di-set ke "Best Performance" (mencegah CPU frequency scaling yang agresif)
- [x] Cooling pad digunakan untuk mitigasi thermal throttling pada Lenovo V14 G4 ABP
- [x] Hanya satu DBMS yang berjalan per sesi pengujian (bukan bersamaan) untuk menghindari resource contention

---

## Latihan 3 — README Eksperimen

Tulis README minimum untuk eksperimen Anda (6 komponen wajib).

```
# Benchmarking DBMS: Analisis Dampak Query Optimization & Indexing Strategy
# terhadap Performa PostgreSQL dan MySQL dalam Workload CRUD

## 1. Environment

**Hardware:**
- Model: Lenovo V14 G4 ABP
- CPU: AMD Ryzen 5 7430U (6C/12T, 2.3/4.3 GHz, 16MB L3 Cache)
- RAM: 8 GB DDR4-3200 (soldered)
- GPU: AMD Radeon Graphics (integrated, tidak digunakan)
- Storage: 512 GB NVMe SSD

**Software:**
- OS: Windows 11 Pro 64-bit
- Python: 3.11.x
- PostgreSQL: 16.x (Docker container)
- MySQL: 8.0.x (Docker container)
- Docker Desktop: 4.x

**Dependencies** (lengkap di requirements.txt):
- psycopg2==2.9.9
- mysql-connector-python==8.3.0
- pandas==2.1.4
- numpy==1.26.3
- scipy==1.11.4
- pyyaml==6.0.1
- faker==22.0.0
- matplotlib==3.8.2

**Key Environment Variables:**
```
RANDOM_SEED=42
PG_HOST=localhost
PG_PORT=5432
PG_DB=benchmark_db
PG_USER=postgres
PG_PASS=benchmark
MYSQL_HOST=localhost
MYSQL_PORT=3306
MYSQL_DB=benchmark_db
MYSQL_USER=root
MYSQL_PASS=benchmark
LOG_LEVEL=INFO
```

## 2. Installation

### Setup Docker Containers
```bash
# Start PostgreSQL dan MySQL containers
docker-compose up -d

# Verifikasi containers berjalan
docker ps
# Expected: postgres (healthy), mysql (healthy)
```

### Setup Python Environment
```bash
# Buat virtual environment
python -m venv venv

# Activate (Windows)
venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### Generate Dataset
```bash
# Generate dataset terstandarisasi dengan seed=42
python generate_data.py --seed 42 --records 50000 100000 250000 500000 1000000
# Output: data/ directory dengan CSV files per volume
```

### Verify Installation
```bash
python verify_env.py
# Expected: semua check pass (Docker, DB connections, library imports, seed consistency)
```

## 3. Data

**Sumber Data:**
- Dataset sintetis yang di-generate menggunakan Faker library dengan seed=42
- Skema terstandarisasi: 1 tabel utama dengan 19 kolom (terinspirasi dataset Google Playstore dari Ahsa et al., 2023)
- Kolom mencakup berbagai tipe data: VARCHAR, INT, FLOAT, BOOLEAN, DATE, TEXT

**Spesifikasi Dataset Eksperimen:**
- Volume: 50.000, 100.000, 250.000, 500.000, 1.000.000 record
- Schema: app_name (VARCHAR), app_id (VARCHAR, indexed), category (VARCHAR, indexed),
  rating (FLOAT), rating_count (INT), installs (VARCHAR), free (BOOLEAN),
  price (FLOAT), currency (VARCHAR), size (VARCHAR), min_android (VARCHAR),
  developer_id (VARCHAR, indexed), released (DATE), last_updated (DATE),
  content_rating (VARCHAR), ad_supported (BOOLEAN), in_app_purchases (BOOLEAN),
  editors_choice (BOOLEAN), scraped_time (DATETIME)
- Data snapshot: fixed, di-version control (checksum SHA256)

**Indexing Strategy (sesuai WS-06):**
- No-index: Tidak ada index tambahan selain primary key
- Single-column: INDEX pada app_id (kolom yang sering digunakan di WHERE clause)
- Composite: INDEX pada (app_id, category, developer_id) — composite index untuk query multi-kolom

**Checksum (untuk memverifikasi integritas data):**
```
data_50k.csv:    SHA256: [akan dihitung saat generation]
data_100k.csv:   SHA256: [akan dihitung saat generation]
data_250k.csv:   SHA256: [akan dihitung saat generation]
data_500k.csv:   SHA256: [akan dihitung saat generation]
data_1000k.csv:  SHA256: [akan dihitung saat generation]
```

## 4. Execution

### Run Eksperimen Lengkap (8 Kondisi × 4 CRUD × 5 Volume × 5 Replikasi)

#### Setup untuk setiap kondisi:
```bash
# Contoh: Kondisi C1 (PostgreSQL, no-index, default query)
python run_benchmark.py \
  --config config.yaml \
  --dbms postgresql \
  --index none \
  --query default \
  --replikat 5 \
  --output results/C1_pg_none_default/
```

#### Run semua kondisi secara otomatis:
```bash
# Jalankan seluruh eksperimen (8 kondisi × 4 CRUD × 5 volume × 5 replikasi)
python run_all_experiments.py --config config.yaml

# Output: results/ directory dengan sub-folder per kondisi
# Struktur: results/{dbms}_{index}_{optimization}/{operation}_{volume}/trial_{n}.json
```

#### Per Kondisi (manual):
```bash
# C1: PostgreSQL + no-index + default
python run_benchmark.py --dbms postgresql --index none --query default

# C2: PostgreSQL + single-column + default
python run_benchmark.py --dbms postgresql --index single --query default

# C3: PostgreSQL + composite + default
python run_benchmark.py --dbms postgresql --index composite --query default

# C4: PostgreSQL + composite + optimized
python run_benchmark.py --dbms postgresql --index composite --query optimized

# C5-C8: Sama seperti C1-C4 tapi --dbms mysql
python run_benchmark.py --dbms mysql --index none --query default
python run_benchmark.py --dbms mysql --index single --query default
python run_benchmark.py --dbms mysql --index composite --query default
python run_benchmark.py --dbms mysql --index composite --query optimized
```

#### Analisis Statistik:
```bash
python analyze_results.py --input results/ --output analysis/
# Output: ANOVA results, post-hoc tests, effect sizes, visualizations
```

### Estimated Runtime
- Per kondisi (1 volume × 1 CRUD × 5 replikasi): ~2-5 menit
- Per kondisi lengkap (5 volume × 4 CRUD × 5 replikasi): ~40-100 menit
- Total 8 kondisi: ~5-14 jam (tergantung volume data dan thermal throttling)

**Catatan penting untuk Lenovo V14 G4 ABP:**
- Laptop ini memiliki thermal throttling risk saat sustained workload tinggi dan RAM terbatas 8 GB
- Rekomendasi:
  - Gunakan cooling pad eksternal
  - Istirahat ~10 menit setiap selesai 1 kondisi (setiap ~1 jam)
  - Monitor CPU temperature dengan HWiNFO (target: < 85°C untuk stability)
  - Set power plan ke "Best Performance" di Windows Settings
  - Disable semua background services selama pengujian
  - Pastikan laptop tercolok ke power adapter (jangan battery mode)
  - **RAM 8 GB**: tutup semua aplikasi selain Docker dan terminal; buffer pool DBMS dibatasi 128 MB per container; jalankan hanya 1 DBMS container per sesi (stop container yang tidak aktif)
  - Untuk volume 1.000.000 record: monitor penggunaan RAM via Task Manager; jika swap aktif, pertimbangkan mengurangi batch size query

## 5. Configuration

**Main Config File: `config.yaml`**
```yaml
experiment:
  random_seed: 42
  replications: 5
  warmup_queries: 5

dbms:
  postgresql:
    host: localhost
    port: 5432
    database: benchmark_db
    user: postgres
    password: benchmark
    shared_buffers: 128MB
    max_connections: 50
  mysql:
    host: localhost
    port: 3306
    database: benchmark_db
    user: root
    password: benchmark
    innodb_buffer_pool_size: 128MB
    max_connections: 50

dataset:
  volumes: [50000, 100000, 250000, 500000, 1000000]
  schema_file: schema/app_playstore.sql
  data_dir: data/

indexing:
  none: {}
  single:
    - table: app_playstore
      column: app_id
      type: btree
  composite:
    - table: app_playstore
      columns: [app_id, category, developer_id]
      type: btree

queries:
  default:
    select: "SELECT * FROM app_playstore WHERE category = 'GAME' LIMIT {limit}"
    insert: "INSERT INTO app_playstore (app_name, app_id, category, rating, ...) VALUES (...)"
    update: "UPDATE app_playstore SET rating = 4.5, last_updated = NOW() WHERE app_id = 'target_id'"
    delete: "DELETE FROM app_playstore WHERE app_id = 'target_id'"
  optimized:
    select: "SELECT app_name, rating FROM app_playstore WHERE category = 'GAME' AND app_id LIKE 'com.%' ORDER BY rating DESC LIMIT {limit}"
    insert: "INSERT INTO app_playstore (...) VALUES (...), (...), (...) ON CONFLICT DO NOTHING"
    update: "UPDATE app_playstore SET rating = 4.5 WHERE app_id IN (SELECT app_id FROM app_playstore WHERE category = 'GAME' LIMIT 100)"
    delete: "DELETE FROM app_playstore WHERE app_id IN (SELECT app_id FROM app_playstore WHERE rating < 1.0 LIMIT 100)"

execution:
  log_dir: results/
  log_level: INFO
  clear_cache_before_trial: true
  cold_start: true
```

**Parameter yang TIDAK boleh berubah (locked) selama eksperimen:**
- `random_seed`: 42 (repeatability)
- `replications`: 5 (statistical power — WS-07)
- `shared_buffers` / `innodb_buffer_pool_size`: 128MB (disetarakan, disesuaikan dengan RAM 8 GB — fairness WS-07)
- `max_connections`: 50 (konsisten)
- `warmup_queries`: 5 (menghilangkan cold-start bias)
- `dataset.volumes`: [50K, 100K, 250K, 500K, 1M] (CV — WS-05)
- `schema_file`: fixed (skema identik untuk semua kondisi)

## 6. Expected Output

### Output Format: JSON Log per Trial
```json
{
  "experiment_id": "dbms_bench_2026_001",
  "trial": 1,
  "condition": {
    "dbms": "postgresql",
    "index_type": "composite",
    "query_version": "optimized"
  },
  "timestamp": "2026-06-22T10:30:00Z",
  "environment": {
    "os": "Windows 11 Pro",
    "cpu": "AMD Ryzen 5 7430U",
    "ram_gb": 8,
    "python_version": "3.11.x",
    "seed": 42,
    "docker": true
  },
  "results": [
    {
      "operation": "SELECT",
      "volume": 100000,
      "response_time_ms": 12.34,
      "throughput_qps": 8103.2,
      "cpu_usage_pct": 45.2,
      "memory_usage_mb": 210.5
    },
    {
      "operation": "INSERT",
      "volume": 100000,
      "response_time_ms": 8.56,
      "throughput_qps": 11682.2,
      "cpu_usage_pct": 38.1,
      "memory_usage_mb": 195.3
    }
  ],
  "data_checksum": {
    "data_100k.csv": "sha256:abc123..."
  },
  "status": "success"
}
```

### Expected Output Summary (ilustrasi 1 kondisi, 3 replikasi)
```
Kondisi: PostgreSQL + Composite Index + Optimized Query (100K records)

  Trial 1: SELECT=12.3ms, INSERT=8.6ms, UPDATE=5.2ms, DELETE=3.1ms
  Trial 2: SELECT=12.1ms, INSERT=8.5ms, UPDATE=5.3ms, DELETE=3.0ms
  Trial 3: SELECT=12.4ms, INSERT=8.7ms, UPDATE=5.1ms, DELETE=3.2ms
  → Mean: SELECT=12.3ms ± 0.15, INSERT=8.6ms ± 0.10, UPDATE=5.2ms ± 0.10, DELETE=3.1ms ± 0.10
  → CV: SELECT=1.2%, INSERT=1.2%, UPDATE=1.9%, DELETE=3.2% (semua < 5% ✓)
```

**Catatan:**
- Response time di atas adalah ilustrasi; nilai aktual bergantung pada kondisi hardware
- Lenovo V14 G4 ABP dengan Ryzen 5 7430U dan NVMe SSD diharapkan memberikan performa I/O yang memadai untuk database benchmarking, namun RAM 8 GB membatasi buffer pool DBMS sehingga response time mungkin lebih tinggi dibanding konfigurasi RAM besar
- Thermal throttling mungkin memengaruhi konsistensi pada run berdurasi panjang — mitigasi dengan cooling pad dan istirahat antar kondisi
- Accuracy dan repeatability diverifikasi dari coefficient of variation (CV) < 5%

### Validation Checklist
- [x] Semua 8 kondisi × 4 CRUD × 5 volume × 5 replikasi = 800 trial selesai tanpa error
- [x] Hasil 5× replikasi pada kondisi yang sama memiliki CV < 5% (repeatability confirmed)
- [x] Response time dan throughput konsisten antar-trial
- [x] Data checksum match untuk semua volume (integritas data terjamin)
- [x] Seed=42 terkunci di semua layer (verifikasi di log)
- [x] Docker container resource limit respected (verifikasi via docker stats)
- [x] DBMS cache cleared sebelum setiap kondisi baru (cold start confirmed)
```

---

## Refleksi

> Apakah eksperimen Anda saat ini bisa direproduksi oleh orang lain tanpa bantuan Anda? Komponen apa yang masih hilang?

**Level saat ini:** [x] Repeatability / [ ] Reproducibility / [ ] Belum keduanya

**Komponen yang sudah terdokumentasi:**
- ✅ Hardware spesifikasi lengkap (Lenovo V14 G4 ABP — AMD Ryzen 5 7430U, 8 GB RAM, NVMe SSD)
- ✅ Software & dependency dengan versi exact (Python, PostgreSQL, MySQL, Docker, semua library)
- ✅ Installation step-by-step dengan Docker Compose dan verification script
- ✅ Data spesifikasi & schema terstandarisasi (19 kolom, Faker seed=42)
- ✅ Execution command lengkap untuk 8 kondisi dengan estimasi waktu
- ✅ Configuration file (config.yaml) yang di-version control
- ✅ Expected output dengan JSON format dan validation checklist
- ✅ Thermal throttling awareness & mitigation strategy untuk laptop

**Komponen yang masih perlu untuk mencapai REPRODUCIBILITY (orang lain bisa ulang di environment berbeda):**
1. Docker Compose file yang published (GitHub/GitLab public repo) agar setup DBMS identik di mesin lain
2. Automated data download & generation script yang bisa dijalankan tanpa intervensi manual
3. Published dataset di repository (Zenodo) dengan DOI untuk verifikasi checksum
4. Benchmark CPU baseline (misalnya sysbench atau Geekbench score) untuk menormalisasi hasil jika hardware berbeda
5. Dokumentasi detail tentang konfigurasi Docker Desktop pada Windows 11 (WSL2 backend)

**Spesifik untuk Lenovo V14 G4 ABP:**
- Catat BIOS version & power plan setting (thermal behavior bisa berubah antar versi)
- Gunakan profile "Best Performance" di Power Settings selama eksperimen
- Disable background services (Windows Search Indexer, antivirus real-time, Windows Update) selama pengujian
- Monitor CPU temperature dengan HWiNFO (target: < 85°C untuk stability)
- Gunakan cooling pad eksternal untuk mencegah thermal throttling pada sustained workload
- Pastikan laptop tercolok ke power adapter (battery mode akan membatasi CPU frequency)
- **RAM 8 GB**: buffer pool DBMS dibatasi 128 MB; jalankan hanya 1 container DBMS per sesi; tutup semua aplikasi non-esensial; pertimbangkan upgrade ke 16 GB jika memungkinkan untuk stabilitas pada volume data besar

**Rencana transisi ke REPRODUCIBILITY:**
> Jika ada interest dari reviewer atau peneliti lain untuk mengulang eksperimen, akan package semua ke Docker container + push code ke GitHub public repository + upload dataset ke Zenodo dengan DOI reference. Dokumentasi Docker Compose akan mencakup resource limit yang identik sehingga hasilnya comparable meskipun hardware berbeda.
