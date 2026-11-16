# Adding features without restructuring the app

There is one active application, built from main. Its initial locale is Latvian and its configured locales are LV/EN/RU/UK. Create short-lived branches from main and merge tested changes back through a PR. Versioned packages identify distributed snapshots; old branches and archives are history, not parallel products.

## Module boundaries

| Responsibility | Existing interface | Change boundary |
|---|---|---|
| Question lookup and visibility | `QuestionnaireModel.create(data)` in `core/model.js` | Consume the bundle and session state; return lookup/visibility/progress results. Preserve question identity and condition semantics. |
| Answer/navigation transitions | `QuestionnaireFlow` in `core/answer-flow.js` | Return navigation destinations; DOM rendering belongs to screens/coordinator. |
| Recovery compatibility | `QuestionnaireRecovery.validate(payload, options)` | Validate and normalize explicit record kinds. Introduce an explicit migration and old-format fixture before changing saved data. Reject unsupported data rather than silently deleting it. |
| Events | `QuestionnaireEvents.bind(app, handlers)` | Delegate DOM events to named injected handlers; feature logic stays out of the dispatcher. |
| Screens and new answer controls | `QuestionnaireScreens` in `screens/` | Accept explicit data/labels/callbacks and return markup. Preserve escape handling and meaningful accessible controls. |
| Reports | `QuestionnaireReports` in `reports/reports.js` | Read normalized answers or separately submitted feedback. Keep clinician and feedback inputs separate and typed text unchanged. |
| Packaging | `build_bundle()`, `make_html()`, package CLI | Assemble validated data, shared runtime and a matching guide into the offline artifact. |

`core/app.js` coordinates session state and existing modules. A feature may add a small integration call here; substantial behavior belongs in a focused module. Keep the existing APIs stable where practical. Add optional parameters compatibly; update all callers and contract tests when a necessary API change is made.

## Adding a feature

1. Describe its input, output, saved-data effects and existing behavior it must preserve.
2. Add a focused failing regression at the relevant module boundary. Use real renderers/runtime and synthetic data.
3. Add the module or component to the explicit order in `src/app/build.json`; connect it through the existing coordinator/event interface.
4. Add wording for every active locale. Read the language style guide. Shared user-facing changes require an update note in all active catalogs. Follow the [audience and privacy rules](../AGENTS.md#audience-and-privacy-in-update-notes): describe patient/doctor-relevant changes only; repository-only maintenance does not create an app entry.
5. If adding an answer kind, update validation, save/restore, reports and synthetic legacy/current fixtures together. Preserve question IDs/codes and add an explicit version migration if the saved representation changes.
6. Run focused checks, then `python tools/run_checks.py` for shared behavior changes. Build/verify the package and review its PDF before distribution.

Do not add a generic plugin framework or move all files in anticipation of unspecified features. Extract a reusable component when concrete features share behavior. A fifth language uses another validated pack and the configured registry; it does not require another application engine.

## Data contracts

- Public invitation sharing uses `QuestionnaireSharing` with localized interface text and a fixed project URL only. Never pass answers, report markup, recovery files, identity or saved feedback to sharing/clipboard payload creation. Device sharing/copying requires a deliberate action; manual selection stays available when APIs are unavailable or reject the request. Public sharing controls must remain outside printed clinician reports.
- Clinician output includes every provided response, including negative, uncertain and refused choices. Only missing/skipped/blank records are omitted. Summary/section progress retains its own coverage counts; the clinician header reports only included entries and explains that omissions are not negative responses.

- Question identity, answer codes, conditions and ordering come from `src/modules/` plus explicit presentation rules. Frozen LV/EN/RU source records stay byte-verified; added languages provide wording by ID/code.
- Active UI/report languages come from the built bundle's `ui` registry. Avoid new hardcoded three-language loops in active-app code or tests.
- Saved answer kinds are `choice`, `text`, `medicine` and `skip`; the recovery schema remains `mental-pilot-recovery-v1`. Clinical meaning is never inferred from a record kind or numeric score.
- Unsaved question drafts and feedback drafts are session state. Unsubmitted feedback must not enter backups or either report. Saved feedback has its own reason codes, locale and comment metadata.
- The app is self-contained and offline. New behavior must preserve the no-network boundary unless an independently approved feature explicitly changes it.

## Current package and publication

`python tools/build_questionnaire.py` builds the current four-language HTML. `python tools/build_review_package.py --output-dir dist/review-<version>` produces HTML/PDF/ZIP plus checksums. The destination must not already exist. `python tools/verify_review_package.py <folder> --with-zip` checks generated bytes against the current source.

Commit source changes before producing a distribution package. The manifest records source commit/tree and whether relevant source was dirty. HTML/PDF/ZIP bytes are deterministic with the pinned toolchain/fonts/epoch. A later merge commit may have a different SHA while preserving the tested source tree; record both instead of relabelling the build's provenance.

`MH_Public_version/` contains the current HTML/PDF and machine manifest. Editable guide text stays in `docs/review/GUIDE_LV_EN_RU_UK.md`. Drive shows only the HTML and PDF, with their stable IDs. Replacing Drive files is deliberate: verify the package first, replace in place, compare downloaded readback hashes, and record synchronization. Routine source commits do not upload automatically.

## Verification limits

CI uses real offline file opening. If a managed browser blocks `file://`, run `python tools/run_checks.py --load-mode memory` and retain that mode in the evidence. Memory loading does not verify physical-device downloaded-file behavior. Human translation, clinical review and device checks retain their actual status independently of main adoption.

## Country-neutral emergency notices

`src/questionnaire/local-emergency-notices.json` supplies only the displayed `time` text for M15_19, M18_13 and M30_17 after locale packs load. It replaces country-specific emergency-number references while retaining time windows, symptoms and urgent-care instructions. Frozen source/translation packs, titles, IDs, choices and conditions remain unchanged. Every active locale must have a notice; missing/number-specific notices fail the build. `tests/full_bank/test_worldwide_support.py` checks this narrow difference and the answer contracts.

`src/questionnaire/panic-peak-clarification.json` adds a localized help explanation to M04_01 after locale packs load. Its title, time window, choices and conditions remain frozen; every active locale must have an explanation.

## Clinician report review priority

`src/questionnaire/report-priority.json` supplies complete ID/code editorial order metadata validated by the builder. `reports/review-priority.js` sorts newly constructed report entries without mutating question/answer/progress objects. All clinician renderers share it; feedback keeps its original order. Related condition/named context stays together and original order breaks ties. Values are internal 1–5 review positions, not a clinical score or triage tool; clinical review remains pending. See [policy and limits](review/REPORT_REVIEW_PRIORITY.md).

`src/questionnaire/appointment-guidance.json` adds localized optional help to M14_02 (medicine observations/timing) and M02_09 (finding separate safety questions) after language packs load. Existing question titles, answer codes, conditions, support triggers and reports retain their original contracts.

## Hosted and downloaded questionnaire

The Pages builder copies the current `MH_Public_version/` HTML verbatim to `questionnaire/index.html`; the app retains its existing language selector, progress format and browser-local processing. Landing pages expose separate online-open and stable Drive-folder download actions. `--require-verified-distribution` gates publication on the matching project-manifest Drive record. Release delivery evidence named `docs/review/checks/*-drive-sync.json` triggers automatic website refresh after verified Drive updates. Local previews can build without that publication gate; they are not delivery evidence.

`src/questionnaire/m46-additions.json` adds three independent M46 items after M46_03 without altering the 712 frozen source records. The builder validates unique IDs/orders, complete active-language wording and answer contracts before applying neutral draft report priorities. The current active total is recorded in the build/package manifest.

`QuestionnaireFeedbackDelivery.composeQuestion` reads one current feedback draft and its question only; immediate email/copy actions do not enqueue feedback or change medical answers/navigation. Opening the flag pauses any pending single-choice timer while retaining the choice. Save-for-later retains its established save/advance behavior.

`src/questionnaire/m06-responsibility-context.json` owns M06_25 wording/codes and its report metadata. `apply_m06_responsibility_context(bundle, priority)` inserts it after M06_24 into the existing section and current-safety report family. A=4 and B–F=3 are draft editorial review positions only; there is no new emergency trigger or score. Existing progress imports without this ID remain valid. Before rolling back to an older app, retain a reader or use an explicitly reviewed migration for newer exports containing M06_25; never silently discard the response.

`src/questionnaire/m06-action-history.json` owns M06_26/27, inserted after M06_09 by `apply_m06_action_history`. M06_26 is independent of earlier No answers and uses the most recent occasion for its intent distinction. M06_27 uses unchanged recency choices and appears only for affirmative A–D. The ordinary context-parent report grouping keeps the pair together without adding it to the named suicide-attempt family. No new emergency prompt or recovery format is introduced. Newer exports require a retained reader/explicit migration if rolling back these IDs; never discard responses silently.
