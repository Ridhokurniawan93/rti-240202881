# Outline Naskah Jurnal

## Judul dan Metadata
- Judul penelitian
- Penulis dan afiliasi
- Abstrak ID / EN
- Kata kunci

## 1. Pendahuluan
- Latar belakang JWKS Endpoint Flooding
- Motivasi dan urgensi mitigasi
- Gap literatur
- Rumusan masalah dan tujuan
- Kontribusi penelitian

## 2. Tinjauan Pustaka
- JWT / JWKS validation
- Cache positif dan negatif
- Rate limiting pada API Gateway
- Related work: mitigasi flooding dan keamanan gateway

## 3. Metodologi
- Arsitektur sistem dan desain eksperimen
- Skema Redis / PostgreSQL
- Implementasi Gateway (mode `none` / `hybrid`)
- Skenario pengujian k6 dan variabel eksperimen
- Metrik evaluasi

## 4. Hasil dan Analisis
- Statistik deskriptif latensi / throughput
- Pengurangan query Postgres
- Efektivitas mitigasi (cache hit ratio, rate-limit blocked)
- Dampak pada traffic legitimate ($D_{perf}$)
- Analisis trade-off dan bottleneck

## 5. Kesimpulan
- Ringkasan temuan utama
- Implikasi arsitektural
- Keterbatasan dan saran penelitian lanjutan

## Daftar Pustaka
- 18 referensi terverifikasi, termasuk RFC, CVE/advisory, dan paper terkait
