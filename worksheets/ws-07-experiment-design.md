# WS-07: Experimental Design & Validity

> **Bab 7 — Experimental Design & Validity**

---

## Ringkasan Materi

### Correlation ≠ Causality

Kausalitas membutuhkan 3 syarat:
1. **Covariance** — X dan Y bergerak bersama
2. **Temporal precedence** — X berubah sebelum Y
3. **Elimination of alternatives** — Tidak ada faktor lain yang menjelaskan Y

Controlled experiment adalah satu-satunya metode yang bisa membuktikan kausalitas.

### Empat Jenis Validitas

| Jenis | Pertanyaan | Ancaman Umum |
|-------|-----------|-------------|
| **Internal** | Apakah hubungan IV→DV nyata? | Confounding variable (cache, warm-up effect), selection bias |
| **External** | Apakah bisa digeneralisasi? | Hardware terlalu spesifik, dataset sintetis |
| **Construct** | Apakah mengukur konsep yang benar? | Response time tidak mencakup aspek performa lain |
| **Conclusion** | Apakah kesimpulan statistik valid? | Sample size kecil, multiple testing tanpa koreksi |

Internal dan external validity sering berkonflik: semakin terkontrol (internal kuat) → semakin artificial (external lemah).

### Tiga Tipe Eksperimen dalam Riset TI

| Tipe | Deskripsi | Kapan Digunakan |
|------|----------|----------------|
| **Comparison Study** | Metode A vs B pada kondisi identik | Membandingkan pendekatan berbeda (PostgreSQL vs MySQL) |
| **Ablation Study** | Full system → lepas komponen satu per satu | Mengukur kontribusi tiap komponen (indexing vs optimization) |
| **Parameter Study** | Variasikan satu parameter, amati dampak | Uji sensitifitas (volume data terhadap response time) |

### Fairness dalam Perbandingan

Perbandingan yang adil = **kondisi identik** untuk semua metode: dataset sama, preprocessing sama, tuning effort sebanding, environment sama, metrik sama.

Contoh tidak adil: PostgreSQL (dengan composite index + optimized query + 16GB buffer pool) vs MySQL (tanpa index + default query + 128MB buffer pool) → hasilnya misleading.

### Threats to Validity = Diidentifikasi Sebelum Eksperimen

Ancaman validitas harus diidentifikasi **sebelum** eksperimen dan mitigasinya dirancang sebagai bagian dari desain — bukan ditulis sebagai boilerplate setelah selesai.

### Research vs Engineering

| Aspek | Engineering | Research |
|-------|------------|----------|
| Tujuan testing | Memastikan sistem memenuhi requirement | Membuktikan hubungan kausal antar variabel |
| Baseline | Versi sebelumnya (last release) | Metode tervalidasi dari literatur |
| Kegagalan | Bug → fix → release | H₀ tidak ditolak → tetap kontribusi ilmiah |
| Sukses | 100% test pass | Evidence valid — mendukung atau menolak hipotesis |

### Istilah Penting

- **Causality** — Hubungan sebab-akibat (covariance + temporal + elimination)
- **Controlled Experiment** — Ubah satu variabel, kontrol sisanya, amati efek
- **Fairness** — Semua metode diuji pada kondisi yang benar-benar identik
- **Threats to Validity** — Faktor yang bisa melemahkan kesimpulan jika tidak dimitigasi
- **Conclusion Validity** — Validitas statistik: power, sample size, uji yang tepat

---

## Template A.7 — Desain Eksperimen Lengkap

```
EXPERIMENT DESIGN

Research Question :
  RQ1: Apakah terdapat perbedaan signifikan dalam response time antara PostgreSQL dan MySQL pada workload CRUD?
  RQ2: Bagaimana dampak indexing strategy terhadap response time?
  RQ3: Apakah terdapat interaksi signifikan antara DBMS, indexing, dan optimization?

Hypothesis        :
  H₀₁: Tidak ada perbedaan signifikan response time antara PostgreSQL dan MySQL.
  H₁₁: Terdapat perbedaan signifikan pada minimal satu operasi CRUD.
  H₀₂: Indexing strategy tidak berdampak signifikan terhadap response time.
  H₁₂: Minimal satu indexing strategy menghasilkan response time signifikan lebih rendah.
  H₀₃: Tidak ada interaksi signifikan antara DBMS, indexing, dan optimization.
  H₁₃: Terdapat interaksi signifikan antara DBMS, indexing, dan optimization.

Tipe Eksperimen   : [x] Comparison  [x] Ablation  [x] Parameter

Kondisi Eksperimen:
| Kondisi | Deskripsi | IV Values | CV Settings |
|---------|-----------|-----------|-------------|
| C1: Baseline PostgreSQL | PostgreSQL, no-index, default query | dbms=pg, idx=none, opt=default | Skema identik, volume data sama, hardware identik, cache cleared |
| C2: PostgreSQL + Single Index | PostgreSQL, single-column index, default query | dbms=pg, idx=single, opt=default | Sama seperti C1 |
| C3: PostgreSQL + Composite Index | PostgreSQL, composite index, default query | dbms=pg, idx=composite, opt=default | Sama seperti C1 |
| C4: PostgreSQL + Optimized | PostgreSQL, composite index, optimized query | dbms=pg, idx=composite, opt=optimized | Sama seperti C1 |
| C5: Baseline MySQL | MySQL, no-index, default query | dbms=mysql, idx=none, opt=default | Sama seperti C1 |
| C6: MySQL + Single Index | MySQL, single-column index, default query | dbms=mysql, idx=single, opt=default | Sama seperti C1 |
| C7: MySQL + Composite Index | MySQL, composite index, default query | dbms=mysql, idx=composite, opt=default | Sama seperti C1 |
| C8: MySQL + Optimized | MySQL, composite index, optimized query | dbms=mysql, idx=composite, opt=optimized | Sama seperti C1 |

Fairness Checklist:
  [x] Dataset identik untuk semua kondisi (same schema, same data generator, same seed)
  [x] Preprocessing setara (same data generation script, same encoding)
  [x] Tuning effort setara (konfigurasi buffer pool, max connections disetarakan; indexing dikonfigurasi secara eksplisit sebagai IV)
  [x] Environment identik (Docker container dengan resource limit sama: CPU, RAM, disk I/O)
  [x] Metrik evaluasi sama (response time ms, throughput QPS, CPU%, memory MB)
  [x] Warm-up phase (5 query warm-up sebelum pengukuran, hasilnya tidak dicatat)
  [x] Cold start (clear DBMS cache sebelum setiap kondisi baru)

Threat Analysis:
| Threat Type | Ancaman Spesifik | Mitigasi |
|-------------|-----------------|----------|
| Internal    | Cache/warm-up effect: query kedua lebih cepat karena data sudah di-cache; confounding dari background processes | Warm-up 5 query sebelum pengukuran; clear cache sebelum setiap kondisi; matikan service non-esensial; randomize order of conditions; 5+ replikasi per kondisi |
| External    | Hasil tidak generalize ke hardware atau workload berbeda | Dokumentasikan spesifikasi hardware secara detail; gunakan dataset yang representatif (bukan hanya synthetic); jelaskan batas generalisasi; usulkan replikasi pada hardware berbeda sebagai future work |
| Construct   | Response time saja tidak mencakup semua aspek performa database | Tambahkan secondary metric (throughput QPS, CPU%, memory MB); gunakan EXPLAIN ANALYZE untuk validasi query plan; laporkan multiple metrics |
| Conclusion  | Multiple testing (banyak kondisi × banyak metrik) meningkatkan Type I error; sample size kecil → power rendah | Gunakan koreksi Bonferroni/FDR untuk multiple comparisons; lakukan power analysis untuk menentukan minimum replikasi; laporkan effect sizes (Cohen's d) dan confidence intervals |

Statistical Plan:
  Uji statistik   : Three-way ANOVA (DBMS × Indexing × Optimization) untuk RQ3; Two-way ANOVA untuk RQ1 dan RQ2; jika asumsi normalitas/homogenitas tidak terpenuhi → Kruskal-Wallis test; post-hoc Tukey HSD untuk pairwise comparison
  Justifikasi     : ANOVA cocok karena memiliki ≥2 faktor (DBMS, Indexing, Optimization) dengan level masing-masing; data response time (ratio) memenuhi skala pengukuran yang dibutuhkan; non-parametric fallback jika asumsi dilanggar
  Alpha           : 0.05 (dengan koreksi Bonferroni untuk multiple comparisons bila diperlukan)
  Effect size min : Cohen's f ≈ 0.25 (medium) untuk ANOVA; Cohen's d ≈ 0.5 (medium) untuk pairwise comparison
  Sample size     : Power analysis: untuk ANOVA dengan f=0.25, power=0.8, alpha=0.05, 3 faktor → minimal n=5 replikasi per sel (total: 2 DBMS × 3 indexing × 2 optimization × 4 CRUD × 5 volume × 5 replikasi = 1.200 observasi per kondisi)
```

---

## Latihan 1 — Desain Eksperimen

Susun desain eksperimen berdasarkan RQ, variabel, dan sistem dari WS-04 sampai WS-06.

**RQ:** RQ1: Perbedaan response time PostgreSQL vs MySQL pada CRUD? RQ2: Dampak indexing strategy? RQ3: Interaksi DBMS × indexing × optimization?
**Tipe eksperimen:** [x] Comparison / [x] Ablation / [x] Parameter

| Kondisi | Deskripsi | IV Value | CV Settings |
|---------|-----------|----------|-------------|
| C1: PG Baseline | PostgreSQL, no-index, default query | dbms=pg, idx=none, opt=default | Skema identik, record_count sesuai konfigurasi, Docker resource limit sama, cache cleared, warm-up 5 queries |
| C2: PG + Single Idx | PostgreSQL, single-column index, default query | dbms=pg, idx=single, opt=default | Sama seperti C1 |
| C3: PG + Composite | PostgreSQL, composite index, default query | dbms=pg, idx=composite, opt=default | Sama seperti C1 |
| C4: PG + Optimized | PostgreSQL, composite index, optimized query | dbms=pg, idx=composite, opt=optimized | Sama seperti C1 |
| C5: MySQL Baseline | MySQL, no-index, default query | dbms=mysql, idx=none, opt=default | Sama seperti C1 |
| C6: MySQL + Single | MySQL, single-column index, default query | dbms=mysql, idx=single, opt=default | Sama seperti C1 |
| C7: MySQL + Composite | MySQL, composite index, default query | dbms=mysql, idx=composite, opt=default | Sama seperti C1 |
| C8: MySQL + Optimized | MySQL, composite index, optimized query | dbms=mysql, idx=composite, opt=optimized | Sama seperti C1 |

---

## Latihan 2 — Fairness Checklist

Evaluasi apakah desain eksperimen di Latihan 1 sudah fair.

| Kriteria | Status | Detail |
|----------|--------|--------|
| Dataset identik | ✅ | Gunakan data generator yang sama dengan seed yang sama untuk semua kondisi; skema database identik; verifikasi checksum setelah generation |
| Preprocessing setara | ✅ | Script data generation identik untuk kedua DBMS; encoding dan charset disetarakan (UTF-8); same data types (dengan penyesuaian sintaks DBMS) |
| Tuning effort setara | ✅ | Buffer pool, max connections, dan konfigurasi server disetarakan; indexing dikonfigurasi secara eksplisit sebagai IV (bukan perbedaan konfigurasi default) |
| Environment identik | ✅ | Docker container dengan resource limit identik (CPU quota, memory limit, disk I/O); kedua DBMS berjalan di host yang sama secara bergantian |
| Metrik evaluasi sama | ✅ | Response time (ms), throughput (QPS), CPU%, memory MB digunakan untuk semua kondisi; pengukuran menggunakan high-resolution timer |
| Warm-up & Cold start | ✅ | 5 warm-up queries sebelum pengukuran (hasil tidak dicatat); clear DBMS cache sebelum setiap kondisi baru |

**Ada yang tidak fair?** [ ] Ya / [x] Tidak
> Jika ya, bagaimana cara memperbaikinya? —

---

## Latihan 3 — Threat Analysis

Identifikasi ancaman validitas untuk desain eksperimen ini.

| Threat Type | Ancaman Spesifik | Mitigasi |
|-------------|-----------------|----------|
| Internal | Cache/warm-up effect: query kedua lebih cepat; background processes mengganggu; order effect (kondisi yang diuji duluan vs terakhir) | Warm-up phase sebelum pengukuran; clear cache antar kondisi; randomize order of conditions; 5+ replikasi; matikan non-essential services |
| External | Hasil tidak generalize ke hardware berbeda, versi DBMS berbeda, atau workload non-CRUD | Dokumentasikan hardware dan versi DBMS secara detail; gunakan dataset representatif; jelaskan batas generalisasi di pembahasan; future work: replikasi multi-hardware |
| Construct | Response time saja tidak cukup mewakili "performa database" secara keseluruhan | Gunakan multi-metric: response time (primary), throughput QPS (secondary), CPU%, memory MB (supplementary); EXPLAIN ANALYZE untuk validasi query plan |
| Conclusion | Multiple comparisons (8 kondisi × 4 CRUD × 5 volume × 2 metrik = banyak uji statistik); power rendah jika replikasi terlalu sedikit | Bonferroni/FDR correction untuk multiple testing; power analysis (f=0.25, power=0.8, alpha=0.05) → minimal 5 replikasi per sel; laporkan effect sizes (Cohen's d/f) dan confidence intervals |

**Ancaman mana yang paling sulit dimitigasi?** External validity
**Mengapa?**
> Karena performa database sangat bergantung pada hardware (CPU, RAM, disk type, I/O bandwidth), versi DBMS, dan karakteristik workload. Pengujian pada satu set hardware dan satu skema database membatasi generalisasi. Mitigasi terbaik adalah transparansi konteks (dokumentasi detail) dan mengusulkan replikasi pada hardware dan workload berbeda sebagai future work. Namun, trade-off ini diperlukan karena tanpa kontrol hardware yang ketat (internal validity), hasil eksperimen tidak bisa diandalkan sama sekali.

---

## Refleksi

> Sebuah paper melaporkan "metode kami mengalahkan semua baseline." Apa 3 pertanyaan pertama yang harus diajukan untuk mengevaluasi klaim ini?

**Jawaban:**
1. Apakah kondisi uji fair? (sama dataset, konfigurasi, indexing strategy, tuning effort, environment — atau ada straw man comparison?)
2. Apakah analisis statistik tepat dan apakah ukuran sampel cukup (power analysis)? Apakah ada multiple testing tanpa koreksi?
3. Apakah metrik yang dipakai valid untuk konstruk yang diklaim (construct validity)? Apakah hanya melaporkan satu metrik yang menguntungkan, atau multi-metric evaluation? Apakah effect size dilaporkan di samping p-value?