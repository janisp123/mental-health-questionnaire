"""Exercise the real package CLI, byte reproducibility and overwrite guard."""
import hashlib
import json
import subprocess
import sys
import tempfile
import unittest
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


class ReviewPackageTests(unittest.TestCase):
    def run_builder(self, destination):
        return subprocess.run([sys.executable, str(ROOT / "tools/build_review_package.py"),
                               "--output-dir", str(destination)], cwd=ROOT, capture_output=True, text=True)

    def test_package_contains_matching_offline_html_and_four_language_pdf(self):
        with tempfile.TemporaryDirectory() as tmp:
            folder = Path(tmp) / "review"
            result = self.run_builder(folder)
            self.assertEqual(result.returncode, 0, result.stderr)
            manifest = json.loads((folder / "manifest.json").read_text())
            self.assertEqual(manifest["languages"], ["lv", "en", "ru", "uk"])
            self.assertEqual(manifest["question_count"], 712)
            self.assertEqual(len(manifest["files"]), 2)
            self.assertEqual(len(manifest["source_commit"]), 40)
            for record in manifest["files"]:
                content = (folder / record["name"]).read_bytes()
                self.assertEqual(hashlib.sha256(content).hexdigest(), record["sha256"])
                self.assertEqual(len(content), record["bytes"])
            html = next(record for record in manifest["files"] if record["name"].endswith(".html"))
            self.assertIn(b'connect-src &#39;none&#39;', (folder / html["name"]).read_bytes())
            pdf = next(record for record in manifest["files"] if record["name"].endswith(".pdf"))
            self.assertTrue((folder / pdf["name"]).read_bytes().startswith(b"%PDF-"))
            with zipfile.ZipFile(folder / manifest["zip"]["name"]) as archive:
                self.assertEqual(sorted(archive.namelist()), sorted(record["name"] for record in manifest["files"]))
                self.assertIsNone(archive.testzip())
                for record in manifest["files"]:
                    self.assertEqual(archive.read(record["name"]), (folder / record["name"]).read_bytes())

    def test_two_builds_have_identical_pdf_html_zip_and_manifest(self):
        with tempfile.TemporaryDirectory() as tmp:
            a, b = Path(tmp) / "a", Path(tmp) / "b"
            for folder in (a, b):
                result = self.run_builder(folder)
                self.assertEqual(result.returncode, 0, result.stderr)
            self.assertEqual(sorted(p.name for p in a.iterdir()), sorted(p.name for p in b.iterdir()))
            for p in a.iterdir():
                self.assertEqual(p.read_bytes(), (b / p.name).read_bytes(), p.name)

    def test_existing_package_is_never_overwritten(self):
        with tempfile.TemporaryDirectory() as tmp:
            folder = Path(tmp) / "existing"
            folder.mkdir()
            sentinel = folder / "keep.txt"
            sentinel.write_text("previous package")
            result = self.run_builder(folder)
            self.assertNotEqual(result.returncode, 0)
            self.assertIn("Output directory already exists", result.stderr)
            self.assertEqual(sentinel.read_text(), "previous package")
            self.assertEqual(list(folder.iterdir()), [sentinel])


if __name__ == "__main__":
    unittest.main()
