"""Exercise the real package CLI, byte reproducibility and overwrite guard."""
import hashlib
import io
import json
import subprocess
import sys
import tempfile
import unittest
import zipfile
from pypdf import PdfReader
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "tools"))
from verify_review_package import verify
from build_review_package import guide_pdf


class ReviewPackageTests(unittest.TestCase):
    def test_current_four_language_guide_contains_opening_and_medical_purpose_notice(self):
        guide = (ROOT / "docs/review/GUIDE_LV_EN_RU_UK.md").read_text(encoding="utf-8")
        reader = PdfReader(io.BytesIO(guide_pdf(guide)))
        self.assertEqual(len(reader.pages), 1)
        text = " ".join(" ".join(page.extract_text() for page in reader.pages).split())
        self.assertNotRegex(text, r"(?i)\b(?:AI|Codex|GitHub)\b|https?://|valid|техніч|техническ|тест")
        for heading in ("Latviešu", "English", "Русский", "Українська"):
            self.assertIn(heading, text)
        self.assertEqual(text.count("HTML"), 4)
        for opening in ("atveriet", "open it in your browser", "откройте", "відкрийте"):
            self.assertIn(opening, text)
        for notice in ("neapkopo", "does not collect", "не собирает", "не збирає",
                       "nav paredzēta", "not intended", "не предназначено", "не призначений",
                       "tikai medicīnas speciālists", "Only a medical professional",
                       "только медицинский специалист", "лише медичний фахівець"):
            self.assertIn(notice, text)
        targets = []
        for page in reader.pages:
            for reference in page.get("/Annots", []):
                annotation = reference.get_object()
                if annotation.get("/Subtype") == "/Link":
                    targets.append(annotation.get("/A", {}).get("/URI"))
        self.assertEqual(targets, [])

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

    def test_verifier_rejects_stale_runtime_even_with_matching_recorded_checksum(self):
        with tempfile.TemporaryDirectory() as tmp:
            folder = Path(tmp) / "review"
            self.assertEqual(self.run_builder(folder).returncode, 0)
            manifest = json.loads((folder / "manifest.json").read_text())
            manifest["source_dirty"] = False
            record = next(item for item in manifest["files"] if item["name"].endswith(".html"))
            path = folder / record["name"]
            path.write_bytes(path.read_bytes().replace(b"<script>", b'<script>throw new Error("synthetic stale runtime");', 1))
            record.update(bytes=path.stat().st_size, sha256=hashlib.sha256(path.read_bytes()).hexdigest())
            (folder / "manifest.json").write_text(json.dumps(manifest))
            with self.assertRaisesRegex(AssertionError, "runtime/styles differ"):
                verify(folder)

    def test_verifier_rejects_stale_guide_even_with_matching_recorded_checksum(self):
        with tempfile.TemporaryDirectory() as tmp:
            folder = Path(tmp) / "review"
            self.assertEqual(self.run_builder(folder).returncode, 0)
            manifest = json.loads((folder / "manifest.json").read_text())
            manifest["source_dirty"] = False
            record = next(item for item in manifest["files"] if item["name"].endswith(".pdf"))
            path = folder / record["name"]
            path.write_bytes(guide_pdf("# English\n\nSynthetic obsolete guide instructions."))
            record.update(bytes=path.stat().st_size, sha256=hashlib.sha256(path.read_bytes()).hexdigest())
            (folder / "manifest.json").write_text(json.dumps(manifest))
            with self.assertRaisesRegex(AssertionError, "PDF differs from current guide"):
                verify(folder)

    def test_verifier_requires_one_html_and_one_pdf(self):
        with tempfile.TemporaryDirectory() as tmp:
            folder = Path(tmp) / "review"
            self.assertEqual(self.run_builder(folder).returncode, 0)
            manifest = json.loads((folder / "manifest.json").read_text())
            html = next(item for item in manifest["files"] if item["name"].endswith(".html"))
            (folder / "duplicate.html").write_bytes((folder / html["name"]).read_bytes())
            manifest.update(source_dirty=False, files=[html, {**html, "name": "duplicate.html"}])
            (folder / "manifest.json").write_text(json.dumps(manifest))
            with self.assertRaisesRegex(AssertionError, "one HTML and one PDF"):
                verify(folder)


if __name__ == "__main__":
    unittest.main()
