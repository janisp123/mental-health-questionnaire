# Current working checkpoint

Updated 9 November 2026. Owner approved the four-language main migration. Integration branch: `codex/promote-four-language-main`; main promotion and Drive synchronization are pending in this checkpoint.

## Active product

- Sole maintained product: LV/EN/RU/UK, 712 questions, 48 immutable source modules, 15 sections. Latvian remains the reference and initial language.
- Default configuration: `src/questionnaire/build.json`, technical-review version `0.2.2-review+full-bank`.
- Source history includes old main, develop’s two future-idea documentation changes, the four-language fixes and the approved plan.
- Stable feature/module contracts: `docs/FEATURE_DEVELOPMENT.md`. Extend focused modules and current APIs; preserve IDs and saved-data compatibility.

## Verification and artifacts

- `python tools/run_checks.py --load-mode memory`: 28 checks pass, including 5,696 question/locale/phone-width renders and legacy recovery import. Direct file opening is blocked in this managed Chromium; GitHub CI is configured to run real offline file opening.
- `MH_Public_version/manifest.json` records the exact repository HTML/PDF hashes and source commit/tree. Package source commit: `e2ce2fa86749012e8336eccca9c89898df3df69f`; source was clean when built.
- Package CLI tests verify byte-identical repeated HTML/PDF/ZIP builds and refusal to overwrite. PDF has one A4 page and was visually inspected.
- New package is verified locally; Drive still contains the verified four-language v0.2.1 pair until promotion/update readback is recorded.

## History and rollback

- Immutable tags `archive/main-before-four-language-2026-11-09`, `archive/develop-before-four-language-2026-11-09` and `archive/candidate-before-four-language-2026-11-09` preserve branch tips.
- Old repository and old Drive three-language packages are separate under `archive/three-language/v0.2.0/` with hashes/provenance. The exact distributed four-language v0.2.1 pair is under `archive/four-language/v0.2.1/`.
- Legacy Latvian downloads remain at their original URLs and are explicitly historical.
- Previous detailed checkpoint: `docs/history/WORK_CHECKPOINT_2026-11-09_before-main.md`.

## Next action

Complete independent review and GitHub checks, merge the migration into main, verify the resulting tree, then update the same two Drive file IDs with the checked package and record readback hashes. Preserve all sharing settings and reviewer links. Human language/clinical review and physical-device downloaded-file testing remain outstanding.
