# English and Russian editions of the Latvian questionnaire

**Plan complete · 5 November 2026.** Latvian v16 is the source. English and Russian are planned editions. This planning update changes documentation only.

**Goal.** A person downloads one HTML file in their language, selects the sections they need, and can save, resume, and prepare a report offline. A Latvian clinician can request the same section numbers in any edition.

## Files in scope

| Deliverable | Starting point | What each language needs |
|---|---|---|
| Offline questionnaire | 162_Sagatavosanas_vizitei_LV_v16.html | All 712 questions, answer choices, timeframes, 48 section titles, concern mappings and displayed labels, opening and safety text, validation messages, medication fields, accessibility labels and file instructions. |
| Reports and exports inside the HTML | Current v16 specialist report, appendix and TXT generator | Translate headings, answer/status labels, dates as displayed, print and copy text, AI instructions and embedded question reference. Preserve original user-entered names and medication text. |
| README | 163_README_LV_v16.md | Full instructions, purpose, scope, limitations, privacy, credits, feedback contact, project funding, future app plans and section index. |
| Information PDF | 147_Informacija_LV_v14.pdf | First rebuild the Latvian guide using current v16 filenames, 712 questions, actual buttons and restore flow. Generate EN and RU PDFs from those same instruction sections. Check page breaks, Cyrillic fonts and links in each PDF. |
| Change history | Revised cumulative Latvian changelog | Keep one maintained history. Generate readable EN and RU views of the same release entries and translation status. |
| Fictional example | Earlier roughly 30%-complete report | If the example is distributed, regenerate it from one synthetic v16 fixture in each language, label it fictional, and verify the actual completion count. |

Older EN/RU HTML and information PDFs may help with vocabulary. Compare every reused phrase against v16 and only distribute files labelled with the version they actually cover.

## Work order and checkpoints

1. **Freeze the source.** Record a checksum of the v16 HTML, inventory every visible string and assign stable keys. Separate patient-facing text, clinician-facing text and instructions. Update the Latvian information guide against the working questionnaire. Finish when every source file and translation key has an owner and version.
2. **Keep one implementation.** Use one navigation, validation, storage and reporting implementation. Keep translatable text in LV/EN/RU catalogs during development. Build three separate, self-contained HTML downloads. No runtime translation service, language menu or external library is needed. Generate the embedded reference, report labels and guide from the same catalog. First build LV from the shared source and rerun its existing browser journeys.
3. **Pilot both languages.** Translate the opening, safety questions, priorities, one conditional section, one medication entry, and a sample report into EN and RU directly from LV. Agree a short glossary for intent, unwanted thoughts, past action, current danger, uncertainty, declining and skipping. Check natural phrasing, timeframes, negation, response order and button lengths before translating the rest.
4. **Translate by section.** Work in small batches keyed by existing question IDs. Translate the question together with its answers and help text. Independently check sensitive wording against Latvian. For named instruments such as PHQ-9 and GAD-7, check the authorized target-language text, version and reuse conditions against primary sources before inclusion. Record provenance separately from custom questions. Mark unresolved wording for review and hold the affected edition until resolved.
5. **Build the information package.** Translate the README, revised information PDF, user-facing history, privacy/legal notice and acknowledgments. Keep the Latvia context, 112 instruction, creator/contact placement and free-project commitment consistent. Do not infer legal or clinical endorsement from translation or review.
6. **Verify each edition.** Use the same fictional answer set across LV, EN and RU. Compare IDs, option codes, order, conditional visibility, progress, answer times, missing-answer states, redaction, selection and safety review. Test actual local HTML in a browser: start, select by concern or number in the checklist, answer/skip, change sections, save JSON, reload, restore, print/copy the specialist report and download the TXT. Check UTF-8/Cyrillic, A4 output, narrow layouts, hidden messages, stale Latvian text and filenames. Verify each TXT checksum independently; translated text will give each language its own checksum.
7. **Release separately.** Mark each edition **draft**, **browser-tested**, or **language-reviewed** according to the evidence. Ask a fluent mental-health reviewer to check high-impact wording before describing that edition as professionally reviewed. Test on an actual Android phone before claiming Android verification. Publish each ready edition with its matching README and PDF. Keep unfinished or older editions clearly labelled.

## Compatibility and future updates

Question IDs, choice codes, section numbers, branching rules, safety rules, schema and machine-readable statuses stay language-independent. Store the display language as metadata. Keep sessions separate by edition and make cross-language backup import explicit. Test LV→EN, LV→RU and EN↔RU imports, plus the supported legacy cases. Preserve free text, timestamps and the original backup. A question whose meaning changes needs an explicit migration decision.

After a Latvian edit, compare source keys and flag only added or changed strings for translation. A wording-only update requires linguistic checks in context. A behavior change requires the shared browser tests in every edition. Add one dated changelog entry and identify which language editions have actually caught up.

**Next implementation checkpoint:** a verified v16 Latvian information guide, a complete text inventory and a small EN/RU pilot. No new questionnaire edition has been published by this plan.
