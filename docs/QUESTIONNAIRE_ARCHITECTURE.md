# Questionnaire architecture

The working build assembles the original 48 modules and 712 questions into one offline HTML file.

- `src/modules/` is the canonical LV/EN/RU question bank. LV is the reference; EN/RU remain drafts.
- `src/app/` contains the shared design, interface text, answering/recovery logic, and report renderer. It has no question bank and reads the data embedded by the builder.
- `src/questionnaire/` contains module titles, navigation/report ordering, explicit report rules, and build metadata.
- `tools/build_questionnaire.py` validates and combines these sources into `dist/QUESTIONNAIRE_LV_EN_RU_NOT_RELEASED.html`.
- `tests/full_bank/` checks source mapping, packaging, reports, offline runtime behavior, and the complete browser journey.
- `archive/pilot/` holds the retired 60-question prototype and its old tests for history only.

The HTML contains its runtime and all questions, works offline, and makes no network requests. Automated desktop Chromium checks pass; native Android testing and clinical review remain outstanding. EN/RU content and the new interface text have not had human language review. This build is for professional review, not diagnosis or clinical validation.

Recovery files retain the existing `mental-pilot-recovery-v1` schema to preserve compatibility with the prior prototype. The file remains local unless the user chooses to copy or share it.
