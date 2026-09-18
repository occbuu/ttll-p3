# Habit, Not Infrastructure — replication package

**Truong Tho Living Lab · Paper 3 · Ho Chi Minh City**

Replication files for:

> Lê, N. H. *Habit, Not Infrastructure: Motorcycle Lock-In and Micro-Enterprise Vulnerability as a Behavioural Baseline on the Eve of Metro Line 1 Operation in Ho Chi Minh City.* Preprint, 2026.

This folder is the **GitHub + Zenodo** deposit: small enough for git, stripped of household identifiers, and ready to mint a DOI.

## What is in here

| Path | Contents |
|---|---|
| `Paper3_Analysis.ipynb` | End-to-end analysis notebook |
| `paper/Paper3_TruongTho_V1.pdf` | Preprint PDF |
| `figures/` | 12 figures (300 dpi PNG) |
| `tables/` | 19 CSV tables (T1–T18 + T15b) |
| `derived/results.json` | Every statistic quoted in the manuscript |
| `derived/citizens_analysis_public.csv` | Resident analysis file **without** names, phones, emails, street addresses, or coordinates |
| `derived/smes_analysis_public.csv` | SME analysis file, same redaction |
| `derived/metro_stations_*.csv`, `bus_stops_*.csv` | OSM-derived stop inventories (public objects) |
| `data/clip/` | GHSL population and built-up clips for the study window |
| `data/pci/` | PCI 2021–2025 files used in Table 16 / Figure 11 |
| `CITATION.cff`, `.zenodo.json` | Citation + Zenodo metadata |

Headline results (from `derived/results.json`): motorcycle as main mode **83.5%**; habit vs infrastructure **68.0% vs 11.1%** (ratio 6.1:1); income OR **1.76** (p = 0.005); resident–official diagnostic gap **51 percentage points**.

## What is *not* in here (on purpose)

- Household GPS and street addresses (identifying). Available from the corresponding author under a data-use agreement.
- Geofabrik Vietnam `.pbf` snapshots (~264 MB + 304 MB). Download from [Geofabrik](https://download.geofabrik.de/asia/vietnam.html) dated **2023-01-01** and **2026-01-01**.
- Global GHSL 100 m rasters (~6 GB each). The four files in `data/clip/` are enough to reproduce the corridor-ring tables.
- Internal working notes and Word drafts.

## How to mint the DOI

See **[HOW_TO_DOI.md](HOW_TO_DOI.md)** (GitHub release → Zenodo, or a direct Zenodo upload).

After Zenodo issues the DOI, put it in `CITATION.cff` under `identifiers` and in the manuscript Data-availability statement.

## How to rerun the notebook

```bash
python -m pip install -r requirements.txt
jupyter notebook Paper3_Analysis.ipynb
```

- Tables, figures, logistic models, and ML comparison can be inspected from the files in `tables/`, `figures/`, and `derived/` without rerunning.
- A full spatial rebuild needs the two `.pbf` files plus the restricted survey coordinates.
- With only this deposit, Step 4 of the notebook will use `data/clip/` and will not need the 6 GB global rasters.

## Licence

[CC BY 4.0](LICENSE). OSM layers remain ODbL. Cite this deposit and the preprint if you reuse the figures or `results.json`.

## Correspondence

Lê Ngọc Hiếu · `lnhieu@ptit.edu.vn` · ORCID [0000-0002-1133-1433](https://orcid.org/0000-0002-1133-1433)
