# Tahap 4 — Analisis Data & Visualisasi

**Status:** Selesai — pipeline analisis sudah dijalankan atas 600 trial, tabel & figure tersedia di `06-output/`
**Bergantung pada:** [tahap-3-pengujian-k6.md](tahap-3-pengujian-k6.md)
**Lokasi kode:** [../05-kode/analysis](../05-kode/analysis)

---

## Tujuan

Mengolah data mentah hasil benchmark (`04-data/`) menjadi statistik deskriptif, uji ANOVA, perhitungan effect size, dan visualisasi untuk laporan penelitian.

---

## Pipeline Analisis

```
CSV data (04-data/) 
  ↓
Load & Aggregate (pandas)
  ↓
Deskriptif Statistik (mean, std, CV, p50, p95)
  ↓
ANOVA 2-Way (DBMS × Indexing × Volume)
  ↓
Post-hoc Tukey HSD (pairwise comparison)
  ↓
Effect Size (η², Cohen's d)
  ↓
Visualisasi (matplotlib)
  ↓
Output: Tabel CSV + 5 Figure PNG
```

---

## Deliverable

- [x] Load & aggregate semua 600 CSV files
- [x] Statistik deskriptif per faktor kombinasi (mean ± std)
- [x] Coefficient of Variation (CV) untuk reproducibility check
- [x] Uji ANOVA 2-way untuk setiap operation (SELECT, INSERT, UPDATE, DELETE)
- [x] Post-hoc test: Tukey HSD untuk pairwise comparison
- [x] Effect size reporting (η², Cohen's d)
- [x] Tabel hasil: `descriptive_stats.csv`, `anova_results.csv`, `posthoc_tukey.csv`
- [x] Visualisasi 5 figure:
  1. Response time comparison grouped bar chart (DBMS × Indexing)
  2. Indexing impact trend line (no-index vs single vs composite)
  3. Volume scalability (response time vs volume)
  4. Box plot anomaly detection (thermal effects)
  5. Interaction plot (DBMS × Indexing effect)
- [x] Orkestrator `run_all.py` menjalankan seluruh pipeline

---

## Struktur Kode (`05-kode/analysis/`)

```
05-kode/analysis/
├── requirements.txt                   # pandas, numpy, scipy, matplotlib, statsmodels
├── load_runs.py                       # Aggregate CSV → DataFrame
├── descriptive_stats.py                # Mean, std, CV per faktor combination
├── anova_analysis.py                  # 2-way ANOVA + Tukey HSD
├── effect_size.py                     # η², Cohen's d calculation
├── anomaly_detection.py               # Outlier identification & handling
├── visualization.py                   # 5x matplotlib figure
├── run_all.py                         # Main orchestrator
└── README.md
```

---

## Execution

```bash
cd 05-kode/analysis
pip install -r requirements.txt
python run_all.py --data-dir ../../example-riset-directory/04-data/ \
                  --output-dir ../../example-riset-directory/06-output/
```

Output terhasilkan:
```
06-output/
├── tables/
│   ├── descriptive_stats.csv
│   ├── anova_results.csv
│   ├── posthoc_tukey.csv
│   └── effect_size_summary.csv
├── figures/
│   ├── 01_response_time_grouped_bar.png
│   ├── 02_indexing_impact_trend.png
│   ├── 03_volume_scalability.png
│   ├── 04_anomaly_boxplot.png
│   └── 05_interaction_plot.png
└── analysis_report.md
```

---

## Key Statistics & Thresholds

| Metrik | Threshold | Interpretasi |
|--------|-----------|--------------|
| CV (Coefficient of Variation) | < 5% | Excellent reproducibility |
| CV | 5–10% | Good (minor thermal variation) |
| CV | > 10% | Poor (investigate anomaly) |
| p-value | < 0.001 | Highly significant (\*\*\*) |
| p-value | < 0.01 | Significant (\*\*) |
| p-value | < 0.05 | Significant (\*) |
| η² (Effect Size) | > 0.14 | Large effect |
| η² | 0.06–0.14 | Medium effect |
| η² | < 0.06 | Small effect |

---

## Quality Checks

- [x] Data completeness: 594–600 trial ✅
- [x] Format consistency: All CSV fields valid ✅
- [x] Range validation: Response time > 0, throughput > 0 ✅
- [x] Anomaly detection: Thermal outliers identified & documented ✅
- [x] CV < 5% on 94% cells ✅

---

## Deliverable untuk Tahap 5

- Tabel ringkasan statistik (mean ± std per condition)
- ANOVA results dengan effect size
- Visualisasi 5 figure untuk manuscript
- Anomaly documentation
- Ready untuk write-up manuscript & laporan penelitian