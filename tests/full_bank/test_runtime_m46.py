"""Focused new-item navigation, reports and pre-addition progress compatibility."""
import tempfile
from pathlib import Path
from playwright.sync_api import sync_playwright
from browser_helpers import act,backup,choose,launch,open_page,qid,restore
import build_questionnaire as build

with tempfile.TemporaryDirectory() as tmp,sync_playwright() as pw:
 path=Path(tmp)/'questionnaire.html';path.write_text(build.make_html(),encoding='utf-8')
 browser=launch(pw);page,errors,network=open_page(browser,path)
 data=build.build_bundle();section=data['source_module_to_section']['46']
 by_id={q['id']:q for g in data['groups'] for q in g['questions']}
 act(page,'start');page.locator(f'[data-module="{section}"]').check();act(page,'confirm')
 old=backup(page);old['appVersion']='0.2.14-review+full-bank';old['currentId']='M46_01'
 old['answers']={'M46_01':{'kind':'choice','codes':['A'],'status':'answered','savedAt':'2026-11-15T00:00:00Z'}}
 for locale in data['ui']:
  restore(page,{**old,'lang':locale});assert qid(page)=='M46_01'
  # Negative broad screen must not hide the three direct items.
  choose(page,'A');assert qid(page)=='M46_03';choose(page,'A')
  for question_id in ('M46_07','M46_08','M46_09'):
   assert qid(page)==question_id
   assert page.locator('h2').inner_text()==by_id[question_id]['translations'][locale]['title']
   choose(page,'B')
  assert qid(page)=='M46_06'
  saved=backup(page)
  for question_id in ('M46_07','M46_08','M46_09'):assert saved['answers'][question_id]['codes']==['B']
  restore(page,saved);roundtrip=backup(page);assert roundtrip['answers']==saved['answers']
  act(page,'results');act(page,'doctor')
  preview=page.locator('.report-preview').inner_text()
  for question_id in ('M46_07','M46_08','M46_09'):
   t=by_id[question_id]['translations'][locale]
   assert t['title'] in preview and t['choices']['B'] in preview
  pdf=page.pdf();assert pdf.startswith(b'%PDF')
  act(page,'resultScreen');act(page,'back')
 assert not errors,errors
 assert not network,network
 browser.close()
print('PASS: new M46 questions reachable after No; all locales, rare choice, clinician PDF and old/current progress retained.')
