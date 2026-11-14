"""Publication bundle must expose only the description page and generated sitemap."""
import subprocess,tempfile,unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
class BuildDiscovery(unittest.TestCase):
 def test_page_only_bundle_and_actual_canonical(self):
  with tempfile.TemporaryDirectory() as tmp:
   out=Path(tmp)/'site'
   subprocess.run(['python',str(ROOT/'tools/build_discovery.py'),'--base-url','https://example.github.io/project','--output',str(out)],check=True,capture_output=True)
   self.assertEqual(sorted(p.name for p in out.iterdir()),['index.html','sitemap.xml'])
   text=(out/'index.html').read_text()
   self.assertIn('<link rel="canonical" href="https://example.github.io/project/">',text)
   self.assertIn('Looking for a depression test?',text)
   self.assertNotIn('Unpublished preview',text)
   self.assertNotIn('<script',text)
   self.assertIn('https://example.github.io/project/',(out/'sitemap.xml').read_text())
 def test_reject_non_https(self):
  with tempfile.TemporaryDirectory() as tmp:
   r=subprocess.run(['python',str(ROOT/'tools/build_discovery.py'),'--base-url','javascript:bad','--output',str(Path(tmp)/'site')],capture_output=True)
   self.assertNotEqual(r.returncode,0)
   self.assertIn(b'Publication URL must be absolute HTTPS',r.stderr)
if __name__=='__main__':unittest.main()
