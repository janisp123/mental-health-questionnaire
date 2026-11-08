# Ukrainian translation checkpoint

Updated 8 November 2026, Riga time. Branch `develop`.

| Scope | Status |
| --- | --- |
| Questionnaire source | Latvian v16 in `src/modules/`, baseline `f25a6c1` |
| Question text | 0 of 712 translated and structurally checked |
| Interface | 69 of 126 keys drafted and checked for matching types. Covers the welcome, results and report screens and the shared footer. |
| Reviewer README | Ukrainian text drafted in `README_REVIEW.uk.md`. Button labels checked against `ui.json`. |
| Remaining localization | 57 interface keys, medication form, module and section titles, and question-specific report labels. |
| Human language review and clinical review of safety wording | Pending |
| Integration and language selectors | Disabled by isolation from the app |

## Next batch

Continue with the remaining interface keys in `ui.json`, starting with the section selector, question navigation and save controls. Compare key names against `src/app/i18n/ui.lv.json` without loading the question modules.

Finish the other localization files before starting the question modules. The first question batch will be module **23**, positions **1–10** in module order.

## Checkpoint history

- 2026-11-08 · Created the isolated workspace and checked the batch export and validation commands. The first translation batch is pending.
- 2026-11-08 · Drafted the welcome, results, report and shared footer text, and the reviewer README. Checked 69 UI keys, ten dated entries, and README button labels. The support-service wording follows the Latvian source and needs verification before integration.
