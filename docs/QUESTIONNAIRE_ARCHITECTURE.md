# Current questionnaire architecture

One four-language offline application is maintained on main. The normal build assembles 712 questions from 48 unchanged source modules into 15 optional sections. Latvian is the reference and initial interface language.

| Area | Responsibility |
|---|---|
| `src/modules/` | Frozen canonical LV/EN/RU source bank, IDs/codes/conditions; filenames describe source provenance. |
| `translations/uk/` | Active Ukrainian question/UI/medicine/section/report pack validated against the source. |
| `src/app/core/` | Model lookup/visibility, answer transitions, recovery validation, event routing and coordinator. |
| `src/app/screens/` | Focused data-driven screen/answer-control renderers. |
| `src/app/styles/` | Ordered layout, feedback, report and safe-area styles. |
| `src/app/reports/` | Clinician answers and separately submitted project feedback. |
| `src/app/i18n/` | Base LV/EN/RU UI and medicine catalogs. |
| `src/questionnaire/` | The single current build config, section layout and explicit report presentation rules. |
| `tools/` | Offline builder, deterministic package builder/verifier and maintained check runner. |
| `MH_Public_version/` | Current HTML, matching PDF and machine-readable provenance/checksums. |
| `archive/` | Immutable prior reviewer packages/build profiles; never default build inputs. |
| `reference/` | Unchanged imported reference baselines and historical source records. |

See [feature development contracts](FEATURE_DEVELOPMENT.md) before adding modules or altering saved data. Extend the explicit app build manifest and existing APIs; keep feature logic out of the coordinator when it warrants a separate module. There is no second engine for Ukrainian or for future languages.

The ordinary command `python tools/build_questionnaire.py` creates `dist/QUESTIONNAIRE_LV_EN_RU_UK_NOT_RELEASED.html`. `python tools/build_review_package.py --output-dir dist/review-<version>` creates its HTML/PDF/ZIP/checksum package from committed sources. The editable guide is `docs/review/GUIDE_LV_EN_RU_UK.md`; fonts and PDF dependency are pinned. Existing package destinations are refused.

`python tools/run_checks.py` runs active app/full-bank/translation/package tests and JavaScript syntax checks. CI runs on main and PRs to main. Tests distinguish immutable three-language source fidelity from four-language application completeness, and preserve legacy recovery compatibility with `mental-pilot-recovery-v1`. The layout sweep covers every question in each active language at 320/390 pixels.

The app contains its runtime and question data and sends no network requests. Answers and unsubmitted feedback stay in the session; save/restore and report generation are explicit. Technical verification does not establish human language review, clinical validation or physical-device compatibility. Managed-browser memory loading is explicitly labelled in test reports.
