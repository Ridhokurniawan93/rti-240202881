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
| **Internal** | Apakah hubungan IV→DV nyata? | Confounding variable, selection bias |
| **External** | Apakah bisa digeneralisasi? | Dataset terlalu spesifik |
| **Construct** | Apakah mengukur konsep yang benar? | Metrik tidak sesuai |
| **Conclusion** | Apakah kesimpulan statistik valid? | Sample size kecil, uji salah |

Internal dan external validity sering berkonflik: semakin terkontrol (internal kuat) → semakin artificial (external lemah).

### Tiga Tipe Eksperimen dalam Riset TI

| Tipe | Deskripsi | Kapan Digunakan |
|------|----------|----------------|
| **Comparison Study** | Metode A vs B pada kondisi identik | Membandingkan pendekatan berbeda |
| **Ablation Study** | Full system → lepas komponen satu per satu | Mengukur kontribusi tiap komponen |
| **Parameter Study** | Variasikan satu parameter, amati dampak | Uji sensitifitas/robustness |

### Fairness dalam Perbandingan

Perbandingan yang adil = **kondisi identik** untuk semua metode: dataset sama, preprocessing sama, tuning effort sebanding, environment sama, metrik sama.

Contoh tidak adil: Transformer (30 fitur tambahan + Bayesian optimization) vs RF (default params) → hasilnya misleading.

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

Research Question : Apakah pengembangan sistem informasi penggajian di Politeknik Ganesha Guru menggunakan Extreme Programming (XP) menghasilkan efisiensi waktu pemrosesan dan akurasi perhitungan yang lebih baik dibandingkan dengan pengembangan tradisional/manual?
Hypothesis        : H0: Tidak ada perbedaan signifikan antara sistem XP dan tradisional/manual pada metrik waktu pemrosesan, akurasi perhitungan, dan kepuasan pengguna. H1: Sistem XP lebih baik pada minimal salah satu metrik utama.
Tipe Eksperimen   : [x] Comparison  [ ] Ablation  [ ] Parameter

Kondisi Eksperimen:
| Kondisi | Deskripsi | IV Value | CV Settings |
|---------|-----------|----------|-------------|
| Control | Sistem penggajian yang dikembangkan dengan metode tradisional/manual | traditional/manual | Data dan config teridentik: employee_count=50, salary_components=8, seed=42 |
| Treatment | Sistem penggajian yang dikembangkan dengan metode Extreme Programming (XP) | XP | Sama seperti Control (dataset, preprocessing, environment)

Fairness Checklist:
  [x] Dataset identik untuk semua kondisi
  [x] Preprocessing setara
  [x] Tuning effort setara (tuning effort didokumentasikan dan disamakan)
  [x] Environment identik (server/VM, dependencies, runtime)
  [x] Metrik evaluasi sama (waktu pemrosesan, persentase kesalahan, skor kepuasan)

Threat Analysis:
| Threat Type | Ancaman Spesifik | Mitigasi |
|-------------|-----------------|----------|
| Internal    | Confounding karena variasi data input atau perbedaan konfigurasi | Lock semua CV di file config; gunakan same dataset snapshot; run trials deterministik dengan seed dan dokumentasikan config version |
| External    | Generalisasi terbatas ke institusi lain | Pilih sampel kasus representatif (variasi jabatan dan komponen gaji); jelaskan batas generalisasi; usulkan replikasi multi-site jika memungkinkan |
| Construct   | Metrik tidak mengukur konstruk (mis. kepuasan tidak mewakili usability) | Validasi instrumen survei dengan pilot test; gunakan metrik tambahan (task completion, error types) sebagai triangulasi |
| Conclusion  | Sample size terlalu kecil → power rendah atau multiple testing bias | Lakukan perencanaan power (lihat Statistical Plan); gunakan koreksi multiple comparisons bila perlu; laporkan effect sizes dan CI

Statistical Plan:
  Uji statistik   : Paired t-test (atau Wilcoxon signed-rank jika distribusi tidak normal) untuk metrik waktu dan error-rate; McNemar atau paired proportion test untuk kejadian kategorikal; uji non-parametrik untuk skor Likert (Wilcoxon)
  Justifikasi     : Pengukuran di-run pada dataset yang sama untuk kedua kondisi sehingga desain paired cocok; pilih uji non-parametrik jika asumsi normalitas tidak terpenuhi
  Alpha           : 0.05
  Effect size min : Cohen's d ≈ 0.5 (medium) atau setara minimal 10% peningkatan operasional pada metrik utama
  Sample size (perkiraan) : Untuk paired t-test dengan d=0.5, power=0.8, alpha=0.05 → n≈34 pasangan (saran: minimal 34 payroll cycles/replicates)
```

---

## Latihan 1 — Desain Eksperimen

Susun desain eksperimen berdasarkan RQ, variabel, dan sistem dari WS-04 sampai WS-06.

**RQ:** __________________________________________________
**Tipe eksperimen:** [ ] Comparison / [ ] Ablation / [ ] Parameter

| Kondisi | Deskripsi | IV Value | CV Settings |
|---------|-----------|----------|-------------|
 | Control | Sistem yang dikembangkan dengan metode tradisional/manual | traditional/manual | employee_count=50; salary_components=8; deduction_types=5; seed=42; same runtime environment |
 | Treatment | Sistem yang dikembangkan dengan metode XP | XP | Sama seperti Control (identical dataset, preprocessing, environment, tuning effort documented) |

---

## Latihan 2 — Fairness Checklist

Evaluasi apakah desain eksperimen di Latihan 1 sudah fair.

| Kriteria | Status | Detail |
|----------|--------|--------|
| Dataset identik | ✅ | Gunakan snapshot dataset payroll yang sama untuk semua trial; simpan dan verifikasi checksum versi dataset yang dipakai |
| Preprocessing setara | ✅ | Semua preprocessing script dipakai identik dan version-controlled; dokumentasikan pipeline dan versi library |
| Tuning effort setara | ✅ | Tetapkan guideline tuning budget (waktu, parameter ranges) dan catat effort/tim untuk setiap metode agar setara |
| Environment identik | ✅ | Jalankan pada VM/container yang sama (Docker) dengan resource limit yang sama; dokumentasikan image dan seed random |
| Metrik evaluasi sama | ✅ | Waktu pemrosesan, persentase kesalahan, dan skor kepuasan digunakan untuk semua kondisi |

**Ada yang tidak fair?** [ ] Ya / [x] Tidak
> Jika ya, bagaimana cara memperbaikinya? —

---

## Latihan 3 — Threat Analysis

Identifikasi ancaman validitas untuk desain eksperimen ini.

| Threat Type | Ancaman Spesifik | Mitigasi |
|-------------|-----------------|----------|
| Internal | Konfounding karena perubahan konfigurasi, operator effect, atau order effect | Lock config, randomize order of runs, multiple independent runs, use automation to avoid operator bias |
| External | Hasil tidak generalize ke institusi lain atau skala lebih besar | Document context in detail; sample diverse payroll cases; plan replication studies di institusi lain sebagai future work |
| Construct | Metrik tidak sepenuhnya mewakili konstruk (mis. kepuasan ≠ usability lengkap) | Gunakan multiple metrics (primary + secondary), validasi survei dengan pilot, triangulasi hasil teknis & subjektif |
| Conclusion | Underpowered study, multiple comparisons, data dredging | Lakukan perencanaan power, gunakan koreksi multiple testing (Bonferroni/FDR) jika banyak uji, laporkan effect sizes dan confidence intervals |

**Ancaman mana yang paling sulit dimitigasi?** External validity
**Mengapa?**
> Karena aspek organisasi, regulasi, dan praktik administrasi berbeda antar institusi; mitigasi terbaik adalah transparansi konteks dan replikasi di site lain.

---

## Refleksi

> Sebuah paper melaporkan "metode kami mengalahkan semua baseline." Apa 3 pertanyaan pertama yang harus diajukan untuk mengevaluasi klaim ini?

**Jawaban:**
1. Apakah kondisi uji fair? (sama dataset, preprocessing, tuning effort, environment)
2. Apakah analisis statistik tepat dan apakah ukuran sampel cukup (power)?
3. Apakah metrik yang dipakai valid untuk konstruk yang diklaim dan apakah ada multiple testing/p-hacking?
