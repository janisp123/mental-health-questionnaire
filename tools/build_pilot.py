#!/usr/bin/env python3
"""Build one deterministic offline HTML prototype from separate module logic and LV/EN/RU text.

Usage: python tools/build_pilot.py
       python tools/build_pilot.py --output /tmp/pilot.html

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
LANGS = ("lv", "en", "ru")


def read_json(path):
    return json.loads(path.read_text(encoding="utf-8"))


def contains_weight_key(value):
    if isinstance(value, dict):
        return any("weight" in key.lower() or contains_weight_key(item)
                   for key, item in value.items())
    if isinstance(value, list):
        return any(contains_weight_key(item) for item in value)
    return False


def build_bundle(apply_layout=True):
    registry = read_json(SOURCE / "modules" / "registry.json")
    ui = {}
    for lang in LANGS:
        catalog = read_json(SOURCE / "i18n" / ("ui." + lang + ".json"))
        assert catalog["lang"] == lang
        ui[lang] = catalog["strings"]
    groups = []
    group_ids = set()
    ids, orders = set(), set()
    for group in registry["groups"]:
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
    layout = read_json(SOURCE / "modules" / "layout.json")
    presentation = read_json(SOURCE / "reports" / "presentation.json")
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
    if set(presentation.get("topicOrder", [])) != set(layout["order"]):
        raise ValueError("Report topic order must list each display topic exactly once")
    if apply_layout:
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
    return {"schema": "offline-questionnaire-pilot-v1", "version": registry["app_version"],
            "layout_version": layout["version"], "legacy_opening_groups": layout["legacy_opening_groups"],
            "baseline": registry["baseline"], "ui": ui, "groups": groups,
            "presentation": presentation,
            "release_status": {"lv": "PROTOTYPE", "en": "DRAFT_NOT_RELEASED", "ru": "DRAFT_NOT_RELEASED"}}


def make_html():
    data = build_bundle()
    style = (SOURCE / "core" / "styles.css").read_text(encoding="utf-8")
    reports = (SOURCE / "reports" / "reports.js").read_text(encoding="utf-8")
    app = (SOURCE / "core" / "app.js").read_text(encoding="utf-8")
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
    parser.add_argument("--output", type=Path, default=ROOT / "dist" / "PILOT_offline_LV_EN_RU_v0.2_NOT_RELEASED.html")
    args = parser.parse_args()
    output = make_html().encode("utf-8")
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_bytes(output)
    print("PILOT BUILT:", args.output)
    print("SHA256:", hashlib.sha256(output).hexdigest())
    print("Languages:", ", ".join(LANGS))
    print("PROTOTYPE ONLY: browser, translation, and clinical approval NOT implied.")


if __name__ == "__main__":
    main()

