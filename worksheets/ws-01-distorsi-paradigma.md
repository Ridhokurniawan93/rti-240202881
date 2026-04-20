# WS-01: Distorsi & Paradigma

> **Bab 1 — Research Mindset in IT**

---
## Ringkasan Materi

### Research Trust Model

Pengetahuan ilmiah tidak muncul langsung dari kenyataan. Ia melewati **6 tahap transformasi** yang masing-masing rawan distorsi:

```
Reality → Data → Processing → Analysis → Inference → Knowledge
```

Contoh: observasi sistem penggajian manual di Politeknik Ganesha Guru menghasilkan data pegawai dan gaji. Distorsi dapat terjadi jika data yang dikumpulkan tidak lengkap, jika input data dimasukkan secara salah, atau jika simpulan dibuat tanpa evaluasi nyata.

Etika mencegah distorsi yang disengaja (fabrikasi, cherry-picking). Validitas mendeteksi distorsi yang tidak disengaja (confounding variable, sampling bias).

### Tiga Jenis Validitas

| Jenis | Pertanyaan | Contoh Ancaman |
|-------|-----------|----------------|
| **Internal Validity** | Apakah hubungan kausal benar ada? | Klaim XP meningkatkan efisiensi tanpa kontrol terhadap faktor lain |
| **External Validity** | Apakah bisa digeneralisasi? | Hasil hanya diambil dari satu kampus, bukan dari beberapa organisasi |
| **Construct Validity** | Apakah mengukur hal yang benar? | Metrik efisiensi hanya berdasarkan fungsi sistem, bukan kepuasan pengguna |

### Paradigma Riset

Studi menunjukkan dua pendekatan sekaligus:
- **Positivis**: mengukur efisiensi dan akurasi secara kuantitatif melalui pengujian dan evaluasi sistem.
- **Design Science**: mengembangkan artefak sistem informasi penggajian sebagai alat untuk menguji hipotesis peningkatan efisiensi.

### Mode Berpikir Peneliti

**Curious** (mengapa penggajian manual bermasalah?) → **Critical** (apa bukti bahwa XP menyelesaikan masalah?) → **Systematic** (bagaimana prosedur penelitian dirancang agar dapat direplikasi?).

### Research vs Engineering

| Aspek | Engineering | Research |
|-------|------------|----------|
| Tujuan | Membuat sistem yang bekerja | Menghasilkan pengetahuan yang valid |
| Pertanyaan khas | "Bagaimana membuatnya jalan?" | "Apakah klaim ini benar?" |
| Ukuran sukses | Sistem berfungsi, client puas | Hipotesis terjawab, temuan tervalidasi |
| Kegagalan | Harus dihindari | Harus dilaporkan (negative result = kontribusi) |

### Istilah Penting

- **Research Mindset** — Pola pikir yang menuntut bukti dan mempertanyakan asumsi
- **Research Ethics** — Prinsip perilaku: kejujuran, objektivitas, keterbukaan, akuntabilitas
- **HARKing** — Hypothesizing After Results are Known — merumuskan hipotesis setelah melihat data
- **Falsifiability** — Hipotesis harus bisa dibuktikan salah

---

## Contoh Ringkas

- Masalah utama: sistem penggajian di Kampus Politeknik Ganesha Guru masih manual, menyebabkan redundansi data dan kesalahan perhitungan.
- Solusi: sistem informasi penggajian berbasis PHP dan MySQL dengan metode Extreme Programming.
- Pengujian: black-box testing dan pengumpulan umpan balik pengguna.
- Hasil: sistem berfungsi sesuai kebutuhan dan meningkatkan efisiensi serta akurasi.

---

## Research Mindset Self-Assessment
```
Nama Peneliti    : Ridho Kurniawan
Tanggal          : 11 April 2026

1. Ketika membaca klaim "metode X 95% akurat":
   - Pertanyaan pertama saya: Apakah data dan metode pengujian sudah dijelaskan secara lengkap?
   - Data yang dibutuhkan untuk verifikasi: Data input, prosedur pengujian, ukuran efisiensi, serta kondisi eksperimen.

2. Posisi paradigma:
   - Pendekatan: [x] Positivis  [ ] Interpretivis  [ ] Design Science  [ ] Mixed
   - Alasan: Studi mengukur efisiensi dan akurasi secara kuantitatif dari sebuah sistem artefak.

3. Identifikasi distorsi:
   - Asumsi tersembunyi: Bahwa semua masalah penggajian dapat diselesaikan hanya dengan sistem baru.
   - Sumber bias potensial: Hanya satu lokasi studi, data manual dari satu instansi, dan tidak ada pembanding dengan metode lain.
   - Langkah mitigasi: Laporkan batasan, gunakan data yang lebih luas, dan lakukan validasi pengguna eksternal.

4. Komitmen etika:
   - Data yang tidak akan dimanipulasi: Data gaji pegawai, hasil pengujian fungsional, laporan bug.
   - Batasan yang diakui sejak awal: Sampel terbatas pada Politeknik Ganesha Guru dan metode pengujian utama adalah black-box testing.
```

---

## Latihan 1 — Identifikasi Distorsi

Pilih satu paper riset di bidang TI yang mengklaim "metode X meningkatkan performa." Telusuri setiap tahap Research Trust Model.

**Paper yang dipilih:**
> Judul: Implementasi Metode Extreme Programming dalam Pengembangan Sistem Informasi Penggajian di Kampus Politeknik Ganesha Guru
> Penulis (Tahun): Putu Maha Putra dkk. (2025)

| Tahap | Apa yang Dilakukan | Potensi Distorsi |
|-------|-------------------|-----------------|
| Reality → Data | Mengamati kondisi penggajian manual di kampus dan mencatat masalah seperti redundansi dan kesalahan perhitungan. | Data observasi bisa tidak lengkap atau hanya berasal dari satu unit organisasi. |
| Data → Processing | Mengolah data kebutuhan pengguna dan perancangan sistem dengan DFD/ERD. | Asumsi fitur bisa bias jika hanya berdasarkan wawancara terbatas atau input manual yang salah. |
| Processing → Analysis | Menganalisis desain sistem, pemilihan XP, dan rencana pengujian. | Analisis dapat keliru jika tidak membandingkan dengan metode pengembangan lain atau tidak mempertimbangkan faktor eksternal. |
| Analysis → Inference | Menyimpulkan bahwa XP meningkatkan efisiensi dan akurasi. | Klaim bisa terlalu kuat jika hanya didukung oleh pengujian terbatas dan tanpa pembandingan kuantitatif. |
| Inference → Knowledge | Menyebarluaskan temuan bahwa sistem informasi penggajian dengan XP efektif di kampus tersebut. | Hasil mungkin tidak generalis, karena hanya satu studi kasus dan tanpa uji ulang di organisasi lain. |

**Distorsi paling besar di tahap:** Reality → Data

**Dua distorsi spesifik yang teridentifikasi:**
1. Pengumpulan data masalah penggajian manual hanya dari satu kampus, sehingga temuan bisa tidak mewakili situasi penggajian di institusi lain.
2. Input data manual pada tahap pemrosesan bisa menghasilkan kesalahan dan menyebabkan sistem baru dibangun berdasarkan informasi yang tidak akurat.

---

## Latihan 2 — Analisis Kasus Etika

Skenario: Seorang peneliti menemukan bahwa jika 3 data point outlier dihapus, hasil eksperimennya menjadi signifikan. Dengan outlier, hasilnya tidak signifikan.

| Perspektif | Analisis |
|------------|---------|
| Kejujuran ilmiah | Harus melaporkan kedua versi hasil: dengan dan tanpa outlier. Menyembunyikan outlier berarti mengabaikan informasi penting. |
| Transparansi | Jelaskan alasan penghapusan outlier, bagaimana outlier dikenali, dan dampak penghapusan terhadap kesimpulan. |
| Peer review | Review sejawat akan meminta bukti tambahan bahwa outlier bukan hasil kesalahan pengukuran atau proses, serta memeriksa apakah penghapusan sah. |

**Keputusan akhir dan justifikasi:**
> Hasil harus dilaporkan secara lengkap: sertakan analisis awal dengan outlier, analisis sekunder tanpa outlier, dan penjelasan mengapa outlier dihapus. Keputusan ini menjaga integritas penelitian dan memberi pembaca konteks penuh.

---

## Latihan 3 — Posisi Paradigma

**Topik riset:** Implementasi metode Extreme Programming dalam pengembangan sistem informasi penggajian di Politeknik Ganesha Guru

| Kriteria | Positivis | Interpretivis | Design Science |
|----------|-----------|---------------|----------------|
| Kesesuaian dengan topik (1–5) | 5 | 2 | 5 |
| Jenis data yang dikumpulkan | Waktu pengembangan, akurasi perhitungan, hasil pengujian black-box | Wawancara pengguna, pengalaman penggunaan | Data artefak, hasil iterasi pengembangan, evaluasi fungsional |
| Limitasi paradigma | Mungkin mengabaikan konteks sosial dan pengalaman pengguna | Kurang cocok untuk klaim efisiensi kuantitatif | Hasil terbatas pada artefak yang dikembangkan, sulit digeneralisasi tanpa replikasi |

**Paradigma yang dipilih:** Design Science
**Alasan:** Topik berfokus pada pengembangan artefak sistem informasi sebagai instrumen untuk menguji klaim peningkatan efisiensi dan akurasi.

---

## Refleksi

> Sebelum membaca materi ini, apakah pernah mempertanyakan klaim "95% akurat"? Setelah memahami rantai distorsi, pertanyaan apa yang sekarang akan diajukan saat membaca paper?

**Jawaban:**
> Saya sekarang akan menanyakan apakah data awal valid, apakah metode pengujian sesuai dengan klaim, dan apakah hasil dapat digeneralisasi di luar konteks satu kampus. Saya juga akan mempertanyakan apakah ada asumsi tersembunyi yang membuat klaim efisiensi terlalu optimistis.

