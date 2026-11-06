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

print("PASS: LV/EN/RU interface and medicine catalogs have matching key structure.")
