# Tahap 2 — Setup Database & Benchmark Scripts

**Status:** Selesai
**Acuan arsitektur:** [tahap-1-arsitektur-dan-skema-database.md](tahap-1-arsitektur-dan-skema-database.md)
**Lokasi kode:** [../05-kode/](../05-kode/)

---

## Tujuan

Menyiapkan environment DBMS dan script benchmark untuk eksekusi eksperimen CRUD pada PostgreSQL dan MySQL dengan strategi indexing yang bervariasi.

## Deliverable

- [x] Docker Compose configuration (`docker-compose.yml`) dengan PostgreSQL 16.3 dan MySQL 8.0.32
- [x] Database & tabel creation script untuk kedua DBMS (`schema_postgres.sql`, `schema_mysql.sql`)
- [x] Data loader script: generate 50K base data, scale ke 100K–1M (`generate_data.py`)
- [x] Benchmark runner script: execute CRUD queries dan catat response time (`run_benchmark.py`)
- [x] Indexing management script: create/drop index sesuai kondisi eksperimen
- [x] CSV logger untuk setiap trial: timestamp, dbms, indexing, operation, volume, response_time_ms, throughput_qps, cpu_percent, memory_mb
- [x] README dengan step-by-step setup

---

## Langkah Setup

### 1. Start DBMS Containers

```bash
cd benchmark_project
docker-compose up -d postgres mysql
```

Verifikasi:
```bash
docker-compose ps  # keduanya harus "Up"
```

### 2. Create Database & Tables

PostgreSQL:
```bash
docker-compose exec postgres psql -U benchmark -d benchmark < schema_postgres.sql
```

MySQL:
```bash
docker-compose exec mysql mysql -u benchmark -p benchmark < schema_mysql.sql
```

### 3. Generate & Load Data

```bash
python3 generate_data.py --volume 50000
# Output: data/app_playstore_50000.csv

# Load ke PostgreSQL
docker-compose exec postgres psql -U benchmark -d benchmark \
  -c "\\COPY app_playstore FROM 'data/app_playstore_50000.csv' WITH CSV HEADER"

# Load ke MySQL
docker-compose exec mysql mysql -u benchmark -p benchmark \
  -e "LOAD DATA LOCAL INFILE '/data/app_playstore_50000.csv' INTO TABLE app_playstore FIELDS TERMINATED BY ',' IGNORE 1 ROWS"
```

Verifikasi:
```bash
docker-compose exec postgres psql -U benchmark -d benchmark -c "SELECT COUNT(*) FROM app_playstore"
docker-compose exec mysql mysql -u benchmark -p benchmark -e "SELECT COUNT(*) FROM app_playstore"
```

### 4. Create Indexing Conditions

```bash
# Condition 1: NO INDEX (default, nothing to do)
# Condition 2: SINGLE INDEX
docker-compose exec postgres psql -U benchmark -d benchmark \
  -c "CREATE INDEX idx_app_playstore_category ON app_playstore(category)"

# Condition 3: COMPOSITE INDEX
docker-compose exec postgres psql -U benchmark -d benchmark \
  -c "CREATE INDEX idx_app_playstore_category_rating ON app_playstore(category, rating DESC)"

# Repeat untuk MySQL
```

---

## Benchmark Execution

Script `run_benchmark.py` mengeksekusi semua kombinasi:

```bash
python3 run_benchmark.py \
  --dbms postgresql,mysql \
  --indexing none,single,composite \
  --operations select,insert,update,delete \
  --volumes 50000,100000,250000,500000 \
  --replications 5 \
  --output ../example-riset-directory/04-data/
```

Output:
```
04-data/
├── postgresql_none_select_50000_r1.csv
├── postgresql_none_insert_100000_r2.csv
├── postgresql_single_select_250000_r1.csv
├── postgresql_composite_delete_500000_r5.csv
├── mysql_none_update_50000_r3.csv
└── ... (600 files total)
```

---

## Checklist

- [x] Docker Compose up (postgres + mysql)
- [x] Database & tabel created
- [x] Data loaded (verify COUNT > 0)
- [x] Indexing created per condition
- [x] Warmup queries executed (cache population)
- [x] Response time measurement instrumented
- [x] CSV logging configured
- [x] Resource monitoring (CPU%, memory) integrated
