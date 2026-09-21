# Validation — map and LaTeX revision, 2026-09-21

- Executed every code cell of `Paper3_Revised_Reproduce.ipynb` sequentially in a shared Python namespace, with full rebuild enabled and the real authorized source inputs. This is a cell-by-cell execution check, not a browser/Jupyter UI test.
- Source linkage and statistical outputs retain 450 source-linked main records and 460 sensitivity records.
- All six aggregate CSVs match the preceding revision exactly; maps do not alter the statistical results.
- Four figures rebuilt. Map audit confirms 390 respondents represented in 30 cells and 59 suppressed; no exact respondent locations plotted.
- Synthetic route: approximately 575 m straight line, 882 m network, origin connector 40 m, destination connector 0 m; both connectors <=100 m.
- Word and bibliography rebuilt: 5 tables, 4 figures, 50 cited references, 46 unique DOIs.
- XeLaTeX compiled twice: 15 A4 pages; no overfull-box or missing-character warnings. All PDF pages visually reviewed.
- Notebook schema validated; Git copy has empty outputs and no private absolute input paths. Full rerun requires restricted survey inputs and external historical PBFs.
- No commit, push, public release or journal submission performed.
