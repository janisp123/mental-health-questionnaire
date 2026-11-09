# Active Ukrainian translation pack

Ukrainian is integrated into the standard four-language app and both language selectors. The current build configuration is `src/questionnaire/build.json`. This folder owns its question/UI/medicine/section/report wording; do not make another app engine. Human language and clinical review remain pending. Read `docs/FEATURE_DEVELOPMENT.md` and this folder’s checkpoint before editing.

## Translation order

Start with `ui.json` and the [Ukrainian reviewer README](README_REVIEW.uk.md). Finish the remaining interface, medication, section and report labels before the question modules. Keep the UI keys, data types and placeholders from the Latvian catalog. Verify the README uses the same button labels.

## Question batches

Run these commands from the repository root. In Windows PowerShell, set `$env:PYTHONUTF8 = "1"` for UTF-8 console output.

```text
python translations/workspace.py source 23 --start 1 --limit 10
python translations/workspace.py check 23
python translations/workspace.py check
```

1. Read the checkpoint and export the next batch. The command reads one source module and prints only the selected Latvian question IDs, titles, time text, help and answer choices. The English and Russian records do not appear in the export.
2. Save the translated entries in `translations/uk/questions/23.json` for module 23. Keep the exported JSON structure and its `source_sha256`. Replace the Latvian wording with Ukrainian, preserve IDs and answer codes in their original order, and retain empty source fields as empty. Merge later batches into the same module file.
3. Check the module and compare the translations with the Latvian source. Update the checkpoint with the exact IDs covered, the result and the next batch. Commit the files under `translations/` so the owner can push the checkpoint in GitHub Desktop.

`check 23 --complete` requires all questions in module 23. `check --complete` requires all 712 questions across the 48 modules. A structural pass checks coverage, field shape, answer codes and the Latvian source hash. Wording and clinical review are tracked separately.

## Ukrainian wording

- Address the reader politely with **Ви**, **Вам**, **Вас** and **Ваш** forms. Prefer gender-neutral phrasing when it preserves the meaning.
- Preserve time windows, negation, frequency and duration ranges, and the distinction between uncertainty, refusal and an answer. Flag ambiguous Latvian wording by ID in the checkpoint.
- Flag sensitive questions and named screening instruments for fluent human review. Confirm the source and reuse status of standardized translations before inclusion.

## Integration criteria

Complete the question files, then translate the interface, medication form, module and section titles, report labels, and reviewer guide. Record human language review and clinical review of safety wording. Integrate in a separate change, verify the existing languages and backups, and test Ukrainian offline, including both PDF paths and Android. Українська is active in both selectors. Continue recording technical checks and outstanding human review separately.
