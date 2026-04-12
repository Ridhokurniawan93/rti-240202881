# WS-02: Problem Statement

> **Bab 2 — Problem Formulation & System Context**

---

## Ringkasan Materi

### Problem Formation Model

Masalah riset melewati 5 tahap transformasi. Melompat langsung dari Reality ke Variable adalah kesalahan paling umum.

```
Reality → Observed Issue (Symptom) → Diagnosed Problem (Root Cause)
→ Researchable Problem (Scoped) → Measurable Variable (Operationalized)
```

### Topic ≠ Problem ≠ Research Problem

| Level | Contoh | Status |
|-------|--------|--------|
| **Topik** | Sistem penggajian di kampus | Terlalu luas, tidak bisa diuji |
| **Problem** | Sistem penggajian Politeknik Ganesha Guru masih manual | Spesifik tapi belum riset |
| **Research Problem** | Apakah metode XP dapat meningkatkan efisiensi dan akurasi sistem penggajian dibandingkan proses manual? | Bisa dirancang eksperimennya |

### Symptom vs Root Cause

Apa yang diamati (gejala) ≠ mengapa terjadi (akar masalah). Gunakan **5 Whys** atau **Fishbone Diagram** untuk menggali.

Contoh dari `paper.md`: "Proses penggajian lambat dan banyak kesalahan" (symptom) → "Sistem manual menyebabkan redundansi data, kesalahan perhitungan, dan kurangnya transparansi" (root cause).

### System Thinking

Setiap masalah riset TI harus terikat pada komponen sistem: **Input → Process → Output → Outcome → Constraints → Stakeholders**.

Dalam konteks `paper.md`: Input (data pegawai, data gaji), Process (perhitungan manual), Output (slip gaji), Outcome (penggajian yang tepat), Constraints (keterbatasan SDM, keterbukuan, regularitas pemerintah), Stakeholders (Admin, Direktur, Pegawai, Dosen).

### Problem Quality Check

Masalah riset yang layak harus memenuhi 5 kriteria:
- **Clarity** — Satu orang membaca akan paham
- **Measurability** — Ada metrik kuantitatif
- **Relevance** — Penting untuk domain
- **Testability** — Bisa gagal (falsifiable)
- **Impact** — Ada kontribusi jika terjawab

### Research vs Engineering

| Aspek | Engineering | Research |
|-------|------------|----------|
| Tujuan | Menyelesaikan masalah (*solve*) | Memahami dan membuktikan (*understand & prove*) |
| Masalah | Bug, error, fitur belum ada | Gap dalam pengetahuan |
| Scope | Selesaikan semua yang perlu | Batasi agar bisa dibuktikan |
| Output | Working system | Evidence, paper, replicable findings |

### Istilah Penting

- **Problem Statement** — Formulasi tertulis: konteks sistem + gap + dampak + justifikasi
- **System Context** — Deskripsi lengkap: input, proses, output, outcome, constraints, stakeholders
- **Problem Drift** — Masalah "bermutasi" dari pendahuluan ke metodologi karena statement awal tidak presisi
- **Solution-First Thinking** — Memulai dari solusi tanpa masalah yang jelas — berbahaya dalam riset
- **Operational Definition** — Definisi variabel yang cukup jelas agar peneliti lain bisa mengukur hal yang sama

---

## Template A.2 — Problem Statement Builder

```
PROBLEM STATEMENT BUILDER

Domain & Konteks
  Domain   : Sistem Informasi Penggajian
  Konteks  : Politeknik Ganesha Guru (institusi pendidikan)

System Context
  Input       : Data pegawai, data gaji, data tunjangan, data potongan pajak
  Process     : Perhitungan gaji pegawai, pemrograman gaji, pembuatan laporan
  Output      : Slip gaji pegawai, laporan penggajian, bukti pembayaran
  Outcome     : Penggajian yang akurat dan tepat waktu
  Constraints : Regulasi pemerintah, keterbatasan SDM administrasi, keterbukaan data
  Stakeholders: Admin, Direktur, Pegawai, Dosen, Auditor

Fenomena → Problem
  Fenomena yang diamati             : Proses penggajian di kampus masih dilakukan secara manual
  Gejala (symptom) yang terukur     : Keterlambatan pembayaran, kesalahan perhitungan, redundansi data, tidak transparan
  Masalah yang didiagnosis          : Sistem manual menciptakan risiko kesalahan manusia tinggi dan ketidakefisienan administrasi
  Masalah riset (researchable)      : Apakah implementasi metode XP dalam sistem informasi penggajian dapat meningkatkan efisiensi dan akurasi?
  Variabel yang terukur             : Efisiensi (kecepatan pemrosesan), akurasi (tingkat kesalahan perhitungan), user satisfaction (tingkat kepuasan pengguna)

Problem Quality Check
  [x] Clarity — Sistem manual → keterlambatan, kesalahan → solusi sistem terkomputerisasi dengan XP
  [x] Measurability — Efisiensi diukur dari waktu proses, akurasi dari persentase kesalahan, kepuasan dari user feedback
  [x] Relevance — Sistem penggajian penting untuk operasional institusi manapun
  [x] Testability — Dapat diuji dengan black-box testing; bisa gagal jika sistem tidak meningkatkan efisiensi
  [x] Impact — Hasil dapat diterapkan di institusi pendidikan lain dengan karakteristik serupa

Problem Statement (1 paragraf):
  Politeknik Ganesha Guru saat ini menerapkan sistem penggajian manual yang menyebabkan berbagai permasalahan, termasuk keterlambatan pembayaran, duplikasi data, dan kesulitan dalam pembuatan laporan keuangan. Sistem manual ini memiliki banyak kekurangan dalam hal kecepatan, keakuratan, dan keamanan data pegawai. Penelitian ini mengimplementasikan metode Extreme Programming (XP) dalam pengembangan sistem informasi penggajian untuk meningkatkan efisiensi dan akurasi perhitungan gaji pegawai dan dosen, dengan pengujian menggunakan metode black-box testing.
```

---

## Latihan 1 — Dari Topik ke Masalah Riset

Pilih satu topik di bidang TI yang diminati. Transformasikan melalui 5 tahap Problem Formation Model.

**Topik awal:** Sistem Informasi Penggajian di Institusi Pendidikan

| Tahap | Hasil |
|-------|-------|
| Reality | Politeknik Ganesha Guru memiliki divisi administrasi yang mengelola penggajian pegawai dan dosen |
| Observed Issue (Symptom) | Proses penggajian memakan waktu lama, terjadi kesalahan perhitungan gaji, data terduplikasi, laporan keuangan sulit dibuat |
| Diagnosed Problem (Root Cause) | Sistem penggajian masih dilakukan secara manual tanpa bantuan teknologi informasi, sehingga rentan terhadap kesalahan manusia dan ketidakefisienan administrasi |
| Researchable Problem | Apakah implementasi metode Extreme Programming (XP) dalam pengembangan sistem informasi penggajian dapat meningkatkan efisiensi dan akurasi dibandingkan proses manual? |
| Measurable Variable | Efisiensi (waktu pemrosesan gaji), akurasi (persentase kesalahan perhitungan), kepuasan pengguna (feedback dari admin dan direktur) |

**Apakah terjebak solution-first thinking?** [ ] Ya / [x] Tidak
> Jika tidak, prinsip yang diterapkan adalah: mulai dari masalah nyata (sistem manual bermasalah) → diagnosa akar penyebab → definisikan variabel terukur sebelum memilih solusi.

---

## Latihan 2 — System Context Decomposition

Gambarkan konteks sistem dari masalah riset di Latihan 1.

| Komponen | Deskripsi |
|----------|----------|
| Input | Data pegawai (nama, NIP, jabatan), data tunjangan, data pajak, data potongan |
| Process | Perhitungan gaji pokok, perhitungan tunjangan, perhitungan potongan pajak, pembuatan slip gaji, pembuatan laporan penggajian |
| Output | Slip gaji digital/cetak, laporan penggajian bulanan, bukti pembayaran, laporan pajak |
| Outcome | Penggajian yang akurat, tepat waktu, transparan, dan sesuai dengan regulasi pemerintah |
| Constraints | Regulasi pemerintah tentang pajak penghasilan, keterbatasan SDM administrasi, keamanan data pegawai, akses terbatas ke sistem |
| Stakeholders | Admin (operator sistem), Direktur (approval), Pegawai/Dosen (penerima gaji), Auditor (verifikasi), Pemerintah (regulasi) |

**Komponen mana yang paling relevan dengan masalah riset?** Process dan Constraints

> Proses manual adalah akar masalah; constraints (regulasi dan SDM terbatas) memperkuat kebutuhan otomasi.

---

## Latihan 3 — Problem Quality Check

Evaluasi problem statement yang sudah dibuat menggunakan 5 kriteria.

| Kriteria | Skor (1-5) | Justifikasi |
|----------|-----------|-------------|
| Clarity | 5 | Pernyataan masalah jelas: sistem manual → keterlambatan, kesalahan, redundansi data |
| Measurability | 5 | Variabel terukur: efisiensi (waktu), akurasi (% kesalahan), kepuasan pengguna (feedback) |
| Relevance | 5 | Sistem penggajian adalah kebutuhan universal di setiap institusi, dampak nyata pada operasional |
| Testability | 4 | Bisa diuji dengan black-box testing dan user acceptance testing; dapat gagal jika tidak ada perbedaan signifikan |
| Impact | 5 | Hasil dapat digeneralisasi ke institusi pendidikan lain dengan karakteristik serupa, kontribusi pada pengetahuan XP di domain penggajian |

**Skor total:** 24 / 25

**Problem statement versi final (1 paragraf):**
> Politeknik Ganesha Guru menjalankan proses penggajian secara manual, menyebabkan keterlambatan pembayaran, kesalahan perhitungan, duplikasi data, dan kesulitan dalam pelaporan keuangan. Sistem manual ini rentan terhadap kesalahan manusia dan tidak memenuhi kebutuhan transparansi serta kepatuhan regulasi pemerintah. Penelitian ini mengimplementasikan metode Extreme Programming (XP) dalam pengembangan sistem informasi penggajian untuk mengatasi masalah tersebut. Efektivitas solusi akan diukur dari peningkatan efisiensi proses (waktu pemrosesan lebih cepat), peningkatan akurasi (pengurangan kesalahan perhitungan), dan kepuasan pengguna terhadap sistem baru.

---

## Refleksi

> Bandingkan "masalah" yang biasa ditemui saat coding (bug, error) dengan masalah riset. Apa perbedaan fundamental dalam cara mendefinisikan dan mendekati keduanya?

**Jawaban:**
> **Masalah Engineering (coding):** "Tombol login tidak berfungsi" — masalah langsung, ada bug spesifik, solusi jelas (debug kode), ukuran sukses: tombol berfungsi.
> 
> **Masalah Research:** "Apakah sistem baru meningkatkan efisiensi?" — masalah abstrak, perlu definisi "efisiensi", perlu desain eksperimen terukur, solusi tidak langsung (butuh iterasi, pengujian, validasi), ukuran sukses: hipotesis terjawab dengan bukti meyakinkan.
> 
> Perbedaan fundamental: Engineering mencari "how" (langsung diperbaiki), Research mencari "why" dan "is X true?" (harus dibuktikan dengan bukti dan dapat direplikasi).
