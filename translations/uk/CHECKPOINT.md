# Ukrainian translation checkpoint

Updated 8 November 2026, Riga time. Branch `develop`.

| Scope | Status |
| --- | --- |
| Questionnaire source | Latvian v16 in `src/modules/`, baseline `f25a6c1` |
| Question text | 0 of 712 translated and structurally checked |
| Interface | 126 of 126 keys drafted. Keys, types, placeholders and dated entries checked against Latvian. |
| Reviewer README | Ukrainian text drafted in `README_REVIEW.uk.md`. Button labels checked against `ui.json`. |
| Remaining localization | Medication form, module and section titles, and question-specific report labels. |
| Human language review and clinical review of safety wording | Pending |
| Integration and language selectors | Disabled by isolation from the app |

## Next batch

Translate the medication form using `src/app/i18n/medicine.lv.json` and save it as `medicine.json` in this workspace. Check nested keys and labels before moving to module and section titles.

Finish the other localization files before starting the question modules. The first question batch will be module **23**, positions **1–10** in module order.

## Checkpoint history

- 2026-11-08 · Created the isolated workspace and checked the batch export and validation commands. The first translation batch is pending.
- 2026-11-08 · Drafted the welcome, results, report and shared footer text, and the reviewer README. Checked 69 UI keys, ten dated entries, and README button labels. The support-service wording follows the Latvian source and needs verification before integration.
- 2026-11-08 · Drafted the remaining 57 interface keys. Checked all 126 keys and placeholders, and tested the Ukrainian section selector, question controls and save flow in an isolated Chromium fixture.
