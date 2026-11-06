# Questionnaire architecture

The working build assembles the original 48 modules and 712 questions into one offline HTML file.

- `src/modules/` is the canonical LV/EN/RU question bank. LV is the reference; EN/RU remain drafts.
- `src/app/screens/` contains separate first-page, section-picker, question, medication, feedback, completion, and report-page templates. Each accepts its data and labels from the runtime.
- `src/app/styles/` contains ordered base, report, navigation, feedback, and safe-area styles. Change a visual area here without opening question files.
- `src/app/core/app.js` coordinates shared answer state, navigation, recovery, event handling, and the screen components. `src/app/reports/` generates doctor and project-feedback reports; `src/app/i18n/` holds interface labels.
- `src/app/build.json` is the explicit ordered list of app styles and scripts. The component builder test uses a synthetic bundle and does not read `src/modules/`.
- `src/questionnaire/` contains module titles, navigation/report ordering, explicit report rules, and build metadata.
- `tools/build_questionnaire.py` validates and combines these sources into `dist/QUESTIONNAIRE_LV_EN_RU_NOT_RELEASED.html`.
- `tests/app/` checks individual screen renderers and source assembly using synthetic content, without loading the 712-question bank.
- `tests/full_bank/` checks source mapping, packaging, reports, offline runtime behavior, and the complete browser journey.
- `.github/workflows/app-components.yml` runs focused synthetic checks for app, screen, style, and interface-locale changes. `.github/workflows/questionnaire-checks.yml` runs the full regression for question-bank and full-build changes; it can also be started manually.
- `archive/pilot/` holds the retired 60-question prototype and its old tests for history only.

The HTML contains its runtime and all questions, works offline, and makes no network requests. Screen and report-page markup has focused synthetic-content tests. A compact synthetic bundle is also used for isolated browser checks, while the 48-module end-to-end journey remains a separate integration gate. Automated desktop Chromium checks pass; native Android testing and clinical review remain outstanding. EN/RU content and the new interface text have not had human language review. This build is for professional review, not diagnosis or clinical validation.

Recovery files retain the existing `mental-pilot-recovery-v1` schema to preserve compatibility with the prior prototype. The file remains local unless the user chooses to copy or share it.
