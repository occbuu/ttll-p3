# v1.0.0 — TTLL P3

Replication package for Truong Tho Living Lab **Paper 3**.

**Habit, Not Infrastructure:** Motorcycle Lock-In and Micro-Enterprise Vulnerability as a Behavioural Baseline on the Eve of Metro Line 1 Operation in Ho Chi Minh City

Lê Ngọc Hiếu (ORCID [0000-0002-1133-1433](https://orcid.org/0000-0002-1133-1433))  
Licence: [CC BY 4.0](LICENSE)

This is the first public archive of the analysis. Tag it on a **public** GitHub repository and Zenodo will mint a DOI for this release.

---

## Paper

A behavioural baseline recorded in the Truong Tho ward cluster (Thu Duc City) immediately before Metro Line 1 entered commercial service (22 December 2024). Face-to-face surveys of **460 residents**, **80 micro-enterprises** and **23 local officials** are combined with two dated OpenStreetMap snapshots (1 Jan 2023, 1 Jan 2026), GHSL settlement layers, and the VCCI Provincial Competitiveness Index.

Target journal: *Travel Behaviour and Society* (preprint in `paper/Paper3_TruongTho_V1.pdf`).

## Headline results

| Result | Value |
|---|---|
| Private motorcycle as main mode | 83.5% (384/460); bus 1.7% |
| Habit vs infrastructure | 68.0% vs 11.1% — ratio **6.1:1** |
| After reclassifying walking discomfort as perceptual | **7.5:1** (83.4% vs 11.1%) |
| Network walking distance, by stated barrier | Kruskal–Wallis *p* = 0.153; ε² = 0.006 |
| Walking-discomfort group vs others | 450 m vs 398 m; *p* = 0.835 |
| Income → motorcycle dependence | OR **1.76** per band (95% CI 1.19–2.62; *p* = 0.005) |
| ML robustness (5-fold CV) | ROC-AUC 0.610–0.635; none beats majority-class 0.853 |
| Resident–official diagnostic gap | χ²(3) = 129.56; *p* < 0.001; **51 pp** |
| Line 1 stations in OSM 2023 and 2026 | 14/14; max shift 31.8 m |

All quantities above are stored in `derived/results.json` and match the preprint.

## What this release contains

- `Paper3_Analysis.ipynb` — end-to-end analysis notebook
- `paper/Paper3_TruongTho_V1.pdf` — preprint
- `figures/` — 12 figures (300 dpi PNG)
- `tables/` — 19 CSV tables (T1–T18 + T15b)
- `derived/results.json` — every statistic quoted in the manuscript
- `derived/citizens_analysis_public.csv`, `smes_analysis_public.csv` — analysis files **without** names, phones, emails, street addresses, or coordinates
- `data/clip/` — GHSL study-window rasters
- `data/pci/` — PCI 2021–2025 files used in Table 16 / Figure 11
- `CITATION.cff`, `.zenodo.json`, `LICENSE`

## What this release does **not** contain

- Household GPS and street addresses (identifying). Available from the corresponding author under a data-use agreement.
- Geofabrik Vietnam `.pbf` extracts (264 MB + 304 MB). Download dated snapshots **2023-01-01** and **2026-01-01** from [Geofabrik](https://download.geofabrik.de/asia/vietnam.html).
- Global GHSL 100 m rasters (~6 GB). The four files in `data/clip/` are sufficient for the corridor-ring tables.

## How to cite this version

Until Zenodo issues the DOI, cite the preprint and this tag (`v1.0.0`). After the DOI appears, use the **concept DOI** in the paper’s Data-availability statement and add it to `CITATION.cff`.

```
Lê, N. H. (2026). Habit, Not Infrastructure: replication package for Truong Tho Living Lab Paper 3 (v1.0.0). GitHub. https://github.com/<USER>/<REPO>/releases/tag/v1.0.0
```

Correspondence: lnhieu@ptit.edu.vn
