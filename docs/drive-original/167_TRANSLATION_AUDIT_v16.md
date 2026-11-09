# v16 translation inventory and recovery audit

**Checkpoint:** 2026-11-05 / ENRU-V16-RELEASE / stage 1 (source inventory and memory recovery).

## Authoritative sources

- Latvian HTML v16: 712 unique question IDs and 48 modules, unchanged.
- Existing EN/RU HTML in shared release folder are v9; do not treat as v16.
- Translation staging spreadsheet has 1,202 three-column rows; none are blank in EN or RU, but many are mistranslated or outdated and are NOT approved.
- Additional LV/EN/RU v9 extended files, each containing 517 question IDs, were located in Google Drive and used only where the exact Latvian field text matches the current v16 field for the same question ID/choice code.

## Recovery results

| Item | Count | Interpretation |
|---|---:|---|
| Latvian questions | 712 | Stable IDs in the v16 bank |
| Sections | 48 | Module order retained |
| Spreadsheet rows | 1202 | Phrase pairs, not keyed to question IDs |
| Recovered bank phrases, per language | 1793 | From sheet and exact-match v9 reuse; **not yet language-reviewed** |
| Unique bank phrases still missing | 8 | Manual translation needed |
| Legacy v9 questions | 517 | Extra reuse resource, not a compatible release |

## Outstanding untranslated bank phrases

| LV field | Source text |
|---|---|
| M01_24.title | Cik ilgi saņēmāt pēdējo šādu palīdzību?  |
| M15_15.choices.C | 1–2 |
| M15_15.choices.D | 3–4 |
| M15_15.choices.E | 5–6 |
| M15_15.choices.F | 7–9 |
| M18_23.choices.C | 2–5 |
| M20_13.choices.C | 1 |
| M20_13.choices.D | 2–3 |

## Found wording issue (requires correction)

- `Pēdējais palīdzības kurss.` was translated as `Last resort.` / `Крайняя мера.`; this is not the correct sense of a course of help/treatment. The sheet therefore cannot be released merely because every cell has text.

## Integration safeguards

- Translate only display strings; preserve IDs, option codes, conditional context, scoring metadata, safety logic, JSON keys, timestamps, migration logic and local storage behavior.
- Do not assume matching text always has matching clinical intent; review phrasing in context with source question and options.
- The included `REFERENCE_DOCUMENT` and specialist/AI exports must use the same translated fields as the questionnaire. Explicitly test their decoding and checksum procedures.
- An AI-generated translation is not independent clinical/professional review. Label as draft until adequate linguistic and functional verification.
- Keep each release separate. No old published HTML/PDF has been changed.

## Exact next step

Generate keyed EN/RU catalogs against every v16 question ID, manually resolve the 8 missing phrases, repair high-impact mistranslations, then produce non-published v16 draft HTML files and run structural/browser tests. Build and verify LV v16 information PDF, then EN/RU README/PDF. Record each checkpoint in `166_CHANGELOG_LV.md`.

## Local source SHA256

- `162_Sagatavosanas_vizitei_LV_v16.html`: `1edd2e3248789b8bf41671f4910ad087624f8703ae01461a45122c96a6d8791b` (924807 bytes)
- `163_README_LV_v16.md`: `48629c928be071c37a92c91c5c58a832ebb1c1e38337aabd5c1d92aa66f69a48` (14583 bytes)
- `147_Informacija_LV_v14.pdf`: `e43340f2a3d2d2e288138b3d36ea3a788a985df89d74fff6c5cee3f2ced8e591` (55051 bytes)
- `118_Questionnaire_English_FULL_v9.html`: `4c737d133b5e869b5657f9b41a305e0f8cf4096cc19f8de6ea2184bf2cf025c4` (413454 bytes)
- `119_Questionnaire_Russian_FULL_v9.html`: `04c1d7908c26747976cb3a91ac2049a418848450e0464fb56f3414b2ebc338b7` (597855 bytes)
- `120_Questionnaire_Latvian_EXTENDED_v9.html`: `8e3fb7a9917062e99fbba1d3fd2231e1225b786741c77ee3ff418ff237bb259e` (478500 bytes)
- `121_Questionnaire_English_EXTENDED_v9.html`: `5024561c9184a3b3540b1f3070871766fc4527b4e2c58622a13399b9a4d7f661` (464036 bytes)
- `122_Questionnaire_Russian_EXTENDED_v9.html`: `57f74f4e4f7a9fa381d503f37537758852766e73b39cd34b14bb8711c642702b` (673190 bytes)
- `129_English info.pdf`: `92bf23f4f25d39ce03ca0aa26fe787d02799fc7b5bf8162cd20820d8296694ee` (48561 bytes)
- `131_Russian info.pdf`: `72f801d767181986b9e96134aeb372c9c06459469fd9007bb50ec8eb247a3549` (57026 bytes)
- `165_Translation_plan_EN_RU_v16.md`: `b2e2db7aa819571cf76da7c4a28937f22ab1b5269209637f9206ebbbc4edba73` (6263 bytes)
- `Temporary translation workspace — questionnaire text only.csv`: `00ebfc8dcab2a2548a884c4c78c90de745bb7823f6b7adc0feb62e92bdb9ca3c` (333359 bytes)
