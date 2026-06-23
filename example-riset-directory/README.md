# [EXAMPLE] DBMS Benchmarking — Perbandingan Performa PostgreSQL vs MySQL

**Judul:** Performance Comparison of PostgreSQL vs MySQL on CRUD Workload with Indexing Strategy Variation

**Target publikasi:** Sinta 6 (Journal of Database Systems) atau Scopus Q3-Q4 (IEEE Transactions on Software Engineering)

## Ringkasan

Penelitian ini mengevaluasi perbandingan performa antara **PostgreSQL 16.3** dan **MySQL 8.0.32** dalam menangani operasi CRUD (Create, Read, Update, Delete) dengan variasi strategi indexing (no-index, single-column, composite) dan volume data (50K–1M record).

Metodologi menggunakan factorial design 2×3×5 (DBMS × Indexing × Volume) dengan 600 trial dan 5 replikasi. Metrik yang diukur: response time, throughput (QPS), CPU utilization, dan memory consumption. Analisis statistik menggunakan ANOVA 2-way dan effect size (η²).

Temuan utama:
- PostgreSQL 27% lebih cepat pada baseline (no-index)
- Composite indexing mengurangi SELECT latency hingga 72%
- Trade-off: composite index memberikan 28% write throughput penalty
- DBMS effect (η²=0.38), Indexing effect (η²=0.84), Interaction effect significant (p=0.002)

Detail lengkap topik & roadmap: [09-docs/](09-docs/)

## Struktur Direktori

| Folder | Isi |
|---|---|
| [00-admin/](00-admin/) | Administrasi penelitian (jadwal, korespondensi) |
| [01-proposal/](01-proposal/) | Proposal penelitian |
| [02-literatur/](02-literatur/) | Referensi & paper terkait (Tinjauan Pustaka) |
| [03-teori/](03-teori/) | Arsitektur & desain sistem (Tahap 1) |
| [04-data/](04-data/) | Data mentah hasil benchmark DBMS & metrik container |
| [05-kode/](05-kode/) | Source code: Generator dataset, script benchmark, analisis statistik (Python) |
| [06-output/](06-output/) | Statistik & visualisasi hasil benchmark (Tahap 4) |
| [07-manuskrip/](07-manuskrip/) | Draf naskah jurnal (Tahap 5) |
| [08-laporan/](08-laporan/) | Laporan progres/akhir penelitian |
| [09-docs/](09-docs/) | Dokumen perencanaan & roadmap tahap-tahap penelitian |

## Status Tahapan

- [x] **Tahap 1** — Perancangan Arsitektur & Skema Database — *Selesai* ([detail](09-docs/tahap-1-arsitektur-dan-skema-database.md))
- [x] **Tahap 2** — Setup Environment & Implementasi Benchmark — *Selesai* ([detail](05-kode/implementation-notes.md))
- [x] **Tahap 3** — Eksekusi Benchmark (600 trial, 5 replikasi) — *Selesai* ([detail](09-docs/tahap-3-pengujian-k6.md))
- [x] **Tahap 4** — Ekstraksi Data & Visualisasi — *Selesai* ([detail](09-docs/tahap-4-analisis-data.md))
- [x] **Tahap 5** — Draf Paper Jurnal — *Selesai* ([detail](09-docs/tahap-5-draf-paper.md))

## Laporan Penelitian

Laporan penelitian komprehensif (ringkasan eksekutif, metodologi per tahap, hasil benchmark, kendala, kesimpulan): [08-laporan/laporan-penelitian-lengkap.md](08-laporan/laporan-penelitian-lengkap.md)

## Author

Ridho Kurniawan
