# v16 question module workflow (development only)

**Authoritative public files:** seven files in `Mental health questionnaire — languages`. The Latvian v16 HTML is the current functional reference; EN/RU v16 HTML files are **DRAFT, not approved**. All three HTML files are standalone offline documents. Do **not** make them fetch JSON files from Drive or the internet.

## Purpose

48 independent module JSON files each contain questions from one numbered section in Latvian, English, and Russian. A module includes the entire original LV question object, translated fields for both languages, question order in the complete 712-question bank, and translation-provenance markers (many values are **unreviewed**). The modules are a lossless question-bank snapshot; they do not split application JavaScript, export/report messages, legal text, or PDF documentation.

## Efficient session workflow

1. Read **only** the first screen of the main changelog and `00_CURRENT_STATE.md` from the archive. Treat the changelog as the only authority for task status.
2. Identify the affected section and open only `182_MODULE_XX_LV_EN_RU_v16.json`. For example, sleep = section 11. Read the relevant adjacent section only when conditional questions cross sections.
3. Modify Latvian wording deliberately; preserve IDs, answer codes, statuses, conditional branching, and timeframes unless a formal migration and full tests are planned. Translate EN/RU with the LV text beside them; never silently mark translations as professionally validated.
4. Save changed module with its original Drive ID if possible (no needless new numbered copies), update the changelog checkpoint, then validate against all 48 modules. Ensure medical wording review is explicitly tracked.
5. To prepare *drafts*, run the Python tool on a local download of all 48 modules and the three current HTML templates:
   `python 183_MODULE_TOOLS_v16.py --modules path/to/modules --templates path/to/downloaded/html --output path/to/draft-output`
   Output is **REBUILT_REVIEW_REQUIRED**. This only replaces the embedded `BANK` question data; it is NOT a replacement for full UI, report/export, clinical, localization, safety, or Android tests.
6. For a no-change integrity check, omit `--output`; this must exactly match the existing HTML question banks. A rebuilt draft must be tested as a self-contained browser file and verified for code, conditionals, backup compatibility, reports and exports before replacing any of the seven published files.

## Mandatory release gate (applies before ANY promotion)

**Opening an HTML file, `node --check`, successful compilation or 712 matching question IDs is NOT sufficient to publish.** All structural, critical-behavior, translation, and safety checks must pass with evidence tied to the exact candidate SHA256. See `185_RELEASE_GATE_v1.md` in `01_SOURCE` (Drive ID `1TJxwqifum2iSNqOghVE1MYd3SmgMOKTY`). A review candidate for invited psychiatric specialists also must pass these gates and prominently say **not clinically validated**. An ordinary public release additionally requires documented qualified HUMAN clinical review and resolution of critical findings; automated checks do not establish clinical accuracy.

To create an empty checklist from a *frozen development candidate*:

`Create a release-evidence.json file containing the required test records listed in 185_RELEASE_GATE_v1.md (all initially PENDING); never pre-mark any PASS.`

After documented tests, fill PASS fields with tester, method, evidence artifact path/hash and UTC timestamp, then run:

`python 186_RELEASE_GATE_CHECK_v1.py --candidate candidate.html --evidence release-evidence.json --mode professional_review`

Use `--mode public_release` and a separate clinical review record for final public release. Any nonzero checker exit code **blocks changes to the main folder**. The checker audits evidence, not browser behavior or medical content. Build/edit in development only until fully cleared. See also `03_TESTS/186_RELEASE_GATE_CHECK_v1.py` (Drive ID `14-ESORp-UPt6ScFrg2GLt3TMlhyJHF8R`).

## Caveats

- The v16 catalogs are not approved translations. Existing translation memory also contains errors; inspect provenance for each field. Standardized scales and high-impact safety language need appropriate independent checks.
- Modules alone are not the whole application or a complete reproducible build system; full UI/translations remain embedded in the HTML templates. Do not claim otherwise.
- For repeatable future releases, develop a separate source generator for all UI text and reports after existing drafts pass tests. Do not force a major code refactor during folder organization.
- The question order is **not** simply numeric section order; entries contain the original global `order` integer. Preserve it.
