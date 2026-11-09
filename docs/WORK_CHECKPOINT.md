# Current working checkpoint

Updated 9 November 2026. Migration DONE. Sole active source: `main`. Promotion PR #2 merged as `1a68d31f385208263be79de5da8c27e3df90354a`; its tree exactly matches the checked head `505187b9b127fe375dafab9b3e341cf4d863ac3b`.

## Active product

- Sole maintained product: LV/EN/RU/UK, 712 questions, 48 immutable source modules, 15 sections. Latvian remains the reference and initial language.
- Default configuration: `src/questionnaire/build.json`, technical-review version `0.2.3-review+full-bank`.
- Source history includes old main, develop’s two future-idea documentation changes, the four-language fixes and the approved plan.
- Stable feature/module contracts: `docs/FEATURE_DEVELOPMENT.md`. Extend focused modules and current APIs; preserve IDs and saved-data compatibility.

## Verification and artifacts

- All 28 maintained scripts pass locally in explicit memory mode, including 5,696 question/locale/phone-width renders and legacy recovery import. Both final GitHub workflows passed with real offline file opening (runs 42586610302 and 42586610292). Physical-device testing is separate.
- `MH_Public_version/manifest.json` records the exact repository HTML/PDF hashes and source commit/tree. Package source commit: `cd854fa8315443e7fca8c5a86cbd12152b1b9fbc`; source was clean when built.
- Package CLI tests verify byte-identical repeated HTML/PDF/ZIP builds and refusal to overwrite. PDF has one A4 page and was visually inspected.
- Repository and Drive contain the same verified four-language v0.2.3 HTML/PDF pair. Both downloads matched exact hashes; existing IDs, folder and sharing are preserved. Evidence: `docs/review/checks/2026-11-09-td-drive-sync.json`.

## History and rollback

- Immutable tags `archive/main-before-four-language-2026-11-09`, `archive/develop-before-four-language-2026-11-09` and `archive/candidate-before-four-language-2026-11-09` preserve branch tips.
- Old repository and old Drive three-language packages are separate under `archive/three-language/v0.2.0/` with hashes/provenance. The exact distributed four-language v0.2.1 pair is under `archive/four-language/v0.2.1/`.
- Legacy Latvian downloads remain at their original URLs and are explicitly historical.
- Previous detailed checkpoint: `docs/history/WORK_CHECKPOINT_2026-11-09_before-main.md`.

## Next action

For the next requested feature, branch from current main and follow `docs/FEATURE_DEVELOPMENT.md`. Build with the ordinary four-language configuration and preserve saved-data/module contracts. Migration and reviewer synchronization are complete; human language/clinical review and physical-device downloaded-file testing remain outstanding.

Distribution snapshot tag: `review/v0.2.3` pins the current application/package; `review/v0.2.2` preserves its predecessor. Older product branches are historical; PR #1 was closed as superseded by PR #2, with its fixes preserved in main ancestry.

## Latest documentation maintenance

9 November 2026: README now foregrounds v0.2.2, current features/downloads, CI and a preview. RELEASE_POLICY describes the implemented CI/package gates and actual answer-saving behavior, with human/device/clinical gates clearly separate. This maintenance changes no application or distributed file bytes; existing Drive readback records remain valid.

## TD coordination

- Pending requests from the owner go in [the central TD list](TD_LIST.md) on `main`. Read it together with `AGENTS.md` and this checkpoint when starting TD work; follow its conflict preflight before making changes.
- The former task to promote `main` for employer visibility is already substantially fulfilled by v0.2.2 and the updated README, so it is not an open TD task. The four-language source-link task and README portfolio improvements are completed via PR #7; only integration-denied repository metadata editing remains in TD.
- This documentation-only coordination change does not alter the current v0.2.2 reviewer HTML/PDF or their distributed hashes.


## Latest TD completion

PR #7 merged as `7684de605c5cbf619cf4ecee05ebfb676a351abd`. All 28 maintained scripts pass locally in explicit memory mode; both GitHub workflows passed with real file opening at head `ec4f4b0` (runs 42597279496 and 42597279500). The checked merge tree is identical. The app About and one-page companion guide have localized explicit GitHub links in all four languages; clinician answer PDFs exclude the link. Guide PDF has four actual repository URI annotations. README documents the actual stack and owner versus AI-assisted roles. Both v0.2.3 Drive files read back byte-identical with IDs/sharing preserved. Prior v0.2.2 package is archived. Current source is `cd854fa`; current package manifest and TD-drive-sync record hold exact hashes.

Completed TD entries were removed after verification. The sole remaining TD item is GitHub About description/topics: authenticated edits returned403 “Resource not accessible by integration.” No metadata change is assumed. Next TD action requires owner/settings access; do not repeat completed app/PDF/README work. Human language/clinical and physical-device review remain pending.
