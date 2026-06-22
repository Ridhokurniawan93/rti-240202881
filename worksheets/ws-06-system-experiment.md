# WS-06: System-Experiment Mapping

> **Bab 6 — System Design sebagai Experimental Artifact**

---

## Ringkasan Materi

### Sistem = Instrumen Pengujian, Bukan Produk

Seorang engineer bertanya "apakah sistem bekerja?" — seorang peneliti bertanya "apa yang bisa dibuktikan sistem ini?" Sistem dalam riset adalah **artifact** — objek yang sengaja dibuat untuk menguji klaim spesifik.

### System as Experiment Model

```
RQ → Variable → System Component → Experimental Setup → Output
```

Setiap komponen sistem harus bisa ditelusuri ke variabel riset (top-down), dan setiap pengukuran harus menjawab RQ (bottom-up).

### Mapping Variabel ke Komponen

| Tipe Variabel | Peran di Sistem | Contoh |
|---------------|----------------|--------|
| **IV** (Independent) | Modul yang bisa di-toggle/swap | DBMS (PostgreSQL vs MySQL), Indexing (none/single/composite) |
| **DV** (Dependent) | Modul pengukuran | Response time logger, throughput calculator |
| **CV** (Control) | Config yang dikunci | Volume data, skema database, hardware spec |

Jika variabel tidak bisa di-map ke komponen apapun → arsitektur perlu didesain ulang.

### 4 Prinsip Desain Eksperimental

| Prinsip | Pertanyaan Kunci |
|---------|-----------------|
| **Traceability** | Komponen ini melayani variabel yang mana? |
| **Modularity** | Bisakah IV diubah tanpa memengaruhi yang lain? |
| **Controllability** | Apakah CV dieksternalisasi ke config file? |
| **Measurability** | Apakah sistem otomatis menghasilkan data yang dibutuhkan? |

### Variable Isolation melalui Arsitektur

- **Modular architecture** — Pisahkan berdasarkan variabel
- **Configuration-driven** — Ubah config (YAML/JSON), bukan code
- **Feature toggles** — On/off flag untuk ablation study

### Research vs Engineering

| Aspek | Engineering | Research |
|-------|------------|----------|
| Tujuan sistem | Memenuhi kebutuhan user | Menguji hipotesis, menghasilkan bukti |
| Arsitektur | Optimasi performa & skalabilitas | Optimasi isolasi variabel & reprodusibilitas |
| Konfigurasi | Sering hardcoded | Dieksternalisasi ke config file |
| Fitur tambahan | Menambah nilai user | Menambah noise jika tidak terkait RQ |

### Istilah Penting

- **Artifact** — Objek yang sengaja dibuat untuk memecahkan masalah atau menguji proposisi
- **Traceability** — Kemampuan menelusuri hubungan RQ → variabel → komponen → output
- **Variable Isolation** — Mengubah hanya satu variabel sambil menahan yang lain konstan
- **Ablation Study** — Menguji kontribusi tiap komponen dengan melepasnya satu per satu
- **Configuration-driven Execution** — Semua parameter di config file, bukan hardcoded

---

## Template A.6 — Mapping RQ ke Arsitektur Sistem

```
SYSTEM-EXPERIMENT MAPPING

Research Question:
  RQ1: Perbedaan response time PostgreSQL vs MySQL pada CRUD?
  RQ2: Dampak indexing strategy terhadap response time?
  RQ3: Interaksi DBMS × indexing × optimization terhadap response time?

Variable → Component Mapping:
| Variabel | Tipe | Komponen Sistem | Cara Manipulasi/Pengukuran |
|----------|------|-----------------|---------------------------|
| Jenis DBMS | IV | DBMS Connection Module | Config: dbms=postgresql atau dbms=mysql |
| Indexing Strategy | IV | Index Manager Module | Config: index_type=none/single/composite; CREATE INDEX / DROP INDEX script |
| Query Optimization | IV | Query Template Module | Config: query_version=default/optimized; separate SQL template files |
| Volume Data | CV | Data Generator Module | Config: record_count=50000/100000/250000/500000/1000000 (tetap per trial) |
| Response Time | DV | Benchmark Logger Module | Otomatis capture start_time - end_time per query (ms precision) |
| Throughput | DV | Throughput Calculator Module | Hitung QPS dari batch execution: total_queries / elapsed_time |
| Jenis Operasi CRUD | CV | Query Executor Module | Config: operation=SELECT/INSERT/UPDATE/DELETE (tetap per trial) |

4 Prinsip Desain:
  [x] Traceability — Setiap komponen bisa ditelusuri ke variabel riset
  [x] Variable Isolation — IV (DBMS, indexing, optimization) bisa diubah tanpa mengubah CV (volume, skema, hardware)
  [x] Measurement Integration — Benchmark Logger dan Throughput Calculator built-in
  [x] Reproducibility — Setup bisa direkonstruksi dari config file (YAML)

Experimental Setup:
  Input data     : Dataset terstandarisasi (Google Playstore-like schema: 19 kolom, berbagai tipe data)
  Parameter      : dbms (postgresql/mysql), index_type (none/single/composite), query_version (default/optimized), record_count (50K-1M), operation (SELECT/INSERT/UPDATE/DELETE)
  Output format  : JSON log: {timestamp, dbms, index_type, query_version, operation, record_count, response_time_ms, throughput_qps, cpu_usage_pct, memory_usage_mb}
```

---

## Latihan 1 — Variable-to-Component Mapping

Gunakan RQ dan variabel dari WS-05. Petakan ke komponen sistem.

**RQ:** RQ1: Perbedaan response time PostgreSQL vs MySQL pada CRUD? RQ2: Dampak indexing strategy? RQ3: Interaksi DBMS × indexing × optimization?

| Variabel | Tipe | Komponen Sistem | Cara Manipulasi / Pengukuran |
|----------|------|-----------------|----------------------------|
| Jenis DBMS | IV | DBMS Connection Module | Config: dbms=postgresql atau dbms=mysql; koneksi ke server masing-masing DBMS |
| Indexing Strategy | IV | Index Manager Module | Config: index_type=none/single/composite; script CREATE/DROP INDEX otomatis |
| Query Optimization | IV | Query Template Module | Config: query_version=default/optimized; file template SQL terpisah |
| Volume Data | CV | Data Generator Module | Config: record_count=50000/100000/250000/500000/1000000 (locked per trial) |
| Response Time | DV | Benchmark Logger Module | Otomatis capture start_time dan end_time menggunakan high-resolution timer, hitung elapsed_time (ms) |
| Throughput | DV | Throughput Calculator Module | Hitung QPS dari batch: total_queries_completed / total_elapsed_time |
| Jenis Operasi CRUD | CV | Query Executor Module | Config: operation=SELECT/INSERT/UPDATE/DELETE (locked per trial) |

**Apakah semua variabel bisa di-map?** [x] Ya / [ ] Tidak
> Jika tidak, komponen apa yang perlu ditambahkan? —

---

## Latihan 2 — 4 Prinsip Desain

Evaluasi desain sistem terhadap 4 prinsip.

| Prinsip | Status | Bukti / Penjelasan |
|---------|--------|-------------------|
| Traceability | ✅ | Setiap modul (DBMS Connection, Index Manager, Query Template, Data Generator, Benchmark Logger, Throughput Calculator, Query Executor) dapat ditelusuri ke satu atau lebih variabel RQ. |
| Modularity | ✅ | DBMS Connection Module bisa di-swap antara PostgreSQL dan MySQL tanpa mengubah modul lain. Index Manager bisa toggle antara none/single/composite tanpa mengubah Query Executor atau Logger. |
| Controllability | ✅ | Semua CV (volume data, skema database, hardware spec) dikontrol melalui config file YAML yang locked selama satu trial. Indexing strategy sebagai IV dikonfigurasi via script terpisah yang dijalankan sebelum trial. |
| Measurability | ✅ | Benchmark Logger otomatis menghasilkan output JSON terstruktur untuk DV: response_time_ms, throughput_qps. Output siap untuk analisis statistik langsung. |

**Prinsip mana yang paling sulit dipenuhi?** Controllability
**Strategi untuk mengatasinya:**
> Menggunakan konfigurasi YAML yang eksplisit untuk semua parameter (DBMS, indexing, optimization, volume data, operasi CRUD). Sebelum setiap trial, jalankan setup script yang: (1) drop dan recreate database, (2) generate data sesuai record_count, (3) apply indexing sesuai index_type, (4) clear DBMS cache. Dokumentasikan versi config dan checksum dataset yang digunakan untuk setiap trial agar fully reproducible. Gunakan Docker container untuk kedua DBMS dengan resource limit yang identik.

---

## Latihan 3 — Ablation Study Planning

Jika sistem memiliki komponen utama untuk indexing dan optimization, rencanakan ablation study.

| Kondisi | DBMS | Indexing | Optimization | Benchmark Logger | Throughput Calc | Hasil yang Diharapkan |
|---------|------|----------|-------------|-----------------|----------------|---------------------|
| Full (baseline) | PostgreSQL | None | Default | ✅ On | ✅ On | Baseline: response time tanpa optimasi apapun |
| + Single Index | PostgreSQL | Single | Default | ✅ On | ✅ On | Dampak single-column index saja |
| + Composite Index | PostgreSQL | Composite | Default | ✅ On | ✅ On | Dampak composite index saja |
| + Optimized Query | PostgreSQL | None | Optimized | ✅ On | ✅ On | Dampak query rewriting saja |
| Full Optimized | PostgreSQL | Composite | Optimized | ✅ On | ✅ On | Dampak kombinasi indexing + optimization |
| Full (MySQL) | MySQL | None | Default | ✅ On | ✅ On | Baseline MySQL tanpa optimasi |
| + MySQL Optimized | MySQL | Composite | Optimized | ✅ On | ✅ On | Dampak kombinasi pada MySQL |
| – Benchmark Logger | PostgreSQL | Composite | Optimized | ❌ Off | ✅ On | Tidak bisa mengukur response time per query (data hilang) |
| – Throughput Calc | PostgreSQL | Composite | Optimized | ✅ On | ❌ Off | Tidak bisa mengukur QPS (throughput unknown) |

**Komponen mana yang diprediksi paling berkontribusi?** Index Manager Module (modul pengelolaan indexing)
**Mengapa?**
> Indexing adalah teknik optimasi paling fundamental di database dan dampaknya terhadap response time sangat signifikan, terutama pada query SELECT dan UPDATE/DELETE dengan WHERE clause. Tanpa Index Manager, tidak bisa mengisolasi dampak indexing dari faktor lain. Selain itu, inkonsistensi hasil studi sebelumnya (Gap dari WS-03) diduga kuat disebabkan oleh ketiadaan kontrol indexing, sehingga modul ini adalah kunci untuk menjawab RQ2 dan RQ3.

---

## Refleksi

> Apa risiko jika sistem dibangun seperti produk (monolitik, fitur lengkap) lalu baru dilakukan eksperimen? Mengapa arsitektur modular penting untuk riset?

**Jawaban:**
> Risiko monolitik: sulit mengisolasi variabel karena semua komponen terikat erat. Jika ingin membandingkan PostgreSQL vs MySQL dengan dan tanpa indexing, tidak bisa swap DBMS atau toggle indexing tanpa rebuild seluruh sistem. Hasilnya tidak bisa direproduksi, dan sulit tahu kontribusi setiap faktor (indexing vs optimization vs DBMS). Arsitektur modular penting karena memungkinkan toggle variabel independen (DBMS swap, indexing config, query template swap) melalui config-driven execution, sehingga hanya variabel eksperimen yang berubah, CV terkontrol, dan DV dapat diukur dengan bersih. Dengan modular design, eksperimen menjadi reproducible dan causal inferences lebih kuat karena isolasi variabel terjaga. Dalam konteks benchmarking DBMS, modularitas memastikan bahwa setiap faktor (DBMS, indexing, optimization) dapat diukur dampaknya secara independen dan dalam interaksi.