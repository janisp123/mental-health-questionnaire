# UX, support and reports — implementation plan

Status: IN_PROGRESS. User's supplied design and implementation workflow are the approved scope. Work only on develop; no release or frozen reference edits.

1. Preserve the current 60-question pilot inventory and add acceptance checks. Introduce separate presentation layout and answer-priority metadata. Keep source logic and all three original translations byte-identical. Test against frozen sources, including deliberately damaged answer mappings.
2. Build compact standalone AI/doctor reports. Preserve actual response text, periods, uncertainty/refusal and context. Doctor entries ascend by per-answer presentation priority; no totals or visible priority labels. Unknown/refused are unrated, placed after ordinary information, never assigned zero. Test deterministic ordering, exclusions, escaping and response fidelity.
3. Apply optional thematic presentation, personal details last, automatic single-choice advancement, guarded taps, manual multi/text save, fixed Skip/Back, accessible persistent support, legacy recovery migration and bottom-only tools/guide/version notes. Test source/structural checks and browser journeys.
4. Run full regression suite on develop CI, inspect actual results, correct failures, update architecture/index/changelog with exact commits. Native Android and human translation/clinical review remain unverified. Mark TASK_DONE only when implemented pilot scope passes; imported remaining bank is not implemented by this task.

## Decisions and verification boundaries
- Original source grouping can remain as storage; a separate layout maps each question exactly once to a display topic. No edited original order or conditions.
- Report priorities are individually reviewable editorial metadata, not clinical validation. Null means unrated. No aggregate computation.
- Existing recorded responses hidden by changed conditions are excluded from current exports; preserved in recovery. Explicitly recorded uncertain/refused answers remain in export.
- Browser downloads failed locally (invalid/truncated Chromium archive). Use CI browser results if a local browser cannot be installed. Desktop Chromium never establishes native Android behavior.
- Support sources checked 2026-11-06: NVD https://www.vmnvd.gov.lv/lv/vienotais-bezmaksas-krizu-talrunis-116-123 (free 24/7, LV/EN/RU); VUGD https://www.vugd.gov.lv/lv/vienotais-arkartas-palidzibas-izsaukuma-numurs-112 (immediate danger). Hotline tool also verified Latvia adult 116123 availability.
