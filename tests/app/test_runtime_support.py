"""Local-help instructions and immediate emergency guidance work offline in every locale."""
import tempfile,sys,re
from pathlib import Path
from playwright.sync_api import sync_playwright
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'full_bank'))
from browser_helpers import act,backup,choose,launch,open_page
from runtime_fixture import make_fixture,LOCALES
import build_questionnaire as build
with tempfile.TemporaryDirectory() as tmp,sync_playwright() as pw:
 data=make_fixture();data['presentation']['questions']={'SYN_01':{'support':{'B':'emergency'}}}
 path=Path(tmp)/'support.html';path.write_text(build.make_html(data),encoding='utf-8')
 browser=launch(pw)
 for locale in LOCALES:
  page,errors,network=open_page(browser,path);page.select_option('#language',locale)
  panel=page.locator('#support-details');panel.locator('summary').click()
  ui=data['ui'][locale]
  assert panel.locator('p').all_inner_texts()==[ui['emergencyBody'],ui['supportBody']]
  assert not re.search(r'\b112\b|\b116\s?123\b',panel.inner_text())
  assert panel.locator('a[href^="tel:"]').count()==0
  act(page,'start');page.locator('[data-module="S01"]').check();act(page,'confirm')
  act(page,'support')
  assert page.locator('#support-message p').all_inner_texts()==[ui['emergencyBody'],ui['supportBody']]
  act(page,'dismissSupport');choose(page,'B')
  card=page.locator('#support-message');assert card.is_visible()
  assert card.locator('p').all_inner_texts()==[ui['emergencyBody'],ui['supportBody']]
  assert page.evaluate('document.documentElement.scrollWidth <= innerWidth')
  assert backup(page)['answers']['SYN_01']['codes']==['B']
  assert not errors,errors
  assert not network,network
  page.close()
 browser.close()
print('PASS: four-locale local-help search instructions, urgent guidance first, no fixed phone links or network requests; saved answer preserved.')
