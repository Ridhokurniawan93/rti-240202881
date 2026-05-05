# WS-04: Research Question & Hypothesis

> **Bab 4 — Research Question, Contribution & Hypothesis**

---

## Ringkasan Materi

### RQ Bukan Pertanyaan Biasa

Research Question yang baik secara implisit mengandung cetak biru eksperimen: subjek, baseline, metrik, domain, dataset.

| Kualitas | Contoh |
|----------|--------|
| **Buruk** | "Bagaimana pengaruh deep learning terhadap deteksi malware?" |
| **Baik** | "Apakah CNN menghasilkan F1-Score lebih tinggi dari RF pada CIC-MalMem-2022?" |

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

Gap Statement  : Implementasi XP pada sistem informasi penggajian belum dievaluasi di konteks institusi pendidikan Indonesia, khususnya Politeknik Ganesha Guru.

Research Question:
  Tipe         : [x] Comparison  [ ] Improvement  [ ] Exploratory
  Formulasi    : Apakah pengembangan sistem informasi penggajian di Politeknik Ganesha Guru menggunakan Extreme Programming (XP) menghasilkan efisiensi waktu pemrosesan dan akurasi perhitungan yang lebih baik dibandingkan dengan pengembangan tradisional serta proses manual?
  Variabel IV  : Metode pengembangan sistem (XP vs tradisional/manual)
  Variabel DV  : Efisiensi waktu pemrosesan, akurasi perhitungan, kepuasan pengguna
  Metrik       : Waktu pemrosesan payroll (menit), persentase kesalahan perhitungan gaji (%), skor kepuasan pengguna (1-5)
  Dataset      : Data pegawai dan data gaji di Politeknik Ganesha Guru serta hasil pengujian sistem penggajian yang dibangun
  Baseline     : Proses manual / pengembangan sistem tradisional sebelum adopsi XP

Quality Check RQ:
  [x] Variabel spesifik
  [x] Metrik jelas
  [x] Baseline ada
  [x] Konteks disebutkan
  [x] Memerlukan eksperimen (bukan hanya survei literatur)

Contribution Statement:
  Apa yang baru diketahui : Efektivitas XP dalam meningkatkan efisiensi dan akurasi sistem penggajian dalam konteks institusi pendidikan Indonesia.
  Jenis kontribusi        : [ ] Improvement  [x] Comparison  [ ] Novel approach
  Gap yang diisi          : Context gap dari WS-03 tentang ketidaktersediaan evaluasi XP pada sistem penggajian di lingkungan akademik.

Hypothesis Pair:
  H₀ : Tidak ada perbedaan signifikan dalam efisiensi waktu pemrosesan, akurasi perhitungan, atau kepuasan pengguna antara sistem penggajian yang dikembangkan dengan XP dan sistem penggajian tradisional/manual di Politeknik Ganesha Guru.
  H₁ : Sistem penggajian yang dikembangkan dengan XP memiliki efisiensi waktu pemrosesan lebih baik, akurasi perhitungan lebih tinggi, dan kepuasan pengguna lebih tinggi dibandingkan metode tradisional/manual.
  Threshold              : p < 0.05 dan minimal 10% peningkatan efektivitas pada metrik utama.
  Justifikasi threshold  : Standar statistik umum menggunakan p < 0.05, dan 10% peningkatan dianggap bernilai operasional dalam konteks pengelolaan gaji.
```

---

## Latihan 1 — Dari Gap ke RQ

Gunakan gap yang ditemukan di WS-03. Transformasikan menjadi Research Question.

**Gap dari WS-03:** Implementasi XP pada sistem penggajian belum dievaluasi di konteks institusi pendidikan Indonesia seperti Politeknik Ganesha Guru.

**RQ versi pertama (tulis bebas):**
> Apakah penggunaan Extreme Programming (XP) untuk mengembangkan sistem informasi penggajian dapat meningkatkan efisiensi dan akurasi di Politeknik Ganesha Guru?

**Evaluasi RQ:**

| Komponen | Ada? | Isi |
|----------|------|-----|
| Metode spesifik | Ya | XP vs tradisional/manual |
| Metrik terukur | Ya | Waktu pemrosesan, akurasi perhitungan, kepuasan pengguna |
| Baseline | Ya | Sistem manual dan metode tradisional pengembangan |
| Dataset/konteks | Ya | Sistem penggajian Politeknik Ganesha Guru |

**Tipe RQ:** [x] Comparison / [ ] Improvement / [ ] Exploratory

**RQ versi revisi (setelah evaluasi):**
> Apakah pengembangan sistem informasi penggajian di Politeknik Ganesha Guru menggunakan Extreme Programming (XP) menghasilkan efisiensi waktu pemrosesan dan akurasi perhitungan yang lebih baik dibandingkan dengan pengembangan tradisional dan proses manual?

---

## Latihan 2 — Hypothesis Pair

Rumuskan pasangan hipotesis dari RQ di Latihan 1.

| Komponen | Isi |
|----------|-----|
| H₀ | Tidak ada perbedaan signifikan dalam efisiensi waktu pemrosesan, akurasi perhitungan, atau kepuasan pengguna antara sistem penggajian XP dan sistem penggajian tradisional/manual di Politeknik Ganesha Guru. |
| H₁ | Sistem penggajian yang dikembangkan dengan XP memiliki efisiensi waktu pemrosesan lebih baik, akurasi perhitungan lebih tinggi, dan kepuasan pengguna lebih tinggi dibandingkan metode tradisional/manual. |
| Metrik | Waktu pemrosesan payroll (menit), persentase kesalahan perhitungan gaji (%), skor kepuasan pengguna (1-5). |
| Threshold | p < 0.05 dan minimal 10% peningkatan efektivitas pada metrik utama. |
| Justifikasi threshold | p < 0.05 merupakan standar statistik umum; 10% peningkatan dianggap signifikan secara operasional untuk sistem penggajian. |

**Apakah hipotesis ini falsifiable?** [x] Ya / [ ] Tidak
> Bagaimana cara membuktikannya salah? Dengan mengumpulkan data pengujian dan menunjukkan bahwa perbedaan antara XP dan tradisional/manual tidak signifikan secara statistik (p ≥ 0.05) atau tidak mencapai peningkatan 10%.

---

## Latihan 3 — Rantai Operasionalisasi

Lengkapi rantai dari RQ hingga metode analisis.

| Tahap | Isi |
|-------|-----|
| RQ | Apakah pengembangan sistem informasi penggajian di Politeknik Ganesha Guru menggunakan XP menghasilkan efisiensi waktu pemrosesan dan akurasi perhitungan yang lebih baik dibandingkan pengembangan tradisional/manual? |
| Variable (IV) | Metode pengembangan sistem (XP vs tradisional/manual) |
| Variable (DV) | Efisiensi waktu pemrosesan, akurasi perhitungan, kepuasan pengguna |
| Metric | Waktu pemrosesan (menit), persentase kesalahan gaji (%), skor kepuasan pengguna (1-5) |
| Data source | Data penggajian Politeknik Ganesha Guru, hasil pengujian sistem baru, survei pengguna sistem |
| Analysis method | Perbandingan kuantitatif dengan uji statistik (misalnya t-test atau uji non-parametrik) dan analisis deskriptif |

**Apakah rantai lengkap?** [x] Ya / [ ] Tidak
> Jika tidak, tahap mana yang perlu direvisi? -

---

## Refleksi

> Ambil satu judul skripsi/paper yang pernah dibaca. Coba ekstrak RQ-nya. Apakah RQ tersebut memenuhi semua komponen (metode, metrik, baseline, konteks)? Jika tidak, apa yang hilang?

**Judul:** Implementasi Extreme Programming pada Sistem Informasi Penggajian.
**RQ yang diekstrak:** Apakah penggunaan XP dalam pengembangan sistem penggajian meningkatkan efisiensi dan akurasi dibanding metode tradisional? 
**Komponen yang hilang:** Jika belum eksplisit, dataset/konteks institusi pendidikan atau baseline tradisional/manual dapat ditambahkan agar lebih lengkap.
