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
support_phrases = {
    "lv": ("sešciparu", "tikai 6 cipari", "anonimitātes", "darbavietai"),
    "en": ("six-digit", "only six digits", "anonymity", "workplace"),
    "ru": ("шестизначный", "всего 6 цифр", "анонимности", "работодателя"),
}
privacy_phrases = {
    "lv": ("nav šifrēts", "personas datus", "klīniski validēta"),
    "en": ("not encrypted", "personal details", "not clinically validated"),
    "ru": ("не зашифрован", "личные данные", "клиническую валидацию"),
}
for lang in LOCALES:
    strings = ui[lang]
    assert "legalBody" in strings and "notesBody" in strings
    assert "116123" in strings["supportBody"]
    assert "116 123" not in strings["supportBody"]
    assert all(phrase in strings["supportBody"] for phrase in support_phrases[lang])
    assert all(phrase in strings["legalBody"] for phrase in privacy_phrases[lang])
    assert "v0.2" not in strings["notesBody"] and "v16" not in strings["statusNote"]

print("PASS: LV/EN/RU catalogs align; review, privacy, support number, and current-change labels are present.")
