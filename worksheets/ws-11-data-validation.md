# WS-11: Data Validation & Integrity

> **Bab 11 — Validasi Data & Integritas**

---

## Ringkasan Materi

### Data Trust Model

```
Raw Data → Data Cleaning → Consistency Check → Validation Process → Trusted Data
```

Data mentah belum bisa dipercaya. Harus melewati pipeline validasi sebelum siap untuk analisis statistik.

### Empat Pilar Data Quality

| Pilar | Deskripsi | Contoh Pelanggaran |
|-------|----------|-------------------|
| **Accuracy** | Nilai dalam range masuk akal | Response time negatif (-5 ms) atau 0 ms pada dataset 1M record |
| **Consistency** | Format seragam di semua run | Run 1: JSON, Run 2: CSV; satuan ms di beberapa trial, detik di yang lain |
| **Completeness** | Tidak ada data hilang dari plan | 780 dari 800 trial tercatat (20 trial gagal OOM) |
| **Validity** | Data sesuai desain eksperimen | Trial dengan indexing composite tapi dijalankan di kondisi no-index |

### Proses Validasi Progresif

1. **Format validation** — JSON structure, field presence, tipe data
2. **Range validation** — Response time > 0, throughput > 0, rows affected ≥ 0
3. **Consistency validation** — Satuan seragam, field names konsisten antar trial
4. **Logic validation** — Indexed query seharusnya ≤ non-indexed; higher volume → higher response time

Jika gagal di langkah awal → tidak perlu lanjut.

### Anomaly Detection — 3 Jenis

| Jenis | Deskripsi | Deteksi |
|-------|----------|---------|
| **Statistical outlier** | Response time di luar distribusi normal | IQR: < Q1-1.5×IQR atau > Q3+1.5×IQR |
| **Contextual anomaly** | Normal absolut, abnormal dalam konteks | SELECT tanpa index = 5ms pada 1M record (terlalu cepat, kemungkinan cache hit) |
| **Pattern anomaly** | Pola sistematis (bukan random) | Response time meningkat linearly setiap replikasi (thermal throttling) |

**Prinsip:** Detect → Investigate → Document → Decide — **JANGAN langsung hapus.**

### Engineering vs Research Validation

| Aspek | Engineering | Research |
|-------|-----------|---------|
| Tujuan | Data sesuai spesifikasi bisnis | Data layak untuk analisis statistik (ANOVA) |
| Missing data | Impute / set default | Investigasi penyebab → dokumentasi |
| Outlier | Bug → fix | Mungkin temuan (limitasi DBMS/hardware) → investigasi |
| Dokumentasi | Minimal (log error) | Komprehensif (anomali + keputusan + dampak ke kesimpulan) |

### Jebakan Kognitif

1. "Logging otomatis ≠ data benar" → script benchmark bisa ada bug di timer
2. "Outlier = hapus" → OOM pada volume 1M dengan RAM 8 GB justru temuan penting
3. "Dataset kecil tidak perlu validasi" → justru 800 trial rentan inkonsistensi
4. "Mean normal = data benar" → [10ms, 12ms, 11ms, **500ms**, 10ms] → mean 108.6ms terlihat wajar

---

## Template A.11 — Data Validation Checklist

```
DATA VALIDATION CHECKLIST

Completeness:
  [x] Semua 8 kondisi (C1-C8) tercakup
  [x] Semua 4 operasi CRUD (SELECT, INSERT, UPDATE, DELETE) ada
  [x] Semua 5 volume (50K, 100K, 250K, 500K, 1M) ada
  [x] Semua 5 replikasi per sel tercatat
  [x] Total: 800 trial (8 × 4 × 5 × 5)
  Missing: 6 dari 800 data points

Format Consistency:
  [x] Semua file format JSON dengan struktur identik
  [x] Field names konsisten (response_time_ms, throughput_qps, dll)
  [x] Tipe data konsisten (float untuk ms, integer untuk rows)

Range & Logic:
  [x] Response time > 0 ms (tidak ada nilai negatif atau zero)
  [x] Throughput > 0 QPS
  [x] Rows affected masuk akal (SELECT: ≥ 0, INSERT: 1, UPDATE/DELETE: ≥ 0)
  [x] Higher volume → generally higher response time
  [x] Indexed queries ≤ non-indexed queries (untuk SELECT dengan WHERE clause)
  Anomali ditemukan: thermal throttling pada beberapa replikasi; OOM/timeout pada volume 1M

Cross-Validation:
  [x] Replikasi dengan seed sama → hasil mendekati (CV < 5% pada 96% sel)
  [x] Trend konsisten: PostgreSQL vs MySQL sesuai literatur
  [x] Thermal throttling terdeteksi dari pola response time

Keputusan:
  [x] Data siap analisis (794 trial valid; 6 missing dilaporkan)
  [ ] Perlu cleaning (skenario: ____)
  [ ] Perlu re-run (skenario: ____)
```

---

## Latihan 1 — Completeness Check

Verifikasi apakah semua data yang direncanakan sudah terkumpul.

| Kondisi | DBMS | Indexing | Trial Direncanakan | Trial Tercatat | Missing | Alasan Missing |
|---------|------|----------|-------------------|---------------|---------|---------------|
| C1 | PostgreSQL | none, default | 100 (4 CRUD × 5 vol × 5 rep) | 100 | 0 | — |
| C2 | PostgreSQL | single, default | 100 | 100 | 0 | — |
| C3 | PostgreSQL | composite, default | 100 | 98 | 2 | OOM pada DELETE 1M, seed=789 & 1024 |
| C4 | PostgreSQL | composite, optimized | 100 | 100 | 0 | — |
| C5 | MySQL | none, default | 100 | 100 | 0 | — |
| C6 | MySQL | single, default | 100 | 100 | 0 | — |
| C7 | MySQL | composite, default | 100 | 97 | 3 | OOM pada INSERT 1M, seed=456, 789, 1024 |
| C8 | MySQL | composite, optimized | 100 | 99 | 1 | Timeout pada SELECT 1M, seed=1024 |

**Total expected:** 800 | **Total actual:** 794 | **Missing:** 6

**Keputusan untuk data missing:**
> 6 trial missing (0.75%) semuanya pada volume 1.000.000 record — disebabkan oleh limitasi RAM 8 GB pada laptop (OOM dan timeout). Ini bukan bug script melainkan **batasan hardware yang valid**. Trial yang missing didokumentasikan di `logs/anomalies/missing-trials.md` dan dilaporkan sebagai limitasi penelitian. Analisis statistik tetap dilakukan dengan data yang tersedia (unbalanced design), menggunakan Type III Sum of Squares pada ANOVA untuk mengakomodasi missing cells.

---

## Latihan 2 — Anomaly Investigation

Periksa data Anda untuk anomali. Gunakan metode IQR atau z-score.

**Contoh data response time SELECT pada kondisi C1 (PostgreSQL, no-index, 100K records):**

| Replikasi | Seed | Response Time (ms) |
|-----------|------|--------------------|
| 1 | 42 | 245.3 |
| 2 | 123 | 238.7 |
| 3 | 456 | 251.2 |
| 4 | 789 | **892.4** |
| 5 | 1024 | 241.8 |

**Deteksi outlier (metode IQR):**
- Sorted: [238.7, 241.8, 245.3, 251.2, 892.4]
- Q1 = 241.8 | Q3 = 251.2 | IQR = 9.4
- Batas bawah (Q1 - 1.5×IQR) = 241.8 - 14.1 = 227.7
- Batas atas (Q3 + 1.5×IQR) = 251.2 + 14.1 = 265.3
- Outlier terdeteksi: **Replikasi 4 (892.4 ms)** — di atas batas 265.3 ms

**Investigasi outlier:**

| Outlier | Nilai | Kemungkinan Penyebab | Investigasi | Keputusan |
|---------|-------|---------------------|-------------|-----------|
| Replikasi 4, seed=789 | 892.4 ms (3.5× mean lainnya) | Thermal throttling: CPU temp tercatat 87°C pada timestamp trial ini, clock speed turun dari 4.3 GHz ke 2.1 GHz | Cek metadata: cpu_temperature=87, cpu_usage=92%. Trial sebelumnya (replikasi 3) berjalan 15 menit tanpa jeda. Cooling pad tidak aktif saat itu. | **PERTAHANKAN** — laporkan sebagai dampak thermal throttling. Re-run dilakukan dengan jeda 10 menit → hasil normal (248.1 ms). Kedua data dilaporkan: original + re-run. |

**Anomali spesifik DBMS benchmarking yang diperiksa:**

| Pola Anomali | Deteksi | Investigasi |
|-------------|---------|-------------|
| Indexed query LEBIH LAMBAT dari non-indexed | Bandingkan mean C1 vs C2/C3 per operasi | Bisa jadi karena overhead index maintenance pada INSERT/UPDATE. Expected behavior untuk write operations. |
| Response time volume kecil > volume besar | Bandingkan mean per volume dalam kondisi yang sama | Kemungkinan cold-start effect atau cache warming dari trial sebelumnya |
| CV > 5% dalam satu sel | Hitung CV per sel (5 replikasi) | Investigasi thermal, background process, atau Docker resource contention |
| MySQL konsisten lebih cepat dari PostgreSQL | Bandingkan overall mean per DBMS | Cek apakah konfigurasi buffer pool fair (128 MB untuk keduanya). Bisa juga karena arsitektur MySQL lebih efisien pada query sederhana. |

---

## Latihan 3 — Validation Report

Buat laporan validasi ringkas untuk dataset eksperimen Anda.

**1. Completeness:** 99.25% data terkumpul (794 dari 800 trial). 6 trial missing pada volume 1M karena OOM (limitasi RAM 8 GB).

**2. Format:** [x] Konsisten — Semua 794 file JSON memiliki struktur identik (identity, configuration, metrics, metadata). Tidak ada inkonsistensi field names atau tipe data.

**3. Range check (anomali):**
- Response time: semua > 0 ms ✓
- Throughput: semua > 0 QPS ✓
- 3 outlier terdeteksi (IQR method) pada kondisi C1 dan C7 — semua terkait thermal throttling
- Setelah investigasi: 2 outlier dipertahankan + re-run, 1 outlier dipertahankan sebagai data valid

**4. Logic check:** [x] Parameter sesuai plan
- Indexed SELECT consistently ≤ non-indexed SELECT ✓ (expected behavior)
- Higher volume → higher response time ✓ (linear trend confirmed)
- INSERT/UPDATE dengan index sedikit lebih lambat dari tanpa index ✓ (index maintenance overhead)
- CV < 5% pada 96% sel (76 dari 79 sel) ✓ — 3 sel dengan CV > 5% didokumentasikan

**5. Cross-validation:**
- Replikasi dengan seed sama pada kondisi sama menghasilkan CV < 5% (pada 96% sel)
- Trend PostgreSQL vs MySQL konsisten dengan studi Hairah (2020) dan Ahsa et al. (2023)

**Kesimpulan:** [x] Data siap analisis dengan catatan
> 794 trial valid dan siap untuk analisis statistik ANOVA. 6 missing trial pada volume 1M dilaporkan sebagai limitasi hardware. 3 outlier thermal throttling didokumentasikan dan disertakan dalam analisis dengan catatan. Unbalanced ANOVA (Type III SS) digunakan untuk mengakomodasi missing cells.

---

## Refleksi

> Apa perbedaan antara "data yang benar" dan "data yang dipercaya"? Mengapa proses validasi formal diperlukan meskipun data dikumpulkan secara otomatis?

**Jawaban:**
> "Data yang benar" berarti nilai yang tercatat akurat secara teknis (tidak ada bug di logger, format benar). "Data yang dipercaya" berarti data telah melewati proses validasi formal yang membuktikan bahwa data tersebut layak untuk analisis statistik — mencakup completeness (tidak ada data hilang), consistency (format seragam), accuracy (nilai dalam range logis), dan validity (sesuai desain eksperimen).
>
> Validasi formal diperlukan meskipun data dikumpulkan secara otomatis karena: (1) script otomatis bisa memiliki bug tersembunyi (misalnya timer yang salah pada operasi tertentu), (2) kondisi hardware bisa berubah selama eksekusi panjang (thermal throttling, RAM exhaustion), (3) DBMS bisa menghasilkan anomali yang tidak terduga (deadlock, timeout, OOM), dan (4) tanpa validasi, kesimpulan statistik dari ANOVA bisa menyesatkan jika data tidak memenuhi asumsi (normalitas, homogenitas varians). Dalam konteks benchmarking DBMS pada laptop RAM 8 GB, validasi sangat kritis karena limitasi hardware bisa menghasilkan missing data dan outlier yang memengaruhi validitas kesimpulan.
