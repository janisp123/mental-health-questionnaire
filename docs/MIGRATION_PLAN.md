# Controlled migration from Google Drive to GitHub

**2026-11-05 status:** source import **VERIFIED COMPLETE**: 79 original Drive source/reference files, all 48 modules. Next phases (shared engine, localization, QA) remain pending. **Active changelog: [`docs/CHANGELOG.md`](CHANGELOG.md).** Repository visibility is **PUBLIC** by owner's choice. Do not commit personal information or real completed tests.

## Verified reference locations (read-only during migration)
- [Public Drive main folder](https://drive.google.com/drive/folders/1BUlc5W7tRw06JOUE250wCuTe-1ick9xb): only the Latvian v16 HTML and Latvian README; EN/RU drafts moved into Drive development archive.
- [Drive development archive](https://drive.google.com/drive/folders/1GxGJBMYRMz0WbjBlYx_XVtXmlSdFvGQy): project working files.
- Imported source modules live in [GitHub `src/modules/`](../src/modules/); the Drive folder of 48 modules is now historical backup only.
- `181_MODULE_INDEX_v16.json`: reference module hashes; `183_MODULE_TOOLS_v16.py`: current baseline rebuild helper; `184_MODULE_WORKFLOW_v16.md`: working procedure.
- `166_CHANGELOG_LV.md` in the Drive archive is read-only past history; all new tasks are recorded in GitHub `docs/CHANGELOG.md`. The questionnaire source files remain read-only Drive references pending a verified Git import.

## Plan and acceptance gates
1. **GIT ACCESS — TESTED:** Create a disposable file on `develop`; fetch, update, verify and delete it. Do not modify `main`.
2. **SCAFFOLD:** Create this directory tree and document the source map, release rules, public privacy guidance and migration checkpoints.
3. **PRE-IMPORT AUDIT:** Inspect candidate public files for identifying health answers, personal contact details not intended for publication, secrets or private correspondence. Copy only approved content; the fact that Drive is shared is not enough to assume publication consent for every file.
4. **IMMUTABLE BASELINE:** Record each source path, exact Drive file ID, size and SHA256. Keep LV v16 HTML and EN/RU draft HTML as preserved *reference snapshots*, not competing editable masters.
5. **MODULE IMPORT:** Import 48 modules into `src/modules/` in independently verifiable batches (e.g., 8 files). Verify source hash/readback after each batch; preserve original global question ordering and permanent IDs. Never treat half an upload as a complete stage.
6. **TOOLS AND DOCUMENTS:** Import and reconcile index, existing module helper, release checker and relevant docs. Keep new work in the already-active `docs/CHANGELOG.md`. Copy the old Drive changelog only as a separate immutable history snapshot after privacy and integrity checks; do not overwrite active entries or edit the Drive changelog.
7. **DATA INTEGRITY:** Reconstruct LV/EN/RU banks and compare against the original HTML baselines; require 48 unique sections, 712 unique question IDs, identical answer codes, stable conditions and complete language entry structure. Failed checks block migration completion.
8. **SHARED ENGINE:** Carefully split the existing HTML application into reusable core, reports, localization and documentation modules without changing behavior. Preserve current original standalone versions for comparison.
9. **TRANSLATION:** Complete English and Russian questions, prompts, UI, exports, summaries and information/legal pages; cross-verify against LV. Flag clinical and sensitive phrases for professional review; no silent fallback into another language.
10. **SINGLE-FILE BUILD:** Deterministically package code, question data, all three translations and documentation into ONE offline HTML. No runtime network fetching or analytics.
11. **RELEASE TESTING:** Gate on structural checks, critical browser behavior, backup/restore compatibility, translation completeness, offline Android Chrome, outputs/printing, privacy and safety semantics. Test results tied to the exact candidate checksum; passing syntax alone is NEVER sufficient.
12. **PROFESSIONAL REVIEW / FREEZE:** Make a clearly labeled reviewer candidate only after required nonclinical tests pass. For an approved clinical/public release, record actual professional assessment and explicit human approval. Freeze reviewer versions, hotfix only critical failures through the same gate.
13. **PUBLISH:** Release a tagged, reproducible HTML and optionally mirror to Google Drive. Keep rollback versions. Development proceeds on `develop`/feature branches.

## Public repository safeguards
- Never upload real questionnaire answers, backup/recovery files or patient medical histories.
- No secrets, API tokens, email archives or private collaborator messages.
- Main branch is not an editable workbench. Protect it with required status checks and approvals when GitHub settings permit.
- Actual GitHub Actions workflows and branch protections are NOT yet installed; written policies alone do not technically enforce the gate.
- The original Drive archive is retained as immutable backup; ongoing edits belong exclusively to GitHub develop and new approved releases are mirrored to the LV distribution folder.
- No license chosen yet. Contributions and permissions need a separate deliberate policy.

## Efficient work across interrupted sessions
- Read `docs/FILE_INDEX.md` and `project-manifest.json` for current paths, then `docs/CHANGELOG.md` for the next task; this migration plan is historical.
- Work on the relevant one of 48 modules, not the whole file corpus, for a narrow change.
- Keep stable IDs, branching semantics and answer statuses unless a formal migration is tested.
- Save a verified commit and checkpoint after each batch.
- Use source hashes and commit SHAs instead of names alone to prevent version mix-ups.
