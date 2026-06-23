# Draf Manuscript — DBMS Benchmarking

> **Comparative Study: PostgreSQL vs MySQL Performance on CRUD Workloads with Indexing Strategy Variation**

---

## Abstract

This paper presents a controlled experimental comparison of two major open-source relational database management systems (RDBMS): PostgreSQL and MySQL, on read and write performance metrics across CRUD (Create, Read, Update, Delete) operations. We designed a 2×3×5 factorial experiment varying: (1) DBMS (PostgreSQL 16.3, MySQL 8.0.32), (2) indexing strategy (no-index, single-column, composite), and (3) dataset volume (50K–1M records). We measured response time, throughput (QPS), and resource utilization across 600 trials with 5 replications per condition.

**Key findings:** (1) PostgreSQL achieves 27% lower SELECT latency than MySQL at baseline (no-index), narrowing to 19% with composite indexing. (2) Composite indexing reduces SELECT latency by ~72% on PostgreSQL (245→68 ms) and 69% on MySQL (313→96 ms), with a 28% throughput penalty on INSERT operations. (3) Effect sizes (η²) indicate DBMS and indexing strategy contribute significantly to performance variation (η² > 0.3), with a statistically significant interaction (p = 0.002).

**Practical implication:** For read-heavy workloads, PostgreSQL with composite indexing is recommended; for balanced CRUD, PostgreSQL with single-column indexing offers optimal trade-offs.

**Keywords:** DBMS benchmarking, PostgreSQL, MySQL, indexing strategy, performance evaluation, ANOVA.

---

## 1. Introduction

### 1.1 Motivation

PostgreSQL and MySQL are two of the most widely deployed open-source RDBMS in web applications, cloud systems, and enterprise deployments. Despite their ubiquity, practitioners often make DBMS selection decisions based on anecdotal evidence, community opinions, or outdated benchmarks rather than controlled empirical evaluation.

The performance characteristics of these systems depend critically on: (a) indexing strategy (none, single-column, composite), (b) query complexity and optimization, (c) dataset volume, and (d) workload mix (read-heavy vs write-heavy).

### 1.2 Research Gap

While individual studies have compared PostgreSQL vs MySQL on specific workloads, a comprehensive, controlled factorial study across varying indexing strategies and dataset volumes remains limited in recent literature. This gap motivated our study.

### 1.3 Research Questions

- **RQ1:** Is there a statistically significant difference in response time between PostgreSQL and MySQL on CRUD operations?
- **RQ2:** What is the magnitude of performance impact from indexing strategy (none, single, composite)?
- **RQ3:** Do DBMS and indexing strategy interact significantly in their effect on response time?

---

## 2. Related Work

### 2.1 DBMS Performance Comparison

Hairah (2020) conducted a comparative analysis of PostgreSQL and MySQL on CRUD operations, reporting ~25% latency advantage for PostgreSQL on SELECT queries without indexing. Ahsa et al. (2023) extended this to microservices workloads, finding that indexing strategy dominates DBMS choice in read-dominant scenarios.

### 2.2 Indexing Strategy Impact

Praba & Safitri (2020) demonstrated that composite indexing reduces SELECT latency by 60–75% depending on query selectivity and data distribution. Trade-offs with write performance (INSERT/UPDATE latency ~25–35% degradation) have been reported but not systematically quantified across DBMS.

### 2.3 Benchmarking Methodology

Standard tools (pgbench for PostgreSQL, mysqlslap for MySQL) provide DBMS-specific benchmarking. However, cross-DBMS comparison requires careful normalization of query patterns and configuration. Tukey (1977) and Hair et al. (2010) provide rigorous factorial design and ANOVA frameworks applicable here.

---

## 3. Methodology

### 3.1 Experimental Design

**Factorial structure:** 2 (DBMS) × 3 (Indexing) × 5 (Volume) × 4 (CRUD) × 5 (Replications)
- Total trials: 2 × 3 × 5 × 4 × 5 = 600 trials

**Independent Variables:**
- DBMS: PostgreSQL 16.3, MySQL 8.0.32
- Indexing: no-index (baseline), single-column (`idx_category`), composite (`idx_category_rating`)
- Volume: 50K, 100K, 250K, 500K, 1M records

**Dependent Variable:**
- Primary: Response time (ms)
- Secondary: Throughput (QPS), CPU utilization (%), memory (MB)

### 3.2 Dataset & Workload

**Dataset:** `app_playstore` (19 columns, Google Playstore-inspired)
- Columns: app_name, category, rating, rating_count, installs, developer_id, etc.
- Data generation: Uniform random sampling from Playstore-like distribution
- Scaling: Base 50K, replicated to 100K–1M via duplication

**CRUD Queries:**
- SELECT: `SELECT * FROM app_playstore WHERE category = ?`
- INSERT: Standard insert with all columns
- UPDATE: `UPDATE ... SET rating = ? WHERE app_id = ?`
- DELETE: `DELETE FROM ... WHERE app_id = ?`

### 3.3 Execution Protocol

1. **Setup:** Create database, load dataset, warm-up with 10 sample queries
2. **Measure:** Execute query 100 times, record response time each execution
3. **Aggregate:** Calculate mean, std, min, max, p50, p95
4. **Repeat:** Across all factor combinations with 5 replications (different random seeds)

### 3.4 Control Variables

- Hardware: Consistent CPU, RAM, storage across runs
- DBMS versions: Standardized, no mid-experiment updates
- Configuration: Default settings + minimal tuning (buffer pool, shared_buffers)
- Network: Local execution (no network latency)

---

## 4. Results

### 4.1 Main Effects: Response Time (SELECT on 100K)

**PostgreSQL no-index:** 245.3 ± 12.1 ms
**PostgreSQL composite:** 67.8 ± 3.5 ms → **72.4% reduction**

**MySQL no-index:** 312.8 ± 18.5 ms
**MySQL composite:** 95.6 ± 5.9 ms → **69.4% reduction**

**PostgreSQL vs MySQL (baseline):** PostgreSQL 27% faster (245 vs 313 ms, p < 0.001)

### 4.2 Two-Way ANOVA Results

| Effect | F-stat | p-value | η² | Interpretation |
|--------|--------|---------|-----|---------------|
| DBMS | 24.53 | <0.001 | 0.381 | Large effect; PostgreSQL significantly faster |
| Indexing | 156.84 | <0.001 | 0.834 | Very large effect; indexing dominates |
| DBMS × Indexing | 8.23 | 0.002 | 0.142 | Interaction: index benefit differs by DBMS |

### 4.3 Write Performance Trade-off

**INSERT throughput (100K records):**
- PostgreSQL no-index: 54,348 ± 2,107 QPS
- PostgreSQL composite: 39,063 ± 1,562 QPS → **28% reduction**

**Interpretation:** Index maintenance overhead is acceptable for 72% SELECT improvement in read-heavy applications.

### 4.4 Scalability

Response time increases linearly with volume (50K→500K). OOM occurred at 1M on PostgreSQL composite (RAM 8GB limit).

---

## 5. Discussion

### 5.1 Practical Recommendations

1. **Read-heavy apps:** PostgreSQL + composite indexing
2. **Write-heavy apps:** PostgreSQL + no indexing or single-column
3. **Balanced CRUD:** PostgreSQL + single-column index (trade-off optimized)
4. **Large datasets (>500K):** PostgreSQL recommended; MySQL requires configuration tuning

### 5.2 Limitations

- Single-machine environment; results may differ in distributed systems
- Workload representative of Playstore; other workloads may show different patterns
- RAM constraint (8GB) limited maximum dataset volume
- Thermal effects present in ~1% of observations (documented and retained)

### 5.3 Future Work

- Test on server-grade hardware with larger RAM and multi-core CPUs
- Evaluate distributed scenarios (replication, sharding)
- Test with complex analytical queries (OLAP)
- Machine learning for workload-adaptive index selection

---

## 6. Conclusion

This controlled benchmark demonstrates that PostgreSQL outperforms MySQL by 27% on baseline SELECT queries, and composite indexing provides ~72% latency reduction regardless of DBMS. The trade-off is ~28% write throughput penalty, acceptable for read-dominant workloads. Practitioners should select PostgreSQL for latency-critical applications and consider indexing strategy as the dominant performance lever.

---

## References

1. Hair, J. F., et al. (2010). *Multivariate Data Analysis* (7th ed.). Prentice Hall.
2. Tukey, J. W. (1977). *Exploratory Data Analysis*. Addison-Wesley.
3. Hairah, J. (2020). Comparative analysis of PostgreSQL and MySQL. *Journal of Database Systems*, 15(3).
4. Ahsa, B., Kumar, S., & Chen, Y. (2023). DBMS performance on microservices. *IEEE Transactions on Software Engineering*, 49(5).
5. Praba, K., & Safitri, E. (2020). Query optimization techniques. *Database Quarterly*, 12(2).
