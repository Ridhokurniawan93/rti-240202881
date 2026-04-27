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

### Empat Jenis Research Gap

| Jenis Gap | Deskripsi | Contoh dari paper.md |
|-----------|----------|--------|
| **Performance Gap** | Performa belum memadai | Belum ada metrik spesifik untuk akurasi sistem penggajian akademik |
| **Method Gap** | Pendekatan belum diterapkan | XP belum diterapkan di institusi akademik |
| **Data Gap** | Dataset terbatas/tidak representatif | Studi XP penggajian hanya pada perusahaan (PT. Pradana, PT. Sugar Labinta) |
| **Context Gap** | Belum diuji pada konteks berbeda | XP untuk penggajian belum dievaluasi di lingkungan akademik |

Gap terkuat dari paper.md = **Context Gap** + **Method Gap**: XP belum diimplementasikan untuk sistem penggajian di kampus/institusi pendidikan.

### Systematic Search Strategy

1. **Database**: IEEE Xplore, ACM DL, Scopus, Google Scholar
2. **Boolean query** yang terdokumentasi eksplisit: Contoh dari paper.md: ("payroll system" OR "penggajian") AND ("information system" OR "sistem informasi")
3. **Snowballing**: 
   - Backward: dari paper.md telusuri referensi [1], [9], [10] (Beck, Sommerville, Laudon)
   - Forward: cari siapa yang mengutip Agus & Gustiawan [13], Setiawansyah [14]
4. Klaim "belum ada penelitian di akademik" harus didukung **bukti pencarian**: bahwa studi XP penggajian sebelumnya hanya di konteks bisnis (PT., perusahaan)

### Baseline Selection — 3 Kriteria

| Kriteria | Pertanyaan | Contoh |
|----------|-----------|--------|
| **Relevan** | Apakah menyelesaikan masalah yang sama? | Agus & Gustiawan [13] relevan: XP untuk sistem penggajian, meski di konteks berbeda |
| **Representatif** | Apakah mewakili common practice? | Semua studi terkait pakai XP atau Agile, bukan waterfall → XP adalah baseline yang tepat |
| **State-of-the-Art** | Apakah terbaru/terbaik? | Fajar et al. [15] lebih baru, tapi White et al. [12] lebih rigorous (30% improvement) |

Membandingkan XP (iteratif) dengan waterfall (tanpa baseline rigorous) = **straw man comparison** — pastikan baseline valid.

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

Topik      : Sistem Informasi Penggajian dengan Extreme Programming di Institusi Akademik
Database   : Google Scholar, IEEE Xplore, Scopus
Query      : ("payroll system" OR "sistem penggajian") AND ("Extreme Programming" OR "XP" OR "Agile")
Tahun      : 2015-2025
Hasil awal : 47 paper → Screening → 8 paper final (sesuai relevance)

Literature Matrix (concept-centric):

| Study | Tahun | Domain | Method | Main Result | Konteks | Limitation |
|-------|-------|--------|--------|-------------|---------|-----------|
| Sommerville [9] | - | Sistem Informasi | Konsep SI penggajian | Komponen: input, process, output, pajak | General | Teoritis |
| Laudon & Laudon [10] | - | SI Architecture | Sistem terpadu | Integrasi komponen SI | General | Tidak spesifik penggajian |
| Rahman et al. [10] | 2022 | Teknologi Penggajian | Digital system | 40% efisiensi vs manual | Bisnis | Limited sample |
| Beck [1] | 1999 | XP Principles | Extreme Programming | Iterasi pendek, user involvement | General | Tidak khusus penggajian |
| White et al. [12] | 2020 | XP Adoption | XP practices | 30% efisiensi improvement | Bisnis/Software | Tidak spesifik aplikasi |
| Agus & Gustiawan [13] | 2023 | Payroll XP | XP implementation | 35% efficiency (PT. Pradana) | Bisnis | Satu perusahaan |
| Setiawansyah et al. [14] | 2022 | Payroll XP | XP + Akuntansi | 20% akurasi peningkatan (PT. Sugar) | Bisnis | Limited scope |
| Fajar et al. [15] | 2023 | Payroll XP | XP development | Implementasi lebih cepat | Bisnis | Tidak terukur jelas |

Pola yang ditemukan:
  Metode dominan     : Extreme Programming dan Agile iteratif
  Domain umum        : Konteks bisnis/perusahaan swasta, bukan akademik
  Hasil berulang     : 20-40% peningkatan efisiensi atau akurasi
  Limitasi berulang  : Studi terbatas pada 1-2 organisasi, tidak di konteks akademik

GAP IDENTIFICATION

Gap 1: [Jenis: CONTEXT GAP + METHOD GAP]
  Deskripsi    : Metode XP untuk sistem penggajian belum diimplementasikan di institusi akademik (kampus). Semua studi sebelumnya fokus pada perusahaan bisnis (PT. Pradana, PT. Sugar Labinta).
  Bukti        : Agus & Gustiawan [13] — PT. swasta; Setiawansyah et al. [14] — PT. swasta; Fajar et al. [15] — perusahaan; tidak ada yang di universitas/politeknik
  Signifikansi : Institusi akademik memiliki struktur penggajian yang berbeda (pegawai tetap, dosen, kontrak), volume lebih kecil, tapi regulasi akademik unik. XP mungkin berbeda efektivitasnya.

Gap 2: [Jenis: PERFORMANCE GAP]
  Deskripsi    : Belum ada metrik spesifik dan terstandar untuk mengukur efisiensi dan akurasi sistem penggajian akademik.
  Bukti        : Agus [13] dan Setiawansyah [14] melaporkan efisiensi dalam persentase umum (35%, 20%), tapi tidak detail metrik: waktu proses, error rate, user satisfaction scores.
  Signifikansi : Diperlukan definisi operasional yang jelas untuk "efisiensi" dan "akurasi" pada konteks akademik.

Baseline Selection:
| Baseline | Relevansi | Representatif | Source | Justifikasi |
|----------|-----------|---------------|--------|------------|
| Agus & Gustiawan [13] — XP for Payroll | Tinggi (metode + domain sama) | Ya (common practice) | Paper terkait langsung | Implementasi XP payroll yang paling terukur |
| White et al. [12] — XP Adoption | Tinggi (metode sama) | Ya (SOTA XP) | Research-based | Prinsip XP yang rigorous dan teruji |
| Manual Process (baseline implisit) | Tinggi (konteks akademik) | Ya (current practice) | Observasi Politeknik Ganesha | Status quo untuk perbandingan |
```

---

## Latihan 1 — Concept-Centric Literature Table

Gunakan topik riset dari WS-02. Cari minimal 5 paper relevan menggunakan Google Scholar atau database lain.

**Topik riset:** Implementasi Extreme Programming dalam Sistem Informasi Penggajian di Institusi Akademik
**Query pencarian:** ("payroll system" OR "sistem penggajian") AND ("Extreme Programming" OR "XP") AND ("academic" OR "akademik" OR "universitas")
**Database:** Google Scholar, IEEE Xplore, Scopus

| # | Study | Tahun | Domain | Method | Result | Limitasi |
|---|-------|-------|--------|--------|--------|----------|
| 1 | Beck [1] | 1999 | Software Development | XP Principles | Iterasi pendek, user involvement | Tidak spesifik aplikasi domain |
| 2 | Agus & Gustiawan [13] | 2023 | Payroll System | XP implementation | 35% efficiency improvement | Konteks perusahaan, bukan akademik |
| 3 | Setiawansyah et al. [14] | 2022 | Payroll Accounting | XP + domain spesifik | 20% akurasi peningkatan | Terbatas pada PT. Sugar Labinta saja |
| 4 | White et al. [12] | 2020 | XP Adoption | Metriks XP success | 30% efisiensi peningkatan | General software, bukan payroll |
| 5 | Fajar et al. [15] | 2023 | Payroll XP | XP development | Implementasi lebih cepat | Metrik tidak detail, tidak terukur |

**Pola yang terlihat — Metode dominan:** Extreme Programming iteratif, pair programming, testing berkelanjutan
**Limitasi yang berulang:** Semua studi di konteks bisnis swasta (PT.), tidak di institusi akademik; metrik efisiensi tidak standar; sample size terbatas pada 1-2 organisasi

---

## Latihan 2 — Gap Identification

Berdasarkan tabel di Latihan 1, identifikasi gap.

| Jenis Gap | Ditemukan? | Gap Statement |
|-----------|-----------|---------------|
| Performance Gap | [x] Ya / [ ] Tidak | Metrik efisiensi dan akurasi tidak standar di antara studi; paper.md juga tidak memberikan baseline metrik spesifik untuk institusi akademik |
| Method Gap | [x] Ya / [ ] Tidak | XP belum diimplementasikan di institusi akademik (kampus/universitas); semua studi adalah di perusahaan bisnis (PT. Pradana, PT. Sugar) |
| Data Gap | [x] Ya / [ ] Tidak | Studi pada payroll system umumnya terbatas pada 1-2 organisasi saja; tidak ada dataset komparatif lintas institusi akademik |
| Context Gap | [x] Ya / [ ] Tidak | XP untuk payroll belum dievaluasi di lingkungan akademik dengan karakteristik unik (dosen tetap, kontrak, beasiswa, pajak akademik) |

**Gap utama yang dipilih:** Context Gap + Method Gap
**Mengapa gap ini penting (bukan sekadar "belum ada yang meneliti")?**
> Karena institusi akademik memiliki struktur penggajian yang berbeda dari bisnis swasta: (1) kategori pegawai beragam (dosen tetap, dosen kontrak, admin tetap, admin kontrak), (2) tunjangan akademik unik (honor mengajar, honor penelitian), (3) batasan anggaran lebih ketat. Efektivitas XP mungkin berbeda di konteks ini, sehingga generalisasi dari studi perusahaan swasta tidak valid tanpa evaluasi.

---

## Latihan 3 — Baseline Selection

Pilih 2 baseline dari literatur yang sudah dibaca.

| # | Baseline | Mengapa Relevan | Mengapa Representatif | Apakah SOTA? | Sumber |
|---|----------|----------------|----------------------|-------------|--------|
| 1 | Agus & Gustiawan [13] — XP for Payroll at PT. Pradana | Domain & method sama: XP untuk sistem penggajian | Ya, salah satu implementasi XP payroll paling terukur yang dilaporkan (6 dari 8 related work menggunakan XP) | Bukan pure SOTA, tapi recent practice (2023) dan common | Jurnal JITET |
| 2 | White et al. [12] — XP Adoption Metrics | Method sama (XP principles), dengan metrik rigorous (30% efficiency improvement) | Ya, mewakili best practice XP berdasarkan penelitian empiris | Ya, research-based dan comprehensive (published in peer-reviewed venue) | Referenced in paper |

**Apakah pemilihan baseline ini bisa dianggap straw man?** [ ] Ya / [x] Tidak
> Justifikasi: Kedua baseline valid karena (1) Agus [13] representatif dari implementasi nyata XP payroll, (2) White et al. [12] representatif dari prinsip dan metrik XP yang rigorous. Keduanya bukan "lemah" atau dipilih untuk membuat metode sendiri terlihat lebih baik. Namun, sebaiknya tambahkan baseline ketiga: sistem penggajian manual (status quo di akademik) untuk perbandingan konteks-spesifik.

---

## Refleksi

> Apa perbedaan antara "belum ada yang meneliti ini" (klaim tanpa bukti) dengan research gap yang valid? Bagaimana cara membuktikan bahwa sebuah gap benar-benar ada?

**Jawaban:**
> **Klaim tanpa bukti:** "Belum ada yang meneliti XP di akademik" — pernyataan lemah tanpa pencarian sistematis.
>
> **Research gap yang valid:** "Semua studi XP untuk payroll (Agus [13], Setiawansyah [14], Fajar [15]) dilakukan di perusahaan bisnis (PT. swasta), tidak di institusi akademik. Institusi akademik memiliki struktur penggajian berbeda (dosen tetap/kontrak, bonus akademik, batasan anggaran), sehingga efektivitas XP mungkin berbeda dan perlu dievaluasi."
>
> **Cara membuktikan gap ada:** (1) Dokumentasi pencarian sistematis (query, database, jumlah paper screening), (2) Tabel literature matrix yang menunjukkan pola domain/konteks, (3) Identifikasi jenis gap spesifik dengan bukti dari paper (bukan sekadar "belum ada"), (4) Alasan mengapa gap penting untuk solved (dampak praktis/teoritis), (5) Pernyataan eksplisit posisi riset: "Penelitian ini akan melanjutkan studi sebelumnya dengan menerapkan XP di lingkungan akademik" (seperti di paper.md).
