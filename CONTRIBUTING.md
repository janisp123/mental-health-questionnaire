# Contributing and professional feedback

Thank you for considering feedback on this free, non-commercial pre-appointment questionnaire.

This is a PUBLIC source repository. **Do not post identifiable health information, completed questionnaires, recovery backups, contact details of patients, or private clinician correspondence** in issues, commits or pull requests. Use invented/non-identifying test cases only.

Good feedback includes a question ID (for example M11_01), language (LV/EN/RU/UK), a clearly described wording/clinical concern, expected meaning, and a citation if relevant. Report broken buttons, missing translations, navigation problems, backup/restore issues and privacy concerns.

**Copyright notice:** no software/content license is currently granted. Public visibility does not permit unrestricted copying or commercial reuse. External contributions may carry their own intellectual-property rights; proposed wording or code changes must be handled under explicitly agreed contribution terms before merging. Until those are settled, prefer issue reports and suggestions over full code/text pull requests.

The questionnaire is not a diagnostic tool, and automated tests do not constitute clinical validation. Professional reviewers determine whether wording or clinical claims are suitable. Only maintainers may approve releases.

Development uses short-lived branches from main and the default four-language build. Read [module/data contracts](docs/FEATURE_DEVELOPMENT.md), run `python tools/run_checks.py`, and preserve synthetic old-format progress-file fixtures when changing saved data.
