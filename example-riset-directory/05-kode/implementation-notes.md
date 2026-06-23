# Setup Environment Eksperimen Benchmark

> **Stage 2 — Testing Environment Setup**

---

## Komponen Sistem Benchmark

### 1. Database Systems

- **PostgreSQL 16.3** — DBMS A untuk perbandingan
- **MySQL 8.0.32** — DBMS B untuk perbandingan

### 2. Dataset: app_playstore

- **File sumber:** [../benchmark_project/data/app_playstore_50000.csv](../benchmark_project/data/app_playstore_50000.csv)
- **Skema:** 19 kolom (app_name, app_id, category, rating, rating_count, installs, free, price, size, developer_id, etc.)
- **Volume:** 50K (base), kemudian scaled ke 100K, 250K, 500K, 1M untuk eksperimen

### 3. Strategi Indexing

Tiga kondisi indexing diuji per DBMS:

| Kondisi | Index | Keterangan |
|---------|-------|-----------|
| **C1** | None | Hanya PK, full table scan |
| **C2** | Single | `CREATE INDEX idx_category ON app_playstore(category)` |
| **C3** | Composite | `CREATE INDEX idx_category_rating ON app_playstore(category, rating DESC)` |

### 4. Operasi CRUD

Empat jenis operasi dijalankan per kondisi × volume:

| Operasi | Query Template | Expected Trend |
|---------|---|---|
| **SELECT** | `SELECT * FROM app_playstore WHERE category = ?` | Index→ latency ↓↓ |
| **INSERT** | `INSERT INTO ... VALUES (...)` | Index → latency ↑ |
| **UPDATE** | `UPDATE ... SET rating = ? WHERE app_id = ?` | Index → latency ↑ |
| **DELETE** | `DELETE FROM ... WHERE app_id = ?` | Index → latency ↑ (modest) |

---

## Setup Checklist

- [x] Kedua DBMS ter-install di environment (Docker atau local)
- [x] Database `benchmark` dibuat di PostgreSQL dan MySQL
- [x] Tabel `app_playstore` dibuat sesuai schema standardized
- [x] Dataset CSV di-load ke kedua DBMS
- [x] Checkpoint 1: Verify data loaded (SELECT COUNT(*) = 50K)
- [x] Indexing script siap untuk create/drop index sesuai kondisi
- [x] Query templates ter-standardisasi untuk fairness
- [x] Timing measurement instrumented (start→ query execute → end)

---

## Procedure Eksekusi Per Kondisi

**Untuk setiap kombinasi (DBMS, indexing, CRUD, volume, replikasi):**

1. **Data Preparation:** Load dataset dengan volume tertentu ke DBMS
2. **Create Index:** Terapkan strategi indexing sesuai kondisi (atau DROP jika no-index)
3. **Warmup:** Jalankan 10 sample queries agar cache ter-populate
4. **Measure:** Jalankan query N kali (misal 100), catat response time setiap query
5. **Aggregate:** Hitung mean, std, min, max, p50, p95, p99
6. **Log Result:** Simpan CSV dengan format: timestamp, dbms, indexing, operation, volume, response_time_ms, throughput_qps, replication_id

---

## Tools & Dependencies

| Tool | Version | Purpose |
|------|---------|---------|
| PostgreSQL | 16.3 | DBMS A |
| MySQL | 8.0.32 | DBMS B |
| Python | 3.10+ | Data loading & analysis scripts |
| pandas | 1.3+ | Data manipulation |
| psycopg2 | 2.9+ | PostgreSQL adapter |
| mysql-connector-python | 8.0+ | MySQL adapter |
| matplotlib | 3.4+ | Visualization |

---

## Expected Output

Setelah benchmark complete, folder `04-data/` berisi:

```
04-data/
  ├── postgres_no_index_select_50k_r1.csv
  ├── postgres_no_index_insert_100k_r2.csv
  ├── postgres_single_index_select_250k_r1.csv
  ├── postgres_composite_index_delete_1m_r5.csv
  ├── mysql_no_index_update_500k_r3.csv
  └── ... (600 files total)
```

Setiap file CSV berisi:
```
timestamp, dbms, indexing, operation, volume, response_time_ms, throughput_qps, cpu_percent, memory_mb, replication_id
```

---

## Troubleshooting

| Issue | Cause | Solution |
|-------|-------|----------|
| OOM pada volume 1M | RAM < 8GB | Reduce volume ke 500K; atau upgrade RAM |
| PostgreSQL connection refused | Service not running | `sudo systemctl start postgresql` atau `docker-compose up -d postgres` |
| MySQL slow query | Warm-up tidak cukup | Increase warmup iterations |
| Inconsistent results | Thermal throttling | Ensure CPU cooling; check with `lscpu` pada Ubuntu |
