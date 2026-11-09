"""Regressions for the four-language current app's phone layout and locale changes."""
import json
import io
import tempfile
import unittest
from pathlib import Path
from pypdf import PdfReader

from playwright.sync_api import sync_playwright
from browser_helpers import act, backup, launch, open_page, restore
import build_questionnaire as build


class CandidateQATests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.tmp = tempfile.TemporaryDirectory()
        cls.path = Path(cls.tmp.name) / "candidate.html"
        cls.data = build.build_bundle()
        cls.path.write_text(build.make_html(cls.data), encoding="utf-8")
        cls.pw = sync_playwright().start()
        cls.browser = launch(cls.pw)

    @classmethod
    def tearDownClass(cls):
        cls.browser.close()
        cls.pw.stop()
        cls.tmp.cleanup()

    def setUp(self):
        self.page, self.errors, self.network = open_page(self.browser, self.path)

    def tearDown(self):
        self.assertEqual(self.errors, [])
        self.assertEqual(self.network, [])
        self.page.close()

    def restore_question(self, qid, lang="en", feedback=None):
        restore(self.page, {
            "schema": "mental-pilot-recovery-v1", "layoutVersion": self.data["layout_version"],
            "answers": {}, "feedback": feedback or {}, "lang": lang,
            "selected": [group["id"] for group in self.data["groups"]],
            "sectionConfirmed": True, "currentId": qid,
        })
        self.assertEqual(self.page.locator(".question").get_attribute("data-question"), qid)

    def test_medication_controls_fit_phone_card_in_every_language(self):
        for width in (320, 390):
            self.page.set_viewport_size({"width": width, "height": 844})
            for lang in ("lv", "en", "ru", "uk"):
                with self.subTest(width=width, lang=lang):
                    self.restore_question("M14_02", lang)
                    self.assert_controls_fit()

    def assert_controls_fit(self):
        dimensions = self.page.locator(".question").evaluate("""card => {
            const bounds=card.getBoundingClientRect();
            return {width:card.clientWidth,content:card.scrollWidth,
                outside:[...card.querySelectorAll('input,select,textarea,button')].filter(el=>{
                    const r=el.getBoundingClientRect();
                    return r.width && (r.left<bounds.left || r.right>bounds.right);
                }).map(el=>el.tagName)};
        }""")
        self.assertLessEqual(dimensions["content"], dimensions["width"] + 1)
        self.assertEqual(dimensions["outside"], [])

    def test_long_russian_titles_keep_feedback_flag_inside_phone_card(self):
        self.page.set_viewport_size({"width": 320, "height": 844})
        for qid in ("M16_08", "M17_03", "M17_08", "M01_05", "M01_13", "M25_07", "M15_09"):
            with self.subTest(qid=qid):
                self.restore_question(qid, "ru")
                self.assert_controls_fit()

    def test_unsent_feedback_survives_repeated_language_changes_without_submission(self):
        self.restore_question("M23_11")
        act(self.page, "feedback")
        self.page.locator('[data-feedback-reason="question"]').check()
        self.page.locator("#feedback-comment").fill("Synthetic unsent correction")
        for lang in ("uk", "ru", "lv", "en"):
            self.page.select_option("#language", lang)
            self.assertEqual(self.page.locator("#feedback-comment").input_value(), "Synthetic unsent correction")
            self.assertTrue(self.page.locator('[data-feedback-reason="question"]').is_checked())
        self.assertEqual(backup(self.page)["feedback"], {})
        act(self.page, "results")
        act(self.page, "doctor")
        self.assertNotIn("Synthetic unsent correction", self.page.locator(".report-preview").inner_text())
        self.assertEqual(self.page.locator('[data-act="feedbackReport"]').count(), 0)
        act(self.page, "resultScreen")
        act(self.page, "back")
        # A backup re-render must also preserve the pending correction.
        self.assertEqual(self.page.locator("#feedback-comment").input_value(), "Synthetic unsent correction")
        act(self.page, "feedbackContinue")
        saved = backup(self.page)
        self.assertEqual(saved["feedback"]["M23_11"]["comment"], "Synthetic unsent correction")
        self.assertEqual(saved["feedback"]["M23_11"]["reasons"], ["question"])
        # Editing already saved feedback must not overwrite it until submitted.
        self.restore_question("M23_11", feedback=saved["feedback"])
        act(self.page, "feedback")
        self.page.locator("#feedback-comment").fill("")
        self.page.locator('[data-feedback-reason="question"]').uncheck()
        self.page.locator('[data-feedback-reason="language"]').check()
        self.page.select_option("#language", "uk")
        self.assertEqual(self.page.locator("#feedback-comment").input_value(), "")
        self.assertFalse(self.page.locator('[data-feedback-reason="question"]').is_checked())
        self.assertTrue(self.page.locator('[data-feedback-reason="language"]').is_checked())
        still_saved = backup(self.page)["feedback"]["M23_11"]
        self.assertEqual(still_saved["comment"], "Synthetic unsent correction")
        self.assertEqual(still_saved["reasons"], ["question"])
        act(self.page, "feedbackContinue")
        updated = backup(self.page)["feedback"]["M23_11"]
        self.assertEqual(updated["comment"], "")
        self.assertEqual(updated["reasons"], ["language"])
        self.assertEqual(updated["language"], "uk")

    def test_clinician_heading_uses_report_language(self):
        self.restore_question("M23_11", "uk", feedback={"M23_11": {
            "reasons": ["question"], "comment": "Synthetic saved feedback", "language": "uk",
            "version": self.data["version"], "updatedAt": "2026-11-09T07:30:00Z",
        }})
        act(self.page, "results")
        for lang in ("lv", "en", "ru", "uk"):
            with self.subTest(lang=lang):
                self.page.select_option("#report-language", lang)
                act(self.page, "doctor")
                try:
                    self.assertEqual(self.page.locator(".report-page>h2").inner_text(), self.data["ui"][lang]["doctorHeading"])
                    self.assertEqual(self.page.locator(".report-preview").get_attribute("lang"), lang)
                    act(self.page, "feedbackReport")
                    self.assertEqual(self.page.locator(".report-preview").get_attribute("lang"), "uk")
                    self.assertIn("Synthetic saved feedback", self.page.locator(".report-preview").inner_text())
                finally:
                    act(self.page, "resultScreen")

    def test_three_language_progress_import_and_ukrainian_round_trip(self):
        payload = json.loads((build.ROOT / "tests/fixtures/recovery-three-language.json").read_text(encoding="utf-8"))
        restore(self.page, payload)
        saved = backup(self.page)
        self.assertEqual(saved["answers"]["M23_11"]["codes"], ["A", "B"])
        self.assertEqual(saved["answers"]["M33_01"]["value"], "Synthetic legacy text — синтетичний запис")
        self.assertEqual(saved["feedback"]["M23_11"]["language"], "ru")
        self.page.select_option("#language", "uk")
        act(self.page, "feedback")
        self.page.locator("#feedback-comment").fill("Синтетичне зауваження")
        act(self.page, "feedbackContinue")
        ukrainian = backup(self.page)
        self.assertEqual(ukrainian["lang"], "uk")
        self.assertEqual(ukrainian["feedback"]["M23_11"]["language"], "uk")
        self.assertEqual(ukrainian["feedback"]["M23_11"]["comment"], "Синтетичне зауваження")
        restore(self.page, ukrainian)
        readback = backup(self.page)
        self.assertEqual(readback["answers"], ukrainian["answers"])
        self.assertEqual(readback["feedback"], ukrainian["feedback"])

    def test_source_link_is_localized_in_about_and_absent_from_answer_report_pdf(self):
        source = "https://github.com/janisp123/mental-health-questionnaire"
        labels = {"lv": "Pirmkods un izstrāde (GitHub)", "en": "Source code and development (GitHub)",
                  "ru": "Исходный код и разработка (GitHub)", "uk": "Початковий код і розробка (GitHub)"}
        for lang, label in labels.items():
            self.page.select_option("#language", lang)
            about = self.page.locator("#project-information")
            self.assertEqual(about.count(), 1)
            about.locator("summary").click()
            link = about.get_by_role("link", name=label, exact=True)
            self.assertTrue(link.is_visible())
            self.assertEqual(link.get_attribute("href"), source)
            self.assertEqual(link.get_attribute("target"), "_blank")
            self.assertIn("noreferrer", link.get_attribute("rel"))
            self.assertIn("noopener", link.get_attribute("rel"))
        act(self.page, "start")
        act(self.page, "all")
        self.assertEqual(self.page.locator(".question a[data-project-source]").count(), 0)
        act(self.page, "results")
        act(self.page, "doctor")
        self.assertNotIn("github.com/janisp123", self.page.locator(".report-preview").inner_text())
        reader = PdfReader(io.BytesIO(self.page.pdf(format="A4")))
        for page in reader.pages:
            self.assertNotIn("github.com/janisp123", page.extract_text())
            for reference in page.get("/Annots", []):
                annotation = reference.get_object()
                self.assertNotEqual(annotation.get("/A", {}).get("/URI"), source)


if __name__ == "__main__":
    unittest.main(argv=[__file__])
