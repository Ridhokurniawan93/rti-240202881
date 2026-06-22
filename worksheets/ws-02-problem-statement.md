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
| **Topik** | Performa database PostgreSQL dan MySQL | Terlalu luas, tidak bisa diuji |
| **Problem** | PostgreSQL dan MySQL menunjukkan perbedaan performa yang tidak konsisten pada workload CRUD | Spesifik tapi belum riset |
| **Research Problem** | Apakah query optimization dan indexing strategy berdampak signifikan terhadap performa PostgreSQL dan MySQL dalam workload CRUD? | Bisa dirancang eksperimennya |

### Symptom vs Root Cause

Apa yang diamati (gejala) ≠ mengapa terjadi (akar masalah). Gunakan **5 Whys** atau **Fishbone Diagram** untuk menggali.

Contoh: "PostgreSQL lebih cepat dari MySQL pada beberapa query tapi lebih lambat di query lain" (symptom) → "Perbedaan arsitektur query optimizer, strategi indexing default, dan konfigurasi buffer pool menyebabkan variasi performa yang tidak konsisten antar DBMS" (root cause).

### System Thinking

Setiap masalah riset TI harus terikat pada komponen sistem: **Input → Process → Output → Outcome → Constraints → Stakeholders**.

Konteks: Input (query CRUD, dataset dengan berbagai volume), Process (eksekusi query oleh DBMS dengan/without indexing dan optimization), Output (response time, throughput), Outcome (pemahaman dampak optimasi terhadap performa), Constraints (spesifikasi hardware, versi DBMS, konfigurasi sistem), Stakeholders (developer, DBA, arsitek sistem, peneliti).

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
| Masalah | Query lambat, database error | Gap dalam pengetahuan tentang dampak optimasi |
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
  Domain   : Database Management System (DBMS) — Performa PostgreSQL dan MySQL
  Konteks  : Workload CRUD (Create, Read, Update, Delete) pada database relasional

System Context
  Input       : Query CRUD (SELECT, INSERT, UPDATE, DELETE), dataset dengan volume bervariasi (50.000, 100.000, 250.000, 500.000, 1.000.000 record)
  Process     : Eksekusi query oleh PostgreSQL dan MySQL dengan variasi indexing strategy (no index, single-column index, composite index) dan query optimization (default vs optimized query)
  Output      : Response time (ms), throughput (queries per second), resource utilization (CPU, memory)
  Outcome     : Pemahaman komprehensif tentang dampak query optimization dan indexing strategy terhadap performa kedua DBMS
  Constraints : Spesifikasi hardware tetap, versi DBMS tertentu, skema database terstandarisasi, konfigurasi buffer pool dan cache dikontrol
  Stakeholders: Developer aplikasi, Database Administrator (DBA), Arsitek sistem informasi, Peneliti bidang database

Fenomena → Problem
  Fenomena yang diamati             : PostgreSQL dan MySQL menunjukkan performa yang tidak konsisten pada berbagai jenis query CRUD
  Gejala (symptom) yang terukur     : Response time bervariasi antar DBMS; pada beberapa studi PostgreSQL lebih cepat (Hairah, 2020; Ahsa et al., 2023), namun pada studi lain MySQL menunjukkan keunggulan (Wendri et al., 2022)
  Masalah yang didiagnosis          : Studi sebelumnya tidak mengontrol strategi indexing dan query optimization sebagai variabel, sehingga perbedaan performa tidak bisa diatribusikan secara jelas ke kemampuan inherent DBMS
  Masalah riset (researchable)      : Apakah query optimization dan indexing strategy berdampak signifikan terhadap performa PostgreSQL dan MySQL dalam workload CRUD, dan bagaimana interaksi antara kedua faktor tersebut?
  Variabel yang terukur             : Response time (ms), throughput (QPS), dampak indexing (no index vs indexed), dampak query optimization (default vs optimized), interaksi DBMS × indexing × optimization

Problem Quality Check
  [x] Clarity — Perbedaan performa DBMS dijelaskan melalui dampak indexing dan optimization yang terukur
  [x] Measurability — Response time (ms), throughput (QPS), CPU/memory usage
  [x] Relevance — Pemilihan dan optimasi DBMS adalah keputusan kritis dalam pengembangan sistem informasi
  [x] Testability — Dapat diuji dengan eksperimen terkontrol; bisa gagal jika indexing/optimization tidak berdampak signifikan
  [x] Impact — Hasil memberikan panduan berbasis bukti untuk DBA dan developer dalam memilih dan mengoptimasi DBMS

Problem Statement (1 paragraf):
  PostgreSQL dan MySQL merupakan dua DBMS open-source paling populer yang sering dibandingkan performanya. Namun, studi-studi sebelumnya (Hairah, 2020; Ahsa et al., 2023; Winata & Putra, 2021; Wendri et al., 2022; Praba & Safitri, 2020) menunjukkan hasil yang tidak konsisten — pada beberapa skenario PostgreSQL unggul, sementara di skenario lain MySQL lebih baik. Inkonsistensi ini diduga disebabkan oleh ketiadaan kontrol terhadap strategi indexing dan query optimization sebagai variabel eksperimen. Penelitian ini menganalisis dampak query optimization dan indexing strategy terhadap performa PostgreSQL dan MySQL dalam workload CRUD (SELECT, INSERT, UPDATE, DELETE) dengan eksperimen terkontrol pada berbagai volume data, menggunakan analisis statistik untuk mengukur signifikansi perbedaan performa.
```

---

## Latihan 1 — Dari Topik ke Masalah Riset

Pilih satu topik di bidang TI yang diminati. Transformasikan melalui 5 tahap Problem Formation Model.

**Topik awal:** Analisis Dampak Query Optimization dan Indexing Strategy terhadap Performa PostgreSQL dan MySQL dalam Workload CRUD

| Tahap | Hasil |
|-------|-------|
| Reality | PostgreSQL dan MySQL digunakan secara luas sebagai DBMS open-source utama dalam pengembangan aplikasi, dan performa database merupakan faktor kritis dalam pemilihan DBMS |
| Observed Issue (Symptom) | Studi perbandingan performa menunjukkan hasil tidak konsisten: PostgreSQL lebih cepat pada response time query (Hairah, 2020; Ahsa et al., 2023; Winata & Putra, 2021), tetapi MySQL menunjukkan keunggulan pada throughput dan execution time (Wendri et al., 2022) |
| Diagnosed Problem (Root Cause) | Studi sebelumnya tidak mengontrol strategi indexing dan query optimization sebagai variabel independen, sehingga perbedaan performa yang dilaporkan mungkin disebabkan oleh konfigurasi, bukan kemampuan inherent DBMS |
| Researchable Problem | Apakah query optimization dan indexing strategy berdampak signifikan terhadap performa PostgreSQL dan MySQL dalam workload CRUD, dan bagaimana interaksi antara DBMS, indexing, dan optimization? |
| Measurable Variable | Response time (ms), throughput (QPS), CPU usage (%), memory usage (MB), dengan variasi: DBMS (PostgreSQL/MySQL), indexing (none/single/composite), optimization (default/optimized) |

**Apakah terjebak solution-first thinking?** [ ] Ya / [x] Tidak
> Jika tidak, prinsip yang diterapkan adalah: mulai dari fenomena inkonsistensi hasil studi sebelumnya → diagnosa akar penyebab (ketiadaan kontrol variabel indexing dan optimization) → definisikan variabel terukur sebelum merancang eksperimen.

---

## Latihan 2 — System Context Decomposition

Gambarkan konteks sistem dari masalah riset di Latihan 1.

| Komponen | Deskripsi |
|----------|----------|
| Input | Query CRUD (SELECT, INSERT, UPDATE, DELETE), dataset terstandarisasi dengan volume 50.000, 100.000, 250.000, 500.000, dan 1.000.000 record |
| Process | Eksekusi query pada PostgreSQL dan MySQL dengan variasi indexing strategy (no index, single-column index, composite index) dan query optimization (default vs rewritten/optimized query) |
| Output | Response time per query (ms), throughput (queries per second), resource utilization (CPU %, memory MB) |
| Outcome | Pemahaman berbasis bukti tentang dampak indexing dan optimization terhadap performa masing-masing DBMS, panduan pemilihan dan tuning DBMS |
| Constraints | Hardware identik untuk semua pengujian, versi DBMS terkontrol, konfigurasi buffer pool dan cache disetarakan, skema database terstandarisasi |
| Stakeholders | Developer aplikasi (pemilihan DBMS), DBA (tuning database), Arsitek sistem (desain infrastruktur), Peneliti (kontribusi literatur) |

**Komponen mana yang paling relevan dengan masalah riset?** Process dan Constraints

> Proses eksekusi query dengan variasi indexing dan optimization adalah inti eksperimen; constraints (hardware identik, konfigurasi terkontrol) memastikan perbandingan yang adil (fair comparison) antara kedua DBMS.

---

## Latihan 3 — Problem Quality Check

Evaluasi problem statement yang sudah dibuat menggunakan 5 kriteria.

| Kriteria | Skor (1-5) | Justifikasi |
|----------|-----------|-------------|
| Clarity | 5 | Masalah jelas: inkonsistensi hasil studi sebelumnya → perlu kontrol variabel indexing dan optimization |
| Measurability | 5 | Variabel terukur: response time (ms), throughput (QPS), CPU/memory usage — semua metrik ratio |
| Relevance | 5 | Performa DBMS adalah keputusan kritis dalam pengembangan sistem; PostgreSQL dan MySQL adalah dua DBMS open-source terpopuler |
| Testability | 5 | Dapat diuji dengan eksperimen benchmarking terkontrol; bisa gagal jika indexing/optimization tidak berdampak signifikan |
| Impact | 4 | Hasil memberikan panduan berbasis bukti untuk DBA dan developer; kontribusi pada literatur perbandingan DBMS |

**Skor total:** 24 / 25

**Problem statement versi final (1 paragraf):**
> PostgreSQL dan MySQL merupakan dua DBMS open-source yang paling banyak digunakan dalam pengembangan aplikasi. Berbagai studi perbandingan performa telah dilakukan (Hairah, 2020; Ahsa et al., 2023; Winata & Putra, 2021; Wendri et al., 2022; Praba & Safitri, 2020), namun menghasilkan kesimpulan yang tidak konsisten — beberapa menunjukkan PostgreSQL lebih unggul, sementara yang lain menunjukkan keunggulan MySQL. Inkonsistensi ini diduga disebabkan oleh ketiadaan kontrol terhadap strategi indexing dan query optimization sebagai variabel eksperimen. Penelitian ini menganalisis dampak query optimization dan indexing strategy terhadap performa PostgreSQL dan MySQL dalam workload CRUD secara eksperimental, dengan mengukur response time, throughput, dan resource utilization pada berbagai volume data dan strategi indexing. Hasil penelitian diharapkan memberikan kontribusi berupa pemahaman berbasis bukti tentang faktor-faktor yang memengaruhi performa DBMS dan panduan praktis bagi developer serta DBA dalam optimasi database.

---

## Refleksi

> Bandingkan "masalah" yang biasa ditemui saat coding (bug, error) dengan masalah riset. Apa perbedaan fundamental dalam cara mendefinisikan dan mendekati keduanya?

**Jawaban:**
> **Masalah Engineering (coding):** "Query SELECT lambat pada tabel dengan 1 juta record" — masalah langsung, ada metrik spesifik (response time tinggi), solusi jelas (tambah index, rewrite query), ukuran sukses: query menjadi cepat.
> 
> **Masalah Research:** "Apakah indexing strategy dan query optimization berdampak signifikan terhadap performa PostgreSQL dan MySQL?" — masalah abstrak, perlu definisi "dampak signifikan", perlu desain eksperimen terkontrol, solusi tidak langsung (butuh pengujian sistematis, analisis statistik, validasi), ukuran sukses: hipotesis terjawab dengan bukti meyakinkan.
> 
> Perbedaan fundamental: Engineering mencari "how" (langsung diperbaiki dengan solusi teknis), Research mencari "why" dan "is X true?" (harus dibuktikan dengan bukti empiris dan dapat direplikasi).