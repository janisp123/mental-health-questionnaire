# Mental health questionnaire

Free, non-commercial, privacy-focused psychiatric **pre-appointment questionnaire** project. **Not a diagnostic tool.** Latvian is the reference language; English and Russian are being prepared for review.

**Project status (2026-11-05): all 79 original source/reference files migrated and indexed on `develop` (48 modules, 712 questions). This is NOT a finished new application or clinically validated instrument. English and Russian remain DRAFT / NOT RELEASED.**

## Goal
Build one completely self-contained HTML file that works offline on Android Chrome with language selection (Latvian, English, Russian), section navigation, conditional questions, manual Save & Next, local recovery, readable doctor summary, AI export, and integrated information/legal/resources.

The [public Google Drive folder](https://drive.google.com/drive/folders/1BUlc5W7tRw06JOUE250wCuTe-1ick9xb) is **distribution-only** and contains LV HTML + LV README. Existing Drive development archives are **read-only historical/source references** pending complete and verified GitHub migration. **All new edits and the active changelog belong on GitHub `develop`**; do not edit or publish directly on Drive.

## Development
- `develop`: everyday development; `main`: future reviewed releases/source only.
- `src/modules/`: 48 imported multilingual question section files (LV reference; EN/RU draft).
- `src/core/`: planned extracted shared interface, navigation, saving/restoring (NOT YET IMPLEMENTED).
- `src/i18n/working/`: imported translation work files; shared UI/report localization NOT YET IMPLEMENTED.
- `src/information/`: planned extracted in-app information (NOT YET IMPLEMENTED).
- `src/reports/`: planned extracted summary/export implementation (NOT YET IMPLEMENTED).
- `tools/`: imported historical module rebuild and release-evidence tools; unified app builder NOT YET IMPLEMENTED.
- `tests/`: structure, behavior, translations, offline/privacy and backup compatibility.
- `.github/workflows/`: future automated release-blocking CI.
- `docs/`: migration plan, release policy and the authoritative changelog (after verified handoff).

Start with [latest verified file index](docs/FILE_INDEX.md), [project manifest](project-manifest.json), then the [active GitHub changelog](docs/CHANGELOG.md). See [Migration Plan](docs/MIGRATION_PLAN.md), [Release Policy](docs/RELEASE_POLICY.md), [Migration Status](docs/MIGRATION_STATUS.md), and [Contributing](CONTRIBUTING.md).

## Privacy and scope
No completed questionnaires, patient details, recovery files or private correspondence belong in the public repository. Questionnaire responses must remain local unless an informed user chooses to export/share them. Do not share personal medical information in Issues or Pull Requests. Do not claim clinical validity based only on programming tests.

## Copyright
**No license has been granted yet.** Public visibility is not a grant of reuse or redistribution rights. Project licensing and contribution terms need a deliberate decision before accepting substantive external code/text contributions.
