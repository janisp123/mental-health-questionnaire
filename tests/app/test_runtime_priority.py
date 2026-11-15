"""Actual preview/PDF order and old-progress conservation; no real patient data."""
import sys,tempfile,io,re
from pathlib import Path
from playwright.sync_api import sync_playwright
from pypdf import PdfReader
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'full_bank'))
from browser_helpers import act,backup,launch,open_page,restore
import build_questionnaire as build

data=build.build_bundle();by_id={q['id']:q for g in data['groups'] for q in g['questions']}
with tempfile.TemporaryDirectory() as tmp,sync_playwright() as pw:
 path=Path(tmp)/'priority.html';path.write_text(build.make_html(data));browser=launch(pw)
 for locale in data['ui']:
  page,errors,network=open_page(browser,path)
  codes={'M06_01':'B','M06_02':'B','M06_02P':'A','M06_03':'A','M06_06':'B','M06_07':'A','M15_19':'B','M14_01':'B','M14_09':'B','M05_13':'B','M05_14':'E','M31_09':'C','M31_10':'D','M43_01':'E'}
  answers={qid:{'kind':'choice','codes':[code],'status':by_id[qid]['answerStatus'][code],'savedAt':'2026-11-15T12:00:00Z'} for qid,code in codes.items()}
  answers['M33_01']={'kind':'text','value':'Synthetic concern for review','status':'answered','savedAt':'2026-11-15T12:00:00Z'}
  payload={'schema':'mental-pilot-recovery-v1','version':'0.2.12-review+full-bank','layoutVersion':data['layout_version'],'lang':locale,'selected':[g['id'] for g in data['groups']],'sectionConfirmed':True,'currentId':'M06_01','answers':answers,'feedback':{}}
  restore(page,payload);assert backup(page)['answers']==answers
  expected=page.evaluate('''payload=>{const d=JSON.parse(document.getElementById('questionnaire-data').textContent),m=QuestionnaireModel.create(d),qs=m.reportQuestions(payload);return QuestionnaireReports.entries(qs,payload.answers,payload.lang,d.presentation,d.ui[payload.lang].medicine).map(e=>({id:e.id,plain:e.plain}));}''',payload)
  act(page,'results');act(page,'doctor')
  rows=page.locator('.report-preview hr ~ p').all_inner_texts()
  normalize=lambda text:' '.join(text.split())
  assert list(map(normalize,rows))==[normalize(e['plain']) for e in expected]
  ids=[e['id'] for e in expected]
  assert ids.index('M06_02')<ids.index('M33_01')
  assert ids.index('M15_19')<ids.index('M14_09')
  assert 'M31_09' in ids and 'M31_10' in ids
  assert data['ui'][locale]['reportOrderNote'] in page.locator('.report-preview').inner_text()
  pdf=PdfReader(io.BytesIO(page.pdf(format='A4')))
  # PDF extraction can insert whitespace inside a hyphenated word at a line/page break.
  compact=lambda value:re.sub(r'\s+','',value)
  text=compact('\n'.join(p.extract_text() or '' for p in pdf.pages))
  positions=[text.index(compact(e['plain'])) for e in expected]
  assert positions==sorted(positions),'PDF must retain the same response order as preview'
  for width in (320,390):
   page.set_viewport_size({'width':width,'height':844});assert page.evaluate('document.documentElement.scrollWidth <= innerWidth')
  act(page,'resultScreen');saved=backup(page);assert saved['answers']==answers and saved['feedback']=={}
  restore(page,saved);assert backup(page)['answers']==answers
  assert not errors,errors
  assert not network,network
  page.close()
 browser.close()
print('PASS: real localized report preview/PDF order, no answer loss, old/current progress round trip and offline phone widths.')
