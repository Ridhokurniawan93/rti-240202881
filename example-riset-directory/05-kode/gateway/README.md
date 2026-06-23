# Gateway Implementation

Dokumentasi awal untuk implementasi API Gateway (Go + Echo) pada penelitian mitigasi JWKS Endpoint Flooding.

## Struktur Direktori yang Disarankan

```
05-kode/gateway/
├── cmd/gateway/            # Entry point aplikasi
├── internal/
│   ├── jwks/              # Resolusi JWK / cache logic
│   ├── ratelimit/         # PostgreSQL rate-limit counter
│   ├── jwtauth/           # JWT verification middleware
│   ├── httpapi/           # HTTP routes & handlers
│   ├── platform/          # Config, logging, environment
│   └── metrics/           # Prometheus metrics collector
├── migrations/            # SQL migration untuk PostgreSQL
├── scripts/               # Seed keypair dan sample JWT
├── docker-compose.yml     # Compose untuk gateway, postgres, redis
└── .env.example           # Template environment variables
```

## Deskripsi

- `cmd/gateway/` berisi entry point yang membaca konfigurasi dan menjalankan server.
- `internal/jwks/` mengelola cache Redis positive/negative dan fallback ke PostgreSQL.
- `internal/ratelimit/` menangani `INSERT ... ON CONFLICT` untuk counter rate limit per `client_ip`.
- `internal/jwtauth/` melakukan parsing JWT, validasi signature RS256, dan error handling.
- `internal/httpapi/` menyediakan endpoint API resource serta health check.
- `internal/metrics/` mengekspor metrik Prometheus seperti cache hit/miss, query count, dan auth outcome.

## Mode Operasi

- `CACHE_MODE=none` — baseline, tidak menggunakan Redis cache dan tidak melakukan rate limiting.
- `CACHE_MODE=hybrid` — menggunakan Redis positive/negative cache dan PostgreSQL rate-limit counter.

## Verifikasi

Langkah verifikasi utama:

1. Jalankan `docker compose up -d`.
2. Pastikan service `gateway`, `postgres`, `redis` sehat.
3. Uji endpoint `/healthz`.
4. Uji JWT valid / invalid dan amati metrik Prometheus.

## Catatan

- Pastikan PostgreSQL diakses via port host yang tidak bentrok (mis. 5433).
- Gunakan `docker compose` di folder ini untuk menyalakan seluruh stack.
