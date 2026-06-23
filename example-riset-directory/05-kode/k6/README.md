# Load Testing k6

Dokumentasi awal untuk skrip k6 yang digunakan dalam penelitian mitigasi JWKS Endpoint Flooding.

## Struktur Direktori yang Disarankan

```
05-kode/k6/
├── lib/
│   ├── config.js
│   ├── tokens.js
│   └── legit-tokens.json
├── legitimate.js
├── attack.js
├── mixed.js
├── run-scenario.sh
├── run-matrix.sh
└── monitor-resources.sh
```

## Skenario Pengujian

- `legitimate.js` — traffic normal dengan JWT valid.
- `attack.js` — flood request dengan `kid` acak atau pool kecil.
- `mixed.js` — kombinasi legitimate + attack secara bersamaan.

## Variabel Lingkungan

- `CACHE_MODE` — `none` atau `hybrid`.
- `LEGIT_VUS`, `LEGIT_DURATION` — untuk traffic legitimate.
- `ATTACK_MAX_VUS`, `ATTACK_RAMP_DURATION`, `ATTACK_HOLD_DURATION` — untuk traffic serangan.
- `KID_STRATEGY` — `unique` atau `pool`.

## Output Per Run

Setiap run menghasilkan:

- `k6-summary.json`
- `gateway-metrics-before.txt`
- `gateway-metrics-after.txt`
- `resources.csv`
- `meta.json`

## Cara Menjalankan

1. Pastikan gateway dan dependensi berjalan.
2. Jalankan `./run-scenario.sh <mode> <variant> <replication>`.
3. Untuk matrix penuh, jalankan `./run-matrix.sh`.

## Catatan

- Gunakan `--summary-export` untuk menghindari output JSON mentah besar.
- Ambil snapshot `/metrics` gateway sebelum dan sesudah setiap run.
- Gunakan `monitor-resources.sh` untuk mencatat CPU dan memori container.
