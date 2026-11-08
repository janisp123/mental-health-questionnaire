# Ukrainian translation checkpoint

Updated 8 November 2026, Riga time. Branch `develop`.

| Scope | Status |
| --- | --- |
| Questionnaire source | Latvian v16 in `src/modules/`, baseline `f25a6c1` |
| Question text | 0 of 712 translated and structurally checked |
| Interface, medication form, section titles, report labels and guide | Pending |
| Human language review and clinical review of safety wording | Pending |
| Integration and language selectors | Disabled by isolation from the app |

## Next batch

Start with module **23** in section **S11**, positions **1–10** in module order.

```text
python translations/workspace.py source 23 --start 1 --limit 10
```

Save the translated entries in `questions/23.json`, run `python translations/workspace.py check 23`, then record the IDs and next position here. Module 23 has 21 questions.

## Checkpoint history

- 2026-11-08 · Created the isolated workspace and checked the batch export and validation commands. The first translation batch is pending.
