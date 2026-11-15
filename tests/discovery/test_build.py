"""Publication bundle must expose only the description page and generated sitemap."""
import subprocess,tempfile,unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
class BuildDiscovery(unittest.TestCase):
 def test_page_only_bundle_and_actual_canonical(self):
  with tempfile.TemporaryDirectory() as tmp:
   out=Path(tmp)/'site'
   subprocess.run(['python',str(ROOT/'tools/build_discovery.py'),'--base-url','https://example.github.io/project','--output',str(out)],check=True,capture_output=True)
   self.assertEqual(sorted(p.relative_to(out).as_posix() for p in out.rglob('*') if p.is_file()),['index.html','lv/index.html','ru/index.html','sitemap.xml'])
   text=(out/'index.html').read_text()
   self.assertIn('<link rel="canonical" href="https://example.github.io/project/">',text)
   self.assertIn('Looking for a depression test?',text)
   self.assertNotIn('Unpublished preview',text)
   self.assertNotIn('<script',text)
   sitemap=(out/'sitemap.xml').read_text()
   folder='https://drive.google.com/drive/folders/1BUlc5W7tRw06JOUE250wCuTe-1ick9xb'
   urls={'en':'https://example.github.io/project/','lv':'https://example.github.io/project/lv/','ru':'https://example.github.io/project/ru/'}
   for locale,url in urls.items():
    page=(out/({'en':'index.html','lv':'lv/index.html','ru':'ru/index.html'}[locale])).read_text()
    self.assertIn('<html lang="'+locale+'">',page)
    self.assertEqual(page.count('<link rel="canonical"'),1)
    self.assertIn('<link rel="canonical" href="'+url+'">',page)
    for alt,target in urls.items():
     self.assertIn('hreflang="'+alt+'" href="'+target+'"',page)
     self.assertIn('href="'+target+'" lang="'+alt+'"',page)
    self.assertIn('hreflang="x-default" href="'+urls['en']+'"',page)
    self.assertEqual(page.count(folder),1)
    self.assertNotIn('<script',page)
    self.assertNotIn('SHARED_STYLE',page)
    self.assertIn('<meta property="og:url" content="'+url+'">',page)
    self.assertIn('<meta property="og:title"',page)
    self.assertNotIn('noindex',page.lower())
    self.assertIn('<loc>'+url+'</loc>',sitemap)
   self.assertIn('depresijas',(out/'lv/index.html').read_text().lower())
   self.assertIn('депресси',(out/'ru/index.html').read_text().lower())
 def test_reject_non_https(self):
  with tempfile.TemporaryDirectory() as tmp:
   r=subprocess.run(['python',str(ROOT/'tools/build_discovery.py'),'--base-url','javascript:bad','--output',str(Path(tmp)/'site')],capture_output=True)
   self.assertNotEqual(r.returncode,0)
   self.assertIn(b'Publication URL must be absolute HTTPS',r.stderr)
if __name__=='__main__':unittest.main()
