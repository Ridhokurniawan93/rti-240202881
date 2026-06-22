# WS-05: Variabel & Metrik

> **Bab 5 — Metric, Measurement & Data**

---

## Ringkasan Materi

### Measurement Alignment Model

Setiap pengukuran yang valid harus bisa ditelusuri melalui rantai ini tanpa lompatan logis:

```
Problem → Concept → Variable → Metric → Data → Result
```

### Operationalization = Keputusan Desain

Menerjemahkan konsep abstrak menjadi variabel terukur bukan proses mekanis. "Database performance" yang diukur via response time membawa asumsi implisit bahwa kecepatan eksekusi query adalah satu-satunya indikator performa. Setiap operasionalisasi harus didokumentasikan dan dijustifikasi.

### Empat Tipe Data (NOIR)

| Tipe | Ciri | Contoh | Operasi Valid |
|------|------|--------|---------------|
| **Nominal** | Kategori, tanpa urutan | Jenis DBMS (MySQL, PostgreSQL) | Modus, chi-square |
| **Ordinal** | Urutan, interval tidak sama | Ranking performa (terbaik, sedang, terburuk) | Median, Spearman |
| **Interval** | Jarak bermakna, tanpa nol absolut | Suhu Celsius | Mean, Pearson, t-test |
| **Ratio** | Jarak bermakna + nol absolut | Response time (ms), throughput (QPS) | Semua operasi |

Tipe data menentukan uji statistik yang valid. Kebanyakan metrik performa TI = ratio; persepsi pengguna = ordinal.

### Kriteria Pemilihan Metrik

- **Representative** — Mewakili konsep yang diteliti
- **Sensitive** — Cukup peka menangkap perbedaan bermakna (hindari ceiling effect)
- **Feasible** — Bisa dikumpulkan dalam batasan waktu dan biaya

### Pre-registration

Metrik harus ditentukan **sebelum** eksperimen. Memilih metrik setelah melihat data = **p-hacking**. Metrik tambahan yang ditemukan kemudian dilaporkan sebagai *exploratory*, bukan *confirmatory*.

### Primary vs Secondary Metric

- **Primary Metric** — Langsung terikat ke hipotesis, menentukan kesimpulan
- **Secondary Metric** — Pendukung, dilaporkan di samping primary; statusnya suplementer

### Research vs Engineering

| Aspek | Engineering | Research |
|-------|------------|----------|
| Pemilihan metrik | Berdasarkan kebiasaan/tool yang ada | Berdasarkan construct validity |
| Anomali | Dihapus untuk laporan bersih | Diinvestigasi — bisa jadi temuan |
| Kapan dipilih | Setelah sistem jadi (monitoring) | Sebelum eksperimen (by design) |

### Istilah Penting

- **Operationalization** — Transformasi konsep abstrak menjadi variabel terukur
- **Construct Validity** — Sejauh mana pengukuran benar-benar mengukur konsep yang dimaksud
- **Measurement Scale** — Klasifikasi data (NOIR) yang menentukan analisis valid
- **Multi-metric Evaluation** — Menggunakan beberapa metrik untuk menangkap konsep kompleks

---

## Template A.5 — Definisi Variabel, Metrik & Justifikasi

```
VARIABLE & METRIC DEFINITION

Research Question:
  RQ1: Apakah terdapat perbedaan signifikan dalam response time antara PostgreSQL dan MySQL pada workload CRUD?
  RQ2: Bagaimana dampak indexing strategy terhadap response time PostgreSQL dan MySQL?
  RQ3: Apakah terdapat interaksi signifikan antara DBMS, indexing strategy, dan query optimization terhadap response time?

| Variabel | Tipe | Konsep | Metrik | Skala | Satuan | Cara Mengukur | Justifikasi |
|----------|------|--------|--------|-------|--------|---------------|-------------|
| Jenis DBMS | IV | Sistem manajemen database yang diuji | Kategori: PostgreSQL vs MySQL | Nominal | — | Klasifikasi berdasarkan DBMS yang digunakan | Memilih DBMS sebagai IV memungkinkan perbandingan langsung performa kedua sistem |
| Indexing Strategy | IV | Strategi pengindeksan yang diterapkan | Kategori: no-index, single-column index, composite index | Nominal | — | Dokumentasi konfigurasi index pada tabel yang diuji | Indexing adalah teknik optimasi utama di database; mengontrol variasi ini memungkinkan pengukuran dampaknya |
| Query Optimization | IV | Tingkat optimasi query yang dijalankan | Kategori: default query vs optimized query | Nominal | — | Dokumentasi versi query yang digunakan (default vs rewritten) | Developer sering melakukan query rewriting untuk meningkatkan performa; variabel ini menangkap dampaknya |
| Volume Data | CV | Jumlah record dalam database | 50.000, 100.000, 250.000, 500.000, 1.000.000 | Ratio | Record | Generate dataset dengan jumlah record yang ditentukan | Volume data memengaruhi response time secara signifikan (Hairah, 2020); dikontrol sebagai CV untuk memastikan fairness |
| Response Time | DV | Waktu yang dibutuhkan DBMS untuk mengeksekusi satu query | Waktu eksekusi query dari submit hingga result diterima | Ratio | Milidetik (ms) | Capture waktu mulai dan selesai eksekusi query menggunakan script benchmarking otomatis | Response time adalah metrik performa paling fundamental dan langsung terikat ke hipotesis (Hairah, 2020; Ahsa et al., 2023; Praba & Safitri, 2020) |
| Throughput | DV (Secondary) | Jumlah query yang dapat diproses per detik | Queries per second (QPS) | Ratio | QPS | Hitung jumlah query yang selesai dalam interval waktu tertentu | Throughput melengkapi response time dengan perspektif kapasitas; relevan untuk skenario concurrent access |
| Jenis Operasi CRUD | CV | Jenis query yang dijalankan | Kategori: SELECT, INSERT, UPDATE, DELETE | Nominal | — | Dokumentasi query yang dijalankan | Setiap operasi CRUD memiliki karakteristik performa berbeda; dikontrol untuk analisis per-operasi |

Alignment Check:
  RQ → Concept → Variable → Metric → Data → Result
  [x] Setiap langkah terdokumentasi
  [x] Tidak ada "lompatan logis"
  [x] Metrik mengukur apa yang dimaksud (construct validity)
```

---

## Latihan 1 — Operationalization Chain

Gunakan RQ dari WS-04. Definisikan variabel dan metriknya.

**RQ:** RQ1: Perbedaan response time PostgreSQL vs MySQL pada CRUD? RQ2: Dampak indexing strategy? RQ3: Interaksi DBMS × indexing × optimization?

| Variabel | Tipe | Konsep Abstrak | Metrik Konkret | Skala (NOIR) | Satuan |
|----------|------|---------------|----------------|-------------|--------|
| Jenis DBMS | IV | Sistem database yang dibandingkan | PostgreSQL vs MySQL | Nominal | — |
| Indexing Strategy | IV | Strategi pengindeksan tabel | No-index / Single-column / Composite | Nominal | — |
| Query Optimization | IV | Tingkat optimasi query | Default query / Optimized query | Nominal | — |
| Volume Data | CV | Jumlah record dalam database | 50K, 100K, 250K, 500K, 1M | Ratio | Record |
| Response Time | DV | Kecepatan eksekusi query | Waktu eksekusi query (start-to-end) | Ratio | Milidetik (ms) |
| Throughput | DV (Sec) | Kapasitas pemrosesan query | Queries per second | Ratio | QPS |
| Jenis Operasi | CV | Tipe query CRUD | SELECT / INSERT / UPDATE / DELETE | Nominal | — |

**Apakah ada lompatan logis dalam rantai?** [ ] Ya / [x] Tidak
> Jika ya, di mana? —

---

## Latihan 2 — Evaluasi Metrik

Evaluasi metrik DV yang dipilih di Latihan 1 menggunakan 3 kriteria.

| Kriteria | Skor (1-5) | Justifikasi |
|----------|-----------|-------------|
| Representative | 5 | Response time (ms) secara langsung mencerminkan kecepatan eksekusi query — konsep performa database yang paling fundamental dan digunakan secara konsisten di semua studi referensi (Hairah, 2020; Ahsa et al., 2023; Winata & Putra, 2021; Wendri et al., 2022; Praba & Safitri, 2020). |
| Sensitive | 5 | Metrik ratio (ms) sangat peka terhadap perubahan performa, bahkan perbedaan kecil (beberapa ms) dapat terdeteksi. Tidak ada ceiling effect karena response time bisa bervariasi dari < 1 ms hingga puluhan detik. |
| Feasible | 5 | Response time dapat diukur secara otomatis menggunakan script benchmarking (Python, shell script) dengan presisi milidetik. Tidak memerlukan tool berbayar. |

**Apakah perlu secondary metric?** [x] Ya / [ ] Tidak
> Jika ya, apa dan mengapa? Throughput (QPS) sebagai secondary metric untuk menangkap aspek kapasitas pemrosesan yang tidak tercermin oleh response time tunggal. Dalam skenario nyata, database harus menangani banyak query secara bersamaan, sehingga throughput memberikan perspektif tambahan tentang performa DBMS.

**Contoh kasus ceiling effect untuk metrik ini:**
> Pada volume data kecil (misalnya 250 record), response time bisa sangat kecil (< 1 ms) sehingga perbedaan antar DBMS sulit terdeteksi. Oleh karena itu, pengujian menggunakan variasi volume data dari 50.000 hingga 1.000.000 record untuk memastikan perbedaan performa dapat terukur secara signifikan.

---

## Latihan 3 — Data Quality Check

Bayangkan data yang akan dikumpulkan dari eksperimen. Evaluasi 4 dimensi kualitas data.

| Dimensi | Pertanyaan | Jawaban | Strategi Mitigasi |
|---------|-----------|---------|------------------|
| Completeness | Apakah semua data point terkumpul? | Data harus mencakup semua kombinasi: 2 DBMS × 3 indexing × 2 optimization × 4 CRUD × 5 volume × N replikasi | Gunakan script otomatis yang mengeksekusi semua kondisi secara berurutan; log setiap eksekusi dengan timestamp dan status; verifikasi jumlah record setelah eksekusi |
| Consistency | Apakah ada kontradiksi internal? | Periksa apakah response time masuk akal (misalnya, INSERT tidak mungkin lebih cepat dari SELECT pada dataset besar tanpa index) | Validasi log dengan sanity check; ulangi pengukuran outlier; gunakan cold start (clear cache) sebelum setiap trial |
| Validity | Apakah benar-benar mengukur yang dimaksud? | Response time harus mengukur waktu eksekusi query murni, bukan termasuk network latency atau client processing time | Ukur response time langsung di server menggunakan EXPLAIN ANALYZE (PostgreSQL) atau profiling (MySQL); minimalisir network overhead dengan menjalankan script di server yang sama |
| Representativeness | Apakah sampel mewakili populasi target? | Dataset harus mencakup variasi data yang representatif (berbagai tipe data, NULL values, duplicate values) | Gunakan generator data yang menghasilkan data realistis dengan distribusi normal/uniform; sertakan edge cases (empty table, all NULL, duplicate keys) |

---

## Refleksi

> Mengapa memilih metrik setelah melihat data dianggap p-hacking? Apa bedanya dengan eksplorasi data yang sah?

**Jawaban:**
> Memilih metrik setelah melihat data dianggap p-hacking karena keputusan tersebut dapat diarahkan untuk mendapatkan hasil signifikan secara statistik, bukan berdasarkan konstruk penelitian yang konsisten. Misalnya, jika peneliti melihat bahwa throughput menunjukkan perbedaan signifikan tetapi response time tidak, lalu memutuskan untuk hanya melaporkan throughput — ini bias seleksi. Eksplorasi data yang sah tetap memisahkan metrik yang telah ditentukan sebelumnya (confirmatory) dari temuan tambahan yang dilaporkan sebagai exploratory, sehingga transparansi dan validitas penelitian terjaga. Dalam konteks benchmarking DBMS, response time dan throughput harus ditentukan sebelum eksperimen sebagai primary dan secondary metric.