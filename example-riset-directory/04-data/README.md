# 04-data

Data mentah hasil benchmark DBMS — output dari **Tahap 3** (eksekusi benchmark), input untuk **Tahap 4** (analisis).

## Isi yang Diharapkan

Folder ini berisi hasil 600 trial benchmark dengan struktur:

```
04-data/
├── postgresql_noindex_select_50000_r1.csv
├── postgresql_noindex_select_50000_r2.csv
├── postgresql_noindex_select_50000_r3.csv
├── ... (600 files total)
├── mysql_composite_delete_500000_r5.csv
└── validation-report.md
```

## Format CSV

Setiap file CSV berisi 100+ rows (iterasi query) dengan kolom:

```
timestamp, dbms, indexing_strategy, operation, volume, response_time_ms, throughput_qps, cpu_percent, memory_mb, replication_id
2026-06-23T10:00:00Z, postgresql, noindex, SELECT, 50000, 45.3, 22099.0, 25.2, 480.5, 1
2026-06-23T10:00:01Z, postgresql, noindex, SELECT, 50000, 43.8, 22831.4, 26.1, 481.2, 1
...
```

## Naming Convention

```
<dbms>_<indexing_strategy>_<operation>_<volume>_r<replication>.csv
```

Contoh:
- `postgresql_noindex_select_50000_r1.csv` — PostgreSQL, no index, SELECT operation, 50K volume, replication 1
- `mysql_composite_insert_250000_r3.csv` — MySQL, composite index, INSERT operation, 250K volume, replication 3

## Struktur Eksperimen

- **DBMS:** postgresql, mysql (2 level)
- **Indexing:** noindex, single, composite (3 level)
- **Operation:** SELECT, INSERT, UPDATE, DELETE (4 level)
- **Volume:** 50000, 100000, 250000, 500000 (4 level)
- **Replication:** r1, r2, r3, r4, r5 (5 replicas)
- **Total:** 2 × 3 × 4 × 4 × 5 = **600 files**

## Catatan

Data di folder ini bersifat mentah (raw) dan belum diolah. Untuk mengisi folder ini, jalankan benchmark sesuai petunjuk di [../09-docs/tahap-3-pengujian-k6.md](../09-docs/tahap-3-pengujian-k6.md) menggunakan script `../05-kode/benchmark/run_benchmark.py`.

Hasil olahan (statistik, visualisasi, ANOVA) disimpan di [../06-output/](../06-output/).
