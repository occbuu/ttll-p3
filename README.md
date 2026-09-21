# ttll-p3

Code and analysis outputs for Truong Tho Living Lab **Paper 3** (Ho Chi Minh City). This repository is **not** the manuscript.

The paper links stated barriers to public transport (resident survey, 2023) with historically mapped bus-stop access from dated OpenStreetMap extracts. The manuscript is authored separately and is not stored here.

## Run

Current analysis:

```bash
python -m pip install -r revision_20260920/requirements.txt
python revision_20260920/verify_package.py
```

Full spatial rebuild (restricted survey coordinates + Geofabrik PBFs, not in this repo):

```bash
python revision_20260920/analyse_paper3.py \
  --clean-survey /path/QData_Citizens.xlsx \
  --raw-survey /path/original_resident_responses.xlsx \
  --pbf-dir /path/osm \
  --make-maps
```

Or open `Paper3_Revised_Reproduce.ipynb` from this folder. Set `FULL_REBUILD=False` to inspect committed tables and figures only.

`Paper3_Analysis.ipynb` plus `figures/`, `tables/`, and `derived/` are the earlier pipeline and its outputs.

## Layout

| Path | Role |
|---|---|
| `revision_20260920/analyse_paper3.py` | Survey–OSM linkage, tests, figures |
| `revision_20260920/spatial_figures.py` | Maps (cell aggregates; no household points) |
| `revision_20260920/analysis/` | CSV/JSON/PNG written by the scripts |
| `Paper3_Revised_Reproduce.ipynb` | Driver notebook |
| `figures/`, `tables/`, `derived/` | Outputs of the original notebook |

Survey workbooks, GPS, OSM `.pbf`, and the paper PDF/Word/TeX are **out of scope**.

## Licence

[CC BY 4.0](LICENSE). OpenStreetMap extracts remain ODbL.
