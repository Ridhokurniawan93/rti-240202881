# WS-12: Result Presentation & Visualization

> **Bab 12 — Penyajian Hasil & Visualisasi**

---

## Ringkasan Materi

### Data → Insight Model

```
Validated Data → Structured Presentation → Visualization → Pattern Recognition → Insight
```

Penyajian **mendahului** analisis. Tabel dan grafik membantu peneliti "melihat" data sebelum menghitung. Langsung ke uji statistik tanpa visualisasi berisiko kesimpulan yang secara teknis benar tapi kontekstual salah (Anscombe's Quartet, 1973).

### Tabel = Presisi, Grafik = Pola

Keduanya **saling melengkapi**:
- Tabel: angka presisi, self-contained (dipahami tanpa teks), sortable
- Grafik: pola visual, tren, perbandingan cepat

### Jenis Grafik Berdasarkan Tujuan

| Tujuan | Jenis Grafik |
|--------|-------------|
| Perbandingan response time antar DBMS | Grouped bar chart (PostgreSQL vs MySQL per operasi) |
| Distribusi response time per kondisi | Box plot (menunjukkan median, IQR, outlier) |
| Tren response time terhadap volume data | Line chart (x = volume, y = response time, per DBMS) |
| Dampak indexing terhadap response time | Grouped bar chart (no-index vs single vs composite) |
| Interaksi DBMS × indexing × optimization | Interaction plot (line chart dengan multiple lines) |

### Contoh Tabel Hasil yang Baik

| Kondisi | DBMS | Index | Query | SELECT (ms) | INSERT (ms) | UPDATE (ms) | DELETE (ms) |
|---------|------|-------|-------|-------------|-------------|-------------|-------------|
| C1 | PostgreSQL | none | default | 245.3 ± 12.1 | 18.4 ± 2.3 | 156.7 ± 8.9 | 42.1 ± 5.2 |
| C5 | MySQL | none | default | 312.8 ± 18.5 | 24.6 ± 3.1 | 189.3 ± 11.2 | 58.4 ± 7.3 |

*N=5 per sel (mean ± std). Volume = 100.000 records.*

### Visualization Bias — Yang Harus Dihindari

| Bias | Deskripsi | Dampak |
|------|----------|--------|
| Truncated axis | Y-axis tidak dari 0 | Memperbesar perbedaan kecil response time |
| Inconsistent scale | Dua grafik skala berbeda | Perbandingan PostgreSQL vs MySQL menyesatkan |
| Cherry-picked data | Hanya tampilkan volume yang "menang" | Selektif, tidak jujur |
| 3D effects | Efek 3D tanpa dimensi data ke-3 | Distorsi tanpa informasi |
| Missing error bar | Tidak ada std/CI | Menyembunyikan variabilitas dan thermal throttling effect |

### Engineering vs Research Presentation

| Aspek | Engineering | Research |
|-------|-----------|---------|
| Tujuan grafik | Dashboard monitoring DBMS | Mendukung argumen ilmiah tentang dampak indexing |
| Informasi wajib | KPI, threshold | Mean, std, CI, N, p-value, effect size |
| Bias handling | Less critical | Wajib dihindari (peer-review) |

---

## Template A.12 — Result Presentation Plan

```
RESULT PRESENTATION PLAN

Research Question :
  RQ1: Perbedaan response time PostgreSQL vs MySQL pada CRUD?
  RQ2: Dampak indexing strategy terhadap response time?
  RQ3: Interaksi DBMS × indexing × optimization?

Metrik Utama      : Response time (ms) — mean ± std, N=5 per sel
Metrik Sekunder   : Throughput (QPS), CPU usage (%), Memory usage (MB)

Tabel Hasil:
| Kondisi | DBMS | Index | Query | SELECT (ms) | INSERT (ms) | UPDATE (ms) | DELETE (ms) | n |
|---------|------|-------|-------|-------------|-------------|-------------|-------------|---|
| C1      | PostgreSQL | none      | default   | 245.3 ± 12.1 | 18.4 ± 2.3  | 156.7 ± 8.9  | 42.1 ± 5.2  | 5 |
| C2      | PostgreSQL | single    | default   | 89.2 ± 4.8  | 22.1 ± 3.1  | 98.3 ± 6.2   | 28.5 ± 3.8  | 5 |
| C3      | PostgreSQL | composite | default   | 67.8 ± 3.5  | 25.6 ± 3.8  | 85.4 ± 5.1   | 24.2 ± 2.9  | 5 |
| C4      | PostgreSQL | composite | optimized | 42.1 ± 2.8  | 19.8 ± 2.4  | 62.3 ± 4.3   | 18.7 ± 2.1  | 5 |
| C5      | MySQL      | none      | default   | 312.8 ± 18.5| 24.6 ± 3.1  | 189.3 ± 11.2 | 58.4 ± 7.3  | 5 |
| C6      | MySQL      | single    | default   | 128.4 ± 7.2 | 31.2 ± 4.5  | 132.7 ± 8.8  | 41.6 ± 5.1  | 5 |
| C7      | MySQL      | composite | default   | 95.6 ± 5.9  | 35.8 ± 5.2  | 112.4 ± 7.5  | 35.2 ± 4.2  | 5 |
| C8      | MySQL      | composite | optimized | 58.3 ± 3.6  | 28.4 ± 3.8  | 78.9 ± 5.8   | 26.8 ± 3.1  | 5 |

Visualisasi yang Direncanakan:
| # | Jenis Grafik | Pesan Utama | Metrik |
|---|-------------|-------------|--------|
| 1 | Grouped bar chart + error bar | Perbandingan response time PostgreSQL vs MySQL per operasi CRUD | Mean response time (ms) ± std |
| 2 | Line chart (x=volume) | Tren response time terhadap volume data per DBMS | Mean response time per volume (50K-1M) |
| 3 | Grouped bar chart | Dampak indexing (none/single/composite) terhadap SELECT per DBMS | Mean SELECT response time ± std |
| 4 | Box plot | Distribusi response time per kondisi (deteksi outlier thermal) | Semua data point per kondisi |
| 5 | Interaction plot | Interaksi DBMS × indexing terhadap response time | Mean response time, lines per DBMS |

Bias Check:
  [x] Y-axis mulai dari 0 (untuk semua bar chart)
  [x] Error bar (±1 std) ditampilkan di semua grafik
  [x] Semua 8 kondisi disertakan (tidak cherry-picked)
  [x] Tidak menggunakan 3D
  [x] Satuan (ms) tercantum di semua axis
  [x] N=5 tercantum di caption
  [x] Volume data disebutkan di setiap tabel/grafik
```

---

## Latihan 1 — Tabel Hasil

Buat tabel hasil eksperimen Anda (boleh dengan data simulasi jika belum punya data riil).

**Tabel 1. Response Time (ms) per Kondisi pada Volume 100.000 Records (N=5, Mean ± Std)**

| Kondisi | DBMS | Index | Query | SELECT (ms) | INSERT (ms) | UPDATE (ms) | DELETE (ms) |
|---------|------|-------|-------|-------------|-------------|-------------|-------------|
| C1 | PostgreSQL | none | default | 245.3 ± 12.1 | 18.4 ± 2.3 | 156.7 ± 8.9 | 42.1 ± 5.2 |
| C2 | PostgreSQL | single | default | 89.2 ± 4.8 | 22.1 ± 3.1 | 98.3 ± 6.2 | 28.5 ± 3.8 |
| C3 | PostgreSQL | composite | default | 67.8 ± 3.5 | 25.6 ± 3.8 | 85.4 ± 5.1 | 24.2 ± 2.9 |
| C4 | PostgreSQL | composite | optimized | 42.1 ± 2.8 | 19.8 ± 2.4 | 62.3 ± 4.3 | 18.7 ± 2.1 |
| C5 | MySQL | none | default | 312.8 ± 18.5 | 24.6 ± 3.1 | 189.3 ± 11.2 | 58.4 ± 7.3 |
| C6 | MySQL | single | default | 128.4 ± 7.2 | 31.2 ± 4.5 | 132.7 ± 8.8 | 41.6 ± 5.1 |
| C7 | MySQL | composite | default | 95.6 ± 5.9 | 35.8 ± 5.2 | 112.4 ± 7.5 | 35.2 ± 4.2 |
| C8 | MySQL | composite | optimized | 58.3 ± 3.6 | 28.4 ± 3.8 | 78.9 ± 5.8 | 26.8 ± 3.1 |

*N=5 per sel. Mean ± standard deviation. Volume = 100.000 records. Data simulasi untuk ilustrasi.*

**Tabel 2. Ringkasan Dampak Indexing pada SELECT (Volume 100K, N=5)**

| DBMS | No Index (ms) | Single Index (ms) | Composite Index (ms) | Penurunan (%) |
|------|---------------|-------------------|---------------------|---------------|
| PostgreSQL | 245.3 ± 12.1 | 89.2 ± 4.8 | 67.8 ± 3.5 | 72.4% |
| MySQL | 312.8 ± 18.5 | 128.4 ± 7.2 | 95.6 ± 5.9 | 69.4% |

**Checklist tabel:**
- [x] Self-contained (judul jelas, satuan ada, N tercantum, volume disebutkan)
- [x] Mean ± std (bukan single number)
- [x] Diurutkan berdasarkan condition ID (C1-C8)
- [x] Format konsisten di semua baris

---

## Latihan 2 — Rencana Visualisasi

Rencanakan 2-3 grafik untuk menyajikan data dari Latihan 1. Setiap grafik = satu pesan.

| # | Jenis Grafik | Pesan | Data yang Digunakan |
|---|-------------|-------|---------------------|
| 1 | **Grouped bar chart + error bar** | PostgreSQL vs MySQL: perbandingan response time per operasi CRUD (volume 100K). PostgreSQL konsisten lebih cepat pada semua operasi, terutama SELECT. | Mean ± std response time C1 vs C5 (no-index), C3 vs C7 (composite) |
| 2 | **Line chart (x = volume data)** | Tren response time SELECT terhadap volume data (50K → 1M). Gap antara PostgreSQL dan MySQL semakin besar seiring volume meningkat. | Mean response time SELECT per volume untuk C1 (PG, none) dan C5 (MySQL, none) |
| 3 | **Grouped bar chart (indexing impact)** | Dampak indexing strategy (none → single → composite) terhadap SELECT per DBMS. Composite index memberikan penurunan response time terbesar (~70%). | Mean ± std SELECT per index type, grouped by DBMS |
| 4 | **Box plot** | Distribusi response time per kondisi — menunjukkan outlier thermal throttling dan variabilitas antar replikasi. | Semua 5 data point per kondisi |
| 5 | **Interaction plot** | Interaksi DBMS × Indexing: garis PostgreSQL dan MySQL tidak paralel, menunjukkan bahwa dampak indexing berbeda antar DBMS. | Mean response time (sumbu Y), Index type (sumbu X), lines per DBMS |

---

## Latihan 3 — Bias Detection

Evaluasi visualisasi berikut untuk bias (skenario dari contoh):

**Skenario:** PostgreSQL SELECT = 245 ms, MySQL SELECT = 313 ms. Bar chart dengan Y-axis mulai dari 200 ms.

| Pertanyaan | Jawaban |
|-----------|---------|
| Apakah Y-axis menyesatkan? | **Ya** — Y-axis mulai dari 200 ms membuat PostgreSQL terlihat 2× lebih cepat, padahal perbedaan sebenarnya hanya ~28%. Jika Y-axis dari 0, perbedaan terlihat proporsional. |
| Apakah error bar ditampilkan? | Tidak — tanpa error bar (±12.1 ms dan ±18.5 ms), pembaca tidak tahu variabilitas data. Bisa saja dalam beberapa replikasi MySQL lebih cepat dari PostgreSQL. |
| Apakah semua kondisi ditampilkan? | Hanya SELECT pada no-index ditampilkan — kondisi lain (indexed, optimized) tidak ditampilkan. Ini cherry-picking jika tujuannya mengklaim "PostgreSQL selalu lebih cepat". |
| Apa solusinya? | (1) Y-axis mulai dari 0, (2) tambahkan error bar ±1 std, (3) tampilkan semua kondisi (8 kondisi × 4 CRUD), (4) sertakan volume data lain sebagai line chart. |

**Evaluasi grafik Anda sendiri dari Latihan 2:**
- [x] Semua bias check lulus:
  - Y-axis mulai dari 0 di semua bar chart
  - Error bar ±1 std ditampilkan di semua grafik
  - Semua 8 kondisi disertakan
  - Tidak menggunakan 3D effects
  - Satuan (ms) tercantum jelas
  - N=5 disebutkan di caption
- [ ] Ada yang perlu diperbaiki: **Untuk grafik #5 (interaction plot), perlu dipastikan Y-axis dari 0 dan kedua garis (PG & MySQL) menggunakan skala yang sama.**

---

## Refleksi

> Mengapa tabel dan grafik keduanya diperlukan — tidak cukup salah satu saja? Pernahkah Anda membuat grafik yang (tanpa sengaja) menyesatkan?

**Jawaban:**
> Tabel dan grafik keduanya diperlukan karena menyajikan informasi yang saling melengkapi. Tabel memberikan angka presisi (misalnya: PostgreSQL SELECT = 245.3 ± 12.1 ms) yang diperlukan untuk analisis statistik dan reproducibility, tetapi sulit untuk melihat pola secara cepat. Grafik memberikan pola visual (misalnya: gap antara PostgreSQL dan MySQL semakin besar seiring volume data meningkat) yang membantu identifikasi tren, outlier, dan interaksi, tetapi tidak memberikan angka eksak.
>
> Dalam konteks DBMS benchmarking, tabel diperlukan untuk melaporkan hasil ANOVA (F-value, p-value, effect size), sementara grafik diperlukan untuk menunjukkan pola seperti: (1) dampak indexing lebih besar pada MySQL daripada PostgreSQL (interaction effect), (2) response time meningkat linear terhadap volume data, dan (3) thermal throttling menyebabkan outlier pada replikasi tertentu. Tanpa keduanya, kesimpulan bisa tidak lengkap atau bahkan menyesatkan — misalnya, hanya melihat mean tanpa box plot bisa menyembunyikan outlier thermal throttling yang memengaruhi validitas hasil.
