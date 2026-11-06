#!/usr/bin/env python3
"""Build one deterministic offline HTML prototype from separate module logic and LV/EN/RU text.

Usage: python tools/build_pilot.py
       python tools/build_pilot.py --output /tmp/pilot.html
       python tools/build_pilot.py --full-bank

To add section 21: create src/pilot/modules/21/{logic,lv,en,ru}.json and
add a registry entry. No edits to existing modules, engine, or translator files.
"""
import argparse
import hashlib
import html
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "src" / "pilot"
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
    """Map one frozen LV/EN/RU module entry to the pilot engine's question shape."""
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


def build_bundle(apply_layout=True, full_bank=False):
    registry = read_json(SOURCE / "modules" / "registry.json")
    ui = {}
    for lang in LANGS:
        catalog = read_json(APP / "i18n" / ("ui." + lang + ".json"))
        assert catalog["lang"] == lang
        ui[lang] = catalog["strings"]
        medicine = read_json(APP / "i18n" / ("medicine." + lang + ".json"))
        if medicine.get("schema") != "medicine-list-ui-v1" or medicine.get("lang") != lang:
            raise ValueError("Wrong medicine-list locale: " + lang)
        ui[lang]["medicine"] = medicine["strings"]
    groups = build_source_groups() if full_bank else []
    group_ids = set()
    ids, orders = set(), set()
    if full_bank:
        for group in groups:
            group_ids.add(group["id"])
            for question in group["questions"]:
                ids.add(question["id"])
                orders.add(question["order"])
    for group in ([] if full_bank else registry["groups"]):
        key = group["id"]
        if not isinstance(key, str) or not key.isalnum() or key in group_ids:
            raise ValueError(f"Invalid or duplicate module ID: {key}")
        group_ids.add(key)
        folder = SOURCE / "modules" / key
        logic = read_json(folder / "logic.json")
        if logic["group"] != key:
            raise ValueError("Wrong module ID in " + key)
        local = {lang: read_json(folder / (lang + ".json")) for lang in LANGS}
        questions = []
        for q in logic["questions"]:
            qid = q["id"]
            if qid in ids or q["order"] in orders:
                raise ValueError("Duplicate ID/order: " + qid)
            ids.add(qid)
            orders.add(q["order"])
            clone = dict(q)
            clone["module"] = key
            clone["translations"] = {}
            for lang in LANGS:
                localized = local[lang]
                if localized["module"] != key or localized["lang"] != lang:
                    raise ValueError("Wrong locale module/language " + key + " " + lang)
                t = localized["questions"].get(qid)
                if not isinstance(t, dict) or not t.get("title"):
                    raise ValueError("Missing title " + qid + " / " + lang)
                if set(t["choices"]) != set(q["choiceCodes"]):
                    raise ValueError("Incorrect answer codes " + qid + " / " + lang)
                clone["translations"][lang] = t
            questions.append(clone)
        for lang in LANGS:
            if set(local[lang]["questions"]) != {q["id"] for q in questions}:
                raise ValueError("Missing/extra translation IDs: " + key + "/" + lang)
        titles = {lang: local[lang]["title"] for lang in LANGS}
        if not all(isinstance(t, str) and t.strip() for t in titles.values()):
            raise ValueError("Missing section title: " + key)
        if len(questions) != group["question_count"]:
            raise ValueError("Question count mismatch: " + key)
        groups.append({"id": key, "titles": titles,
                       "concerns": {lang: local[lang].get("concern", titles[lang]) for lang in LANGS}, "required": bool(group["required"]), "questions": questions})
    by_id = {q["id"]: q for group in groups for q in group["questions"]}
    for group in groups:
        for q in group["questions"]:
            context = q.get("context")
            if context and context.get("id") not in ids:
                raise ValueError("Unresolved condition " + q["id"])
            if context and by_id[context["id"]]["order"] >= q["order"]:
                raise ValueError("Condition must reference an earlier question: " + q["id"])
    layout = read_json(QUESTIONNAIRE / "layout.json")
    presentation = read_json(QUESTIONNAIRE / "presentation.json")
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
    full_order = layout.get("full_order", [])
    topic_order = presentation.get("topicOrder", [])
    full_module_ids = {f"{number:02d}" for number in range(1, 49)}
    if (len(full_order) != 48 or len(set(full_order)) != 48
            or set(full_order) != full_module_ids
            or len(topic_order) != len(set(topic_order))
            or not set(full_order).issubset(topic_order)):
        raise ValueError("Full report topic order must list each source module exactly once")
    if full_bank and apply_layout:
        by_group = {group["id"]: group for group in groups}
        if set(by_group) != set(full_order):
            raise ValueError("Full navigation order must cover every source module")
        groups = [by_group[key] for key in full_order]
    elif apply_layout:
        # Original files remain storage/source-fidelity units. Presentation topics are separate.
        topics = {}
        for source in groups:
            for q in source["questions"]:
                key = str(q["originModule"]).zfill(2) if source["id"] == "opening" else source["id"]
                if key not in topics:
                    titles = layout["titles"].get(key, source["titles"])
                    topics[key] = {"id": key, "titles": titles, "concerns": titles,
                                   "required": False, "questions": []}
                q["module"] = key
                topics[key]["questions"].append(q)
        order = layout["order"] + [key for key in topics if key not in layout["order"]]
        groups = [topics[key] for key in order if key in topics]
        positions = {q["id"]: i for i, q in enumerate(q for g in groups for q in g["questions"])}
        for g in groups:
            for q in g["questions"]:
                if q.get("context") and positions[q["context"]["id"]] >= positions[q["id"]]:
                    raise ValueError("Presentation must keep parent before follow-up: " + q["id"])
    return {"schema": "offline-questionnaire-full-bank-v1" if full_bank else "offline-questionnaire-pilot-v1",
            **({"build_mode": "full_bank"} if full_bank else {}),
            "version": registry["app_version"] + ("+full-bank" if full_bank else ""),
            "layout_version": layout["version"] + ("-full-bank" if full_bank else ""),
            "legacy_opening_groups": [] if full_bank else layout["legacy_opening_groups"],
            "baseline": registry["baseline"], "ui": ui, "groups": groups,
            "presentation": presentation,
            "release_status": {"lv": "PROTOTYPE", "en": "DRAFT_NOT_RELEASED", "ru": "DRAFT_NOT_RELEASED"}}


def make_html(full_bank=False):
    data = build_bundle(full_bank=full_bank)
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
            '<script id="pilot-data" type="application/json">' + data_json + '</script>'
            '<script>' + reports + '</script><script>' + app + '</script>'
            '</body></html>\n')


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--full-bank", action="store_true",
                        help="Build the separate 712-question prototype instead of the 60-question pilot.")
    parser.add_argument("--output", type=Path, default=None)
    args = parser.parse_args()
    default_name = ("FULL_BANK_offline_LV_EN_RU_NOT_RELEASED.html" if args.full_bank
                    else "PILOT_offline_LV_EN_RU_v0.2_NOT_RELEASED.html")
    output_path = args.output or (ROOT / "dist" / default_name)
    output = make_html(full_bank=args.full_bank).encode("utf-8")
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_bytes(output)
    print("FULL-BANK PROTOTYPE BUILT:" if args.full_bank else "PILOT BUILT:", output_path)
    print("SHA256:", hashlib.sha256(output).hexdigest())
    print("Languages:", ", ".join(LANGS))
    print("PROTOTYPE ONLY: browser, translation, and clinical approval NOT implied.")


if __name__ == "__main__":
    main()

