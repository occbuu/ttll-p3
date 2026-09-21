# Paper3: revised replication package

**Beyond distance to a bus stop: Stated barriers and historically mapped transit access in Ho Chi Minh City.**

The current analysis is in [`revision_20260920/`](revision_20260920/). It supersedes the interpretation and results of the original *Habit, Not Infrastructure* notebook. Original root-level notebooks, tables, figures and `derived/` remain historical files, not the inputs or results of this revision. No new journal submission, GitHub release or Zenodo DOI is implied by this update.

## Run the complete notebook

Open **[Paper3_Revised_Reproduce.ipynb](Paper3_Revised_Reproduce.ipynb)** from this repository root. It rebuilds the analysis, four figures, Word/Markdown and LaTeX/PDF, with configurable private input paths. `FULL_REBUILD=True` is the default; aggregate-only mode is explicitly labelled. Install the Python requirements plus Pandoc and XeLaTeX before running. The notebook saved in Git has no outputs or private absolute paths.

The portable LaTeX package is in `paper/revised/`; the local authoring copy is in `Paper3/_TruongTho/` outside this repository. Rebuild with `python revision_20260920/build_latex.py` after rebuilding the manuscript.

## Current package

- `analyse_paper3.py`: source-linked survey cohort, historical OSM extraction, walking networks, spatial-block bootstrap, exploratory adjusted associations and sensitivity checks.
- `analysis/`: aggregate CSV/JSON results and four figures. No respondent-level records are added by this revision.
- `build_manuscript.py` and `manuscript_template.md`: rebuild Markdown, Word and the 50-reference bibliography from the aggregate outputs.
- `Paper3_Revised.docx`: revised Word manuscript; `paper/revised/Paper3_Revised.pdf` is the PDF compiled from the companion LaTeX source.
- `references_verified.json`, `Reference_Audit_50.csv`, `References_50.ris`: 50 cited references and metadata audit. Metadata verification does not mean full-text review of all sources.
- `README_VI.md`, `Editorial_Package.md`: revision notes and author information still needed before submission.

The main cohort contains 450 records linked to the original export. The 460-record cleaned dataset is a sensitivity cohort. OSM 2023 is the historical comparison; OSM 2026 is a mapping sensitivity, not a causal before/after evaluation.

## Reproduce

Python 3.12 was used for the analysis. Install the revision dependencies in an isolated environment:

```bash
python -m pip install -r revision_20260920/requirements.txt
python revision_20260920/verify_package.py
python revision_20260920/analyse_paper3.py --help
```

To rebuild the analysis, obtain authorized access to the cleaned and original resident XLSX files, including coordinates. They are not bundled with this revision. Download the historical `vietnam-230101.osm.pbf` and `vietnam-260101.osm.pbf` snapshots from [Geofabrik](https://download.geofabrik.de/asia/vietnam.html). Their SHA-256 checksums are recorded in `analysis/results.json`.

```bash
python revision_20260920/analyse_paper3.py --clean-survey "/private/QData_Citizens.xlsx" --raw-survey "/private/original_resident_responses.xlsx" --pbf-dir "/public-data/osm" --make-maps
python revision_20260920/build_manuscript.py
python revision_20260920/verify_package.py
```

Use `--output-dir` and `--cache-dir` to redirect generated results and OSM extraction caches. The manuscript builder reads `revision_20260920/analysis/`; copy reviewed results there if an alternate output directory was used. The first PBF extraction can take several minutes. A cached extraction is accepted only when its source PBF hash matches. The analysis writes aggregate outputs only; do not add survey inputs or local caches to Git.

`build_manuscript.py` does not export PDF. Run `build_latex.py` to produce the LaTeX PDF, or export Word separately; inspect either layout after changes. The package verifier checks counts and internal consistency, not scientific validity or ethics documentation. The full spatial analysis cannot be independently rerun from aggregates alone.

## Publication and licensing

The revised manuscript still requires author confirmation of recruitment, consent/ethics, author declarations and shared-data disclosures. Refer to the revision notes. Do not use the historical DOI instructions or release notes as evidence that the revised manuscript has been released or accepted.

Existing repository material is under [CC BY 4.0](LICENSE); OSM data retain their applicable ODbL terms. Data-sharing permissions for restricted survey records must be established separately. Historical respondent-level files already in the repository are outside this aggregate-only addition and should be reviewed before any new public release.

## Map interpretation and context provenance

The study map displays 30 occupied 500 m cells with at least five source-linked respondents (390 people represented; 59 in smaller cells suppressed). These symbols are cell centres, not household locations. The network illustration is a synthetic origin on actual public 2023 OSM geometry, not a household example or observed route. The ECDF is Figure 3; the reasons chart remains Figure 4.

See `revision_20260920/context/README.md` for context-layer provenance and the unresolved source/licence confirmation for the archived ward boundary. It is not used in distance analysis. Metro Line 1 is an undated context layer; it must not be interpreted as a 2023 operating line.

Journal positioning is documented in `revision_20260920/JOURNAL_POSITIONING.md`: Journal of Transport Geography is an ambitious thematic target, with Case Studies on Transport Policy as a practical alternative. No acceptance probability is asserted.
