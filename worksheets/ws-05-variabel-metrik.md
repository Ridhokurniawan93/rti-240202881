# WS-05: Variabel & Metrik

> **Bab 5 — Metric, Measurement & Data**

---

## Ringkasan Materi

### Measurement Alignment Model

Setiap pengukuran yang valid harus bisa ditelusuri melalui rantai ini tanpa lompatan logis:

```
Problem → Concept → Variable → Metric → Data → Result
```

### Operationalization = Keputusan Desain

Menerjemahkan konsep abstrak menjadi variabel terukur bukan proses mekanis. "Code quality" yang diukur via SonarQube code smells membawa asumsi implisit. Setiap operasionalisasi harus didokumentasikan dan dijustifikasi.

### Empat Tipe Data (NOIR)

| Tipe | Ciri | Contoh | Operasi Valid |
|------|------|--------|---------------|
| **Nominal** | Kategori, tanpa urutan | Jenis algoritma (RF, SVM, CNN) | Modus, chi-square |
| **Ordinal** | Urutan, interval tidak sama | Skala Likert (1-5) | Median, Spearman |
| **Interval** | Jarak bermakna, tanpa nol absolut | Suhu Celsius | Mean, Pearson, t-test |
| **Ratio** | Jarak bermakna + nol absolut | Waktu eksekusi (ms) | Semua operasi |

Tipe data menentukan uji statistik yang valid. Kebanyakan metrik performa TI = ratio; persepsi pengguna = ordinal.

### Kriteria Pemilihan Metrik

- **Representative** — Mewakili konsep yang diteliti
- **Sensitive** — Cukup peka menangkap perbedaan bermakna (hindari ceiling effect)
- **Feasible** — Bisa dikumpulkan dalam batasan waktu dan biaya

### Pre-registration

Metrik harus ditentukan **sebelum** eksperimen. Memilih metrik setelah melihat data = **p-hacking**. Metrik tambahan yang ditemukan kemudian dilaporkan sebagai *exploratory*, bukan *confirmatory*.

### Primary vs Secondary Metric

- **Primary Metric** — Langsung terikat ke hipotesis, menentukan kesimpulan
- **Secondary Metric** — Pendukung, dilaporkan di samping primary; statusnya suplementer

### Research vs Engineering

| Aspek | Engineering | Research |
|-------|------------|----------|
| Pemilihan metrik | Berdasarkan kebiasaan/tool yang ada | Berdasarkan construct validity |
| Anomali | Dihapus untuk laporan bersih | Diinvestigasi — bisa jadi temuan |
| Kapan dipilih | Setelah sistem jadi (monitoring) | Sebelum eksperimen (by design) |

### Istilah Penting

- **Operationalization** — Transformasi konsep abstrak menjadi variabel terukur
- **Construct Validity** — Sejauh mana pengukuran benar-benar mengukur konsep yang dimaksud
- **Measurement Scale** — Klasifikasi data (NOIR) yang menentukan analisis valid
- **Multi-metric Evaluation** — Menggunakan beberapa metrik untuk menangkap konsep kompleks

---

## Template A.5 — Definisi Variabel, Metrik & Justifikasi

```
VARIABLE & METRIC DEFINITION

Research Question: Apakah pengembangan sistem informasi penggajian di Politeknik Ganesha Guru menggunakan Extreme Programming (XP) menghasilkan efisiensi waktu pemrosesan dan akurasi perhitungan yang lebih baik dibandingkan dengan pengembangan tradisional dan proses manual?

| Variabel | Tipe | Konsep | Metrik | Skala | Satuan | Cara Mengukur | Justifikasi |
|----------|------|--------|--------|-------|--------|---------------|-------------|
| Metode pengembangan sistem | IV | Pendekatan desain dan pengelolaan pengembangan perangkat lunak | Kategori: XP vs tradisional/manual | Nominal | — | Klasifikasi metode berdasarkan dokumentasi proses pengembangan | Memilih metode sebagai variabel independen memungkinkan perbandingan pengaruh desain pengembangan terhadap outcome sistem.
| Efisiensi pemrosesan payroll | DV | Kecepatan sistem dan proses penggajian | Rata-rata waktu pemrosesan payroll per periode | Ratio | Menit | Ukur waktu mulai hingga selesai pemrosesan payroll pada sistem yang diuji | Waktu merupakan indikator langsung efisiensi dan memiliki nol absolut, cocok sebagai metrik utama untuk hypothesis.
| Akurasi perhitungan gaji | DV | Ketepatan hasil output sistem penggajian | Persentase kesalahan perhitungan gaji terhadap total transaksi | Ratio | Persen (%) | Bandingkan jumlah kesalahan gaji dengan total transaksi payroll dalam periode pengujian | Mengukur seberapa akurat sistem menghitung gaji, langsung terkait dengan tujuan utama sistem penggajian.
| Kepuasan pengguna | DV | Persepsi pengguna terhadap kualitas sistem | Skor rata-rata kepuasan pengguna menggunakan survei Likert 1-5 | Ordinal | Skor | Survei pengguna sistem (admin dan pemangku kepentingan) setelah penggunaan sistem | Menangkap aspek subjektif kualitas sistem yang tidak tercermin oleh metrik teknis saja.
| Kompleksitas data payroll | CV | Kondisi input data yang mempengaruhi pengujian | Jumlah pegawai dan variasi komponen gaji | Ratio / Nominal | jumlah / jenis | Hitung jumlah pegawai yang diproses dan kategori komponen gaji yang digunakan | Kontrol terhadap variasi data untuk memastikan perbandingan kausal antara metode pengembangan.

Alignment Check:
  RQ → Concept → Variable → Metric → Data → Result
  [x] Setiap langkah terdokumentasi
  [x] Tidak ada "lompatan logis"
  [x] Metrik mengukur apa yang dimaksud (construct validity)
```

---

## Latihan 1 — Operationalization Chain

Gunakan RQ dari WS-04. Definisikan variabel dan metriknya.

**RQ:** Apakah pengembangan sistem informasi penggajian di Politeknik Ganesha Guru menggunakan Extreme Programming (XP) menghasilkan efisiensi waktu pemrosesan dan akurasi perhitungan yang lebih baik dibandingkan pengembangan tradisional/manual?

| Variabel | Tipe | Konsep Abstrak | Metrik Konkret | Skala (NOIR) | Satuan |
|----------|------|---------------|----------------|-------------|--------|
| Metode pengembangan | IV | Pendekatan desain sistem penggajian | XP vs tradisional/manual | Nominal | — |
| Waktu pemrosesan payroll | DV | Efisiensi proses penggajian | Rata-rata waktu pemrosesan per periode | Ratio | Menit |
| Kesalahan perhitungan gaji | DV | Akurasi output sistem | Persentase kesalahan perhitungan | Ratio | Persen |
| Kepuasan pengguna | DV | Persepsi kualitas sistem | Skor rata-rata Likert 1-5 | Ordinal | Skor |
| Kompleksitas data payroll | CV | Kondisi input data dan variasi kasus | Jumlah pegawai dan variasi komponen gaji | Ratio | jumlah/jenis |

**Apakah ada lompatan logis dalam rantai?** [ ] Ya / [x] Tidak
> Jika ya, di mana? —

---

## Latihan 2 — Evaluasi Metrik

Evaluasi metrik DV yang dipilih di Latihan 1 menggunakan 3 kriteria.

| Kriteria | Skor (1-5) | Justifikasi |
|----------|-----------|-------------|
| Representative | 5 | Waktu pemrosesan dan persentase kesalahan langsung mencerminkan efisiensi dan akurasi sistem penggajian. |
| Sensitive | 4 | Metrik ratio seperti waktu dan kesalahan peka terhadap perubahan performa, tetapi perlu standar pengukuran konsisten. |
| Feasible | 5 | Data waktu dan kesalahan dapat dikumpulkan dari log sistem dan uji penghitungan dengan mudah. |

**Apakah perlu secondary metric?** [x] Ya / [ ] Tidak
> Jika ya, apa dan mengapa? Kepuasan pengguna sebagai secondary metric mendukung hasil teknis dengan perspektif pengalaman pengguna, terutama karena sistem penggajian harus diterima oleh admin dan pemangku kepentingan.

**Contoh kasus ceiling effect untuk metrik ini:**
> Jika skor kepuasan pengguna rata-rata sudah sangat tinggi (misalnya 4.8-5.0), perbedaan antara metode menjadi sulit dideteksi karena skala Likert terbatas.

---

## Latihan 3 — Data Quality Check

Bayangkan data yang akan dikumpulkan dari eksperimen. Evaluasi 4 dimensi kualitas data.

| Dimensi | Pertanyaan | Jawaban | Strategi Mitigasi |
|---------|-----------|---------|------------------|
| Completeness | Apakah semua data point terkumpul? | Data harus mencakup semua eksekusi payroll dalam periode pengujian dan semua respon survei pengguna. | Gunakan checklist log pengujian dan reminder survei untuk memastikan tidak ada data yang hilang. |
| Consistency | Apakah ada kontradiksi internal? | Periksa apakah total waktu pemrosesan selaras dengan jumlah transaksi dan apakah persentase kesalahan dihitung dengan rumus yang konsisten. | Standarisasi format pelaporan dan verifikasi ganda antara log sistem dan hasil perhitungan manual. |
| Validity | Apakah benar-benar mengukur yang dimaksud? | Waktu pemrosesan mengukur efisiensi, kesalahan gaji mengukur akurasi, dan kepuasan mengukur pengalaman pengguna. | Gunakan definisi metrik yang jelas dan validasi dengan stakeholder bahwa metrik merepresentasikan konsep yang dimaksud. |
| Representativeness | Apakah sampel mewakili populasi target? | Sampel harus mencakup variasi pegawai dan tipe gaji di Politeknik Ganesha Guru, bukan hanya skenario sederhana. | Pilih unit pengujian dengan jumlah pegawai dan kondisi tunjangan yang mencerminkan keseluruhan populasi institusi. |

---

## Refleksi

> Mengapa memilih metrik setelah melihat data dianggap p-hacking? Apa bedanya dengan eksplorasi data yang sah?

**Jawaban:**
> Memilih metrik setelah melihat data dianggap p-hacking karena keputusan tersebut dapat diarahkan untuk mendapatkan hasil signifikan secara statistik, bukan berdasarkan konstruk penelitian yang konsisten. Eksplorasi data yang sah tetap memisahkan metrik yang telah ditentukan sebelumnya (confirmatory) dari temuan tambahan yang dilaporkan sebagai exploratory, sehingga transparansi dan validitas penelitian terjaga.
