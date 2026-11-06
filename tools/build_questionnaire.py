#!/usr/bin/env python3
"""Build the complete offline questionnaire from separate app and question sources.

Usage: python tools/build_questionnaire.py
       python tools/build_questionnaire.py --output /tmp/questionnaire.html
"""
import argparse
import hashlib
import html
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
APP = ROOT / "src" / "app"
QUESTIONNAIRE = ROOT / "src" / "questionnaire"
LANGS = ("lv", "en", "ru")


def read_json(path):
    return json.loads(path.read_text(encoding="utf-8"))


def load_module_titles():
    """Load exact frozen section headings for the full-bank module selector."""
    result = {}
    expected = [f"{number:02d}" for number in range(1, 49)]
    for lang in LANGS:
        catalog = read_json(QUESTIONNAIRE / "i18n" / ("module-titles." + lang + ".json"))
        titles = catalog.get("titles")
        if (catalog.get("schema") != "frozen-module-titles-v1" or catalog.get("lang") != lang
                or not isinstance(titles, dict) or list(titles) != expected
                or not all(isinstance(title, str) and title.strip() for title in titles.values())):
            raise ValueError("Invalid full-bank module titles: " + lang)
        result[lang] = titles
    return result


def adapt_source_entry(entry):
    """Map one frozen LV/EN/RU module entry to the shared engine's question shape."""
    lv = entry["lv"]
    section = lv["section"]
    q = {
        "id": lv["id"],
        "order": entry["order"],
        "module": str(section).zfill(2),
        "originModule": section,
        "section": section,
        "profile": lv["profile"],
        "multi": lv["multi"],
        "context": lv["context"],
        "choiceCodes": list(lv["choices"]),
        "exclusive": lv["exclusive"],
        "incompatible": lv["incompatible"],
        "answerStatus": lv["answerStatus"],
        "type": lv.get("type", "choice"),
        "translations": {},
    }
    if "maxChoices" in lv:
        q["maxChoices"] = lv["maxChoices"]
    if "help" in lv:
        q["help"] = lv["help"]
    for lang in LANGS:
        source = lv if lang == "lv" else entry[lang]
        translation = {
            "title": source["title"],
            "time": source["time"],
            "choices": source["choices"],
        }
        if "help" in source:
            translation["help"] = source["help"]
        q["translations"][lang] = translation
    return q


def build_source_groups():
    """Build optional engine groups directly from the immutable 48-module bank."""
    titles = load_module_titles()
    files = sorted((ROOT / "src" / "modules").glob("182_MODULE_*_LV_EN_RU_v16.json"))
    if len(files) != 48:
        raise ValueError(f"Expected 48 original module files; found {len(files)}")
    groups = {}
    ids, orders = set(), set()
    for expected_section, path in enumerate(files, 1):
        module = read_json(path)
        section = module.get("section")
        if (module.get("schema") != "question-module-bundle-v1" or section != expected_section
                or module.get("count") != len(module.get("entries", []))):
            raise ValueError("Invalid source module: " + path.name)
        for lang in LANGS:
            if module["published_status"].get(lang) not in ("v16", "draft-not-reviewed"):
                raise ValueError("Unknown source language status: " + lang)
        for entry in module["entries"]:
            q = adapt_source_entry(entry)
            if q["id"] in ids or q["order"] in orders:
                raise ValueError("Duplicate full-bank ID/order: " + q["id"])
            ids.add(q["id"]);orders.add(q["order"])
            key = q["module"]
            if key not in groups:
                group_titles = {lang: titles[lang][key] for lang in LANGS}
                groups[key] = {"id": key, "titles": group_titles, "concerns": group_titles,
                               "required": False, "questions": []}
            groups[key]["questions"].append(q)
    by_id = {q["id"]: q for group in groups.values() for q in group["questions"]}
    for group in groups.values():
        for q in group["questions"]:
            context = q.get("context")
            if context and (context["id"] not in by_id or by_id[context["id"]]["order"] >= q["order"]):
                raise ValueError("Invalid source condition: " + q["id"])
    expected_groups = {f"{number:02d}" for number in range(1, 49)}
    if set(groups) != expected_groups or len(ids) != 712:
        raise ValueError(f"Full-bank count/group mismatch: {len(groups)} groups, {len(ids)} questions")
    return [groups[key] for key in sorted(groups)]


def contains_weight_key(value):
    if isinstance(value, dict):
        return any("weight" in key.lower() or contains_weight_key(item)
                   for key, item in value.items())
    if isinstance(value, list):
        return any(contains_weight_key(item) for item in value)
    return False


def build_bundle():
    """Assemble the complete 48-section bank without copying question sources."""
    config = read_json(QUESTIONNAIRE / "build.json")
    if config.get("schema") != "questionnaire-build-v1":
        raise ValueError("Invalid questionnaire build configuration")
    ui = {}
    for lang in LANGS:
        catalog = read_json(APP / "i18n" / ("ui." + lang + ".json"))
        if catalog.get("lang") != lang:
            raise ValueError("Wrong interface locale: " + lang)
        ui[lang] = catalog["strings"]
        medicine = read_json(APP / "i18n" / ("medicine." + lang + ".json"))
        if medicine.get("schema") != "medicine-list-ui-v1" or medicine.get("lang") != lang:
            raise ValueError("Wrong medicine-list locale: " + lang)
        ui[lang]["medicine"] = medicine["strings"]

    groups = build_source_groups()
    by_id = {q["id"]: q for group in groups for q in group["questions"]}
    layout = read_json(QUESTIONNAIRE / "layout.json")
    presentation = read_json(QUESTIONNAIRE / "presentation.json")
    if (layout.get("schema") != "questionnaire-layout-v1"
            or presentation.get("schema") != "questionnaire-presentation-v1"):
        raise ValueError("Invalid questionnaire presentation configuration")
    if contains_weight_key(presentation):
        raise ValueError("Weight metadata is no longer supported")
    contact = presentation.get("feedbackContactEmail", "")
    if not isinstance(contact, str) or not re.fullmatch(r"[^\s@]+@[^\s@]+\.[^\s@]+", contact):
        raise ValueError("A valid project-feedback contact email is required")
    for qid, rule in presentation["questions"].items():
        if qid not in by_id:
            raise ValueError("Presentation references an unknown question: " + qid)
        q = by_id[qid]
        if "labels" in rule and set(rule["labels"]) != set(LANGS):
            raise ValueError("Missing report label language: " + qid)
        if any(code not in q["choiceCodes"] or level not in ("support", "emergency")
               for code, level in rule.get("support", {}).items()):
            raise ValueError("Invalid support trigger: " + qid)
    for qid, codes in presentation.get("boldAnswers", {}).items():
        if qid not in by_id or not isinstance(codes, list) or not codes:
            raise ValueError("Invalid bold-answer question: " + qid)
        if len(set(codes)) != len(codes) or any(code not in by_id[qid]["choiceCodes"] for code in codes):
            raise ValueError("Invalid bold-answer code: " + qid)

    module_ids = {f"{number:02d}" for number in range(1, 49)}
    full_order = layout.get("full_order", [])
    topic_order = presentation.get("topicOrder", [])
    if (len(full_order) != 48 or len(set(full_order)) != 48 or set(full_order) != module_ids
            or len(topic_order) != 48 or len(set(topic_order)) != 48 or set(topic_order) != module_ids):
        raise ValueError("Navigation and report order must list each source module exactly once")
    by_group = {group["id"]: group for group in groups}
    groups = [by_group[key] for key in full_order]
    positions = {q["id"]: index for index, q in enumerate(
        question for group in groups for question in group["questions"])}
    for qid, q in by_id.items():
        if q.get("context") and positions[q["context"]["id"]] >= positions[qid]:
            raise ValueError("Navigation must keep condition parent before follow-up: " + qid)

    return {
        "schema": "offline-questionnaire-full-bank-v1",
        "version": config["version"],
        "layout_version": layout["version"] + "-full-bank",
        "legacy_opening_groups": [],
        "baseline": config["baseline"],
        "ui": ui,
        "groups": groups,
        "presentation": presentation,
        "release_status": {"lv": "PROTOTYPE", "en": "DRAFT_NOT_RELEASED", "ru": "DRAFT_NOT_RELEASED"},
    }

def make_html():
    data = build_bundle()
    style = (APP / "core" / "styles.css").read_text(encoding="utf-8")
    reports = (APP / "reports" / "reports.js").read_text(encoding="utf-8")
    app = (APP / "core" / "app.js").read_text(encoding="utf-8")
    data_json = json.dumps(data, ensure_ascii=False, separators=(",", ":"))
    # Never allow JSON values to prematurely terminate their script tag.
    data_json = data_json.replace("<", "\\u003c").replace(">", "\\u003e")
    return ('<!doctype html><html lang="lv"><head><meta charset="utf-8">'
            '<meta name="viewport" content="width=device-width, initial-scale=1">'
            '<meta http-equiv="Content-Security-Policy" content="default-src &#39;none&#39;; '
            'script-src &#39;unsafe-inline&#39;; style-src &#39;unsafe-inline&#39;; '
            'img-src data:; connect-src &#39;none&#39;; form-action &#39;none&#39;; '
            'base-uri &#39;none&#39;; object-src &#39;none&#39;">'
            '<meta name="project-status" content="TEST ONLY — not clinically validated">'
            '<title>' + html.escape(data["ui"]["lv"]["project"]) + '</title>'
            '<style>' + style + '</style></head><body><div id="app"></div>'
            '<script id="questionnaire-data" type="application/json">' + data_json + '</script>'
            '<script>' + reports + '</script><script>' + app + '</script>'
            '</body></html>\n')


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=None)
    args = parser.parse_args()
    output_path = args.output or (ROOT / "dist" / "QUESTIONNAIRE_LV_EN_RU_NOT_RELEASED.html")
    output = make_html().encode("utf-8")
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_bytes(output)
    print("COMPLETE QUESTIONNAIRE BUILT:", output_path)
    print("SHA256:", hashlib.sha256(output).hexdigest())
    print("Languages:", ", ".join(LANGS))
    print("PROTOTYPE ONLY: browser, translation, and clinical approval NOT implied.")


if __name__ == "__main__":
    main()

