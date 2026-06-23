# Tahap 3 — Eksekusi Benchmark CRUD

**Status:** Selesai — 600 trial dijalankan
**Bergantung pada:** [tahap-2-implementasi-gateway.md](tahap-2-implementasi-gateway.md)
**Lokasi kode:** [../05-kode/benchmark/](../05-kode/benchmark/)

---

## Tujuan

Menjalankan benchmark eksperimen dengan semua kombinasi faktor (DBMS × Indexing × Volume × Operation × Replication) dan mengumpulkan response time, throughput, dan resource metrics.

---

## Eksperimen Matrix

| Faktor | Level | Count |
|--------|-------|-------|
| DBMS | PostgreSQL, MySQL | 2 |
| Indexing | none, single, composite | 3 |
| Volume | 50K, 100K, 250K, 500K | 4 |
| Operation | SELECT, INSERT, UPDATE, DELETE | 4 |
| Replication | seed 42, 123, 456, 789, 1024 | 5 |
| **Total Trials** | 2×3×4×4×5 | **600** |

---

## Execution Protocol

### Setup Setiap Trial

1. **Prepare Database**: Load dataset dengan volume tertentu
2. **Create Index**: Terapkan strategi indexing (atau DROP jika no-index)
3. **Warmup**: Jalankan 10 sample queries untuk cache population
4. **Baseline Capture**: Catat CPU%, memory sebelum benchmark

### Measurement Phase

Untuk setiap operasi CRUD:

```python
start_time = time.time()
for i in range(N_ITERATIONS):  # misal N=100
    execute_query(operation, dbms, indexing, volume, seed)
    record_response_time(i)
end_time = time.time()

# Aggregate
mean_response_time = statistics.mean(response_times)
std_response_time = statistics.stdev(response_times)
throughput_qps = N_ITERATIONS / (end_time - start_time)
```

### Data Logging

Setiap trial hasil dicatat ke CSV:

```
timestamp, dbms, indexing_strategy, operation, volume, response_time_ms, throughput_qps, cpu_percent, memory_mb, replication_id
2026-06-23T10:00:00Z, postgresql, composite, SELECT, 100000, 67.8, 14749.6, 28.5, 512.3, 1
2026-06-23T10:01:30Z, postgresql, composite, SELECT, 100000, 68.2, 14682.5, 29.1, 514.7, 2
...
```

---

## Execution Steps

### 1. Run All Trials

```bash
cd ../benchmark
python3 run_benchmark.py \
  --config config.yaml \
  --output ../example-riset-directory/04-data/ \
  --verbose
```

Script akan:
- Iterate setiap kombinasi faktor
- Create/drop index sesuai kondisi
- Execute queries
- Log hasil ke CSV

### 2. Monitor Progress

Terminal terpisah untuk resource monitoring:

```bash
cd ../benchmark
./monitor_resources.sh > resources.log &
```

### 3. Verify Output

```bash
# Check total files
ls ../example-riset-directory/04-data/ | wc -l  # should be ~600

# Check data format
head -5 ../example-riset-directory/04-data/postgresql_composite_select_100000_r1.csv
```

---

## Expected Results

Setelah semua 600 trial selesai:

- **Data Completeness**: 594–600 trial (99%) berhasil; 0–6 mungkin OOM pada volume 1M
- **Response Time Pattern**: 
  - SELECT: composite < single < no-index
  - INSERT: no-index < single < composite (inverse pattern)
- **DBMS Pattern**: PostgreSQL ~20% lebih cepat pada kebanyakan operasi
- **Volume Pattern**: Linear scaling dengan volume

---

## Troubleshooting

| Issue | Cause | Solution |
|-------|-------|----------|
| OOM Error | Volume 1M × RAM < 8GB | Reduce volume ke 500K atau skip 1M |
| Query Timeout | DBMS overloaded | Reduce VU atau increase duration |
| Inconsistent Results | Thermal throttling | Check CPU temp, ensure cooling |
| CSV Missing Data | Benchmark interrupted | Restart from last completed trial |

---

## Checkpoint

- [x] All 600 trials queued
- [x] Response times logged
- [x] Resource metrics captured
- [x] Data validated for completeness
- [x] Ready for Tahap 4 (Analysis)