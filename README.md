# Mental health questionnaire — four languages

Free offline questionnaire for adults preparing for a mental-health appointment. The current application includes Latvian, English, Russian and Ukrainian: 712 questions from 48 source modules, arranged into 15 optional sections. Latvian is the reference and initial language. It does not diagnose or calculate a screening score.

## Current files

- [Questionnaire HTML](MH_Public_version/187_Questionnaire_FULL_712Q_LV_EN_RU_UK_v0.2.2_REVIEW_BUILD.html)
- [Four-language PDF guide](MH_Public_version/188_README_LV_EN_RU_UK_v0.2.2_REVIEW_BUILD.pdf)
- [Google Drive review folder](https://drive.google.com/drive/folders/1BUlc5W7tRw06JOUE250wCuTe-1ick9xb)

Download the HTML and open it in your browser; Drive/GitHub preview is not the questionnaire. It runs offline and sends no answers. Download progress explicitly to continue later. Clinician reports and project-feedback PDFs are separate. Recovery files may contain sensitive information; keep and share them carefully.

## Development

`main` is the only active product source. Create short-lived branches from main. Older develop/candidate branches and [archived packages](archive/three-language/v0.2.0/README.md) are historical. Legacy `downloads/` paths remain for existing links.

```sh
python -m pip install -r tools/review-requirements.txt playwright
python -m playwright install chromium
python tools/run_checks.py
python tools/build_questionnaire.py
python tools/build_review_package.py --output-dir dist/review-0.2.2
python tools/verify_review_package.py dist/review-0.2.2 --with-zip
```

The normal HTML output is `dist/QUESTIONNAIRE_LV_EN_RU_UK_NOT_RELEASED.html`. Package destinations are never overwritten. CI runs the same checks on PRs to main and on main, then uploads the matching four-language package.

Read [feature/module contracts](docs/FEATURE_DEVELOPMENT.md), [architecture](docs/QUESTIONNAIRE_ARCHITECTURE.md) and [current checkpoint](docs/WORK_CHECKPOINT.md) before working. For a managed browser that blocks file navigation, explicitly use `--load-mode memory` and record that limitation.

## Review and contribution

This is a technical-review project. Human language review, clinical review and physical-device verification remain separate requirements. Main adoption does not establish clinical validation. Anyone may use the questionnaire for free, including clinicians during appointments. Source/content reuse terms are separate: no general license has been granted.

Use synthetic data in public issues/tests; never post patient answers or recovery files. Project feedback: janis.paegle.email@gmail.com. See [contribution guidance](CONTRIBUTING.md) and the [future-ideas parking lot](docs/FUTURE_IDEAS.md), which is not an approved feature roadmap.
