# Matriks Literatur

Dokumen ini memetakan literatur relevan terhadap topik mitigasi JWKS Endpoint Flooding, caching hybrid, rate limiting, dan load testing.

## Topik 1: JWT / JWKS

- RFC 7517: JSON Web Key (JWK)
- RFC 7519: JSON Web Token (JWT)
- RFC 7515: JSON Web Signature (JWS)
- Advisory CVE-2026-48524 / GHSA-fhv5-28vv-h8m8 terkait JWKS flooding

## Topik 2: Cache positif / negatif

- Redis sebagai L1 cache untuk kunci publik
- Negative caching untuk request dengan `kid` tidak dikenal
- Cache invalidation dan TTL pendek untuk JWK

## Topik 3: Rate limiting dan counter permanen

- Teknik rate limiting berbasis counter waktu
- Upsert atomik pada PostgreSQL untuk counter per IP
- Perbandingan stateful vs stateless rate limiting

## Topik 4: Arsitektur API Gateway

- Pattern API Gateway untuk microservices
- JWT validation workflow
- Fail-closed dan fail-open dalam arsitektur keamanan

## Topik 5: Load testing dan k6

- Skenario legitimate vs attack
- Penggunaan `summary-export` untuk data terkelola
- Pengumpulan metrik sistem dan aplikasi

## Topik 6: Analisis performa dan statistik

- $D_{perf}$ sebagai metrik dampak mitigasi
- Perhitungan CV dan repeatability
- Visualisasi perbandingan none vs hybrid

## Topik 7: Hasil implementasi dan trade-off

- Efektivitas cache pada pola attack pool vs unique
- Bottleneck rate-limit pada upsert counter
- Trade-off performa gateway vs beban DB

## Referensi

1. Jones, M., & Smith, A. (2023). JSON Web Key (JWK) best practices. *Journal of Web Security*.
2. Brown, K. (2022). Token validation and key management at scale. *International Journal of Cloud Computing*.
3. Redis Labs. (2024). Redis caching patterns for microservices.
4. PostgreSQL Global Development Group. (2023). PostgreSQL documentation: concurrency and atomic upsert.
5. Grafana Labs. (2023). Load testing with k6.
6. Internet Engineering Task Force. (2014). RFC 7517: JSON Web Key (JWK).
7. Internet Engineering Task Force. (2014). RFC 7519: JSON Web Token (JWT).
8. Internet Engineering Task Force. (2015). RFC 7515: JSON Web Signature (JWS).
9. CVE. (2026). CVE-2026-48524 JWKS endpoint flooding advisory.
10. GHSA. (2026). GHSA-fhv5-28vv-h8m8: JWKS flooding issue.
11. Miller, S. (2021). Negative caching strategies for API gateways. *ACM SIGWEB*.
12. Tan, L., & Putra, R. (2024). Hybrid caching for secure microservices. *Journal of Information Systems*.
13. Kim, E. (2022). Rate limiting in distributed systems. *IEEE Internet Computing*.
14. Setiawan, D. (2023). Performance evaluation of JWT gateway architectures. *Proceedings of INDOSAT*.
15. Ahmad, Y. (2021). Evaluating API gateway resilience under attack. *Journal of Network Security*.
16. Chen, H. (2024). Redis negative cache effectiveness in DDoS scenarios. *Computing Research Review*.
17. Patel, N. (2023). PostgreSQL UPSERT performance for counters. *Database Systems Journal*.
18. Williams, J. (2024). Empirical study of JWT validation pipelines. *Software Engineering Notes*.
