# WS-04: Research Question & Hypothesis

> **Bab 4 — Research Question, Contribution & Hypothesis**

---

## Ringkasan Materi

### RQ Bukan Pertanyaan Biasa

Research Question yang baik secara implisit mengandung cetak biru eksperimen: subjek, baseline, metrik, domain, dataset.

| Kualitas | Contoh |
|----------|--------|
| **Buruk** | "Bagaimana pengaruh indexing terhadap performa database?" |
| **Baik** | "Apakah composite indexing menghasilkan response time SELECT yang lebih rendah dibandingkan no-index pada PostgreSQL dan MySQL dengan dataset 100.000-1.000.000 record?" |

Perbedaan: RQ yang baik menyebutkan **metode spesifik**, **metrik terukur**, **baseline**, dan **dataset**.

### Tiga Jenis RQ

| Jenis | Pola | Kebutuhan |
|-------|------|-----------|
| **Comparison** | A vs B → mana lebih baik? | ≥ 2 metode, metrik sama |
| **Improvement** | A' vs A → modifikasi lebih baik? | Pre/post, bukti perbaikan |
| **Exploratory** | Faktor X₁...Xₙ → pengaruh terhadap Y? | Multi-variabel, korelasi/regresi |

### Contribution Statement

Tiga jenis kontribusi: **Improvement** (metode terbukti lebih baik), **Comparison** (perbandingan sistematis yang belum ada), **Novel Approach** (pendekatan baru). Kontribusi harus terhubung langsung dengan gap — kontribusi tanpa gap = klaim tanpa justifikasi.

### Hypothesis H₀ / H₁

- **H₀** (Null) = Tidak ada perbedaan signifikan — asumsi default, harus dibuktikan salah
- **H₁** (Alternative) = Ada perbedaan signifikan — diterima hanya jika H₀ ditolak
- Harus **falsifiable**, mengandung **metrik terukur**, dirumuskan **SEBELUM eksperimen**

### Rantai Operasionalisasi

```
RQ → Variable → Metric → Data → Analysis
```

Jika rantai ini tidak lengkap, RQ belum mature. Bi-directional: RQ yang tidak bisa jadi hipotesis testable harus direvisi mundur.

### Research vs Engineering

| Aspek | Engineering | Research |
|-------|------------|----------|
| Tujuan pertanyaan | Apa yang harus dibangun? | Apa yang harus dibuktikan? |
| Bentuk jawaban | Sistem yang berfungsi | Bukti empiris terukur |
| Sukses diukur oleh | User satisfaction, uptime | Signifikansi statistik, effect size |
| Jika gagal | Debug dan perbaiki | Laporkan, analisis mengapa |

### Istilah Penting

- **Research Question (RQ)** — Pertanyaan spesifik: variabel terukur + metrik + konteks
- **Contribution Statement** — Apa yang diketahui setelah riset selesai yang sebelumnya belum ada
- **H₀ / H₁** — Null vs Alternative Hypothesis
- **Falsifiability** — Kondisi hipotesis ditolak harus bisa didefinisikan sebelum eksperimen
- **Operationalization** — Proses mewujudkan konsep abstrak menjadi variabel terukur

---

## Template A.4 — RQ-Contribution-Hypothesis

```
RQ-CONTRIBUTION-HYPOTHESIS

Gap Statement  : Studi sebelumnya tidak mengontrol strategi indexing dan query optimization sebagai variabel independen, menyebabkan inkonsistensi hasil perbandingan performa MySQL vs PostgreSQL (Method Gap + Performance Gap).

Research Question:
  RQ1:
    Tipe         : [x] Comparison  [ ] Improvement  [ ] Exploratory
    Formulasi    : Apakah terdapat perbedaan signifikan dalam response time (ms) antara PostgreSQL dan MySQL pada workload CRUD (SELECT, INSERT, UPDATE, DELETE) dengan variasi volume data (50.000, 100.000, 250.000, 500.000, 1.000.000 record)?
    Variabel IV  : Jenis DBMS (PostgreSQL vs MySQL)
    Variabel DV  : Response time (ms)
    Metrik       : Response time per query dalam milidetik
    Dataset      : Dataset terstandarisasi dengan volume 50.000 hingga 1.000.000 record
    Baseline     : Konfigurasi default tanpa indexing (no-index)

  RQ2:
    Tipe         : [ ] Comparison  [ ] Improvement  [x] Exploratory
    Formulasi    : Bagaimana dampak indexing strategy (no-index, single-column index, composite index) terhadap response time PostgreSQL dan MySQL pada workload CRUD?
    Variabel IV  : Indexing strategy (no-index, single-column, composite)
    Variabel DV  : Response time (ms), throughput (QPS)
    Metrik       : Response time per query (ms), queries per second
    Dataset      : Dataset terstandarisasi (sama dengan RQ1)
    Baseline     : No-index condition

  RQ3:
    Tipe         : [ ] Comparison  [ ] Improvement  [x] Exploratory
    Formulasi    : Apakah terdapat interaksi signifikan antara jenis DBMS, indexing strategy, dan query optimization terhadap response time pada workload CRUD?
    Variabel IV  : DBMS × Indexing × Query Optimization (faktor interaksi)
    Variabel DV  : Response time (ms)
    Metrik       : Response time per query (ms)
    Dataset      : Dataset terstandarisasi (sama dengan RQ1)
    Baseline     : Default query tanpa optimization, no-index

Quality Check RQ:
  [x] Variabel spesifik
  [x] Metrik jelas
  [x] Baseline ada
  [x] Konteks disebutkan
  [x] Memerlukan eksperimen (bukan hanya survei literatur)

Contribution Statement:
  Apa yang baru diketahui : Bukti empiris tentang dampak indexing strategy dan query optimization terhadap performa PostgreSQL dan MySQL pada workload CRUD, serta interaksi antar faktor tersebut.
  Jenis kontribusi        : [ ] Improvement  [x] Comparison  [ ] Novel approach
  Gap yang diisi          : Method Gap (kontrol indexing dan optimization) dan Performance Gap (inkonsistensi hasil studi sebelumnya).

Hypothesis Pair:
  H₀₁ : Tidak ada perbedaan signifikan dalam response time antara PostgreSQL dan MySQL pada workload CRUD.
  H₁₁ : Terdapat perbedaan signifikan dalam response time antara PostgreSQL dan MySQL pada minimal satu jenis operasi CRUD.

  H₀₂ : Indexing strategy (no-index, single-column, composite) tidak berdampak signifikan terhadap response time PostgreSQL dan MySQL.
  H₁₂ : Minimal satu indexing strategy menghasilkan response time yang signifikan lebih rendah dibandingkan no-index pada salah satu DBMS.

  H₀₃ : Tidak ada interaksi signifikan antara jenis DBMS, indexing strategy, dan query optimization terhadap response time.
  H₁₃ : Terdapat interaksi signifikan antara jenis DBMS, indexing strategy, dan query optimization terhadap response time.

  Threshold              : p < 0.05
  Justifikasi threshold  : Standar statistik umum dalam penelitian eksperimen; alpha 0.05 memberikan keseimbangan antara Type I dan Type II error.
```

---

## Latihan 1 — Dari Gap ke RQ

Gunakan gap yang ditemukan di WS-03. Transformasikan menjadi Research Question.

**Gap dari WS-03:** Method Gap (tidak ada kontrol indexing/optimization) dan Performance Gap (inkonsistensi hasil studi).

**RQ versi pertama (tulis bebas):**
> Apakah indexing dan query optimization memengaruhi performa MySQL dan PostgreSQL pada operasi CRUD?

**Evaluasi RQ:**

| Komponen | Ada? | Isi |
|----------|------|-----|
| Metode spesifik | Ya | PostgreSQL vs MySQL dengan variasi indexing dan optimization |
| Metrik terukur | Ya | Response time (ms), throughput (QPS) |
| Baseline | Ya | No-index condition, default query |
| Dataset/konteks | Ya | Dataset terstandarisasi, 50.000-1.000.000 record, workload CRUD |

**Tipe RQ:** [ ] Comparison / [ ] Improvement / [x] Exploratory (multi-factor)

**RQ versi revisi (setelah evaluasi):**
> (RQ1) Apakah terdapat perbedaan signifikan dalam response time antara PostgreSQL dan MySQL pada workload CRUD dengan variasi volume data?
> (RQ2) Bagaimana dampak indexing strategy (no-index, single-column, composite) terhadap response time PostgreSQL dan MySQL?
> (RQ3) Apakah terdapat interaksi signifikan antara DBMS, indexing strategy, dan query optimization terhadap response time pada workload CRUD?

---

## Latihan 2 — Hypothesis Pair

Rumuskan pasangan hipotesis dari RQ di Latihan 1.

| Komponen | Isi |
|----------|-----|
| H₀₁ | Tidak ada perbedaan signifikan dalam response time antara PostgreSQL dan MySQL pada workload CRUD. |
| H₁₁ | Terdapat perbedaan signifikan dalam response time antara PostgreSQL dan MySQL pada minimal satu jenis operasi CRUD. |
| H₀₂ | Indexing strategy tidak berdampak signifikan terhadap response time pada kedua DBMS. |
| H₁₂ | Minimal satu indexing strategy menghasilkan response time signifikan lebih rendah dibandingkan no-index. |
| H₀₃ | Tidak ada interaksi signifikan antara DBMS, indexing strategy, dan query optimization terhadap response time. |
| H₁₃ | Terdapat interaksi signifikan antara DBMS, indexing strategy, dan query optimization terhadap response time. |
| Metrik | Response time (ms), throughput (QPS) |
| Threshold | p < 0.05 |
| Justifikasi threshold | Standar alpha 0.05 dalam penelitian eksperimen, memberikan keseimbangan antara risiko Type I error (false positive) dan Type II error (false negative). |

**Apakah hipotesis ini falsifiable?** [x] Ya / [ ] Tidak
> Bagaimana cara membuktikannya salah? Dengan mengumpulkan data eksperimen dan menunjukkan bahwa perbedaan response time antar kondisi tidak signifikan secara statistik (p ≥ 0.05). Jika indexing tidak memberikan dampak signifikan, H₀₂ tidak ditolak — ini tetap menjadi kontribusi ilmiah (negative result).

---

## Latihan 3 — Rantai Operasionalisasi

Lengkapi rantai dari RQ hingga metode analisis.

| Tahap | Isi |
|-------|-----|
| RQ | RQ1: Perbedaan response time PostgreSQL vs MySQL pada CRUD? RQ2: Dampak indexing strategy? RQ3: Interaksi DBMS × indexing × optimization? |
| Variable (IV) | DBMS (PostgreSQL/MySQL), Indexing strategy (none/single/composite), Query optimization (default/optimized), Volume data (50K-1M) |
| Variable (DV) | Response time (ms), Throughput (QPS) |
| Metric | Response time per query dalam milidetik; Throughput dalam queries per second |
| Data source | Eksperimen benchmarking dengan script otomatis pada hardware terkontrol |
| Analysis method | Two-way/three-way ANOVA (atau Kruskal-Wallis jika asumsi tidak terpenuhi) untuk menguji efek utama dan interaksi; post-hoc test (Tukey HSD) untuk pairwise comparison |

**Apakah rantai lengkap?** [x] Ya / [ ] Tidak
> Jika tidak, tahap mana yang perlu direvisi? —

---

## Refleksi

> Ambil satu judul skripsi/paper yang pernah dibaca. Coba ekstrak RQ-nya. Apakah RQ tersebut memenuhi semua komponen (metode, metrik, baseline, konteks)? Jika tidak, apa yang hilang?

**Judul:** Analisis Perbandingan Performa Antara MySQL dan PostgreSQL (Ahsa et al., 2023)
**RQ yang diekstrak:** Bagaimana perbandingan response time MySQL dan PostgreSQL pada query SELECT, INSERT, UPDATE, dan DELETE dengan variasi jumlah record?
**Komponen yang hilang:** Baseline tidak eksplisit (konfigurasi default tanpa justifikasi); tidak ada kontrol indexing strategy sebagai variabel; tidak ada hipotesis formal yang dirumuskan sebelum eksperimen. Penambahan kontrol indexing dan optimization sebagai variabel akan membuat RQ lebih rigor dan hasilnya lebih informatif.