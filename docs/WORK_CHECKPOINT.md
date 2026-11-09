# Current working checkpoint

Guide notice revision IN PROGRESS: the new four-language privacy/medical-purpose PDF is checked locally; Drive still has the opening-instructions guide pending checked merge and readback. Earlier readback records describe their original revisions.

Updated 9 November 2026. Migration DONE. Sole active source: `main`. Promotion PR #2 merged as `1a68d31f385208263be79de5da8c27e3df90354a`; its tree exactly matches the checked head `505187b9b127fe375dafab9b3e341cf4d863ac3b`.

## Active product

- Sole maintained product: LV/EN/RU/UK, 712 questions, 48 immutable source modules, 15 sections. Latvian remains the reference and initial language.
- Default configuration: `src/questionnaire/build.json`, technical-review version `0.2.4-review+full-bank`.
- Source history includes old main, develop’s two future-idea documentation changes, the four-language fixes and the approved plan.
- Stable feature/module contracts: `docs/FEATURE_DEVELOPMENT.md`. Extend focused modules and current APIs; preserve IDs and saved-data compatibility.

## Verification and artifacts

- All 28 maintained scripts pass locally in explicit memory mode, including 5,696 question/locale/phone-width renders and legacy recovery import. Both final GitHub workflows passed with real offline file opening (runs 42586610302 and 42586610292). Physical-device testing is separate.
- `MH_Public_version/manifest.json` records the exact repository HTML/PDF hashes and source commit/tree. Package source commit: `3a8f9227bda6a85b509703c17cf10b1b37de514e`; source was clean when built.
- Package CLI tests verify byte-identical repeated HTML/PDF/ZIP builds and refusal to overwrite. PDF has one A4 page and was visually inspected.
- Repository and Drive contain the same verified four-language v0.2.4 HTML/PDF pair. Both downloads matched exact hashes; existing IDs, folder and sharing are preserved. Evidence: `docs/review/checks/2026-11-09-opening-guide-drive-sync.json`.

## History and rollback

- Immutable tags `archive/main-before-four-language-2026-11-09`, `archive/develop-before-four-language-2026-11-09` and `archive/candidate-before-four-language-2026-11-09` preserve branch tips.
- Old repository and old Drive three-language packages are separate under `archive/three-language/v0.2.0/` with hashes/provenance. The exact distributed four-language v0.2.1 pair is under `archive/four-language/v0.2.1/`.
- Legacy Latvian downloads remain at their original URLs and are explicitly historical.
- Previous detailed checkpoint: `docs/history/WORK_CHECKPOINT_2026-11-09_before-main.md`.

## Next action

For the next requested feature, branch from current main and follow `docs/FEATURE_DEVELOPMENT.md`. Build with the ordinary four-language configuration and preserve saved-data/module contracts. Migration and reviewer synchronization are complete; human language/clinical review and physical-device downloaded-file testing remain outstanding.

Distribution snapshot tag: `review/v0.2.4` pins the current application/package; `review/v0.2.3` preserves its predecessor. Older product branches are historical; PR #1 was closed as superseded by PR #2, with its fixes preserved in main ancestry.

## Latest documentation maintenance

9 November 2026: README now foregrounds v0.2.2, current features/downloads, CI and a preview. RELEASE_POLICY describes the implemented CI/package gates and actual answer-saving behavior, with human/device/clinical gates clearly separate. This maintenance changes no application or distributed file bytes; existing Drive readback records remain valid.

## TD coordination

- Pending requests from the owner go in [the central TD list](TD_LIST.md) on `main`. Read it together with `AGENTS.md` and this checkpoint when starting TD work; follow its conflict preflight before making changes.
- The former task to promote `main` for employer visibility is already substantially fulfilled by v0.2.2 and the updated README, so it is not an open TD task. The four-language source-link task and README portfolio improvements are completed via PR #7; only integration-denied repository metadata editing remains in TD.
- This documentation-only coordination change does not alter the current v0.2.2 reviewer HTML/PDF or their distributed hashes.


## Prior TD completion (v0.2.3)

PR #7 merged as `7684de605c5cbf619cf4ecee05ebfb676a351abd`. All 28 maintained scripts pass locally in explicit memory mode; both GitHub workflows passed with real file opening at head `ec4f4b0` (runs 42597279496 and 42597279500). The checked merge tree is identical. The app About and one-page companion guide have localized explicit GitHub links in all four languages; clinician answer PDFs exclude the link. Guide PDF has four actual repository URI annotations. README documents the actual stack and owner versus AI-assisted roles. Both v0.2.3 Drive files read back byte-identical with IDs/sharing preserved. Prior v0.2.2 package is archived. Current source is `cd854fa`; current package manifest and TD-drive-sync record hold exact hashes.

Completed TD entries were removed after verification. The sole remaining TD item is GitHub About description/topics: authenticated edits returned403 “Resource not accessible by integration.” No metadata change is assumed. Next TD action requires owner/settings access; do not repeat completed app/PDF/README work. Human language/clinical and physical-device review remain pending.


## Current creator credit and attribution

Owner clarified: AI/Codex attribution belongs in GitHub documentation only, not downloaded app/guide files. The app now displays `made by Janis Paegle GitHub 2026` with only GitHub linked immediately after the name; localized accessible labels and report exclusion remain. The old duplicate About link was removed. Current UI/catalog scan and PDF text/metadata contain no AI/Codex disclosure. The accurate repository README attribution remains intact.

PR #9 merged as `20b5adb765f8dbe3c949518a7edf9bf736e31ab6` after both GitHub workflows passed with real offline file opening (42599111309 and 42599111111). The merge tree equals checked head b602d25. All 28 local scripts passed in explicit memory mode. Both v0.2.4 Drive files read back byte-identical, preserving IDs/sharing. The guide PDF bytes are unchanged from the previously checked guide; only its versioned filename was aligned. Current source is 3a8f922. Verification/provenance: `docs/review/checks/2026-11-09-opening-guide-drive-sync.json`.

No new TD task was created: this was an explicit owner revision to the completed source-link placement. The sole repository-settings permission blocker remains unchanged.

## Update-note audience policy

The current v0.2.4 HTML was downloaded from Drive and its embedded update notes reviewed in LV/EN/RU/UK; no personal coordination or career-related entries were present. [AGENTS.md](../AGENTS.md#audience-and-privacy-in-update-notes) now limits app notes to patient/doctor-relevant changes and prohibits publishing private conversations or motives in public logs without explicit publication authorization. Feature and release instructions reference this rule. This documentation-only change adds no app note, changes no product bytes and requires no Drive replacement. The existing TD blocker and pending human/device reviews remain unchanged.

## Opening-instructions guide revision

The guide now contains HTML download/browser-opening instructions only in all four languages, with no external links or review-status statements. Seven package tests, exact-source package/ZIP verification and source-index integrity pass. The one-page PDF was rendered and visually checked. Application HTML remains `8d3dba5b3652b0d137f9c19cbfa30b9aec541dc779a576e243c09c8b89ab0b91`; new guide PDF is `6b0cfe0f3eaab3ed5360fd665053c2054e586596b6edba527e9595069b1141d4`. Prior v0.2.4 pair is preserved in `archive/four-language/v0.2.4/`. New package source: `ef965b3`; application version remains v0.2.4. No app entry is added. PR #12 merged as `fd2765b9c844321db81075e75c79e3567404ab9e` after full/app CI passed (42601226659 / 42601226670), with an identical checked merge tree. Replaced only the same Drive PDF ID; both files read back byte-identical and folder/sharing remain unchanged. Snapshot: `review/v0.2.4-guide-instructions`; previous `review/v0.2.4` tag is preserved. Next: start the next requested task from main; no further guide publication is pending.

## Privacy and medical-purpose guide revision

Added the privacy, visit-preparation/non-diagnostic purpose and professional-interpretation statements in LV/EN/RU/UK. Seven package tests and complete current-source HTML/PDF/ZIP verification pass; the one-page PDF was rendered and visually checked. App HTML, version, questions and notes are unchanged. Package source: `1c928a49c5f3475bcc04e9e5992b8bf2dd1185b2`; PDF SHA256: `b479f037a089360370aa08544ba35141dd0e39ab2ae1a39e5d8fe43c306a1ec9`. Prior pair preserved under `archive/four-language/v0.2.4-guide-instructions/`. Next: merge after PR checks, replace the existing Drive PDF and verify both downloads/sharing.
