"""The same released questionnaire works via HTTPS and offline with shared recovery files."""
import contextlib,functools,io,json,os,re,ssl,subprocess,tempfile,threading
from http.server import SimpleHTTPRequestHandler,ThreadingHTTPServer
from pathlib import Path
from urllib.parse import urlsplit
from playwright.sync_api import sync_playwright
from pypdf import PdfReader
from browser_helpers import act,backup,choose,launch,open_page,qid,restore
import build_discovery as site

ROOT=Path(__file__).resolve().parents[2]
manifest=json.loads((ROOT/'MH_Public_version/manifest.json').read_text())
artifact=ROOT/'MH_Public_version'/next(f['name'] for f in manifest['files'] if f['name'].endswith('.html'))
data=json.loads(re.search(r'<script id="questionnaire-data" type="application/json">(.*?)</script>',artifact.read_text(),re.S).group(1))
by_id={q['id']:q for g in data['groups'] for q in g['questions']}

@contextlib.contextmanager
def origin(tmp):
 live=os.getenv('QUESTIONNAIRE_HOSTED_BASE_URL')
 if live:
  yield live.rstrip('/')+'/'
  return
 webroot=Path(tmp)/'web';webroot.mkdir()
 class QuietHandler(SimpleHTTPRequestHandler):
  def log_message(self,*args):pass
 server=ThreadingHTTPServer(('127.0.0.1',0),functools.partial(QuietHandler,directory=str(webroot)))
 cert,key=Path(tmp)/'cert.pem',Path(tmp)/'key.pem'
 subprocess.run(['openssl','req','-x509','-newkey','rsa:2048','-nodes','-keyout',str(key),'-out',str(cert),'-days','1','-subj','/CN=localhost'],check=True,capture_output=True)
 secure=ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER);secure.load_cert_chain(cert,key)
 server.socket=secure.wrap_socket(server.socket,server_side=True)
 base=f'https://127.0.0.1:{server.server_port}/project/'
 # CI stages previews before Drive delivery; only the deployment workflow enables its guard.
 site.build(base,webroot/'project')
 thread=threading.Thread(target=server.serve_forever,daemon=True);thread.start()
 try:yield base
 finally:server.shutdown();server.server_close();thread.join()

with tempfile.TemporaryDirectory() as tmp,origin(tmp) as base,sync_playwright() as pw:
 browser=launch(pw)
 for landing_locale,path in [('en',''),('lv','lv/'),('ru','ru/')]:
  context=browser.new_context(ignore_https_errors=True,accept_downloads=True,viewport={'width':390,'height':844})
  page=context.new_page();requests=[];errors=[]
  page.on('request',lambda r:requests.append((r.url,r.method,r.post_data)))
  page.on('pageerror',lambda e:errors.append(str(e)))
  page.on('dialog',lambda d:d.accept())
  response=page.goto(base+path);assert response.status==200
  for width in (320,390,1280):
   page.set_viewport_size({'width':width,'height':844});assert page.evaluate('document.documentElement.scrollWidth <= innerWidth')
  folder='https://drive.google.com/drive/folders/1BUlc5W7tRw06JOUE250wCuTe-1ick9xb'
  assert page.locator(f'a[href="{folder}"]').count()==1
  page.locator('[data-open-questionnaire]').click();page.wait_for_selector('[data-act="start"]')
  assert page.url==base+'questionnaire/'
  # Check actual HTTP response bytes and MIME, not a source viewer or rewritten app.
  response=context.request.get(page.url);assert response.status==200
  assert response.headers['content-type'].startswith('text/html')
  assert response.body()==artifact.read_bytes()
  baseline_requests=len(requests)
  page.select_option('#language','en');act(page,'start')
  page.locator('#optionalS02').check();act(page,'confirm');assert qid(page)=='M02_01'
  choose(page,'B');saved=backup(page);assert saved['answers']['M02_01']['codes']==['B']
  # Hosted -> offline -> hosted round trip using the actual exported file format.
  offline,offline_errors,offline_network=open_page(browser,artifact)
  restore(offline,saved);assert backup(offline)['answers']==saved['answers']
  assert qid(offline)=='M02_02';choose(offline,'A');saved=backup(offline)
  restore(page,saved);assert backup(page)['answers']==saved['answers']
  for locale in data['ui']:
   page.select_option('#language',locale)
   assert backup(page)['answers']==saved['answers']
  page.select_option('#language','en')
  # Synthetic context verifies medicine notes and No/uncertain/refusal report preservation.
  for question_id,code in [('M06_01','A'),('M06_02','C'),('M06_23','D')]:
   saved['answers'][question_id]={'kind':'choice','codes':[code],'status':by_id[question_id]['answerStatus'][code],'savedAt':'2026-11-15T12:00:00Z'}
  medicine={k:'' for k in data['ui']['en']['medicine']['fields']}
  medicine.update(name='SYNTHETIC_HOSTED_MEDICINE',status='past',effects='SYNTHETIC notes only')
  saved['answers']['M14_02']={'kind':'medicine','records':[medicine],'discussion':'SYNTHETIC discussion only','status':'answered','savedAt':'2026-11-15T12:00:00Z'}
  saved['selected']=['S01','S02','S04'];saved['lang']='en'
  restore(page,saved)
  act(page,'results');act(page,'doctor')
  for width in (320,390,1280):
   page.set_viewport_size({'width':width,'height':844});assert page.evaluate('document.documentElement.scrollWidth <= innerWidth')
  report=page.locator('.report-preview').inner_text();assert 'SYNTHETIC_HOSTED_MEDICINE' in report
  for question_id,code in [('M06_01','A'),('M06_02','C'),('M06_23','D')]:
   assert by_id[question_id]['translations']['en']['choices'][code] in report
  pdf=PdfReader(io.BytesIO(page.pdf(format='A4')))
  assert 'SYNTHETIC_HOSTED_MEDICINE' in '\n'.join(p.extract_text() or '' for p in pdf.pages)
  act(page,'shareQuestionnaire');invitation=page.locator('#questionnaire-share-copy').input_value()
  assert 'SYNTHETIC' not in invitation
  assert 'https://janisp123.github.io/mental-health-questionnaire/' in invitation
  assert len(requests)==baseline_requests,'Answers/report/sharing must make no HTTP request'
  assert all(method=='GET' and body is None and urlsplit(url).netloc==urlsplit(base).netloc for url,method,body in requests)
  assert not errors and not offline_errors and not offline_network,(errors,offline_errors,offline_network)
  offline.close();context.close()
 browser.close()
print('PASS: real HTTPS launch from all landing locales, exact release bytes, hosted/offline recovery, languages, responsive report/PDF and no answer transmission. Offline load mode: '+os.getenv('QUESTIONNAIRE_LOAD_MODE','file'))
