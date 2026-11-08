# Ukrainian translation checkpoint

Updated 8 November 2026, Riga time. Branch `develop`.

| Scope | Status |
| --- | --- |
| Questionnaire source | Latvian v16 in `src/modules/`, baseline `f25a6c1` |
| Question text | 0 of 712 translated and structurally checked |
| Interface | 126 of 126 keys drafted. Keys, types, placeholders and dated entries checked against Latvian. |
| Reviewer README | Ukrainian text drafted in `README_REVIEW.uk.md`. Button labels checked against `ui.json`. |
| Medication form | All 32 strings drafted. Nested keys, saved answer codes and clinician report labels checked. |
| Titles and report labels | 48 module titles, 15 section titles, five legacy titles and 17 question-specific report labels drafted. IDs and ordering checked. |
| Human language review and clinical review of safety wording | Pending |
| Integration and language selectors | Disabled by isolation from the app |

## Next batch

Start question module **23**, positions **1–10** in module order. Export only the next batch with `python translations/workspace.py source 23 --start 1 --limit 10`.

## Checkpoint history

- 2026-11-08 · Created the isolated workspace and checked the batch export and validation commands. The first translation batch is pending.
- 2026-11-08 · Drafted the welcome, results, report and shared footer text, and the reviewer README. Checked 69 UI keys, ten dated entries, and README button labels. The support-service wording follows the Latvian source and needs verification before integration.
- 2026-11-08 · Drafted the remaining 57 interface keys. Checked all 126 keys and placeholders, and tested the Ukrainian section selector, question controls and save flow in an isolated Chromium fixture.
- 2026-11-08 · Drafted all 32 medication form strings. Checked nested keys and tested saving a synthetic entry and rendering its Ukrainian labels in the clinician report.
- 2026-11-08 · Drafted module and section titles, legacy titles and question-specific report labels. Checked all IDs against their source catalogs. Next is the first question batch.
