# Migration status — VERIFIED COMPLETE (2026-11-05)

**GitHub source import:** 79/79 original development/reference files committed to `develop` with matching source Git blob SHA1 hashes; 48/48 multilingual modules present, 712 questions in LV/EN/RU question-bank baselines. Source snapshot commit: `24d25c992cd866daf0589e16b4c4a1a9b8b7d63f`. An earlier blocked attempt was resolved through the working connector; it is HISTORY, not the present state.

**Current file/version authority:** [`project-manifest.json`](../project-manifest.json) and [`docs/FILE_INDEX.md`](FILE_INDEX.md). **Only active changelog:** [`docs/CHANGELOG.md`](CHANGELOG.md). The original Drive changelog lives at `docs/drive-original/166_CHANGELOG_LV.md` as read-only prior history.

**Distribution:** Google Drive contains exactly 2 Latvian v16 files in [the renamed Latvian folder](https://drive.google.com/drive/folders/1BUlc5W7tRw06JOUE250wCuTe-1ick9xb). EN/RU remain DRAFT_NOT_RELEASED.

**Next task:** extract shared application engine, build multilingual single offline HTML, finish complete EN/RU translation and release testing. Those phases are NOT completed by file transfer.

---

## Previous interrupted migration attempts — historical record only

# Original staging checkpoints (outdated)

**Historical note (superseded 2026-11-05):** [`docs/CHANGELOG.md`](CHANGELOG.md) on GitHub `develop` is the single active log for future work. The archived Google Drive changelog is read-only historical evidence. GitHub source migration is still BLOCKED (0/48), so Drive source files remain immutable references until verified Git import. This page is a migration reference, not another active changelog.

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

## 2026-11-05 — GITHUB-SOURCE-MIGRATION — BLOCKED

- Drive source inventory verified: 48 separate LV/EN/RU module files, current 3 original HTML files, source tooling, translation catalogs and documentation.
- GitHub connector rejected direct migration operations to this PUBLIC repo with a generic safety-check block. It also rejected copying a small development document. **Zero of 48 questionnaire modules are committed to GitHub.** Do not mistake an uncommitted Git blob for an imported file.
- Google Drive source is unchanged and remains authoritative. The Drive changelog is authoritative until an explicit verified handoff.
- Recovery: complete local ZIP prepared named `190_GITHUB_MIGRATION_READY_MANUAL_UPLOAD.zip`, with **79 original source/reference files**, import instructions, per-file Drive ID and SHA256 manifest, and `tools/verify_drive_bundle.py`.
- Validation: all 48 source module SHA256 values match the Drive module index; all 712 questions are structurally complete; reconstructed LV/EN/RU question BANKs exactly equal their original HTML; ZIP integrity and local import validator passed. This does not establish translation accuracy, clinical validation or browser functionality.
- ZIP SHA256: `e7c77000356bcbcbcda9008150562decf3924a10321c5e28fab2d2e7eaf1dd8e`.
- Privacy check: only known deliberately published creator contact email was found in included text; manually review before publishing because this is a PUBLIC repository and scans are not guarantees.
- **Next action:** repository owner imports the unzipped bundle into a local checkout on **develop** (e.g. via GitHub Desktop); push; then run `python tools/verify_drive_bundle.py`. After 48/48 module readback and validation, record source-of-truth handoff. Keep `main` and current Drive files untouched. No license/clinical approval inferred.
