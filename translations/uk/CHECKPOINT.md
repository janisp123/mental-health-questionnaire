# Ukrainian translation checkpoint

Updated 9 November 2026, Riga time. Active source: `main`; previous develop isolation notes are retained only as history.

| Scope | Status |
| --- | --- |
| Questionnaire source | Latvian v16 in `src/modules/`, baseline `f25a6c1` |
| Question text | 712 of 712 translated and structurally checked |
| Interface | 126 of 126 keys drafted. Keys, types, placeholders and dated entries checked against Latvian. |
| Reviewer README | Ukrainian text drafted in `README_REVIEW.uk.md`. Button labels checked against `ui.json`. |
| Medication form | All 32 strings drafted. Nested keys, saved answer codes and clinician report labels checked. |
| Titles and report labels | 48 module titles, 15 section titles, five legacy titles and 17 question-specific report labels drafted. IDs and ordering checked. |
| Human language review and clinical review of safety wording | Pending |
| Integration and language selectors | Active in the default four-language app and report selector |

## Next action

Maintain the integrated pack from main. Validate wording/source hashes with `python translations/workspace.py check --complete`, run the active checks and verify report/recovery behavior after changes. Human language and clinical review remain pending; prioritize safety wording and applicability of support details. Integration is already complete and must not be repeated.

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
- 2026-11-08 · Drafted all 43 S06 questions in modules 07, 08, 25 and 46. Checked childhood versus current time windows, missing choice codes in the source and the distinction between speech and language.
- 2026-11-08 · Drafted all 37 S10 questions in module 15. Checked numeric ranges, standard-drink examples, different substance-use periods and current versus past withdrawal prompts against Latvian. Clinical review of the safety wording remains pending.
- 2026-11-08 · Drafted all 20 caregiving and safety questions in module 31. Checked the distinctions among hardship, unmet needs, thoughts, wishes, and intent. Flag M31_09–10 and M31_14–20 for clinical review.
- 2026-11-08 · Drafted the first 25 questions in module 32, through M32_26. Checked family and living context, age bands, and inclusive boundaries for event recency. The remaining 25 questions are pending.
- 2026-11-08 · Drafted the final 25 questions in module 32, completing S13 with 70 questions. Verified all 50 module 32 IDs and codes with the completion check. Flag childhood harm and bullying questions for human review.
- 2026-11-08 · Drafted all 19 questions in S12 module 19. Checked privacy and recency wording and made small wording corrections in module 32. Flag M19_07–08 and M19_13–15 for safety review.
- 2026-11-08 · Drafted the remaining 23 S12 questions in modules 24 and 38. Checked age and duration boundaries, the distinction between ongoing patterns and episodes, and the wording around real threats and loss.
- 2026-11-08 · Drafted 28 S14 questions in modules 20 and 28. Checked the wording on eating patterns, loss of control and worries about health. The remaining four S14 modules are pending.
- 2026-11-08 · Drafted the remaining 21 S14 questions in modules 36, 37, 44 and 45. Checked duration boundaries and distinctions between eating restrictions, body-image concerns and physical symptoms. S14 is complete.
- 2026-11-08 · Drafted all 47 S15 questions in modules 26, 27, 34 and 40. Checked cycle and postpartum boundaries, distinctions between personal and family history, and gender and sexuality wording. Flag pregnancy and postpartum safety wording for clinical review.
- 2026-11-08 · Drafted all 45 S07 questions in modules 09, 29, 39, 47 and 48. Checked distinctions among routines, compulsions, repeated urges and current safety concerns.
- 2026-11-08 · Drafted all 48 S08 questions in modules 10, 35, 41 and 42. Checked event timing, bereavement and dissociation language, and marked trauma and current danger wording for human review.
- 2026-11-08 · Drafted all 38 S02 questions in modules 02 and 05. Checked two-week frequency bands, duration boundaries and the instruction to use the same episode. Flag M02_01–09 for review of the legacy instrument wording and reuse conditions.
- 2026-11-08 · Drafted all 40 S03 questions in modules 03, 04 and 22. Checked panic-like episodes, time windows and the distinction between wanting uncertainty or distress to end and wanting life to end. Flag M03_01–07 and M22_16 for appropriate human review.
- 2026-11-08 · Drafted modules 06 and 21, including current safety, self-harm, unusual experiences, and the caution about actual violence or discrimination. The Ukrainian safety wording still needs clinical and native-language review.
- 2026-11-08 · Drafted module 18 (S05) and ran the full structural completion check for all 48 modules. Ukrainian remains in the translation workspace pending review.

- 2026-11-09 · Integrated as a normal required pack in the main-based four-language build; prior isolation notes above are historical. Human review remains pending.
