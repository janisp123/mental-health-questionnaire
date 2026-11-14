"""The M04_01 explanation is actually visible in every locale and preserves the question."""
import tempfile,sys
from pathlib import Path
from playwright.sync_api import sync_playwright
from browser_helpers import launch,open_page,restore
sys.path.insert(0,str(Path(__file__).resolve().parents[2]/'tools'))
import build_questionnaire as build
bundle=build.build_bundle();question=next(q for g in bundle['groups'] for q in g['questions'] if q['id']=='M04_01')
with tempfile.TemporaryDirectory() as tmp,sync_playwright() as pw:
 path=Path(tmp)/'panic.html';path.write_text(build.make_html(bundle),encoding='utf-8');browser=launch(pw)
 for locale in bundle['ui']:
  page,errors,network=open_page(browser,path)
  restore(page,{'schema':'mental-pilot-recovery-v1','version':bundle['version'],'layoutVersion':bundle['layout_version'],'lang':locale,'selected':[question['module']],'sectionConfirmed':True,'currentId':'M04_01','answers':{},'feedback':{}})
  help=page.locator('.question p.help');assert help.is_visible()
  assert help.inner_text()==question['translations'][locale]['help']
  assert page.locator('#question-heading').inner_text()==question['translations'][locale]['title']
  assert page.evaluate('document.documentElement.scrollWidth <= innerWidth')
  assert not errors,errors
  assert not network,network
  page.close()
 browser.close()
print('PASS: panic-peak explanation visible in all four locales; title and mobile layout preserved.')
