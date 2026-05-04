# WS-03: Literature Mapping & Gap

> **Bab 3 — Literature Review, Research Gap & Baseline**

---

## Ringkasan Materi

### Literature Review = Positioning, Bukan Ringkasan

Literature review bukan merangkum paper satu per satu. Pendekatan yang benar adalah **concept-centric** — organisasi berdasarkan tema, metode, atau variabel. Tujuan: menemukan **pola, kontradiksi, dan gap**.

   literatur diorganisir dalam 3 konsep utama:
1. **Sistem Informasi Penggajian** — definisi, komponen, manfaat teknologi
2. **Extreme Programming (XP)** — metodologi, prinsip, hasil implementasi
3. **Penelitian Terkait** — studi sebelumnya pada konteks berbeda
**Perbandingan pendekatan Author-centric vs Concept-centric:**

| Aspek | Author-centric (Hindari) | Concept-centric (Gunakan) |
|-------|--------------------------|---------------------------|
| Struktur | Per penulis/paper ("Rahman et al. menyatakan...") | Per konsep/metode ("Pendekatan berbasis transformer") |
| Tujuan | Ringkasan isi paper | Perbandingan metode & identifikasi gap |
| Contoh paragraph | "Rahman (2023) pakai CNN. Lee (2022) pakai LSTM. Zhang (2021) pakai RF." | "Tiga pendekatan dominan: CNN digunakan oleh 4 paper untuk representasi fitur visual; LSTM untuk data sekuensial; RF sebagai baseline klasik." |
| Hasil akhir | Daftar paper | Peta pengetahuan + gap yang teridentifikasi |

### Empat Jenis Research Gap

| Jenis Gap | Deskripsi | Contoh |
|-----------|----------|--------|
| **Performance Gap** | Performa belum memadai | Akurasi deteksi hanya 78% pada kasus tertentu |
| **Method Gap** | Pendekatan belum diterapkan | Belum ada yang pakai transformer untuk task ini |
| **Data Gap** | Dataset terbatas/tidak representatif | Semua studi pakai dataset sintetis |
| **Context Gap** | Belum diuji pada konteks berbeda | Belum ada evaluasi di negara berkembang |

Gap terkuat = kombinasi 2+ jenis.

### Systematic Search Strategy

1. **Database utama**: IEEE Xplore, ACM DL, Scopus
   - Akses IEEE/ACM melalui jaringan kampus atau VPN institusi
   - Alternatif bebas biaya: Google Scholar, ResearchGate ([researchgate.net](https://www.researchgate.net)), arXiv ([arxiv.org](https://arxiv.org))
2. **Boolean query** yang terdokumentasi eksplisit
   - Contoh: `("anomaly detection" OR "intrusion detection") AND ("deep learning" OR "neural network") NOT ("medical imaging")`
   - Gunakan tanda kutip untuk frasa eksak; AND/OR/NOT mengontrol scope
3. **Snowballing** — dua arah:
   - **Backward snowballing**: buka daftar referensi di paper kunci → telusuri paper yang dikutip
   - **Forward snowballing**: di Google Scholar, klik "Cited by" di bawah paper kunci → temukan paper yang mengutipnya
   - Ulangi 1–2 tingkat untuk membangun cakupan komprehensif
4. Klaim "belum ada penelitian" harus didukung **bukti pencarian**

### Baseline Selection — 3 Kriteria

| Kriteria | Pertanyaan | Contoh |
|----------|-----------|--------|
| **Relevan** | Apakah menyelesaikan masalah yang sama? | Agus & Gustiawan [13] relevan: XP untuk sistem penggajian, meski di konteks berbeda |
| **Representatif** | Apakah mewakili common practice? | Semua studi terkait pakai XP atau Agile, bukan waterfall → XP adalah baseline yang tepat |
| **State-of-the-Art** | Apakah terbaru/terbaik? | Fajar et al. [15] lebih baru, tapi White et al. [12] lebih rigorous (30% improvement) |

Membandingkan deep learning 2024 dengan decision tree sederhana tanpa justifikasi = **straw man comparison** (perbandingan tidak jujur).

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

Topik      : Implementasi Metode Extreme Programming dalam Pengembangan Sistem Informasi Penggajian
Database   : Google Scholar, IEEE Xplore
Query      : ("extreme programming" OR "XP") AND ("payroll system" OR "salary information system") AND ("agile development")
Tahun      : 2020-2025
Hasil awal : 10 paper → Screening → 5 paper final

Literature Matrix (concept-centric):

| Study | Tahun | Method | Data | Result | Limitation |
|-------|-------|--------|------|--------|------------|
| White et al. | 2020 | XP practices in software engineering | Productivity analysis across projects | 30% productivity gain in agile projects | General software, not payroll-specific |
| Agus & Gustiawan | 2021 | XP in payroll system development | PT. Pradana Energi Gemilang case study | 35% efficiency increase in payroll management | Specific to energy company, not educational institutions |
| Setiawansyah et al. | 2022 | XP in overtime payroll accounting | PT. Sugar Labinta case study | 20% accuracy improvement in salary calculations | Focused on overtime, not general payroll |
| Fajar et al. | 2023 | XP in payroll system implementation | General software development | Faster implementation time with better code quality | No specific metrics on accuracy or efficiency |
| Johnson & Lee | 2022 | Agile methodologies in payroll system development | Case studies in educational institutions | Improved efficiency and user satisfaction | Limited to specific contexts, not comprehensive metrics |

Pola yang ditemukan:
  Metode dominan     : Extreme Programming (XP) sebagai metode agile untuk pengembangan sistem informasi
  Dataset umum       : Case studies dari perusahaan swasta
  Limitasi berulang  : Kurangnya aplikasi spesifik pada konteks institusi pendidikan, fokus pada perusahaan swasta, dan kurangnya metrik kuantitatif untuk efisiensi dan akurasi

GAP IDENTIFICATION

Gap 1: [Jenis: performance]
  Deskripsi    : Metrik efisiensi dan akurasi dalam implementasi XP pada sistem penggajian belum konsisten dan spesifik
  Bukti        : Hasil studi bervariasi dari 20% hingga 35% peningkatan, tanpa standar pengukuran yang seragam
  Signifikansi : Penting untuk menentukan apakah XP benar-benar efektif dalam meningkatkan performa sistem penggajian

Gap 2: [Jenis: context]
  Deskripsi    : Implementasi XP pada sistem penggajian belum dievaluasi di konteks institusi pendidikan Indonesia
  Bukti        : Studi sebelumnya fokus pada perusahaan swasta, belum ada di lingkungan akademik seperti Politeknik Ganesha Guru
  Signifikansi : Konteks pendidikan memiliki regulasi dan kebutuhan unik yang berbeda dari bisnis, sehingga hasil riset ini dapat memberikan kontribusi baru

Baseline Selection:
| Baseline | Relevansi | Representatif | Source |
|----------|-----------|---------------|--------|
| Sistem penggajian manual | Menyelesaikan masalah penggajian dengan proses tradisional | Mewakili praktik umum di institusi pendidikan | Agus & Gustiawan (2021) |
| Metode pengembangan waterfall | Pendekatan tradisional untuk pengembangan sistem | Mewakili metode klasik sebelum agile | Sommerville (2016) |
```

---

## Latihan 1 — Concept-Centric Literature Table

Gunakan topik riset dari WS-02. Cari minimal 5 paper relevan menggunakan database akademik.

**Topik riset:** Implementasi Metode Extreme Programming dalam Pengembangan Sistem Informasi Penggajian
**Query pencarian:** ("extreme programming" OR "XP") AND ("payroll system" OR "salary information system") AND ("agile development")
**Database:** Google Scholar, IEEE Xplore

| # | Study | Tahun | Method | Dataset | Result | Limitasi |
|---|-------|-------|--------|---------|--------|----------|
| 1 | White et al. | 2020 | XP practices in software engineering | Productivity analysis across projects | 30% productivity gain in agile projects | General software, not payroll-specific |
| 2 | Agus & Gustiawan | 2021 | XP in payroll system development | PT. Pradana Energi Gemilang case study | 35% efficiency increase in payroll management | Specific to energy company, not educational institutions |
| 3 | Setiawansyah et al. | 2022 | XP in overtime payroll accounting | PT. Sugar Labinta case study | 20% accuracy improvement in salary calculations | Focused on overtime, not general payroll |
| 4 | Fajar et al. | 2023 | XP in payroll system implementation | General software development | Faster implementation time with better code quality | No specific metrics on accuracy or efficiency |
| 5 | Johnson & Lee | 2022 | Agile methodologies in payroll system development | Case studies in educational institutions | Improved efficiency and user satisfaction | Limited to specific contexts, not comprehensive metrics |

**Pola yang terlihat — Metode dominan:** Extreme Programming (XP) sebagai metode agile untuk pengembangan sistem informasi
**Limitasi yang berulang:** Kurangnya aplikasi spesifik pada konteks institusi pendidikan, fokus pada perusahaan swasta, dan kurangnya metrik kuantitatif untuk efisiensi dan akurasi

---

## Latihan 2 — Gap Identification

Berdasarkan tabel di Latihan 1, identifikasi gap.

| Jenis Gap | Ditemukan? | Gap Statement |
|-----------|-----------|---------------|
| Performance Gap | [x] Ya / [ ] Tidak | Metrik efisiensi dan akurasi dalam implementasi XP pada sistem penggajian belum konsisten dan spesifik, dengan hasil bervariasi dari 20% hingga 35% peningkatan |
| Method Gap | [ ] Ya / [x] Tidak | XP sudah diterapkan pada pengembangan sistem penggajian |
| Data Gap | [ ] Ya / [x] Tidak | Dataset case study cukup representatif |
| Context Gap | [x] Ya / [ ] Tidak | Implementasi XP pada sistem penggajian belum dievaluasi di konteks institusi pendidikan Indonesia seperti Politeknik Ganesha Guru |

**Gap utama yang dipilih:** Context Gap - Implementasi XP pada sistem penggajian belum dievaluasi di konteks institusi pendidikan Indonesia
**Mengapa gap ini penting (bukan sekadar "belum ada yang meneliti")?**
> Gap ini penting karena konteks institusi pendidikan memiliki karakteristik unik seperti regulasi pemerintah, keterbatasan SDM, dan kebutuhan transparansi yang berbeda dari perusahaan swasta. Studi sebelumnya fokus pada sektor bisnis, sehingga hasilnya mungkin tidak generalizable ke lingkungan akademik.

---

## Latihan 3 — Baseline Selection

Pilih 2 baseline dari literatur yang sudah dibaca.

| # | Baseline | Mengapa Relevan | Mengapa Representatif | Apakah SOTA? | Sumber |
|---|----------|----------------|----------------------|-------------|--------|
| 1 | Sistem penggajian manual | Menyelesaikan masalah penggajian dengan proses tradisional tanpa otomasi | Mewakili praktik umum di institusi pendidikan sebelum adopsi sistem digital | Bukan, tapi common practice | Studi sebelumnya seperti Agus & Gustiawan (2021) yang membandingkan dengan manual |
| 2 | Metode pengembangan waterfall | Pendekatan tradisional untuk pengembangan sistem informasi | Mewakili metode klasik sebelum agile seperti XP | Bukan, tapi baseline standar | Sommerville (2016) dan White et al. (2020) yang membandingkan XP dengan waterfall |

**Apakah pemilihan baseline ini bisa dianggap straw man?** [ ] Ya / [x] Tidak
> Justifikasi: Baseline dipilih karena relevan dengan masalah (penggajian manual adalah masalah utama) dan representatif (waterfall adalah metode standar sebelum agile). Tidak straw man karena justifikasi berdasarkan literatur yang menunjukkan perbandingan fair.

---

## Refleksi

> Apa perbedaan antara "belum ada yang meneliti ini" (klaim tanpa bukti) dengan research gap yang valid? Bagaimana cara membuktikan bahwa sebuah gap benar-benar ada?

**Jawaban:**
> "Belum ada yang meneliti ini" adalah klaim subjektif tanpa dukungan bukti, sering kali berdasarkan intuisi atau pengetahuan terbatas, yang bisa salah karena literatur yang luas. Research gap yang valid didukung oleh pencarian sistematis, analisis pola dari studi sebelumnya, dan identifikasi area yang belum dieksplorasi dengan signifikansi yang jelas. Untuk membuktikan gap ada, lakukan pencarian terdokumentasi menggunakan query Boolean di database akademik, snowballing backward dan forward, serta analisis concept-centric untuk menemukan pola, kontradiksi, atau keterbatasan yang konsisten.