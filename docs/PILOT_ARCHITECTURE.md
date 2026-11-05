# Editing the offline pilot

The editable pilot on develop has the required 20-question opening and optional 21-question mood section. LV v16 is the frozen behavioral reference. The EN/RU text is an unreviewed draft. The artifact is a development build.

## Change one translation

Edit the question under its stable ID in `src/pilot/modules/{id}/en.json` (or the corresponding LV/RU file). Each locale owns its section title, prompts, choice labels, time and help text. Preserve the choice codes. A wording edit needs no changes to the registry, engine, other languages or logic. Patient answers refer to question IDs and codes, independently of displayed wording.

## Register a section

Create `src/pilot/modules/{id}/{logic,lv,en,ru}.json`. Copy the shape of section 02. Include original question IDs, order, response statuses, choice rules and conditions. Each locale must contain the same question IDs and choice codes. Append one entry to the registry's ordered groups array with id, required and question_count. The builder checks ID/order uniqueness, counts, titles, language coverage and earlier condition parents. Add any clinically reviewed discussion or immediate-help triggers to the corresponding question logic. The current pilot targets the input types used by these two groups. A future section introducing a new input type needs separate implementation and verification.

## Build and check

Run `python tools/build_pilot.py` for a standalone HTML file. Run `python tests/pilot/test_build.py` for data and packaging checks. With Playwright Chromium installed, run `python tests/pilot/test_browser.py` and `python tests/pilot/test_independence.py`. CI runs these against local file URLs and verifies the frozen source inventory. The independence test builds a temporary extra section, changes one English prompt, restores previous answers and compares untouched source bytes. It never registers the fixture in the real pilot.

## Behavioral comparison with LV v16

| Workflow | Evidence or remaining difference |
|---|---|
| Module registration and translation isolation | Verified by a real Chromium journey with temporary section 21. Checkbox selection, skip-to-next, titles, report counts and cross-build recovery use the registry. |
| Opening, manual save, language switch, results | Chromium exercises entry, unsaved edits, backing up, starting another respondent, restoring and traversing the opening. |
| Safety | Opening safety items cannot be individually skipped. Incomplete results disclose missing safety answers. Immediate-help and discussion hints follow pilot question metadata. Review safety traverses the opening safety items, can resume from a pilot backup and returns to the previous screen. Flagged answers include their saved timestamps. Full v16 legacy review behavior still needs comparison. |
| Conditions and status | The pilot data include little branching. Recheck original condition/exclusion rules when importing a module. Omitted and conditionally hidden answers must remain distinct from unanswered items. |
| Section chooser | Manual and all-section selection work. The pilot guide offers a localized concern per section. Confirmed sections support direct jumps after the opening. The broader v16 many-to-many concern map is outside the two-section pilot. |
| Recovery | Supports pilot-v1 files and previous pilot wording. Full 712-question v16 backups use a different format. Importing those files needs a migration policy that preserves out-of-pilot responses. |
| Report and print | Doctor report, redacted coded report, decoding key and TXT are available. A4 print uses flowing text. The full v16 clinician overview, timestamped safety review, validated scale handling and single-page layout still require comparison. |
| Information and contributors | Expandable legal/privacy/help text and credits placeholder exist. Original full information, credits and contact placement still require review. |
| Device and release | Automated Chromium on Linux. Native Android Chrome file opening, recovery downloads, clipboard and printing require a device check. Professional wording review and release approval remain outstanding. |

Use `docs/CHANGELOG.md` for current checkpoints. Keep generated HTML in workflow artifacts and retain original source pointers and hashes in the manifest.
