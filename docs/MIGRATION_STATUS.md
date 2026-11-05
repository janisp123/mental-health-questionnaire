# GitHub migration status — single source of progress

## 2026-11-05 — GITHUB-SCAFFOLD — IN_PROGRESS

Goal: Validate ChatGPT GitHub write access and create development-only scaffolding for the Latvian-first, offline, 48-section / 712-question questionnaire. Do not import clinical data, questionnaire answers, existing HTML, translations, or reports yet.

Source of truth until migration verification: existing Google Drive project and its changelog. This file is a GitHub staging status only. Do not claim that migration is complete, that EN/RU translations are reviewed, or that a production single-HTML build exists.

Plan:
1. Create and inspect `develop` branch without modifying `main`.
2. In `test/`, create, fetch, edit, verify, and delete disposable test content.
3. Create a minimal, documented folder skeleton on `develop`.
4. Verify source files, directory paths, and permissions using readback.
5. Record exact results and pending migration steps here.

Non-negotiable:
- No personal questionnaire responses or identifying patient information in this public repository.
- All user releases must remain fully offline and single-file.
- Release blocked until structural, critical behavioral, translation, and safety checks are evidenced. Clinical review is required before claims of clinical validation.
- Public project source is viewable/copyable even when no license has been granted. Licensing/contribution policy is pending.
- Work only on `develop` unless explicitly publishing an approved release.
