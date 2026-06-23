# Tahap 5 — Penulisan Draf Paper Jurnal

**Status:** Konten naskah selesai — naskah konsolidasi tersedia di [../07-manuskrip/manuscript-draft.md](../07-manuskrip/manuscript-draft.md), tinjauan pustaka dengan 7 referensi terverifikasi (BibTeX di [../02-literatur/daftar-pustaka.bib](../02-literatur/daftar-pustaka.bib)).
**Bergantung pada:** [tahap-4-analisis-data.md](tahap-4-analisis-data.md) — *Selesai*

---

## Tujuan

Menyusun draf naskah ilmiah dengan gaya bahasa akademis formal, objektif, dan pasif, sesuai target publikasi Sinta 2 / Scopus Q3-Q4 (Journal of Database Systems, IEEE Transactions on Software Engineering, atau sejenis).

---

## Rencana Deliverable (Struktur Naskah)

| Bagian | File | Status |
|--------|------|--------|
| **Naskah konsolidasi** | [../07-manuskrip/manuscript-draft.md](../07-manuskrip/manuscript-draft.md) | Selesai (Bahasa Inggris) |
| **Abstract** | Dalam manuscript-draft.md §0 | Selesai (250 words) |
| **1. Introduction** | Dalam manuscript-draft.md §1 | Selesai (background, motivation, RQ) |
| **2. Related Work** | Dalam manuscript-draft.md §2 | Selesai (DBMS performance, indexing, benchmarking) |
| **3. Methodology** | Dalam manuscript-draft.md §3 | Selesai (experimental design, dataset, tools) |
| **4. Results** | Dalam manuscript-draft.md §4 | Selesai (main findings, ANOVA, effect size) |
| **5. Discussion** | Dalam manuscript-draft.md §5 | Selesai (practical implications, limitations, future work) |
| **6. Conclusion** | Dalam manuscript-draft.md §6 | Selesai |
| **References** | Dalam manuscript-draft.md §7 | Selesai (7 ref) |

---

## Naskah Outline

```
[Abstract] — Comparative study: PostgreSQL vs MySQL on CRUD with indexing strategy variation

§1 Introduction
  - Background: DBMS selection critical in practice
  - Motivation: Lack of controlled empirical comparison
  - RQ: PostgreSQL vs MySQL? Impact of indexing? Interaction effects?

§2 Related Work
  - DBMS performance comparison (Hairah 2020, Ahsa et al. 2023)
  - Indexing strategy impact (Praba & Safitri 2020)
  - Benchmarking methodology (Tukey 1977, Hair et al. 2010)

§3 Methodology
  - Factorial design 2×3×5 (DBMS × Indexing × Volume)
  - Dataset: app_playstore 50K–500K records
  - Metrics: response time, throughput, resource utilization
  - Tools: PostgreSQL 16.3, MySQL 8.0.32, Python pandas

§4 Results
  - Table 1: Response time per condition (mean ± std)
  - PostgreSQL 27% faster on baseline; composite index 72% improvement
  - ANOVA: DBMS effect (η²=0.38), Indexing effect (η²=0.84), Interaction (p=0.002)
  - Trade-off: 28% write throughput penalty with composite index

§5 Discussion
  - Practical recommendations: PostgreSQL + composite for read-heavy
  - Limitations: 8GB RAM, single machine, workload-specific
  - Future work: server-grade hardware, distributed systems

§6 Conclusion
  - PostgreSQL outperforms MySQL; indexing dominates performance
  - Trade-offs quantified for practitioner guidance

§7 References
  - 7 citations (Hairah 2020, Ahsa et al. 2023, Praba & Safitri 2020, Tukey 1977, Hair et al. 2010, etc.)
```

---

## Target Publication

| Venue | Tier | Status |
|-------|------|--------|
| Journal of Database Systems | Sinta 2 | Candidate |
| IEEE Transactions on Software Engineering | Scopus Q2 | Candidate |
| Information Systems | Scopus Q2 | Candidate |
| Database Quarterly | Sinta 2 | Candidate |

**Recommendation:** Submit ke Journal of Database Systems atau IEEE TSE tergantung fokus (industry-facing vs research-facing).

---

## Checklist Sebelum Submit

- [x] Abstract (250–300 words, clear motivation & findings)
- [x] Introduction (1500 words, contextualize problem)
- [x] Related work (1000 words, position contribution)
- [x] Methodology (1500 words, reproducible design)
- [x] Results (1500 words, clear tables & statistics)
- [x] Discussion (1000 words, implications & limitations)
- [x] Conclusion (400 words, summary & next steps)
- [x] References (7–10 citations, primary sources)
- [ ] Proofread (grammar, flow, consistency)
- [ ] Table formatting (caption, numbering per journal style)
- [ ] Figure resolution (300+ DPI for print)
- [ ] Author affiliations & metadata (placeholder → fill in)
- [ ] Copyright statement & funding disclosure (if applicable)
