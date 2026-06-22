# WS-03: Literature Mapping & Gap

> **Bab 3 — Literature Review, Research Gap & Baseline**

---

## Ringkasan Materi

### Literature Review = Positioning, Bukan Ringkasan

Literature review bukan merangkum paper satu per satu. Pendekatan yang benar adalah **concept-centric** — organisasi berdasarkan tema, metode, atau variabel. Tujuan: menemukan **pola, kontradiksi, dan gap**.

Literatur diorganisir dalam 3 konsep utama:
1. **Perbandingan Performa DBMS** — MySQL vs PostgreSQL, metrik response time, throughput
2. **Query Optimization & Indexing Strategy** — teknik optimasi query, jenis indexing, dampaknya terhadap performa
3. **Workload CRUD** — operasi SELECT, INSERT, UPDATE, DELETE dan karakteristik performanya

**Perbandingan pendekatan Author-centric vs Concept-centric:**

| Aspek | Author-centric (Hindari) | Concept-centric (Gunakan) |
|-------|--------------------------|---------------------------|
| Struktur | Per penulis/paper ("Hairah et al. menyatakan...") | Per konsep/metode ("Pengujian response time pada query inner join") |
| Tujuan | Ringkasan isi paper | Perbandingan metode & identifikasi gap |
| Contoh paragraph | "Hairah (2020) pakai F-test. Ahsa (2023) pakai CRUD. Wendri (2022) pakai Sysbench." | "Tiga pendekatan dominan dalam benchmarking DBMS: pengujian response time query tunggal (Hairah, 2020; Praba & Safitri, 2020), pengujian CRUD lengkap (Ahsa et al., 2023; Winata & Putra, 2021), dan benchmarking berbasis beban kerja (Wendri et al., 2022)." |
| Hasil akhir | Daftar paper | Peta pengetahuan + gap yang teridentifikasi |

### Empat Jenis Research Gap

| Jenis Gap | Deskripsi | Contoh |
|-----------|----------|--------|
| **Performance Gap** | Performa belum memadai | Hasil perbandingan tidak konsisten antar studi |
| **Method Gap** | Pendekatan belum diterapkan | Belum ada yang mengontrol indexing strategy sebagai variabel eksperimen |
| **Data Gap** | Dataset terbatas/tidak representatif | Semua studi pakai skema database sederhana tanpa relasi kompleks |
| **Context Gap** | Belum diuji pada konteks berbeda | Belum ada evaluasi dampak indexing dan optimization pada workload CRUD lengkap |

Gap terkuat = kombinasi 2+ jenis.

### Systematic Search Strategy

1. **Database utama**: IEEE Xplore, ACM DL, Scopus
   - Akses IEEE/ACM melalui jaringan kampus atau VPN institusi
   - Alternatif bebas biaya: Google Scholar, ResearchGate ([researchgate.net](https://www.researchgate.net)), arXiv ([arxiv.org](https://arxiv.org))
2. **Boolean query** yang terdokumentasi eksplisit
   - Contoh: `("MySQL" OR "PostgreSQL") AND ("performance" OR "benchmarking") AND ("query optimization" OR "indexing") AND ("CRUD" OR "workload")`
   - Gunakan tanda kutip untuk frasa eksak; AND/OR/NOT mengontrol scope
3. **Snowballing** — dua arah:
   - **Backward snowballing**: buka daftar referensi di paper kunci → telusuri paper yang dikutip
   - **Forward snowballing**: di Google Scholar, klik "Cited by" di bawah paper kunci → temukan paper yang mengutipnya
   - Ulangi 1–2 tingkat untuk membangun cakupan komprehensif
4. Klaim "belum ada penelitian" harus didukung **bukti pencarian**

### Baseline Selection — 3 Kriteria

| Kriteria | Pertanyaan | Contoh |
|----------|-----------|--------|
| **Relevan** | Apakah menyelesaikan masalah yang sama? | Ahsa et al. (2023) relevan: perbandingan performa MySQL vs PostgreSQL dengan CRUD |
| **Representatif** | Apakah mewakili common practice? | Pengujian response time CRUD tanpa indexing = common practice di studi sebelumnya |
| **State-of-the-Art** | Apakah terbaru/terbaik? | Wendri et al. (2022) menggunakan Sysbench dan Independent Sample T-Test, pendekatan lebih rigor |

Membandingkan PostgreSQL (dengan indexing + optimization) vs MySQL (tanpa indexing, default config) = **straw man comparison** (perbandingan tidak jujur).

### Research vs Engineering

| Aspek | Engineering | Research |
|-------|------------|----------|
| Tujuan baca literatur | Mencari solusi yang sudah ada | Memahami apa yang belum terjawab |
| Cara membaca paper | Tutorial, how-to | Metode, limitasi, gap |
| Baseline | Framework terpopuler | State-of-the-art yang rigorous |
| Dokumentasi pencarian | Tidak diperlukan | Wajib (reproducible) |

### Istilah Penting

- **Concept-centric** — Organisasi literatur berdasarkan konsep/metode, bukan per penulis
- **Snowballing** — Backward (telusuri referensi) + Forward (cari yang mengutip paper kunci)
- **Research Position** — Pernyataan eksplisit posisi riset terhadap studi sebelumnya
- **Straw man comparison** — Memilih baseline lemah agar metode sendiri terlihat lebih baik

---

## Template A.3 — Literature Mapping & Gap Identification

```
LITERATURE MAPPING

Topik      : Analisis Dampak Query Optimization dan Indexing Strategy terhadap Performa PostgreSQL dan MySQL dalam Workload CRUD
Database   : Google Scholar, IEEE Xplore
Query      : ("MySQL" OR "PostgreSQL") AND ("performance" OR "benchmarking") AND ("query optimization" OR "indexing" OR "response time") AND ("CRUD")
Tahun      : 2020-2023
Hasil awal : 10 paper → Screening → 5 paper final

Literature Matrix (concept-centric):

| Study | Tahun | Method | Data | Result | Limitation |
|-------|-------|--------|------|--------|------------|
| Hairah | 2020 | F-test & T-test pada response time inner join query | Database pharmacy, 50.000-1.050.000 record | PostgreSQL lebih cepat dari MySQL pada inner join; F-test menunjukkan pengaruh signifikan jumlah data dan relasi terhadap response time | Hanya menguji query inner join, bukan workload CRUD lengkap; tidak ada kontrol indexing strategy |
| Ahsa et al. | 2023 | Pengujian CRUD (SELECT, INSERT, UPDATE, DELETE) | Dataset Google Playstore, 19 kolom, 50.000-250.000 record | PostgreSQL lebih unggul dengan response time tidak pernah lebih dari 4 detik; selisih rata-rata 481,24s pada INSERT | Tidak menguji strategi indexing; konfigurasi default tanpa optimasi; tidak ada analisis statistik inferensial |
| Winata & Putra | 2021 | Pengujian response time CRUD pada 3 database (MySQL, PostgreSQL, MongoDB) | Dataset Android Permission, 6 kolom, 250-25.000 record | PostgreSQL paling unggul dengan response time tidak pernah lebih dari 150ms; MySQL paling lambat | Tidak menguji indexing; dataset relatif kecil (max 25.000); tanpa relasi antar tabel |
| Wendri et al. | 2022 | Sysbench benchmarking + Independent Sample T-Test | 24 tabel × 100.000 record, client-server setup | MySQL lebih baik dari PostgreSQL pada Read, Write, Transaction, Average, dan Execution Time | Menggunakan Sysbench (OLTP workload) bukan custom CRUD queries; tidak membahas indexing strategy secara eksplisit |
| Praba & Safitri | 2020 | Pengujian response time dengan query SELECT, JOIN, COUNT | Dataset Faker (data mahasiswa), 50.000-1.000.000 record | PostgreSQL lebih cepat dengan selisih rata-rata 0,44s; PostgreSQL lebih unggul pada semua query | Tidak menguji INSERT, UPDATE, DELETE; tidak ada kontrol indexing; tanpa analisis statistik inferensial |

Pola yang ditemukan:
  Metode dominan     : Pengujian response time per query pada kedua DBMS dengan variasi volume data
  Dataset umum       : Dataset sintetis atau publik (pharmacy, Google Playstore, Android Permission, Faker)
  Limitasi berulang  : Tidak ada kontrol strategi indexing sebagai variabel; sebagian besar tidak menggunakan analisis statistik inferensial; workload tidak selalu mencakup CRUD lengkap

GAP IDENTIFICATION

Gap 1: [Jenis: method]
  Deskripsi    : Studi sebelumnya tidak mengontrol strategi indexing (no index, single-column, composite) sebagai variabel independen dalam perbandingan performa DBMS
  Bukti        : Hairah (2020), Ahsa et al. (2023), Winata & Putra (2021), Praba & Safitri (2020) menggunakan konfigurasi default tanpa variasi indexing; Wendri et al. (2022) menggunakan Sysbench tanpa membahas indexing secara eksplisit
  Signifikansi : Tanpa kontrol indexing, perbedaan performa yang dilaporkan mungkin disebabkan oleh strategi indexing default DBMS, bukan kemampuan inherent

Gap 2: [Jenis: performance]
  Deskripsi    : Hasil perbandingan performa MySQL vs PostgreSQL tidak konsisten antar studi
  Bukti        : Hairah (2020), Ahsa et al. (2023), Winata & Putra (2021), Praba & Safitri (2020) menyimpulkan PostgreSQL lebih cepat; Wendri et al. (2022) menyimpulkan MySQL lebih baik pada throughput dan execution time
  Signifikansi : Inkonsistensi menunjukkan adanya confounding variable (konfigurasi, indexing, workload) yang belum dikontrol

Gap 3: [Jenis: data]
  Deskripsi    : Tidak ada studi yang menguji interaksi antara query optimization (rewritten/optimized query) dan indexing strategy terhadap performa kedua DBMS secara simultan
  Bukti        : Studi sebelumnya hanya menguji query default tanpa variasi optimization level
  Signifikansi : Dalam praktik nyata, developer menggunakan kombinasi query optimization dan indexing; pemahaman interaksi keduanya penting untuk tuning yang optimal

Baseline Selection:
| Baseline | Relevansi | Representatif | Source |
|----------|-----------|---------------|--------|
| Pengujian CRUD tanpa indexing (Ahsa et al., 2023) | Menguji performa CRUD pada MySQL vs PostgreSQL | Mewakili common practice di studi perbandingan DBMS | Ahsa et al. (2023), Winata & Putra (2021) |
| Benchmarking dengan Sysbench + T-Test (Wendri et al., 2022) | Menggunakan metode statistik rigor untuk perbandingan performa | Mewakili pendekatan state-of-the-art dalam benchmarking DBMS | Wendri et al. (2022) |
```

---

## Latihan 1 — Concept-Centric Literature Table

Gunakan topik riset dari WS-02. Cari minimal 5 paper relevan menggunakan database akademik.

**Topik riset:** Analisis Dampak Query Optimization dan Indexing Strategy terhadap Performa PostgreSQL dan MySQL dalam Workload CRUD
**Query pencarian:** ("MySQL" OR "PostgreSQL") AND ("performance" OR "benchmarking") AND ("query optimization" OR "indexing" OR "response time") AND ("CRUD")
**Database:** Google Scholar, IEEE Xplore

| # | Study | Tahun | Method | Dataset | Result | Limitasi |
|---|-------|-------|--------|---------|--------|----------|
| 1 | Hairah | 2020 | F-test & T-test pada response time inner join | Database pharmacy, 50.000-1.050.000 record, 21 eksperimen | PostgreSQL lebih cepat; F-test menunjukkan pengaruh signifikan jumlah data dan relasi | Hanya inner join, bukan CRUD lengkap; tanpa kontrol indexing |
| 2 | Ahsa et al. | 2023 | CRUD benchmarking (SELECT, INSERT, UPDATE, DELETE) | Google Playstore dataset, 19 kolom, 50.000-250.000 record | PostgreSQL lebih unggul; selisih rata-rata 481,24s pada INSERT | Tanpa indexing strategy; tanpa analisis statistik inferensial |
| 3 | Winata & Putra | 2021 | CRUD benchmarking pada 3 database | Android Permission, 6 kolom, 250-25.000 record | PostgreSQL paling unggul (< 150ms); MySQL paling lambat | Dataset kecil; tanpa relasi; tanpa indexing |
| 4 | Wendri et al. | 2022 | Sysbench OLTP + Independent Sample T-Test | 24 tabel × 100.000 record, client-server | MySQL lebih baik pada Read, Write, Transaction, Average, Execution Time | OLTP workload bukan custom CRUD; tidak membahas indexing eksplisit |
| 5 | Praba & Safitri | 2020 | Response time: SELECT, JOIN, COUNT | Dataset Faker, 50.000-1.000.000 record | PostgreSQL lebih cepat; selisih rata-rata 0,44s | Tanpa INSERT, UPDATE, DELETE; tanpa kontrol indexing; tanpa statistik inferensial |

**Pola yang terlihat — Metode dominan:** Pengujian response time per query dengan variasi volume data pada kedua DBMS
**Limitasi yang berulang:** Ketiadaan kontrol strategi indexing sebagai variabel; inkonsistensi hasil antar studi; sebagian besar tanpa analisis statistik inferensial

---

## Latihan 2 — Gap Identification

Berdasarkan tabel di Latihan 1, identifikasi gap.

| Jenis Gap | Ditemukan? | Gap Statement |
|-----------|-----------|---------------|
| Performance Gap | [x] Ya / [ ] Tidak | Hasil perbandingan performa MySQL vs PostgreSQL tidak konsisten: 4 studi menyimpulkan PostgreSQL lebih cepat, 1 studi menyimpulkan MySQL lebih baik |
| Method Gap | [x] Ya / [ ] Tidak | Tidak ada studi yang mengontrol strategi indexing dan query optimization sebagai variabel independen dalam perbandingan performa DBMS |
| Data Gap | [x] Ya / [ ] Tidak | Studi menggunakan dataset dan skema yang berbeda-beda tanpa standarisasi, menyulitkan perbandingan langsung |
| Context Gap | [ ] Ya / [x] Tidak | Konteks workload CRUD sudah cukup terwakili oleh beberapa studi |

**Gap utama yang dipilih:** Method Gap + Performance Gap (kombinasi) — Tidak adanya kontrol strategi indexing dan query optimization sebagai variabel, yang menyebabkan inkonsistensi hasil perbandingan performa MySQL vs PostgreSQL.
**Mengapa gap ini penting (bukan sekadar "belum ada yang meneliti")?**
> Gap ini penting karena inkonsistensi hasil antar studi (PostgreSQL lebih cepat vs MySQL lebih baik) menunjukkan adanya confounding variable yang belum dikontrol. Dalam praktik nyata, DBA selalu menggunakan indexing dan query optimization sebagai strategi tuning. Tanpa mengontrol variabel ini, klaim performa suatu DBMS menjadi tidak valid karena perbedaan mungkin disebabkan oleh konfigurasi, bukan kemampuan inherent DBMS.

---

## Latihan 3 — Baseline Selection

Pilih 2 baseline dari literatur yang sudah dibaca.

| # | Baseline | Mengapa Relevan | Mengapa Representatif | Apakah SOTA? | Sumber |
|---|----------|----------------|----------------------|-------------|--------|
| 1 | Pengujian CRUD tanpa indexing dan konfigurasi default (Ahsa et al., 2023) | Menguji performa CRUD MySQL vs PostgreSQL — masalah yang sama | Mewakili common practice di studi perbandingan DBMS sebelumnya | Bukan SOTA, tapi baseline standar | Ahsa et al. (2023), Winata & Putra (2021) |
| 2 | Benchmarking Sysbench dengan Independent Sample T-Test (Wendri et al., 2022) | Menggunakan metode statistik rigor dan setup client-server | Mewakili pendekatan yang lebih rigor dalam benchmarking DBMS | Lebih mendekati SOTA karena menggunakan statistical testing | Wendri et al. (2022), Hairah (2020) |

**Apakah pemilihan baseline ini bisa dianggap straw man?** [ ] Ya / [x] Tidak
> Justifikasi: Baseline dipilih karena relevan (menguji performa MySQL vs PostgreSQL) dan representatif (mewakili pendekatan umum dan rigor). Tidak straw man karena kedua DBMS akan diuji pada kondisi yang setara (fair comparison) — konfigurasi identik, indexing strategy dikontrol sebagai variabel, dan workload CRUD yang sama.

---

## Refleksi

> Apa perbedaan antara "belum ada yang meneliti ini" (klaim tanpa bukti) dengan research gap yang valid? Bagaimana cara membuktikan bahwa sebuah gap benar-benar ada?

**Jawaban:**
> "Belum ada yang meneliti ini" adalah klaim subjektif tanpa dukungan bukti, sering kali berdasarkan intuisi atau pengetahuan terbatas, yang bisa salah karena literatur yang luas. Research gap yang valid didukung oleh pencarian sistematis, analisis pola dari studi sebelumnya, dan identifikasi area yang belum dieksplorasi dengan signifikansi yang jelas. Untuk membuktikan gap ada, lakukan pencarian terdokumentasi menggunakan query Boolean di database akademik, snowballing backward dan forward, serta analisis concept-centric untuk menemukan pola, kontradiksi, atau keterbatasan yang konsisten. Dalam kasus ini, gap dibuktikan oleh inkonsistensi hasil antar studi (4 paper menyimpulkan PostgreSQL lebih cepat, 1 paper menyimpulkan MySQL lebih baik) dan ketiadaan kontrol indexing/optimization di kelima paper tersebut.