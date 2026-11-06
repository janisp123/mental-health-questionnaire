"""Small synthetic bundle for isolated offline browser checks."""
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "tools"))
import build_questionnaire as build


def _question(qid, title, codes, *, multi=False, context=None):
    translations = {
        lang: {"title": title, "time": "", "choices": {code: f"Option {code}" for code in codes}}
        for lang in ("lv", "en", "ru")
    }
    return {
        "id": qid, "module": "01", "multi": multi, "context": context,
        "choiceCodes": codes, "exclusive": [], "incompatible": [],
        "answerStatus": {}, "type": "choice", "translations": translations,
    }


def make_fixture():
    ui = {}
    for lang in ("lv", "en", "ru"):
        ui[lang] = json.loads((ROOT / "src/app/i18n" / f"ui.{lang}.json").read_text(encoding="utf-8"))["strings"]
        ui[lang]["medicine"] = json.loads((ROOT / "src/app/i18n" / f"medicine.{lang}.json").read_text(encoding="utf-8"))["strings"]
    titles = {"lv": "Sintētiska sadaļa", "en": "Synthetic section", "ru": "Тестовый раздел"}
    group = {
        "id": "01", "required": True, "titles": titles, "concerns": titles,
        "questions": [
            _question("SYN_01", "Single choice", ["A", "B"]),
            _question("SYN_02", "Multiple choice", ["A", "B"], multi=True),
            _question("SYN_03", "Conditional follow-up", ["A"], context={"id": "SYN_01", "showValues": ["B"]}),
        ],
    }
    return {
        "schema": "offline-questionnaire-full-bank-v1", "version": "synthetic-test",
        "layout_version": "synthetic-test", "legacy_opening_groups": [], "ui": ui,
        "groups": [group],
        "presentation": {"questions": {}, "boldAnswers": {}, "topicOrder": ["01"], "feedbackContactEmail": "test@example.invalid"},
    }


def write_fixture(path):
    path.write_text(build.make_html(make_fixture()), encoding="utf-8")
