# Proposal Penelitian: DBMS Benchmarking — Perbandingan Performa PostgreSQL vs MySQL pada Workload CRUD

## 1. Latar Belakang

PostgreSQL dan MySQL adalah dua sistem manajemen basis data relasional (RDBMS) terbuka yang paling banyak digunakan dalam aplikasi web dan sistem informasi. Meskipun keduanya open-source, karakteristik performa mereka berbeda signifikan tergantung pada konfigurasi, strategi indexing, dan optimasi query.

Dalam praktik industry, perbedaan performa antara kedua DBMS sering diperdebatkan namun belum divalidasi melalui eksperimen terkontrol secara komprehensif. Penelitian ini bermaksud mengisi gap tersebut dengan menjalankan benchmark sistematis pada workload CRUD (Create, Read, Update, Delete) dengan variasi indexing strategy dan volume data.

## 2. Rumusan Masalah

1. Apakah terdapat perbedaan signifikan dalam response time antara PostgreSQL dan MySQL pada workload CRUD?
2. Bagaimana dampak strategi indexing (no-index, single-column, composite) terhadap performa kedua DBMS?
3. Apakah terdapat interaksi signifikan antara DBMS, indexing strategy, dan optimasi query terhadap response time dan throughput?

## 3. Tujuan Penelitian

Tujuan penelitian ini adalah:

- Mengidentifikasi perbedaan performa antara PostgreSQL dan MySQL pada operasi CRUD dengan metrik response time dan throughput.
- Mengukur dampak strategi indexing terhadap performa kedua DBMS pada berbagai volume data (50K–1M record).
- Menganalisis trade-off antara latency read (SELECT) dan latency write (INSERT/UPDATE/DELETE) saat menggunakan composite indexing.
- Memberikan rekomendasi berbasis data untuk pemilihan DBMS dan strategi indexing dalam konteks workload CRUD.

## 4. Kontribusi

Kontribusi yang diharapkan:

- Dataset benchmark terstandarisasi (app_playstore 50K–1M record) dengan hasil eksperimen 600 trial (replikasi penuh).
- Analisis statistik komprehensif dengan uji ANOVA 2-way untuk faktor DBMS, indexing, dan volume.
- Temuan empiris tentang dampak kuantitatif indexing terhadap performa (e.g., composite index mengurangi SELECT latency ~72%).
- Rekomendasi implementasi untuk memilih DBMS dan strategi optimasi dalam project real-world.

## 5. Metodologi Singkat

Metodologi penelitian meliputi:

- Tahap 1 — Perancangan arsitektur dan skema database (schema CRUD standardized).
- Tahap 2 — Setup environment: PostgreSQL, MySQL, generate dataset, create indexing variations.
- Tahap 3 — Eksekusi benchmark CRUD (SELECT, INSERT, UPDATE, DELETE) pada 600 trial dengan 5 replikasi.
- Tahap 4 — Analisis data, statistik deskriptif, ANOVA, visualisasi.
- Tahap 5 — Penyusunan draf manuscript dan laporan penelitian.

## 6. Struktur Direktori Proposal

- `01-proposal/` — dokumen proposal dan rumusan masalah.
- `02-literatur/` — tinjauan pustaka, matriks literatur, daftar pustaka.
- `03-teori/` — arsitektur eksperimen, skema database, strategi indexing.
- `04-data/` — dataset benchmark dan raw hasil eksperimen.
- `05-kode/` — kode generator dataset, script benchmark, analisis statistik.
- `06-output/` — tabel hasil, visualisasi, statistik deskriptif.
- `07-manuskrip/` — draf naskah jurnal.
- `08-laporan/` — laporan penelitian lengkap.
- `09-docs/` — dokumentasi tahap eksekusi (tahap-1 s/d tahap-5).
- `08-laporan/` — laporan penelitian.
- `09-docs/` — dokumen rencana dan status tiap tahap.
