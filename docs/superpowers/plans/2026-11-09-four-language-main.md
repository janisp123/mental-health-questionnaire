# Four-language main implementation plan

> **For agentic workers:** Use `superpowers:executing-plans` to implement the approved plan inline, with a final independent review. Track each task below; do not execute this plan during the planning request.

**Goal:** Make the fixed Latvian/English/Russian/Ukrainian questionnaire the only active product and default development build, archive superseded deliverables, and align GitHub, tests, documentation and Google Drive.

**Architecture:** Retain the existing offline HTML application and translation-pack loader. Promote the four-language profile into the default configuration; keep one current package and an explicitly historical archive. Use `main` for current source, with short-lived work branches and versioned distribution snapshots.

**Tech stack:** Existing Python builder, JavaScript/CSS runtime, JSON question/locale sources, Chromium/Playwright checks, GitHub Actions and Google Drive. Add a small reproducible PDF/package build tool using the existing four-language guide source.

**Spec:** Owner's 9 November request: continue only with the multilingual model; the four-language model becomes primary; archive the old version and establish the working structure. The architecture choices here are recommendations for review. This document is a plan, not evidence that migration has happened.

## Current facts

- Fixed source: `codex/fix-four-language-qa` at `46b138eb10921e0ab02b2b8ba7b5a08465a7f127`.
- PR #1 is open, targeting `codex/four-language-candidate`; it has not been merged.
- `main` is still the older Latvian v16 distribution at `a8790a38bdc9702cbc5890bdce86bec4fdc593a7`.
- `develop` at `c6b68dbe8390ffa8d02ad6474acb1358ef191511` diverges from the fixed branch. Its two unique commits document an optional future idea and link its parking lot; preserve these records without treating that idea as approved scope.
- The default `src/questionnaire/build.json` still enables only LV/EN/RU. Four languages require the `v0.2.1-reports` candidate profile.
- README, architecture notes, manifest and CI still identify the old default. Some integration tests explicitly require exactly three languages.
- Google Drive already holds the verified four-language HTML and one-page guide in the existing two file IDs. No further Drive replacement is required merely to adopt this plan.

### Verified distributed baseline

| Item | Source or ID | SHA-256 |
|---|---|---|
| Current HTML | source commit `46b138e`; `v0.2.1-reports` profile | `4bbcccbdfd06a124bb28d13fd843e23e303464c0e05796a4d403dad3848a82b7` |
| Current PDF | `docs/review/README_LV_EN_RU_UK_v0.2.1.md`, generated 9 November | `262cf6ec898e37b59490ef374318ec7d500361f46ae84893e8781a71fa885a25` |
| Previous Drive HTML | downloaded before replacement | `98b50ec80c665ec5bb7c4d476f706f824949ab0c6f0cb4eb0d9d99d93a45ab39` |
| Previous Drive PDF | downloaded before replacement | `17b84900179dfff97f47b375e91824ce11d6cf1b439f315ba0486a0cdbd9a8bc` |

Current Drive folder: `1BUlc5W7tRw06JOUE250wCuTe-1ick9xb`. HTML ID: `1l7d0SQef5RneOCMeXfcsA0czmGzxBlb9`. PDF ID: `1JIpyYvgB5pAJSYc5cHQJa9lDEDlNU3g8`.

The previous Drive files and repository `MH_Public_version` snapshots are not assumed identical. Archive and hash them separately with their provenance.

Current-session backup locations: `/workspace/attachments/5077a559-bcf1-4db1-8602-5fc9157a55a0/` contains the old Drive HTML; `/workspace/attachments/28439fd2-4669-40ea-afd0-1a962f7e33c2/` contains its PDF. The checked current four-language pair is under `/workspace/shared/questionnaire-four-language-fixed/`. These are temporary workspace locations, so Task 1 must preserve them durably. If unavailable in a later session, inspect Drive revision history and recover the exact hashes above rather than substituting another snapshot.

## Recommended approach and alternatives

**Recommended:** one active product, default four-language build, `main` as the current source, and feature branches for changes. Preserve history through tags and archival packages. This removes the ambiguity between candidate, develop and distribution source while retaining rollback.

**Alternative:** retain `develop` as the active integration branch and promote periodically to `main`. This is workable, but leaves two standing branch roles to maintain and document. It is less useful for this project's current single-product workflow.

Do not make another repository or duplicate the application for four languages. Do not reorganize every translation file during promotion; the loader already supports the existing source layout.

## Global constraints

- Active locales: exactly `lv`, `en`, `ru`, `uk`; Latvian remains the reference and initial interface language.
- Preserve all 712 question IDs, 48 source modules, 15 user sections, codes, conditions, safety behavior and existing recovery schema.
- Keep the imported reference files and historical inventory intact. Source files named `LV_EN_RU` remain valid source inputs for the four-language app; they are not a second active product.
- Preserve old three-language progress-file import. Do not silently drop Ukrainian feedback to enable downgrades to an archived app that cannot read it.
- No real responses, patient data or identifiable feedback enter repository fixtures or archives.
- “Main version” means primary maintained technical-review version; human language/clinical review and physical-device checks retain their actual status.
- No force pushes, branch deletion or history rewriting. Archive branch tips first. Remote promotion happens after checks on the integrated tree.
- Keep existing Drive IDs, folder and sharing. Keep only the current HTML and PDF in the reviewer folder.

## Proposed working structure

```text
src/app/                         shared runtime, screens, styles, LV/EN/RU UI
src/modules/                     unchanged canonical source bank
src/questionnaire/build.json     single current four-language configuration
translations/uk/                 active Ukrainian pack; no longer labelled unintegrated
docs/review/                     current editable guide + review evidence
tools/build_questionnaire.py     default four-language HTML
tools/build_review_package.py   HTML + PDF + checksums + ZIP
tests/app/                       focused component/runtime checks
tests/full_bank/                 all four languages and legacy-import checks
tests/fixtures/                  synthetic legacy recovery/config fixtures
MH_Public_version/               two current review deliverables + machine manifest
archive/three-language/v0.2.0/   labelled previous packages and provenance
reference/                      unchanged frozen source/reference materials
dist/review/                     generated working package; ignored by Git
```

The manifest is machine-readable package metadata, not an extra reviewer document. Google Drive still shows only two files.

## Review focus

1. Branch divergence: preserve unique work in both main and develop before changing the default branch content.
2. Locale assumptions: source-bank fidelity may remain three-language; active product checks must cover four languages.
3. Recovery compatibility: legacy imports work; new Ukrainian answers/feedback survive current-version save/restore without loss.
4. Package drift: tested HTML, archived originals, matching guide, repository package and Drive readbacks have distinct recorded hashes.
5. Repeatability: the documented default commands and CI must produce the current multilingual package from a fresh checkout.

## Task 1 — Preserve history and prepare the integration branch

**Files/refs:** new migration branch; `archive/three-language/v0.2.0/README.md` and `manifest.json`; immutable archival tags for current main/develop/candidate tips.

- [x] Refresh remote refs and inspect the unique commits; record the exact current SHAs before changing anything.
- [x] Create a migration branch based on the fixed four-language source. Reconcile the unique main download/readme change and both develop documentation commits explicitly. Preserve the future-ideas parking lot without adding it to the active roadmap.
- [x] Keep PR #1's fixes in the migration ancestry. Once the promotion PR contains them, resolve PR #1 as superseded or merge it through its original branch; record which route was used. Do not leave its work appearing unintegrated.
- [x] Preserve the pre-promotion branch tips with clearly named archival tags. Keep existing branches until migration verification is complete.
- [x] Archive the old repository reviewer files and the exact pre-replacement Drive files in separately labelled subdirectories. Add origin, original name, original Drive ID where applicable, byte size and SHA-256 to the archive manifest. Use the already downloaded backups; do not reconstruct old Drive bytes from Git.
- [x] Preserve the exact currently distributed four-language HTML/PDF pair as a versioned v0.2.1 snapshot before regenerating package bytes. Its PDF has generation-time metadata, so Markdown alone does not reproduce the recorded PDF hash. Verify downloads against the pinned hashes before preserving them.
- [x] Verify every archived file against its manifest. Record rollback commands and the archived file pair to restore in Drive.

**Done when:** no unique branch work is lost, both historical package variants are distinguishable, and the new work can be rolled back without guessing.

## Task 2 — Make the normal build multilingual

**Files:** `src/questionnaire/build.json`, `tools/build_questionnaire.py`, `tests/full_bank/test_build.py`, `tests/full_bank/test_translation_packs.py`, `tests/full_bank/test_source_adapter.py`, and tests using candidate-only config paths.

- [x] First add failing checks that `build_bundle()` and the ordinary CLI include LV/EN/RU/UK in the UI, all 712 questions, report selectors, medication labels and report labels.
- [x] Promote the fixed candidate settings into `build.json`; record the source/promotion revision. Preserve `v0.2.1-reports` as the already distributed baseline. Assign a new build identifier for any changed packaged HTML and record that it replaces the baseline; do not overwrite the historical checksum record.
- [x] Make Ukrainian a normal required translation pack. Missing/incomplete/stale Ukrainian data must fail the current build rather than silently dropping the language.
- [x] Update integration tests to use the default build. Keep a deliberately three-language test fixture only to test the loader boundary and legacy compatibility.
- [x] Separate source-fidelity assertions from active-locale assertions: compare frozen LV/EN/RU source content unchanged, then verify Ukrainian by ID, codes and source hash.
- [x] Retire redundant active candidate profiles after replacing their test dependencies. Historical profiles remain recoverable from tags; remove candidate commands from normal instructions.

**Verify:** `python tools/build_questionnaire.py` succeeds and produces the documented four-language artifact; default-build, source-adapter, translation-pack and source-audit tests pass.

## Task 3 — Establish one repeatable review package

**Files:** new `tools/build_review_package.py` and pinned `tools/review-requirements.txt`; current guide source in `docs/review/`; `MH_Public_version/`; new package manifest and package-builder tests.

- [x] Add a failing package test: a fresh temporary output directory receives the current four-language HTML, one-page four-language PDF, checksum manifest and ZIP containing exactly the two reviewer files.
- [x] Build HTML through the existing builder. Generate PDF from the current editable four-language guide; pin its dependency/fonts. Normalize PDF metadata and ZIP entry order/timestamps using an explicit build epoch. Test that two builds of the same source, epoch and pinned toolchain have identical HTML/PDF/ZIP hashes; do not confuse repeatable generation with byte reproducibility.
- [x] Put source commit/tree, build epoch, build identifier, language list, question count, filenames and SHA-256 hashes in the package manifest. Record hashes from actual generated bytes. Distinguish the tested source commit from the final promotion merge SHA if they differ; record both and whether their source trees match.
- [x] Make replacement behavior explicit: do not overwrite a versioned package accidentally. Provide one documented command for a new package and a separate deliberate step for updating the current repository copies.
- [x] Replace the old active repository reviewer files with the current four-language pair after archiving them. Use filenames matching the manifest and guide links.
- [x] Extract and compare PDF text to its source and render every page for visual review. Keep HTML/PDF versions consistent.

**Done when:** one command builds both deliverables and ZIP from a clean checkout; another assistant does not have to recreate the PDF manually.

## Task 4 — Make four-language verification the normal gate

**Files:** `.github/workflows/app-component-checks.yml`, `.github/workflows/questionnaire-checks.yml`, `tests/app/test_ui_catalogs.py`, `tests/app/runtime_fixture.py`, `tests/full_bank/test_candidate_qa.py`, full-bank runtime/report/recovery tests; new `tools/run_checks.py` if needed to provide one maintained command.

- [x] Parameterize relevant app, full-bank, medication and report checks over the active locale list. Include Ukrainian in synthetic fixtures where testing localization rather than frozen source mapping.
- [x] Promote the four regressions into ordinary full-bank QA; rename the candidate-specific test if helpful. Preserve the data-separation and unsaved-feedback assertions.
- [x] Add synthetic old-three-language recovery imports and current four-language round trips, including Ukrainian typed text/feedback, to the current build tests. Document that rollback to an older app cannot promise import of Ukrainian feedback.
- [x] Retain the 320/390 phone-width cases, desktop screens, independent report language, offline/no-network assertions and PDF separation. Automate the full layout sweep as a maintained test if runtime is reasonable.
- [x] Run CI on pull requests targeting main and pushes to main, with workflow_dispatch retained. Include app/style/locale changes, the package builder, guide source, pinned dependency/font inputs and package tests in the full checks' path coverage. Do not leave the full gate scoped only to develop.
- [x] Build and verify the ZIP and checksum manifest in CI before uploading the current multilingual package as its artifact. Add a maintained local check command so the same active suite can run from a fresh checkout.
- [x] Run the real file-opening journey in CI where allowed. Treat in-memory runs as a distinct test mode and retain the unresolved physical-device check; never relabel it as tested.

**Done when:** an ordinary change to any active language or shared screen triggers the four-language checks, and CI cannot publish a three-language “current” artifact.

## Task 5 — Align the instructions and current-state record

**Files:** `AGENTS.md`, `README.md`, `CONTRIBUTING.md`, `project-manifest.json`, `docs/FILE_INDEX.md`, `docs/QUESTIONNAIRE_ARCHITECTURE.md`, `docs/LANGUAGE_STYLE_GUIDE.md`, `docs/WORK_CHECKPOINT.md`, `docs/CHANGELOG.md`, `docs/RELEASE_POLICY.md`, `translations/uk/README.md` and `translations/uk/CHECKPOINT.md`.

- [x] Describe one active four-language app and current build command. Use main as source of truth; feature branches are for work in progress, tags identify distributed snapshots.
- [x] Replace instructions to work only on develop or use a special candidate. Update AGENTS to require relevant tests and updates across all active locales when shared wording changes.
- [x] Mark Ukrainian as integrated while preserving the actual human review status of every language. Add Ukrainian address/tone conventions to the language style guide based on the existing translation workspace rules.
- [x] Record verified Drive replacement, both current file IDs and hashes, current PDF source, archive locations and the actual synchronization state. Re-read Drive metadata/content when implementation reaches this step; do not assume the folder stayed unchanged.
- [x] Keep the short checkpoint focused on active branch/commit, current artifact, last checks and next action. Preserve historical translation audits under history with links.
- [x] Validate internal links, current paths and `python tools/verify_project_index.py`. Distinguish historical references to three languages from stale active instructions; do not globally replace language strings.

**Done when:** opening README or AGENTS unambiguously directs future work to the four-language version, and repository metadata agrees with Drive.

## Task 6 — Verify the integrated result and promote it

- [x] Run the maintained full active suite on the reconciled migration tree, then build the package from that exact tree. Record results, commit and actual artifact hashes.
- [x] Review the default HTML offline in four languages; test the archived progress import, medication form, long Russian titles, unsaved feedback and independent clinician language.
- [x] Obtain an independent review of the migration diff, including branch reconciliation, archive provenance and unchanged source/backup behavior. Correct blocking findings before promotion.
- [x] Open a promotion PR targeting main, with explicit archive, migration and rollback instructions. Preserve main's unique history with a normal merge; do not force-reset it to the candidate.
- [x] After checks pass, merge through the normal GitHub process and verify the exact resulting main revision. If that merge changes the tested tree, rerun the affected verification before distributing its package.
- [x] Confirm GitHub still identifies main as the default branch. Mark older long-lived branches as superseded in documentation; do not delete them as part of this migration.
- [x] If the promotion produces different distributed bytes, update the same two Drive IDs only after package checks. Read both files back, verify hashes/parents/sharing and update the manifest/checkpoint. Otherwise verify and retain the already current Drive pair.
- [x] Tag the exact distributed source snapshot with an explicitly technical-review version. Keep clinical approval and physical-device review status separate from Git adoption.

**Final acceptance:** fresh main checkout; one normal four-language build; one matching HTML/PDF package; recoverable archived old versions; passing current tests; current reviewer links preserved; no remaining instructions pointing work at the old product.

## Future working routine

1. Start from current main and read the short checkpoint.
2. Create a short-lived branch for the requested change.
3. Modify the shared app or the relevant translation; preserve question identity and recovery compatibility.
4. Run focused checks, then the full gate for shared behavior/locale changes.
5. Build and review the matching package; merge the checked change into main.
6. For an intended reviewer update, replace the two existing Drive files, verify readbacks and record exact source/artifact hashes. Ordinary commits do not automatically publish to Drive.

## Planning status

Planning was completed before execution. The owner subsequently approved execution. All six tasks are now complete: archives and history preserved, default four-language build/package/CI established, main promoted through PR #2, and Drive synchronized by verified readback. See `docs/review/migration-progress.md` and `docs/review/checks/2026-11-09-main-drive-sync.json`. No branches were deleted.

A separate read-only plan review found no blockers. Its suggestions on backup availability, packaging CI coverage and reproducibility/provenance are included above.
