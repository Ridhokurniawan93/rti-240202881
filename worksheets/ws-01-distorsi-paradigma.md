# WS-01: Distorsi & Paradigma

> **Bab 1 — Research Mindset in IT**

---
## Ringkasan Materi

### Research Trust Model

Pengetahuan ilmiah tidak muncul langsung dari kenyataan. Ia melewati **6 tahap transformasi** yang masing-masing rawan distorsi:

```
Reality → Data → Processing → Analysis → Inference → Knowledge
```

Contoh: observasi kinerja database PostgreSQL dan MySQL dalam workload CRUD menghasilkan data response time. Distorsi dapat terjadi jika data yang dikumpulkan tidak representatif (misalnya hanya satu volume data), jika query yang diuji tidak standar, atau jika simpulan dibuat tanpa memperhitungkan faktor konfigurasi dan indexing.

Etika mencegah distorsi yang disengaja (fabrikasi, cherry-picking). Validitas mendeteksi distorsi yang tidak disengaja (confounding variable, sampling bias).

### Tiga Jenis Validitas

| Jenis | Pertanyaan | Contoh Ancaman |
|-------|-----------|----------------|
| **Internal Validity** | Apakah hubungan kausal benar ada? | Klaim indexing meningkatkan performa tanpa mengontrol volume data dan konfigurasi hardware |
| **External Validity** | Apakah bisa digeneralisasi? | Hasil hanya dari satu spesifikasi hardware dan satu skema database |
| **Construct Validity** | Apakah mengukur hal yang benar? | Performa hanya diukur dari response time tanpa mempertimbangkan throughput dan resource utilization |

### Paradigma Riset

Studi menunjukkan dua pendekatan sekaligus:
- **Positivis**: mengukur response time dan performa secara kuantitatif melalui pengujian eksperimental dengan kontrol variabel.
- **Design Science**: mengembangkan framework pengujian benchmarking sebagai artefak untuk menguji hipotesis perbedaan performa.

### Mode Berpikir Peneliti

**Curious** (mengapa performa MySQL dan PostgreSQL berbeda pada workload CRUD?) → **Critical** (apa bukti bahwa query optimization dan indexing memberikan dampak signifikan?) → **Systematic** (bagaimana prosedur pengujian dirancang agar dapat direplikasi?).

### Research vs Engineering

| Aspek | Engineering | Research |
|-------|------------|----------|
| Tujuan | Memilih database terbaik untuk proyek | Menghasilkan pengetahuan valid tentang dampak optimasi |
| Pertanyaan khas | "Database mana yang lebih cepat?" | "Apakah indexing strategy berdampak signifikan terhadap performa?" |
| Ukuran sukses | Database terpilih, sistem berjalan | Hipotesis terjawab, temuan tervalidasi |
| Kegagalan | Harus dihindari | Harus dilaporkan (negative result = kontribusi) |

### Istilah Penting

- **Research Mindset** — Pola pikir yang menuntut bukti dan mempertanyakan asumsi
- **Research Ethics** — Prinsip perilaku: kejujuran, objektivitas, keterbukaan, akuntabilitas
- **HARKing** — Hypothesizing After Results are Known — merumuskan hipotesis setelah melihat data
- **Falsifiability** — Hipotesis harus bisa dibuktikan salah

---

## Contoh Ringkas

- Masalah utama: perbedaan performa antara PostgreSQL dan MySQL pada workload CRUD belum dipahami secara menyeluruh, khususnya terkait dampak query optimization dan indexing strategy.
- Solusi: pengujian eksperimental terkontrol dengan variasi strategi indexing dan query optimization pada kedua DBMS.
- Pengujian: benchmarking dengan query CRUD (SELECT, INSERT, UPDATE, DELETE) pada berbagai volume data.
- Hasil: identifikasi dampak spesifik query optimization dan indexing terhadap performa masing-masing DBMS.

---

## Research Mindset Self-Assessment
```
Nama Peneliti    : Ridho Kurniawan
Tanggal          : 22 Juni 2026

1. Ketika membaca klaim "PostgreSQL lebih cepat dari MySQL":
   - Pertanyaan pertama saya: Apakah pengujian dilakukan dengan konfigurasi yang adil, termasuk indexing strategy yang setara?
   - Data yang dibutuhkan untuk verifikasi: Spesifikasi hardware, konfigurasi database, strategi indexing, volume data, query yang diuji, serta prosedur pengukuran response time.

2. Posisi paradigma:
   - Pendekatan: [x] Positivis  [ ] Interpretivis  [ ] Design Science  [ ] Mixed
   - Alasan: Studi mengukur performa database secara kuantitatif melalui eksperimen terkontrol dengan metrik response time.

3. Identifikasi distorsi:
   - Asumsi tersembunyi: Bahwa perbedaan performa hanya disebabkan oleh DBMS itu sendiri, tanpa mempertimbangkan konfigurasi, indexing, dan workload.
   - Sumber bias potensial: Spesifikasi hardware yang berbeda, konfigurasi default yang tidak setara, dan ketiadaan strategi indexing yang terkontrol.
   - Langkah mitigasi: Gunakan hardware identik, standarisasi konfigurasi, dan dokumentasikan semua parameter pengujian.

4. Komitmen etika:
   - Data yang tidak akan dimanipulasi: Response time hasil pengujian, konfigurasi database, hasil statistik.
   - Batasan yang diakui sejak awal: Pengujian terbatas pada satu spesifikasi hardware dan skema database tertentu.
```

---

## Latihan 1 — Identifikasi Distorsi

Pilih satu paper riset di bidang TI yang mengklaim "metode X meningkatkan performa." Telusuri setiap tahap Research Trust Model.

**Paper yang dipilih:**
> Judul: SQL Inner Join: MySQL and PostgreSQL Performance
> Penulis (Tahun): Ummul Hairah (2020)

| Tahap | Apa yang Dilakukan | Potensi Distorsi |
|-------|-------------------|-----------------|
| Reality → Data | Mengamati perbedaan performa MySQL dan PostgreSQL pada query inner join dengan data pharmacy dari 50.000 hingga 1.050.000 record. | Data hanya berasal dari satu skema database (pharmacy) dan satu jenis query (inner join), tidak mencakup workload CRUD secara lengkap. |
| Data → Processing | Mengukur response time menggunakan HeidiSQL 10.2 pada kedua DBMS dengan struktur tabel dan jumlah record yang identik. | Potensi distorsi dari konfigurasi default DBMS yang tidak disetarakan, serta ketiadaan strategi indexing yang terkontrol. |
| Processing → Analysis | Menganalisis data menggunakan regresi linier berganda, F-test, dan T-test untuk mengetahui pengaruh jumlah data dan relasi terhadap response time. | Analisis hanya menggunakan satu metode statistik; tidak mempertimbangkan faktor lain seperti penggunaan memori, CPU, atau konfigurasi server. |
| Analysis → Inference | Menyimpulkan bahwa PostgreSQL lebih cepat dari MySQL berdasarkan response time inner join, didukung uji statistik F-test dan T-test. | Klaim bisa terlalu luas karena hanya diuji pada query inner join, bukan pada operasi CRUD lengkap (INSERT, UPDATE, DELETE). |
| Inference → Knowledge | Menyebarluaskan temuan bahwa PostgreSQL memiliki response time lebih cepat daripada MySQL untuk operasi join. | Hasil mungkin tidak generalis karena hanya satu skema database, satu hardware, dan tanpa variasi indexing strategy. |

**Distorsi paling besar di tahap:** Reality → Data

**Dua distorsi spesifik yang teridentifikasi:**
1. Pengujian hanya menggunakan satu jenis query (inner join) tanpa mencakup operasi CRUD lainnya (SELECT sederhana, INSERT, UPDATE, DELETE), sehingga kesimpulan tentang performa keseluruhan DBMS menjadi tidak lengkap.
2. Tidak adanya kontrol terhadap strategi indexing dan konfigurasi DBMS yang dapat memengaruhi response time secara signifikan, sehingga perbedaan performa bisa jadi disebabkan oleh konfigurasi, bukan kemampuan inherent DBMS.

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

**Topik riset:** Analisis Dampak Query Optimization dan Indexing Strategy terhadap Performa PostgreSQL dan MySQL dalam Workload CRUD

| Kriteria | Positivis | Interpretivis | Design Science |
|----------|-----------|---------------|----------------|
| Kesesuaian dengan topik (1–5) | 5 | 2 | 4 |
| Jenis data yang dikumpulkan | Response time (ms), throughput (QPS), CPU/memory usage, hasil uji statistik | Pengalaman developer dalam memilih database | Artefak benchmarking framework, hasil evaluasi eksperimen |
| Limitasi paradigma | Mungkin mengabaikan konteks penggunaan nyata dan preferensi developer | Kurang cocok untuk klaim performa kuantitatif | Hasil terbatas pada artefak yang dikembangkan, sulit digeneralisasi tanpa replikasi |

**Paradigma yang dipilih:** Positivis
**Alasan:** Topik berfokus pada pengukuran performa database secara kuantitatif melalui eksperimen terkontrol, dengan metrik response time yang objektif dan analisis statistik untuk membuktikan dampak query optimization dan indexing strategy.

---

## Refleksi

> Sebelum membaca materi ini, apakah pernah mempertanyakan klaim "PostgreSQL lebih cepat dari MySQL"? Setelah memahami rantai distorsi, pertanyaan apa yang sekarang akan diajukan saat membaca paper?

**Jawaban:**
> Saya sekarang akan menanyakan apakah konfigurasi kedua DBMS sudah disetarakan, apakah strategi indexing sudah dikontrol, apakah pengujian mencakup workload CRUD yang lengkap, dan apakah hasil dapat direplikasi pada hardware dan skema database yang berbeda. Saya juga akan mempertanyakan apakah ada confounding variable seperti perbedaan versi DBMS, konfigurasi buffer pool, atau cache yang tidak dikontrol.
