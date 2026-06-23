# Proposal Penelitian: Mitigasi JWKS Endpoint Flooding

## 1. Latar Belakang

API Gateway sering digunakan di arsitektur mikroservis untuk memvalidasi JWT yang diterbitkan oleh Identity Provider. JWT memuat header `kid` yang menunjuk ke JWK publik yang dipakai untuk verifikasi tanda tangan. Pada implementasi naif, setiap `kid` yang belum dikenal dapat memicu resolusi kunci baru ke datastore atau Identity Service.

Kerentanan yang dibahas dalam penelitian ini adalah **JWKS Endpoint Flooding**: penyerang mengirim banyak permintaan JWT dengan `kid` acak atau tidak terdaftar sehingga Gateway melakukan banyak query ke backend dan menyebabkan resource exhaustion. Masalah ini mirip dengan CVE-2026-48524 dan GHSA-fhv5-28vv-h8m8.

## 2. Rumusan Masalah

1. Bagaimana merancang mekanisme mitigasi yang menurunkan beban query backend akibat JWKS Endpoint Flooding?
2. Bagaimana memadukan Redis sebagai L1 cache (positive + negative cache) dengan PostgreSQL sebagai source of truth dan rate-limit counter?
3. Seberapa besar dampak mitigasi terhadap latensi traffic legitimate dan beban resource saat serangan?

## 3. Tujuan Penelitian

Tujuan penelitian ini adalah:

- Mendesain arsitektur hybrid caching untuk Gateway JWT/JWKS yang dapat memperkecil beban backend saat serangan flood.
- Mengimplementasikan API Gateway berbasis Go + Echo dengan mode `CACHE_MODE=none|hybrid`.
- Mengevaluasi performa dan efektivitas mitigasi menggunakan load testing k6 pada 5 varian traffic.
- Mengukur dampak mitigasi terhadap latency, throughput, cache hit ratio, query reduction, dan penggunaan CPU/memori.

## 4. Kontribusi

Kontribusi yang diharapkan:

- Desain hybrid caching untuk mitigasi JWKS Endpoint Flooding.
- Framework eksperimen yang membandingkan baseline tanpa cache dengan mitigasi hybrid.
- Temuan empiris pada 400 run (40 replikasi) yang menunjukkan apakah mitigasi melindungi traffic legitimate tanpa overhead signifikan.
- Rekomendasi arsitektural untuk implementasi gateway JWT yang tahan terhadap flooding serangan.

## 5. Metodologi Singkat

Metodologi penelitian meliputi:

- Perancangan arsitektur Tahap 1.
- Implementasi API Gateway dan migrasi database Tahap 2.
- Pengujian beban k6 Tahap 3.
- Analisis data & visualisasi Tahap 4.
- Penyusunan draf naskah dan laporan Tahap 5.

## 6. Struktur Direktori Proposal

- `01-proposal/` — dokumen proposal.
- `02-literatur/` — daftar pustaka dan matriks literatur.
- `03-teori/` — arsitektur dan skema database.
- `05-kode/` — implementasi Gateway, k6, dan analisis.
- `06-output/` — hasil olahan data dan figure.
- `07-manuskrip/` — draf naskah jurnal.
- `08-laporan/` — laporan penelitian.
- `09-docs/` — dokumen rencana dan status tiap tahap.
