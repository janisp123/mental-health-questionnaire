# Release and technical-review policy

Updated 9 November 2026. `main` contains the sole active LV/EN/RU/UK application. The current distributed package is **v0.2.4, for technical review**. It is not a clinically validated release.

## What is implemented

Automated CI is active on pull requests targeting main and on main. The [full questionnaire workflow](../.github/workflows/questionnaire-checks.yml) runs the maintained suite with real offline file opening, builds the four-language HTML/PDF/ZIP package, verifies it, and uploads the package and test evidence. The [component workflow](../.github/workflows/app-component-checks.yml) supplies focused application checks.

| Gate | Current verification |
|---|---|
| Source integrity | 79 imported files; 48 module hashes; 712 unique question IDs/orders, preserved answer codes/conditions and 15 current user sections. |
| Four-language consistency | UI/medicine catalogs, question packs, placeholders, source hashes and report labels. Structural coverage does not establish translation accuracy. |
| Critical runtime behavior | Section choice, conditions, answer handling, skip/back, medication entries, support prompts, language switching, recovery and separate reports. |
| Saved-data compatibility | Synthetic older-three-language progress import and current Ukrainian answer/feedback round trips. Unsupported answer/feedback records are rejected rather than silently discarded. |
| Phone layouts | Every question in four languages at 320/390 pixels; targeted medication, long-heading and feedback regressions. |
| Packaging | Pinned PDF dependency/fonts, repeatable HTML/PDF/ZIP bytes, overwrite protection, checksums and clean-source provenance. |
| Current-source equivalence | Complete HTML including runtime/styles, regenerated guide PDF, and exactly one HTML/PDF pair. Negative tests reject stale packages even if their recorded checksums were updated. |

Single-choice answers save in the session after a short visible selection delay. Multiple-choice, text and medication answers require explicit save. Progress-file downloads are user-initiated. Tests must preserve these actual behaviors; “selection never autosaves” is not the current product contract.

CI checks are not automatic publication or evidence of configured branch protection. Maintainers must wait for the relevant checks before merging; do not claim merges are technically blocked unless required-check rules have separately been verified.

## Review status and outstanding gates

| Status | Meaning |
|---|---|
| Development source | Changes on a short-lived branch from main; not yet a new reviewer distribution. |
| Technical-review package | A checked, versioned HTML/PDF pair intended to collect professional feedback, with limitations recorded. This describes the current package. |
| Human-reviewed language/clinical content | Requires actual reviewer records for the relevant wording, safety meaning and any standardized instruments. CI cannot grant this status. |
| Physical-device compatibility | Requires testing downloaded files on the named real device/browser. Desktop Chromium and simulated phone widths are separate evidence. |
| Clinically validated/public clinical release | Requires appropriate qualified clinical and safety review and explicit owner approval of that claim. Main adoption and a green workflow do not establish it. |

Human language/clinical review and physical-phone downloaded-file testing remain outstanding. Record these as pending; do not turn missing evidence into a pass. An unverified device or clinical claim remains blocked even when a technical-review package is shared with its limitations disclosed.

## Before merging a change

1. Use a short-lived branch from current main. Preserve question IDs, codes, conditions and the `mental-pilot-recovery-v1` import contract, or supply an explicit tested migration for an approved change.
2. Run focused checks and `python tools/run_checks.py` for shared runtime, language, source or packaging changes. Syntax checks alone are insufficient.
3. Update all active locales and their change notes when user-facing wording/behavior changes. Read the notes in every locale against the [audience and privacy rules](../AGENTS.md#audience-and-privacy-in-update-notes). Keep private coordination and repository-only work out of app notes and the downloadable guide; repository-only maintenance does not require a reviewer package. Obtain human review where the claim or wording requires it.
4. Inspect failed/unknown checks and resolve them before claiming verification. Never manufacture or reuse unrelated PASS evidence.
5. Merge the checked head through a PR. If the resulting product tree differs, verify the affected behavior again before distribution.

For managed Chromium that blocks `file://`, `--load-mode memory` is an explicitly labelled fallback. It does not replace file-opening checks in CI or physical-device evidence.

## Before distributing a reviewer update

1. Commit the relevant source and assign a new build identifier for changed distributed bytes. Update the README version, download links and feature summary alongside the package pointers; refresh its screenshot when the visible UI changes. Build using `python tools/build_review_package.py --output-dir dist/review-<version>`; existing destinations must not be overwritten accidentally.
2. Run `python tools/verify_review_package.py <folder> --with-zip`. Require `source_dirty: false`, complete current-source equivalence and matching file/ZIP hashes.
3. Extract/compare guide text and render every PDF page for visual inspection. Check relevant clinician/feedback print behavior; never include real patient data in evidence.
4. Record source commit/tree, tested revision, actual artifact hashes and test mode/results. If the promotion merge has a different SHA, record it separately rather than relabelling source provenance.
5. Preserve the previous package and rollback point. Tag the distributed technical-review snapshot; keep frozen source references and archives unchanged.
6. Deliberately replace the same Drive HTML/PDF IDs. Preserve folder/sharing and existing links, download both files back, compare bytes/hashes, and update `project-manifest.json` and the current checkpoint after successful readback.

Ordinary source commits do not publish to Drive automatically. Documentation-only changes that do not change the app or guide do not require rebuilding or republishing an identical reviewer package.

## Evidence and historical material

Current package/provenance: [repository manifest](../MH_Public_version/manifest.json). Latest verified reviewer synchronization: [Drive readback record](review/checks/2026-11-09-credit-link-drive-sync.json). Ongoing status: [working checkpoint](WORK_CHECKPOINT.md). Rollback provenance: [three-language archive](../archive/three-language/v0.2.0/README.md) and [four-language v0.2.1 snapshot](../archive/four-language/v0.2.1/manifest.json).

`docs/drive-original/`, historical checkpoints and `tools/186_RELEASE_GATE_CHECK_v1.py` preserve earlier policy/evidence formats. They do not override this current workflow or replace actual current test runs. No import/reconciliation task remains pending merely because an archived document describes one.

Never commit questionnaire responses, identifiable health information, real recovery files or private correspondence. New functionality must preserve the offline/no-transmission boundary unless an independently approved feature explicitly changes it.
