"""Publication exposes only landing pages, sitemap and the verified questionnaire artifact."""
import copy,hashlib,json,re,shutil,subprocess,sys,tempfile,unittest
from unittest.mock import patch
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT/'tools'))
import build_discovery as site
class BuildDiscovery(unittest.TestCase):
 def test_allowlisted_bundle_and_actual_canonical(self):
  with tempfile.TemporaryDirectory() as tmp:
   out=Path(tmp)/'site'
   subprocess.run(['python',str(ROOT/'tools/build_discovery.py'),'--base-url','https://example.github.io/project','--output',str(out)],check=True,capture_output=True)
   self.assertEqual(sorted(p.relative_to(out).as_posix() for p in out.rglob('*') if p.is_file()),['index.html','lv/index.html','questionnaire/index.html','ru/index.html','sitemap.xml'])
   text=(out/'index.html').read_text()
   self.assertIn('<link rel="canonical" href="https://example.github.io/project/">',text)
   self.assertIn('Looking for a depression test?',text)
   self.assertNotIn('Unpublished preview',text)
   self.assertNotIn('<script',text)
   artifact=next((ROOT/'MH_Public_version').glob('*.html'))
   self.assertEqual((out/'questionnaire/index.html').read_bytes(),artifact.read_bytes())
   sitemap=(out/'sitemap.xml').read_text()
   folder='https://drive.google.com/drive/folders/1BUlc5W7tRw06JOUE250wCuTe-1ick9xb'
   urls={'en':'https://example.github.io/project/','lv':'https://example.github.io/project/lv/','ru':'https://example.github.io/project/ru/'}
   for locale,url in urls.items():
    page=(out/({'en':'index.html','lv':'lv/index.html','ru':'ru/index.html'}[locale])).read_text()
    self.assertIn('<html lang="'+locale+'">',page)
    # Landing descriptions follow the verified Drive release while a newer package may be staged.
    active_count=json.loads((ROOT/'project-manifest.json').read_text())['review_distribution']['questions']
    described_counts=re.findall(r'\b(\d+) (?:questions?|jautājumi(?:em)?|вопрос(?:ов|а)?|запитань)\b',page)
    self.assertTrue(described_counts,locale+' needs its questionnaire size description')
    self.assertEqual(set(map(int,described_counts)),{active_count},locale+' published count must match the delivered app')
    self.assertEqual(page.count('<link rel="canonical"'),1)
    self.assertIn('<link rel="canonical" href="'+url+'">',page)
    for alt,target in urls.items():
     self.assertIn('hreflang="'+alt+'" href="'+target+'"',page)
     self.assertIn('href="'+target+'" lang="'+alt+'"',page)
    self.assertIn('hreflang="x-default" href="'+urls['en']+'"',page)
    self.assertEqual(page.count(folder),1)
    self.assertEqual(page.count('data-open-questionnaire'),1)
    self.assertIn('href="https://example.github.io/project/questionnaire/"',page)
    self.assertNotIn('__QUESTIONNAIRE_URL__',page)
    self.assertNotIn('<script',page)
    self.assertNotIn('SHARED_STYLE',page)
    self.assertIn('<meta property="og:url" content="'+url+'">',page)
    self.assertIn('<meta property="og:title"',page)
    self.assertNotIn('noindex',page.lower())
    self.assertIn('<loc>'+url+'</loc>',sitemap)
   self.assertIn('depresijas',(out/'lv/index.html').read_text().lower())
   self.assertIn('депресси',(out/'ru/index.html').read_text().lower())
 def package_fixture(self,folder):
  root=Path(folder)
  shutil.copytree(ROOT/'MH_Public_version',root/'MH_Public_version')
  shutil.copy2(ROOT/'project-manifest.json',root/'project-manifest.json')
  shutil.copytree(ROOT/'docs/discovery-preview',root/'docs/discovery-preview')
  # A new release can legitimately precede Drive verification.
  p=root/'project-manifest.json';doc=json.loads(p.read_text())
  doc['review_distribution']['version']='0.0.0';p.write_text(json.dumps(doc))
  return root
 def test_reject_tampered_or_unsafe_package(self):
  mutations=[lambda x:x['files'][0].update(sha256='0'*64),
             lambda x:x['files'][0].update(bytes=1),
             lambda x:x['files'][0].update(name='../unexpected.html'),
             lambda x:x.update(source_dirty=True),
             lambda x:x.update(version='99.0.0-review+full-bank')]
  for mutate in mutations:
   with self.subTest(mutation=mutate),tempfile.TemporaryDirectory() as tmp:
    root=self.package_fixture(tmp);p=root/'MH_Public_version/manifest.json'
    doc=json.loads(p.read_text());mutate(doc);p.write_text(json.dumps(doc))
    with patch.object(site,'ROOT',root),self.assertRaises(ValueError):site.questionnaire_bytes()
 def test_publication_requires_verified_matching_drive_distribution(self):
  with tempfile.TemporaryDirectory() as tmp:
   root=self.package_fixture(tmp);p=root/'project-manifest.json';doc=json.loads(p.read_text())
   package=json.loads((root/'MH_Public_version/manifest.json').read_text())
   doc['review_distribution'].update(version=package['version'].split('-')[0],source_commit=package['source_commit'],synchronization='VERIFIED: synthetic test fixture',files=package['files'])
   p.write_text(json.dumps(doc));verified=copy.deepcopy(doc)
   with patch.object(site,'ROOT',root):self.assertTrue(site.questionnaire_bytes(require_verified_distribution=True))
   for key,value in [('version','0.0.0'),('source_commit','unshipped-source'),('synchronization','PENDING')]:
    doc=copy.deepcopy(verified);doc['review_distribution'][key]=value;p.write_text(json.dumps(doc))
    with patch.object(site,'ROOT',root):
     self.assertTrue(site.questionnaire_bytes())
     with self.assertRaises(ValueError):site.questionnaire_bytes(require_verified_distribution=True)
   # Ordinary future-release CI must work before the new Drive upload; deployment must not.
   with patch.object(site,'ROOT',root):
    site.build('https://example.github.io/project/',root/'preview')
    self.assertEqual((root/'preview/questionnaire/index.html').read_bytes(),site.questionnaire_bytes())
    with self.assertRaises(ValueError):site.build('https://example.github.io/project/',root/'blocked',require_verified_distribution=True)
    self.assertFalse((root/'blocked').exists())
 def test_reject_overwrite(self):
  with tempfile.TemporaryDirectory() as tmp:
   out=Path(tmp)/'site';out.mkdir();(out/'keep.txt').write_text('keep')
   with self.assertRaises(FileExistsError):site.build('https://example.github.io/project/',out)
   self.assertEqual((out/'keep.txt').read_text(),'keep')
 def test_reject_non_https(self):
  with tempfile.TemporaryDirectory() as tmp:
   r=subprocess.run(['python',str(ROOT/'tools/build_discovery.py'),'--base-url','javascript:bad','--output',str(Path(tmp)/'site')],capture_output=True)
   self.assertNotEqual(r.returncode,0)
   self.assertIn(b'Publication URL must be absolute HTTPS',r.stderr)
if __name__=='__main__':unittest.main()
