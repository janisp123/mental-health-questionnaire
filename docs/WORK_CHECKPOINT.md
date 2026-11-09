# Current working checkpoint

Updated 9 November 2026. Migration DONE. Sole active source: `main`. Promotion PR #2 merged as `1a68d31f385208263be79de5da8c27e3df90354a`; its tree exactly matches the checked head `505187b9b127fe375dafab9b3e341cf4d863ac3b`.

## Active product

- Sole maintained product: LV/EN/RU/UK, 712 questions, 48 immutable source modules, 15 sections. Latvian remains the reference and initial language.
- Default configuration: `src/questionnaire/build.json`, technical-review version `0.2.2-review+full-bank`.
- Source history includes old main, develop’s two future-idea documentation changes, the four-language fixes and the approved plan.
- Stable feature/module contracts: `docs/FEATURE_DEVELOPMENT.md`. Extend focused modules and current APIs; preserve IDs and saved-data compatibility.

## Verification and artifacts

- All 28 maintained scripts pass locally in explicit memory mode, including 5,696 question/locale/phone-width renders and legacy recovery import. Both final GitHub workflows passed with real offline file opening (runs 42586610302 and 42586610292). Physical-device testing is separate.
- `MH_Public_version/manifest.json` records the exact repository HTML/PDF hashes and source commit/tree. Package source commit: `e2ce2fa86749012e8336eccca9c89898df3df69f`; source was clean when built.
- Package CLI tests verify byte-identical repeated HTML/PDF/ZIP builds and refusal to overwrite. PDF has one A4 page and was visually inspected.
- Repository and Drive contain the same verified four-language v0.2.2 HTML/PDF pair. Both downloads matched exact hashes; existing IDs, folder and sharing are preserved. Evidence: `docs/review/checks/2026-11-09-main-drive-sync.json`.

## History and rollback

- Immutable tags `archive/main-before-four-language-2026-11-09`, `archive/develop-before-four-language-2026-11-09` and `archive/candidate-before-four-language-2026-11-09` preserve branch tips.
- Old repository and old Drive three-language packages are separate under `archive/three-language/v0.2.0/` with hashes/provenance. The exact distributed four-language v0.2.1 pair is under `archive/four-language/v0.2.1/`.
- Legacy Latvian downloads remain at their original URLs and are explicitly historical.
- Previous detailed checkpoint: `docs/history/WORK_CHECKPOINT_2026-11-09_before-main.md`.

## Next action

For the next requested feature, branch from current main and follow `docs/FEATURE_DEVELOPMENT.md`. Build with the ordinary four-language configuration and preserve saved-data/module contracts. Migration and reviewer synchronization are complete; human language/clinical review and physical-device downloaded-file testing remain outstanding.

Distribution snapshot tag: `review/v0.2.2` pins the promoted application/package. Older product branches are historical; PR #1 was closed as superseded by PR #2, with its fixes preserved in main ancestry.

## Latest documentation maintenance

9 November 2026: README now foregrounds v0.2.2, current features/downloads, CI and a preview. RELEASE_POLICY describes the implemented CI/package gates and actual answer-saving behavior, with human/device/clinical gates clearly separate. This maintenance changes no application or distributed file bytes; existing Drive readback records remain valid.
