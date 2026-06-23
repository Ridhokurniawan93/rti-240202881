# 04-data

Data mentah hasil pengujian — output dari **Tahap 3**, input untuk **Tahap 4**.

## Isi yang diharapkan

- Hasil pengujian k6 dalam format CSV/JSON, per kombinasi mode (`CACHE_MODE=none|hybrid`) × jenis traffic (legitimate/attack/mixed)
- Metrik resource container (CPU, memori) PostgreSQL & Redis selama pengujian
- Metadata eksekusi tiap run (timestamp, konfigurasi, durasi)

## Catatan

Folder ini berisi _template_ struktur data mentah hasil pengujian, tetapi data aktual tidak disertakan dalam repository. Untuk mengisi folder ini, jalankan eksperimen k6 sesuai petunjuk di `example-riset-directory/09-docs/tahap-3-pengujian-k6.md` dan simpan output run ke subfolder seperti:

- `04-data/<cache_mode>__<traffic_variant>__rep<N>__<timestamp>/`

Data di folder ini bersifat mentah (raw) dan belum diolah. Hasil olahan (statistik, grafik) disimpan di [../06-output/](../06-output/).
