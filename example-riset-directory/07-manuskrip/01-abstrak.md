# Abstrak

Penelitian ini mengevaluasi mitigasi **JWKS Endpoint Flooding** pada API Gateway mikroservis dengan skema **Redis-PostgreSQL Hybrid Caching**. Solusi yang diuji menggabungkan cache positif untuk JWK valid, cache negatif untuk `kid` yang tidak dikenal, dan rate limiting permanen di PostgreSQL untuk membatasi beban query backend.

Eksperimen dilakukan dengan dua mode operasi (`CACHE_MODE=none` vs `CACHE_MODE=hybrid`) dan lima varian traffic menggunakan k6. Hasil analisis menunjukkan bahwa mitigasi hybrid menurunkan beban query PostgreSQL hingga 93-99,997%, melindungi latensi traffic legitimate sampai 92,9% pada skenario mixed, dan tidak menimbulkan overhead signifikan pada kondisi normal.

Kata kunci: JWKS, JWT, API Gateway, Redis, PostgreSQL, cache negatif, rate limiting, k6.
