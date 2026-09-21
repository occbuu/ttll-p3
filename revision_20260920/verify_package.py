"""Check the aggregate replication package without restricted survey inputs."""
from pathlib import Path
import ast, json, re
from docx import Document
P=Path(__file__).resolve().parent
refs=json.loads((P/'references_verified.json').read_text(encoding='utf-8'))
assert len(refs)==50 and len({r['id'] for r in refs})==50
assert len({r['DOI'].lower() for r in refs if r.get('DOI')})==46
checks=json.loads((P/'build_checks.json').read_text(encoding='utf-8'))
assert checks['unique_cited_references']==50 and not checks['unresolved_placeholders']
results=json.loads((P/'analysis/results.json').read_text(encoding='utf-8'))
assert results['verified_n']==450 and results['clean_n']==460
assert results['verified_geo_reason_n']==438
for item in results['raw_item_checks'].values():
    assert item['matched']==450 and item['different']==0
ris=(P/'References_50.ris').read_text(encoding='utf-8')
assert ris.count('TY  -')==50 and ris.count('ER  -')==50
doc=Document(P/'Paper3_Revised.docx')
paragraphs=[p.text for p in doc.paragraphs]
assert len([p for p in paragraphs[paragraphs.index('References')+1:] if p.strip()])==50
assert len(doc.tables)==5 and len(doc.inline_shapes)==4
for name in ['analyse_paper3.py','build_manuscript.py']:
    ast.parse((P/name).read_text(encoding='utf-8'))
print('PASS: 50 references; 450 source-linked records; 5 tables; 4 figures; scripts parse.')

map_audit=json.loads((P/"analysis/map_audit.json").read_text())
assert not map_audit["exact_respondent_points_published"]
assert map_audit["displayed_respondents"]+map_audit["suppressed_respondents"]==449
