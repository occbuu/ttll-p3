"""Check committed aggregate outputs without restricted survey inputs."""
from pathlib import Path
import ast
import json

P = Path(__file__).resolve().parent
results = json.loads((P / "analysis" / "results.json").read_text(encoding="utf-8"))
assert results["verified_n"] == 450
assert results["clean_n"] == 460
assert results["verified_geo_reason_n"] == 438
for item in results["raw_item_checks"].values():
    assert item["matched"] == 450 and item["different"] == 0

for name in [
    "reasons.csv",
    "distances_by_reason.csv",
    "walking_contrasts.csv",
    "adjusted_associations.csv",
    "cohort_sensitivity.csv",
    "omnibus_tests.csv",
]:
    assert (P / "analysis" / name).is_file(), name

for name in [
    "Figure1_reasons.png",
    "Figure1_study_area.png",
    "Figure2_accessibility.png",
    "Figure2_network_method.png",
]:
    assert (P / "analysis" / name).is_file(), name

audit = json.loads((P / "analysis" / "map_audit.json").read_text(encoding="utf-8"))
assert not audit["exact_respondent_points_published"]
assert audit["displayed_respondents"] + audit["suppressed_respondents"] == 449

ast.parse((P / "analyse_paper3.py").read_text(encoding="utf-8"))
ast.parse((P / "spatial_figures.py").read_text(encoding="utf-8"))
print("PASS: aggregate outputs present; 450 source-linked records; map audit OK; scripts parse.")
