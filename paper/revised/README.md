# Paper3 revised LaTeX

Build from this directory: `xelatex -interaction=nonstopmode -halt-on-error Paper3_Revised.tex` (twice).

The source is self-contained with `figures/`. On a different platform, replace the Times New Roman font with an available font or regenerate with `build_latex.py --font "TeX Gyre Termes"`.

The editable analytical source of truth is `../../revision_20260920/`. To regenerate everything, run `../../Paper3_Revised_Reproduce.ipynb`. Do not edit this generated `.tex` without preserving the corresponding manuscript-template changes.

Four figures, five tables, exactly 50 references. Figure 1 uses aggregated survey locations; Figure 2 uses a synthetic origin on the actual OSM graph. Context boundary provenance requires author confirmation; see the repository context README. No journal submission is implied.
