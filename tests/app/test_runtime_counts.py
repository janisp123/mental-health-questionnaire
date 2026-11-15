"""Summary and clinician counts agree across selection, conditions and recovery."""
import sys,tempfile
from pathlib import Path
from playwright.sync_api import sync_playwright
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'full_bank'))
from browser_helpers import act,backup,launch,open_page,restore
from runtime_fixture import write_fixture,LOCALES

with tempfile.TemporaryDirectory() as tmp,sync_playwright() as pw:
 path=Path(tmp)/'counts.html';write_fixture(path);browser=launch(pw)
 for locale in LOCALES:
  page,errors,network=open_page(browser,path)
  data=page.locator('#questionnaire-data').evaluate('e=>JSON.parse(e.textContent)')
  ui=data['ui'][locale]
  answers={'SYN_01':{'kind':'choice','codes':['B']},'SYN_02':{'kind':'skip'},'SYN_03':{'kind':'choice','codes':['A']}}
  for record in answers.values():record.update(status='skipped' if record['kind']=='skip' else 'answered',savedAt='2026-11-14T12:00:00Z')
  payload={'schema':'mental-pilot-recovery-v1','version':'0.2.8-review+full-bank','layoutVersion':data['layout_version'],'selected':['S01'],'sectionConfirmed':True,'lang':locale,'answers':answers}
  restore(page,payload);act(page,'results')
  def summary(expected):
   assert page.locator('.stats b').all_inner_texts()==list(map(str,expected))
   text=page.locator('.stats').inner_text()
   for label in ('reportCountSelected','reportCountDone','reportCountSkip'):assert ui[label] in text
   assert ui['coverageNote'] in page.locator('#app').inner_text()
  def clinician(expected,report_locale):
   page.select_option('#report-language',report_locale);act(page,'doctor')
   report=page.locator('.report-preview').inner_text();r=data['ui'][report_locale]
   assert r['reportCountIncluded']+': '+str(expected[1]) in report
   assert r['reportCountSelected']+':' not in report and r['reportCountSkip']+':' not in report
   assert r['omissionNote'] in report and r['coverageNote'] not in report
   return report
  complete_answers=dict(answers)
  del answers['SYN_03']
  payload['answers']=answers;restore(page,payload);act(page,'results')
  summary((3,1,1));report=clinician((3,1,1),'en')
  assert 'Conditional follow-up' not in report
  act(page,'resultScreen')
  answers=complete_answers;payload['answers']=answers;restore(page,payload);act(page,'results')
  summary((3,2,1));report=clinician((3,2,1),'en')
  assert 'Next section' not in report and 'Multiple choice' not in report
  act(page,'resultScreen')
  assert backup(page)['answers']==answers
  answers['SYN_04']={'kind':'choice','codes':['B'],'status':'answered','savedAt':'2026-11-14T12:00:00Z'}
  payload['answers']=answers;restore(page,payload);act(page,'results')
  summary((4,3,1));report=clinician((4,3,1),locale)
  assert 'Next section' in report
  act(page,'resultScreen')
  answers['SYN_01']={'kind':'choice','codes':['A'],'status':'answered','savedAt':'2026-11-14T12:00:00Z'}
  payload['answers']=answers;restore(page,payload);act(page,'results')
  summary((3,2,1));report=clinician((3,2,1),locale)
  assert 'Conditional follow-up' not in report and 'Next section' in report
  act(page,'resultScreen');assert backup(page)['answers']==answers
  act(page,'sections')
  progress=page.locator('[data-module="S01"]').locator('..').inner_text()
  assert ui['sectionProgress'].replace('{total}','3').replace('{completed}','1').replace('{skipped}','1') in progress
  assert page.evaluate('document.documentElement.scrollWidth <= innerWidth')
  assert not errors,errors
  assert not network,network
  page.close()
 browser.close()
print('PASS: four-language selected/saved/conditional counts; answered and skipped stay distinct in summary, selector and clinician output; old progress preserves all records.')
