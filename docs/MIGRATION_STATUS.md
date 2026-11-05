# GitHub migration status — staging checkpoints only

**Authority:** the Google Drive `166_CHANGELOG_LV.md` remains authoritative until a verified handoff. This is a staging record; do not use it to override Drive's incomplete EN/RU task.

## 2026-11-05 — GITHUB-SCAFFOLD — TASK_DONE

Goal: verify GitHub writes and create public, development-only project structure WITHOUT importing any questionnaire source data or changing public releases.

### Verified checkpoints
1. GitHub repository `janisp123/mental-health-questionnaire` is PUBLIC and connector reports read/write privileges. Default branch `main`.
2. Created separate `develop` branch; `main` was not edited by this task.
3. Disposable `test/connectivity.txt` was created, fetched, updated, fetched again and deleted on `develop`. All five operations succeeded and edit content matched readback. The deleted test content remains in Git history; it contained no personal or questionnaire data.
4. Created the documented development skeleton as one tree + commit `ad171fdd2608ab43e0bf9b13f1d841aa2d410adc`. Branch ref update completed successfully.
5. Verified repository tree was not truncated, source folder placeholders exist, and successfully read back: `docs/MIGRATION_PLAN.md`, `docs/RELEASE_POLICY.md`, `project-manifest.json`, `src/modules/.gitkeep`, `README.md`.
6. No clinical response data, passwords, private messages, real questionnaire HTML, or actual questionnaire modules were uploaded in the scaffold phase.

### Current state
- `main`: untouched starter README and .gitignore, NOT a release.
- `develop`: organized empty development structure, migration plan, release policy, public contribution warnings, placeholder manifest.
- Source modules imported: **0/48**. LV baseline still v16, 712 questions; EN/RU still draft.
- Release automation: **NOT INSTALLED**. A written release policy does not enforce GitHub Actions or branch protection.
- Next task: **GITHUB-SOURCE-MIGRATION — NOT STARTED**. Before importing, record a matching new task in the authoritative Drive changelog, audit each public-bound file for privacy, preserve all Drive originals, import 48 multilingual modules in small hash-verified batches, migrate tools and changelog, then separately build/translate/test the unified HTML.

### Safe continuation
Read this status and `docs/MIGRATION_PLAN.md`, then inspect the Git branch SHA and Drive changelog. Do not assume that the latest GitHub status is the current Drive task status, that any English/Russian translation is approved, or that a working user questionnaire exists in GitHub.

## 2026-11-05 — GITHUB-SOURCE-MIGRATION — IN_PROGRESS

Drive inventory verified. Public source migration attempted on develop; initial batch was blocked by connector safety checks before a branch commit. Previous Git branch head is unchanged. No questionnaire module is committed yet. Drive originals remain authoritative. Continue with source-only validation and record actual committed files before closing.
