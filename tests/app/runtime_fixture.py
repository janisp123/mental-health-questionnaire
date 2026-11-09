"""Small synthetic bundle for isolated offline browser checks."""
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "tools"))
import build_questionnaire as build

PACKS = json.loads((ROOT / "src/questionnaire/build.json").read_text())["translationPacks"]
LOCALES = (*build.SOURCE_LANGS, *PACKS)

def catalog_path(stem, lang):
    return ROOT / "src/app/i18n" / f"{stem}.{lang}.json" if lang in build.SOURCE_LANGS else ROOT / "translations" / lang / f"{stem}.json"


def _question(qid, title, codes, *, multi=False, max_choices=None, context=None, module="S01"):
    translations = {
        lang: {"title": title, "time": "", "choices": {code: f"Option {code}" for code in codes}}
        for lang in LOCALES
    }
    question = {
        "id": qid, "module": module, "multi": multi, "context": context,
        "choiceCodes": codes, "exclusive": [], "incompatible": [],
        "answerStatus": {}, "type": "choice", "translations": translations,
    }
    if max_choices is not None:
        question["maxChoices"] = max_choices
    return question


def make_fixture():
    ui = {}
    for lang in LOCALES:
        ui[lang] = json.loads(catalog_path("ui", lang).read_text(encoding="utf-8"))["strings"]
        ui[lang]["medicine"] = json.loads(catalog_path("medicine", lang).read_text(encoding="utf-8"))["strings"]
    titles = {"lv": "Sintētiska sadaļa", "en": "Synthetic section", "ru": "Тестовый раздел", "uk": "Тестовий розділ"}
    group = {
        "id": "S01", "required": False, "questionCount": 3, "titles": titles, "concerns": titles,
        "questions": [
            _question("SYN_01", "Single choice", ["A", "B"]),
            _question("SYN_02", "Multiple choice", ["A", "B", "C", "D"], multi=True, max_choices=3),
            _question("SYN_03", "Conditional follow-up", ["A"], context={"id": "SYN_01", "showValues": ["B"]}),
        ],
    }
    next_titles = {"lv": "Nākamā sintētiskā sadaļa", "en": "Next synthetic section", "ru": "Следующий тестовый раздел", "uk": "Наступний тестовий розділ"}
    next_group = {
        "id": "S02", "required": False, "questionCount": 1,
        "titles": next_titles, "concerns": next_titles,
        "questions": [_question("SYN_04", "Next section", ["A", "B"], module="S02")],
    }
    return {
        "schema": "offline-questionnaire-full-bank-v1", "version": "synthetic-test",
        "languageNames": PACKS,
        "layout_version": "synthetic-test", "legacy_opening_groups": [], "ui": ui,
        "groups": [group, next_group],
        "source_module_to_section": {"01":"S01"}, "previous_layout_versions": [],
        "presentation": {"questions": {}, "boldAnswers": {}, "topicOrder": ["S01", "S02"], "feedbackContactEmail": "test@example.invalid"},
    }


def write_fixture(path):
    path.write_text(build.make_html(make_fixture()), encoding="utf-8")
