# WS-06: System-Experiment Mapping

> **Bab 6 — System Design sebagai Experimental Artifact**

---

## Ringkasan Materi

### Sistem = Instrumen Pengujian, Bukan Produk

Seorang engineer bertanya "apakah sistem bekerja?" — seorang peneliti bertanya "apa yang bisa dibuktikan sistem ini?" Sistem dalam riset adalah **artifact** — objek yang sengaja dibuat untuk menguji klaim spesifik.

### System as Experiment Model

```
RQ → Variable → System Component → Experimental Setup → Output
```

Setiap komponen sistem harus bisa ditelusuri ke variabel riset (top-down), dan setiap pengukuran harus menjawab RQ (bottom-up).

### Mapping Variabel ke Komponen

| Tipe Variabel | Peran di Sistem | Contoh |
|---------------|----------------|--------|
| **IV** (Independent) | Modul yang bisa di-toggle/swap | Algoritma A vs B |
| **DV** (Dependent) | Modul pengukuran | Logger, metrics collector |
| **CV** (Control) | Config yang dikunci | Dataset, parameter tetap |

Jika variabel tidak bisa di-map ke komponen apapun → arsitektur perlu didesain ulang.

### 4 Prinsip Desain Eksperimental

| Prinsip | Pertanyaan Kunci |
|---------|-----------------|
| **Traceability** | Komponen ini melayani variabel yang mana? |
| **Modularity** | Bisakah IV diubah tanpa memengaruhi yang lain? |
| **Controllability** | Apakah CV dieksternalisasi ke config file? |
| **Measurability** | Apakah sistem otomatis menghasilkan data yang dibutuhkan? |

### Variable Isolation melalui Arsitektur

- **Modular architecture** — Pisahkan berdasarkan variabel
- **Configuration-driven** — Ubah config (YAML/JSON), bukan code
- **Feature toggles** — On/off flag untuk ablation study

### Research vs Engineering

| Aspek | Engineering | Research |
|-------|------------|----------|
| Tujuan sistem | Memenuhi kebutuhan user | Menguji hipotesis, menghasilkan bukti |
| Arsitektur | Optimasi performa & skalabilitas | Optimasi isolasi variabel & reprodusibilitas |
| Konfigurasi | Sering hardcoded | Dieksternalisasi ke config file |
| Fitur tambahan | Menambah nilai user | Menambah noise jika tidak terkait RQ |

### Istilah Penting

- **Artifact** — Objek yang sengaja dibuat untuk memecahkan masalah atau menguji proposisi
- **Traceability** — Kemampuan menelusuri hubungan RQ → variabel → komponen → output
- **Variable Isolation** — Mengubah hanya satu variabel sambil menahan yang lain konstan
- **Ablation Study** — Menguji kontribusi tiap komponen dengan melepasnya satu per satu
- **Configuration-driven Execution** — Semua parameter di config file, bukan hardcoded

---

## Template A.6 — Mapping RQ ke Arsitektur Sistem

```
SYSTEM-EXPERIMENT MAPPING

Research Question: Apakah pengembangan sistem informasi penggajian di Politeknik Ganesha Guru menggunakan XP menghasilkan efisiensi waktu pemrosesan dan akurasi perhitungan yang lebih baik dibandingkan pengembangan tradisional/manual?

Variable → Component Mapping:
| Variabel | Tipe | Komponen Sistem | Cara Manipulasi/Pengukuran |
|----------|------|-----------------|---------------------------|
| Metode pengembangan | IV | Process Framework Module | Config: development_method=XP atau traditional |
| Waktu pemrosesan payroll | DV | Performance Logger Module | Otomatis capture start_time - end_time |
| Akurasi perhitungan gaji | DV | Validation & Verification Module | Compare hasil vs referensi, hitung error rate |
| Kepuasan pengguna | DV | Survey/Feedback Collector Module | Post-test Likert 1-5 survey |
| Kompleksitas data payroll | CV | Data Configuration Module | Config: employee_count=50, salary_components=8 (tetap konstan) |

4 Prinsip Desain:
  [x] Traceability — Setiap komponen bisa ditelusuri ke variabel
  [x] Variable Isolation — IV bisa diubah tanpa mengubah CV
  [x] Measurement Integration — Pengukuran DV built-in
  [x] Reproducibility — Setup bisa direkonstruksi dari config file

Experimental Setup:
  Input data     : Data pegawai, gaji, tunjangan, potongan dari Politeknik Ganesha Guru
  Parameter      : development_method (XP/traditional), employee_count (50), iteration_period (1 bulan)
  Output format  : JSON log: {timestamp, method, processing_time, error_count, validation_status, user_satisfaction_score}
```

---

## Latihan 1 — Variable-to-Component Mapping

Gunakan RQ dan variabel dari WS-05. Petakan ke komponen sistem.

**RQ:** Apakah pengembangan sistem informasi penggajian di Politeknik Ganesha Guru menggunakan XP menghasilkan efisiensi waktu pemrosesan dan akurasi perhitungan yang lebih baik dibandingkan pengembangan tradisional/manual?

| Variabel | Tipe | Komponen Sistem | Cara Manipulasi / Pengukuran |
|----------|------|-----------------|----------------------------|
| Metode pengembangan | IV | Process Framework Module | Config file: development_method=XP atau development_method=traditional |
| Waktu pemrosesan payroll | DV | Performance Logger Module | Otomatis capture start_time dan end_time, hitung elapsed time per payroll cycle |
| Akurasi perhitungan gaji | DV | Validation & Comparison Module | Bandingkan output sistem dengan perhitungan referensi, hitung persentase error |
| Kepuasan pengguna | DV | Survey Collector Module | Form Likert 1-5 untuk admin dan stakeholder setelah penggunaan sistem |
| Kompleksitas data payroll | CV | Data Configuration Module | Config: employee_count=50, salary_components=8, deduction_types=5 (tetap konstan) |

**Apakah semua variabel bisa di-map?** [x] Ya / [ ] Tidak
> Jika tidak, komponen apa yang perlu ditambahkan? —

---

## Latihan 2 — 4 Prinsip Desain

Evaluasi desain sistem terhadap 4 prinsip.

| Prinsip | Status | Bukti / Penjelasan |
|---------|--------|-------------------|
| Traceability | ✅ | Setiap modul (Process Framework, Performance Logger, Validation, Survey Collector) dapat ditelusuri ke satu atau lebih variabel RQ. |
| Modularity | ✅ | Process Framework Module dapat di-toggle antara XP dan tradisional tanpa mengubah modul pengukuran (Performance Logger, Validation, Survey Collector). |
| Controllability | ✅ | Kompleksitas data (CV) dikontrol melalui config file yang tetap selama eksperimen, mencegah noise eksternal. |
| Measurability | ✅ | Sistem otomatis menghasilkan output dalam format terstruktur (JSON log) untuk DV: waktu pemrosesan, akurasi, kepuasan pengguna. |

**Prinsip mana yang paling sulit dipenuhi?** Controllability
**Strategi untuk mengatasinya:**
> Menggunakan konfigurasi file yang explicit (YAML/JSON) untuk semua parameter data (jumlah pegawai, komponen gaji, potongan pajak). Sebelum eksperimen dimulai, lock config file agar tidak berubah. Dokumentasikan versi config yang digunakan untuk setiap trial eksperimen agar reproducible.

---

## Latihan 3 — Ablation Study Planning

Jika sistem memiliki komponen utama untuk XP dan untuk tradisional, rencanakan ablation study.

| Kondisi | Metode | Performance Logger | Validation Module | Survey Collector | Hasil yang Diharapkan |
|---------|--------|------|------|---------|---------------------|
| Full (XP) | ✅ XP | ✅ On | ✅ On | ✅ On | Baseline XP: waktu pemrosesan min, akurasi max, kepuasan user tinggi |
| Full (Tradisional) | ✅ Traditional | ✅ On | ✅ On | ✅ On | Baseline tradisional: waktu pemrosesan lebih lama, akurasi lebih rendah |
| – Performance Logger | ✅ XP | ❌ Off | ✅ On | ✅ On | Tidak bisa mengukur waktu pemrosesan (data waktu hilang) |
| – Validation Module | ✅ XP | ✅ On | ❌ Off | ✅ On | Tidak bisa mengukur akurasi perhitungan (error rate unknown) |
| – Survey Collector | ✅ XP | ✅ On | ✅ On | ❌ Off | Tidak bisa mengukur kepuasan pengguna (feedback missing) |

**Komponen mana yang diprediksi paling berkontribusi?** Performance Logger (modul pengukuran waktu pemrosesan)
**Mengapa?**
> Waktu pemrosesan adalah salah satu DV utama dalam hipotesis dan metrik terkunci untuk membuktikan efisiensi XP. Tanpa Performance Logger, tidak bisa mengumpulkan data utama untuk menerima atau menolak H₁. Selain itu, waktu pemrosesan adalah indikator langsung dari metodologi pengembangan (XP dengan iterasi pendek vs tradisional dengan fase panjang).

---

## Refleksi

> Apa risiko jika sistem dibangun seperti produk (monolitik, fitur lengkap) lalu baru dilakukan eksperimen? Mengapa arsitektur modular penting untuk riset?

**Jawaban:**
> Risiko monolitik: sulit mengisolasi variabel karena semua komponen terikat erat. Jika ingin membandingkan XP vs tradisional, tidak bisa swap metode tanpa rebuild seluruh sistem. Hasilnya tidak bisa direproduksi, dan sulit tahu kontribusi setiap komponen. Arsitektur modular penting karena memungkinkan toggle variabel independen (feature flags, config-driven execution) sehingga hanya variabel eksperimen yang berubah, CV terkontrol, dan DV dapat diukur dengan bersih. Dengan modular design, eksperimen menjadi reproducible dan causal inferences lebih kuat karena isolasi variabel terjaga.
