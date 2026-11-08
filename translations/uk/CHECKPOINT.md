# Ukrainian translation checkpoint

Updated 8 November 2026, Riga time. Branch `develop`.

| Scope | Status |
| --- | --- |
| Questionnaire source | Latvian v16 in `src/modules/`, baseline `f25a6c1` |
| Question text | 173 of 712 translated and structurally checked |
| Interface | 126 of 126 keys drafted. Keys, types, placeholders and dated entries checked against Latvian. |
| Reviewer README | Ukrainian text drafted in `README_REVIEW.uk.md`. Button labels checked against `ui.json`. |
| Medication form | All 32 strings drafted. Nested keys, saved answer codes and clinician report labels checked. |
| Titles and report labels | 48 module titles, 15 section titles, five legacy titles and 17 question-specific report labels drafted. IDs and ordering checked. |
| Human language review and clinical review of safety wording | Pending |
| Integration and language selectors | Disabled by isolation from the app |

## Next batch

Start S06 with module **07** (attention and activity). Then modules 08, 25 and 46.

## Checkpoint history

- 2026-11-08 · Created the isolated workspace and checked the batch export and validation commands. The first translation batch is pending.
- 2026-11-08 · Drafted the welcome, results, report and shared footer text, and the reviewer README. Checked 69 UI keys, ten dated entries, and README button labels. The support-service wording follows the Latvian source and needs verification before integration.
- 2026-11-08 · Drafted the remaining 57 interface keys. Checked all 126 keys and placeholders, and tested the Ukrainian section selector, question controls and save flow in an isolated Chromium fixture.
- 2026-11-08 · Drafted all 32 medication form strings. Checked nested keys and tested saving a synthetic entry and rendering its Ukrainian labels in the clinician report.
- 2026-11-08 · Drafted module and section titles, legacy titles and question-specific report labels. Checked all IDs against their source catalogs. Next is the first question batch.
- 2026-11-08 · S11 modules 23 and 33 complete (21 and 10 questions). Checked every ID, answer code and source hash. Review the wording about privacy, sensitive identity and readiness for help with a fluent reviewer.
- 2026-11-08 · Drafted S11 modules 43, 16 and 17, completing all five source modules for S11. Checked all 62 records, including digital-use duration boundaries and the distinction between lifetime and past-year gambling.
- 2026-11-08 · Drafted all 23 questions in S01 module 01. Checked clinical-history wording and inclusive time boundaries against Latvian. Diagnosis names require human review.
- 2026-11-08 · Drafted modules 14 and 30, completing S01. Checked all 61 S01 records. Flag M14_21 for a fluent and clinical comparison: Ukrainian uses the involuntary-movement meaning of the existing English wording. Emergency, medication and neurological wording also needs clinical review.
- 2026-11-08 · Drafted all 50 S09 questions across modules 11, 12 and 13. Checked response counts, inclusive and exclusive time boundaries, and distinctions between sleepiness, fatigue and pain. Flag sleep-related safety wording for clinical review.
