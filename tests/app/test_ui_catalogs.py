"""Interface-label files stay structurally aligned without loading question content."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
LOCALES = ("lv", "en", "ru")


def key_paths(value, prefix=""):
    paths = set()
    for key, child in value.items():
        path = f"{prefix}.{key}" if prefix else key
        paths.add(path)
        if isinstance(child, dict):
            paths.update(key_paths(child, path))
    return paths


for stem in ("ui", "medicine"):
    catalogs = {
        lang: json.loads((ROOT / "src" / "app" / "i18n" / f"{stem}.{lang}.json").read_text(encoding="utf-8"))
        for lang in LOCALES
    }
    expected = key_paths(catalogs["lv"])
    for lang in LOCALES[1:]:
        actual = key_paths(catalogs[lang])
        assert actual == expected, (
            f"{stem}.{lang}.json catalog keys differ: "
            f"missing={sorted(expected - actual)}, extra={sorted(actual - expected)}"
        )

ui = {
    lang: json.loads((ROOT / "src" / "app" / "i18n" / f"ui.{lang}.json").read_text(encoding="utf-8"))["strings"]
    for lang in LOCALES
}
assert all("chooseGuide" not in ui[lang] for lang in LOCALES)
for lang in LOCALES:
    assert not set(("chooseAll", "chooseOwn", "confirmSections", "clearSections", "countSkip", "countOpen", "noAuto", "selected", "notSelected")) & set(ui[lang])
support_phrases = {
    "lv": ("sešciparu", "tikai 6 cipari", "anonimitātes", "darbavietai"),
    "en": ("six-digit", "only six digits", "anonymity", "workplace"),
    "ru": ("шестизначный", "всего 6 цифр", "анонимности", "работодателя"),
}
privacy_phrases = {
    "lv": ("nav šifrēts", "personas datus", "klīniski validēta"),
    "en": ("not encrypted", "personal details", "not clinically validated"),
    "ru": ("не зашифрован", "личные сведения", "клиническую проверку"),
}
for lang in LOCALES:
    strings = ui[lang]
    assert "legalBody" in strings and "notesBody" in strings
    assert "backupWarning" in strings and "sectionProgress" in strings
    assert "share it only" in strings["legalBody"] if lang == "en" else True
    assert "social media" in strings["legalBody"] if lang == "en" else True
    assert "public" in strings["legalBody"] if lang == "en" else True
    assert "116123" in strings["supportBody"]
    assert "116 123" not in strings["supportBody"]
    assert all(phrase in strings["supportBody"] for phrase in support_phrases[lang])
    assert all(phrase in strings["legalBody"] for phrase in privacy_phrases[lang])
    assert "v0.2" not in strings["notesBody"] and "v16" not in strings["statusNote"]
    assert "Nesteidzies" not in strings["intro"]
    assert "Take your time" not in strings["intro"]
    assert "Не спешите" not in strings["intro"]
    assert "48 source modules" in strings["statusNote"] if lang == "en" else True
    if lang == "lv":
        assert "tikai ar cilvēkiem, kuriem uzticies" in strings["legalBody"]
        assert "sociālajos tīklos" in strings["legalBody"]
    if lang == "ru":
        assert "только с людьми, которым Вы доверяете" in strings["legalBody"]
        assert "социальных сетях" in strings["legalBody"]
assert "Tev" in ui["lv"]["intro"]
assert "Вам" in ui["ru"]["intro"] and "Вы" in ui["ru"]["guideBody"]
assert "you" in ui["en"]["intro"] and "You" not in ui["en"]["intro"]

print("PASS: LV/EN/RU catalogs align; review, privacy, support number, and current-change labels are present.")
