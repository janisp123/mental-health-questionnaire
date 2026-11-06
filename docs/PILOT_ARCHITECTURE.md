# Editing the offline pilot v0.2

The develop-only default pilot implements 60 original questions in LV/EN/RU. All topics are optional, ordered 23, 02, 21, 06, 18, 31, 33. Personal details are last. Sections 02 and 21 are complete within this pilot; the other topics contain only the former opening questions, not their complete imported modules. The builder also has an opt-in full-bank mode that packages all 712 source questions in 48 optional groups. That mode is a build/data milestone; full 712-question runtime behavior still needs separate verification. EN/RU and new interface/report wording need human review.

## Source, layout and presentation

- `src/pilot/modules/registry.json` registers storage groups (opening, 02, 21). Their original logic, IDs, order, answer codes, statuses, conditions and three locale files remain unchanged.
- `src/pilot/modules/layout.json` defines display order and titles. The builder distributes the old opening items by their original `originModule`, without modifying original order. All display groups are optional. New registered modules append without engine changes. Parent conditions must precede follow-ups in both source and display order.
- `src/pilot/reports/presentation.json` holds independently reviewable, provisional answer-specific priorities, concise labels and support triggers. It never changes source answers. Unknown/refused responses have null priority; skipped/missing responses also return null, and are excluded from report entries. Null entries are placed after ordinary information, before weighted difficulties; that placement is not a severity claim.
- Priorities 0–3 order individual answered entries only. Multiple selections retain every chosen answer and use the highest explicit presentation priority. No total, probability, diagnosis or automatic clinical risk category is calculated. Past experiences, current thoughts, intentions and preparations retain their original time/context and distinct rules. No cross-question clinical inference is made. Future clinicians can review the metadata against original answer wording.
- `src/pilot/i18n/ui.{lv,en,ru}.json` contains shared interface/support/report instructions. Source question translations remain in their original modules. Never edit frozen v16 to make fidelity checks pass.

## Answering and recovery

Single-choice activation saves and advances immediately. A 500 ms answer-only lock and double-click filtering stop a second accidental activation; Skip is never locked. Multi-choice/text entries retain manual save. Back returns to the previous applicable item and allows changing or keeping an answer. Subsequent navigation follows applicable display order, including previously saved/skipped items.

Skip is centered in a fixed bottom navigation bar with Back and Support. The question pane reserves the navigation viewport, including safe-area space. Individual Skip advances without confirmation. Section skip and finish retain their existing confirmations. Source statuses remain distinct; a skip never becomes No.

The pilot-v1 recovery schema remains supported. New files include `layoutVersion`. Old files omitted their implicitly mandatory opening topic; restore maps that topic to its new optional groups without changing answers. Legacy review queues remain resumable. Invalid/unknown codes, conflicting choices, unknown sections and malformed records are rejected before replacing the session. Out-of-pilot full v16 recovery files still require a separate migration policy. Answers stay in session memory and explicitly downloaded files; there is no server, local-storage autosave, analytics or network request. Cumulative recovery downloads still occur every ten individual saves/skips.

## Support and reports

Support is an accessible persistent nonmodal card after a relevant saved answer, including automatic advancement. It is focused for assistive technology, remains until dismissed, and avoids repeating an identical prompt. An explicit immediate-danger response can surface emergency guidance after an earlier general support message. Help is always available through the navigation and a footer disclosure. Nothing contacts anyone automatically.

Verified 2026-11-06: Latvia's NVD describes 116 123 as free and available 24/7 in Latvian, English and Russian: https://www.vmnvd.gov.lv/lv/vienotais-bezmaksas-krizu-talrunis-116-123 . The hotline lookup also confirmed adult availability. VUGD describes 112 for immediate threats to life, health and safety: https://www.vugd.gov.lv/lv/vienotais-arkartas-palidzibas-izsaukuma-numurs-112 . The interface distinguishes emergency assistance from emotional support.

AI export contains only recorded responses in ordinary text, independently understandable labels, original selected answer wording and original time periods. It includes an omission note and a short non-diagnostic instruction. No IDs, codes, JSON, decoding key or separate upload is needed. Explicit uncertainty/refusal is retained. Personal text is included when provided: the user can read the export before choosing to share it.

Doctor output contains the same actual responses, compact coverage counts and ascending presentation priorities, with stable topic order within ties. There is no alert summary, warning icon, numerical weight or risk score. It flows across A4 pages in black and white. If only sensitive responses were provided, no ordinary responses are invented to fill the first page. Existing TXT and decoding-key downloads remain available separately.

Recorded applicable responses remain in reports even when their topic is deselected. Responses hidden by changed conditions stay in recovery but are excluded from current reports; the doctor report explains this. The default pilot counts cover applicable pilot questions; full-bank runtime report behavior has not been audited. Tools, progress, in-app usage guide, version history, legal/privacy and contributors are below the main content, collapsed by default. A separate user README is not needed for this artifact; frozen release documentation is unchanged.

## Build and verification

`python tools/build_pilot.py` builds `dist/PILOT_offline_LV_EN_RU_v0.2_NOT_RELEASED.html`. `python tools/build_pilot.py --full-bank` builds `dist/FULL_BANK_offline_LV_EN_RU_NOT_RELEASED.html` from the frozen source modules. Both are test prototypes, not public releases. CI stores the default pilot as a test artifact; the full-bank build is structurally checked but not published.

Run:

- `python tools/verify_project_index.py` — all 79 imported files, 48 module hashes, 712 original IDs/orders (requires the full repository).
- `python tests/pilot/test_build.py` — source structure, three language keys and offline package.
- `python tests/pilot/test_source_fidelity.py` — every active original field/translation against frozen v16, plus deliberate swapped-label rejection.
- `python tests/pilot/test_layout.py` — fixed 60-ID scope, optional display topics, personal details last.
- `node tests/pilot/test_reports.js` — per-answer metadata coverage, actual text/time, ascending order, null statuses, HTML escaping and all three output languages.
- `node --check src/pilot/core/app.js` and `node --check src/pilot/reports/reports.js`.
- With Playwright Chromium: `test_browser.py`, `test_independence.py`, `test_section21.py` under `tests/pilot/` — actual offline browser answering, double taps, skip/back, recovery, copy/print/export, support, module independence, conditions, invalid restore and source-to-output mapping.

Desktop Chromium checks are not native Android verification. Remaining manual checks: downloaded-file opening, touch/keyboard behavior and fixed navigation with Android browser controls, every-ten-answer downloads, file-picker restoration, clipboard and multi-page printing. Translation review and clinical review of source wording/presentation rules remain outstanding. See `docs/CHANGELOG.md` for exact verified commits and CI runs.
