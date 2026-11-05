# Project file index — latest verified versions

**Status: SOURCE TRANSFER COMPLETE (79/79 files). Application refactor and EN/RU release are NOT complete.**

## Where to start each time

1. **Current version pointers and full machine-verifiable list:** [`project-manifest.json`](../project-manifest.json). Treat this as authoritative for which file/version is current; it pins the Git blob SHA1 and size of all **79 imported original files**.
2. **New work progress:** [`docs/CHANGELOG.md`](CHANGELOG.md). Register tasks before editing; checkpoint every verified batch.
3. **Release policy:** [`docs/RELEASE_POLICY.md`](RELEASE_POLICY.md). A successful source import does NOT certify behavior, translations or clinical validity.

## Current source, per type

| Role | Exact current path | Meaning |
|---|---|---|
| Questions in LV/EN/RU | `src/modules/182_MODULE_01_LV_EN_RU_v16.json` through `182_MODULE_48_LV_EN_RU_v16.json` | 48 sections, 712 questions, language fields per module; LV reference, EN/RU **unreviewed drafts** |
| Module source index | `tests/fixtures/181_MODULE_INDEX_v16.json` | Frozen initial module SHA256, count and order; do not confuse with the current overall manifest |
| Existing working application | `reference/baseline/html/162_Sagatavosanas_vizitei_LV_v16.html` | Exact frozen LV v16 single-file browser reference; **not** yet split into a new app engine |
| English app snapshot | `reference/baseline/html/172_Questionnaire_EN_v16_DRAFT_NOT_RELEASED.html` | Reference draft only, **not a release** |
| Russian app snapshot | `reference/baseline/html/172_Questionnaire_RU_v16_DRAFT_NOT_RELEASED.html` | Reference draft only, **not a release** |
| Working language resources | `src/i18n/working/` | EN/RU catalogs, memory, overrides and one CSV snapshot of the prior Google Sheet |
| Standalone README/PDF snapshots | `reference/baseline/readme/`, `reference/baseline/information/` | Current v16 LV reference and unreviewed EN/RU documents |
| Module reconstruction tool | `tools/183_MODULE_TOOLS_v16.py` | Rebuilds BANK data, not full UI or reports |
| Release-evidence verifier | `tools/186_RELEASE_GATE_CHECK_v1.py` | Checks evidence metadata; is not an automated browser or clinical test |
| Active development history | `docs/CHANGELOG.md` | **Only active change log** |
| Historical Drive change log | `docs/drive-original/166_CHANGELOG_LV.md` | Frozen prior history, **never update during development** |
| Older artifacts | `reference/history/` | Six outdated reference versions; not build inputs unless specifically needed |

## Directory roles

- `src/modules/`: source questionnaires (48 exact modules).
- `src/i18n/working/`: existing translation drafts/resources. New stable localization code goes under `src/i18n/`.
- `src/core/`, `src/reports/`, `src/information/`: reserved for future shared engine, outputs and in-app information. **Not yet implemented.**
- `reference/baseline/html/`, `reference/baseline/readme/`, `reference/baseline/information/`: immutable v16 reference snapshots.
- `reference/history/`: legacy v9/v14 references; never assume newest.
- `docs/drive-original/`: immutable former Drive development directions, indexes, and prior changelog, preserved for traceability; some old wording points to Drive because these are historical snapshots.
- `docs/`: active GitHub changelog, instructions, migration record and release policy.
- `tests/fixtures/`: imported module index and past EN/RU draft build report; *not* evidence of current full test passes.
- `tools/`: existing original build helpers and new verification tools.
- `.github/workflows/`: automated CI to be added and tested (not active).
- `main` branch is **not** the active source tree; `develop` holds the import.

## Distribution — separate from development

Google Drive's [Latvian public folder](https://drive.google.com/drive/folders/1BUlc5W7tRw06JOUE250wCuTe-1ick9xb), now named **“Sagatavošanās vizītei pie psihiskās veselības speciālista — latviešu versija”**, contains exactly the LV v16 HTML and LV README. It is **distribution only**. Do not edit the Drive files while developing. Build, run all required release gates, promote an approved version, and only then publish an updated artifact there. EN/RU are still **drafts** and remain unpublished.

## Rules for identifying the latest version

1. Read `project-manifest.json > current_versions`, not the largest filename prefix and not the newest Drive timestamp.
2. Use the active source paths there, not `reference/history/` or the `docs/drive-original/` text.
3. A change to a source path, major version, or release status MUST update `project-manifest.json` in the same Git commit.
4. Old baselines stay frozen. Real code changes go into version-controlled `src/`; only a reviewed build is copied to distribution.
5. Git history tracks previous versions; we do not create endless numbered duplicates in the active source folders.
6. Validate imports with `python tools/verify_project_index.py`. This is source integrity, not a user-interface, translation or clinical release approval.

**Next development task:** extract the shared application code and reports from the frozen LV HTML into `src/core`, `src/reports`, `src/information`; build one multilingual offline HTML; complete translation and release testing.
