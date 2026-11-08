"""Regression coverage for adding a locale without editing questionnaire modules."""

from pathlib import Path
import subprocess
import sys
import unittest
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "tools"))
import build_questionnaire as build


class TranslationPackTests(unittest.TestCase):
    def build_with_ukrainian(self):
        config = build.QUESTIONNAIRE / "candidates" / "v0.2.1-review.json"
        bundle = build.build_bundle(config_path=config)
        self.assertEqual(bundle["version"], "0.2.1-review+full-bank")
        return bundle

    def test_disabled_pack_is_never_read(self):
        with patch.object(build, "apply_translation_packs") as load:
            default = build.build_bundle()
        load.assert_not_called()
        self.assertEqual(list(default["ui"]), ["lv", "en", "ru"])
        self.assertNotIn("languageNames", default)

    def test_adding_pack_only_adds_localized_data(self):
        default = build.build_bundle()
        enabled = self.build_with_ukrainian()
        enabled["version"] = default["version"]
        self.assertEqual(enabled.pop("languageNames"), {"uk": "Українська"})
        self.assertEqual(enabled["release_status"].pop("uk"), "DRAFT_NOT_RELEASED")
        ui = enabled["ui"].pop("uk")
        self.assertIn("Почати", ui["start"])
        self.assertEqual(set(ui["medicine"]["fields"]), set(default["ui"]["lv"]["medicine"]["fields"]))
        count = 0
        for group in enabled["groups"]:
            self.assertTrue(group["titles"].pop("uk"))
            self.assertIs(group["concerns"], group["titles"])
            for q in group["questions"]:
                wording = q["translations"].pop("uk")
                self.assertEqual(list(wording["choices"]), q["choiceCodes"])
                self.assertTrue(wording["title"])
                count += 1
        for rule in enabled["presentation"]["questions"].values():
            if "labels" in rule:
                self.assertTrue(rule["labels"].pop("uk"))
        self.assertEqual(count, 712)
        self.assertEqual(enabled, default)

    def test_stale_pack_is_rejected(self):
        sys.path.insert(0, str(ROOT))
        from translations import workspace
        read = workspace.read_json

        def stale_pack(path):
            data = read(path)
            if path == ROOT / "translations" / "uk" / "questions" / "01.json":
                data["source_sha256"] = "stale"
            return data

        with patch.object(workspace, "read_json", side_effect=stale_pack):
            with self.assertRaisesRegex(ValueError, "Latvian source hash differs"):
                self.build_with_ukrainian()

    def test_catalog_keys_and_placeholders_must_match(self):
        reference = {"text": "Example {count}"}
        for invalid in ({"text": "Missing marker"}, {"text": "Value {count}", "extra": "?"}, {"text": ["Example {count}"]}):
            with self.subTest(invalid=invalid), self.assertRaises(ValueError):
                build.check_catalog(reference, invalid, "test")

    def test_candidate_rejects_arbitrary_paths(self):
        for args, expected in (
            (["--candidate", "../build"], "Invalid candidate name"),
            (["--candidate", "v0.2.1-review", "--output", "unused.html"], "not allowed with argument"),
        ):
            with self.subTest(args=args):
                result = subprocess.run(
                    [sys.executable, str(ROOT / "tools" / "build_questionnaire.py"), *args],
                    capture_output=True,
                    text=True,
                )
                self.assertNotEqual(result.returncode, 0)
                self.assertIn(expected, result.stderr)

    def test_test_build_rejects_custom_output(self):
        result = subprocess.run(
            [sys.executable, str(ROOT / "tools" / "build_questionnaire.py"),
             "--translation-pack-test", "--output", "unused.html"],
            capture_output=True,
            text=True,
        )
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("not allowed with argument", result.stderr)


if __name__ == "__main__":
    unittest.main()
