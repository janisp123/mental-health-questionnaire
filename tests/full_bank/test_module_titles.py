"""Every full-bank module title must match its frozen localized source."""
import importlib.util,json,re
from pathlib import Path

ROOT=Path(__file__).resolve().parents[2]
spec=importlib.util.spec_from_file_location('questionnaire_build',ROOT/'tools'/'build_questionnaire.py')
build=importlib.util.module_from_spec(spec);spec.loader.exec_module(build)
references={
 'lv':ROOT/'reference/baseline/html/162_Sagatavosanas_vizitei_LV_v16.html',
 'en':ROOT/'reference/baseline/html/172_Questionnaire_EN_v16_DRAFT_NOT_RELEASED.html',
 'ru':ROOT/'reference/baseline/html/172_Questionnaire_RU_v16_DRAFT_NOT_RELEASED.html',
}
titles=build.load_module_titles()
assert set(titles)==set(references)
for lang,path in references.items():
 source=path.read_text(encoding='utf-8')
 raw=re.search(r'const TITLES\s*=\s*(\[.*?\]);',source,re.S)
 assert raw, f'Frozen module titles missing: {lang}'
 expected=json.loads(raw.group(1))
 assert len(expected)==48 and list(titles[lang])==[f'{i:02d}' for i in range(1,49)]
 assert list(titles[lang].values())==expected, f'Title text/order changed: {lang}'
print('PASS: 48 section titles in LV/EN/RU exactly match the frozen references.')
