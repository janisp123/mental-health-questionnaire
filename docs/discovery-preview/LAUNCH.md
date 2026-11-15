# Discovery page preview and owner launch plan

Status: **LIVE** at https://janisp123.github.io/mental-health-questionnaire/ — published 14 November 2026 after owner approval. `index.html` is a reviewable static description page, not a newly released questionnaire. The original preview remains the editable source. Indexing and actual AI-search suggestions are not yet verified; no bot-policy or Drive/questionnaire changes were made.

## Scope and maintenance choice

One self-contained HTML page uses semantic text, inline CSS and no JavaScript, dependencies, accounts, tracking, forms or patient data. It points to the existing v0.2.5 technical-review download and guide. The current application source is undergoing separate work; this page describes the distributed package, not unshipped changes.

The smallest publication option is a GitHub Pages deployment artifact containing only the approved English `index.html`, `lv/index.html`, `ru/index.html` and generated `sitemap.xml`. No domain purchase or full website is needed. The public page uses stable download links and generic file instructions. Routine patches do not require editing a version number or filename on the page. Maintain the page when features, privacy/review status or download destinations actually change; keep exact package versions and hashes in release records. Hosting also has its own request handling; the offline app's no-answer-transmission claim is not a claim that GitHub or Drive receives no visit/download requests.

GitHub's branch publishing supports the branch root or `/docs`, not arbitrary `/docs/discovery-preview` as the publishing root. **Do not select the whole existing `/docs` tree just to publish this preview.** After approval, use a reviewed Pages Actions workflow that uploads only a staging directory containing the approved page, or an owner-maintained dedicated publishing branch containing only that page. A manual-only GitHub Actions workflow is now prepared in `.github/workflows/discovery-pages.yml`; it is not deployed or automatically triggered by merge. Actions adds a small workflow to maintain; a dedicated branch needs deliberate copying on updates. Prefer the isolated Actions artifact if the owner wants updates reviewed in normal PRs.

## Before requesting deployment approval

1. Review the visible copy and LV/RU/UK summaries. They are draft wording, not evidence of human translation or clinical review. Preserve the technical-review status, absence of clinical validation, pending human review and physical-phone testing limits.
2. Reconfirm the current release/download pointers against `README.md`, `docs/RELEASE_POLICY.md` and `MH_Public_version/manifest.json`. The HTML download intentionally follows README's working Drive folder route; the exact versioned file to select is named on the page. Raw GitHub HTML is source/plain text, not a running app.
3. Test the page locally without JavaScript at narrow and desktop widths, keyboard-only navigation, visible focus, 200% zoom, text wrapping and sufficient contrast. Open the single Drive folder, download the HTML and PDF, check their hashes against the manifest, and test the downloaded HTML in a browser. Use synthetic answers only. Do not substitute simulated widths for physical-phone verification.
4. Present the page and proposed publishing mechanism to the owner. Obtain explicit approval to deploy before enabling Pages, adding a publishing workflow/branch, changing visibility or performing indexing submissions. Existing product source/guide/reviewer-distribution gates still apply independently.

## After owner approval: publish and verify

1. Use a checked PR for the approved publication configuration. In repository **Settings → Pages → Build and deployment**, choose **GitHub Actions** for an isolated artifact, or **Deploy from a branch** with the approved dedicated branch and root folder. Settings access may require the owner; file write access does not imply settings access.
2. Establish the actual HTTPS publication URL from GitHub Pages settings. Do not guess the canonical from the repository name. Before making the page public, add a self-referencing absolute canonical for the chosen final URL and remove the unpublished-preview banner. The builder now adds reciprocal `en`/`lv`/`ru` alternatives (including each page itself) and an English `x-default`, for actual equivalent localized URLs. Do not add alternatives for languages without a published page.
3. After deployment, record the final URL, checked commit, deployment result and date. Check HTTPS status and redirects, HTML content type, visible text with JavaScript disabled, correct canonical, download/PDF/source links and mobile layout. Re-download and compare the current package to its manifest. A successful page request does not establish that a crawler can access it or that a phone can open the downloaded app.
4. Inspect the final response headers and HTML for accidental `X-Robots-Tag: noindex` or robots `noindex`. Inspect the actual origin's `/robots.txt` and host restrictions for Googlebot, Bingbot and OAI-SearchBot. A project subdirectory cannot control the origin-root robots file by adding a local nested one. Record restrictions and what GitHub Pages allows the owner to control; do not silently alter bot/training policy.
5. Use Search Console/Bing inspection tools and any available real crawler access evidence. A request with a crawler User-Agent is only a simulated request, not proof of an actual crawler visit or access from its published IP range. Record unverified crawler access as pending.

## Owner indexing steps

- **Google:** add a URL-prefix Search Console property for the actual Pages URL and verify ownership using a supported method available on that host (for example, an HTML file/tag added through a separate reviewed change). Inspect the final page URL, run a live test and request indexing if eligible. An owner or full user is required. Inspect the indexing result later; repeated requests do not accelerate crawling. A one-page site does not need a sitemap to use URL Inspection.
- **Bing:** add and verify the actual site in Bing Webmaster Tools, inspect the URL and use **Submit URLs** for this page. The generated sitemap.xml may also be submitted, though URL submission is sufficient for this one-page site. No API key, IndexNow integration or content-submission system is needed.
- **AI search:** Google says ordinary Search eligibility and useful, accessible text apply to its AI features; inclusion requires indexing and snippet eligibility and is not guaranteed. OpenAI identifies OAI-SearchBot as search crawling and GPTBot as model-training crawling, with independent controls. Assess search access without changing the owner's training preferences. `llms.txt`, structured data or special AI instructions are not required here and do not switch on recommendations. No provider endorsement is implied.

Crawling, indexing, ranking, citation and AI recommendations are not guaranteed. Hosting controls and third-party indexing may remain outside the owner's control.

## Observe realistic search results after indexing

Record dates, service, query, country/language context, observed result URL/citation and whether the page actually appears. Use several sessions and later checks; one generated answer is not a stable ranking measurement. Do not report a test as executed before publication/indexing.

| Language | Example question-led query |
| --- | --- |
| English | Where can I find free offline questions to prepare for a psychiatrist appointment? |
| English | Is there a mental health questionnaire with a PDF summary for my therapist? |
| Latvian | Kur atrast bezmaksas anketu, lai sagatavotos vizītei pie psihiatra? |
| Russian | Где найти бесплатную офлайн-анкету для подготовки к приёму у психиатра? |
| Ukrainian | Де знайти безкоштовну офлайн-анкету для підготовки до прийому у психіатра? |

Try conventional Google/Bing results and available ChatGPT Search, Gemini/Google AI Search, Copilot and Perplexity interfaces. Record unavailable services as untested. If relevant, the owner can share the factual page with interested professionals or communities under their rules; no unsolicited outreach, fabricated endorsements or backlink campaigns are part of this work.

## Existing About metadata blocker

The TD list records repository description/topics edits returning HTTP 403 on 9 November. This preview does not retry settings writes or claim that blocker is resolved. The owner can open the gear beside the repository's **About**, use the approved description/topics from `docs/TD_LIST.md`, save, and verify the public readback. Keep the pending task until that readback exists.

## Official guidance consulted

Retrieved on 14 November 2026; recheck before launching if the interface or policy changes.

- [GitHub Pages: configure a publishing source](https://docs.github.com/en/pages/getting-started-with-github-pages/configuring-a-publishing-source-for-your-github-pages-site) — branch root/`docs` or a custom Actions publishing workflow.
- [Google: AI features and your website](https://developers.google.com/search/docs/appearance/ai-features) — Search access, indexing and snippet eligibility.
- [Google: ask to recrawl URLs](https://developers.google.com/search/docs/crawling-indexing/ask-google-to-recrawl) — URL Inspection, permissions and indexing limits.
- [Bing: URL submission](https://www.bing.com/webmasters/help/url-submission-62f2860b) — verified site and manual submission; inclusion is not guaranteed.
- [OpenAI crawler documentation](https://developers.openai.com/api/docs/bots) — OAI-SearchBot and GPTBot have distinct purposes and controls.

## Verification boundary

Local checks performed on 14 November 2026: HTML parser checks passed for unique IDs, valid fragment links, language tags, one main heading and absence of scripts/forms/iframes/images. System Chromium rendered the page with JavaScript disabled at 320, 390 and 1280 pixels without text/link overflow; keyboard skip-link focus passed. The desktop full-page screenshot was visually inspected. These used explicitly labelled **memory loading** because managed Chrome blocked `file://` navigation; no downloaded-file or physical-device pass is claimed.

The existing public Drive folder returned HTTP 200. The PDF link returned HTTP 200, 49,212 bytes, SHA256 `b479f037a089360370aa08544ba35141dd0e39ab2ae1a39e5d8fe43c306a1ec9`, matching the current package manifest. This run did not newly download/read back the Drive HTML; the 14 November record on the release branch (`docs/review/checks/2026-11-14-feedback-drive-sync.json`) is the evidence for the current v0.2.5 Drive bytes. Recheck both actual downloads before launch. The initial preview added no dependencies; the prepared publication builder now has a focused regression test at `tests/discovery/test_build.py`.

This is a local unpublished preview. Public HTTPS, canonical, host robots/header behavior, actual crawler access, search ownership verification, indexing and AI-search appearance remain **not executed / pending publication and owner approval**. It does not change the questionnaire, question bank, translations inside the app, reviewer package or Drive files.

## Prepared publication implementation — 14 November 2026

- `.github/workflows/discovery-pages.yml` runs only by manual dispatch. Merging does not deploy. It reads an owner-enabled Pages configuration (`enablement: false`), builds from the actual configured base URL, and uploads only the generated localized HTML pages and `sitemap.xml`. It does not upload the questionnaire, source tree, docs or test data. Deployment needs the standard `github-pages` environment and narrowly scoped Pages/OIDC permissions.
- `tools/build_discovery.py` rejects non-HTTPS/credential/query/fragment URLs and existing output directories, removes the preview banner and adds the actual canonical plus sitemap. A test-only example URL is not a claimed publication URL.
- Enable GitHub Actions in Settings → Pages only after deployment approval; merge the checked PR, then run **Publish approved discovery page** on main. Read the workflow's environment URL and verify that actual URL before sharing/submitting it. No presumed github.io address is announced as live.
- The page now explicitly answers depression-test searches while explaining the unvalidated, non-diagnostic appointment-preparation purpose. It does not label itself best, validated or recommended by an AI provider.
- Drive v0.2.5 is already verified from the earlier update. The PDF uses its stable Drive file link because repository-package PR #23 remains unmerged; this avoids publishing a broken v0.2.5 main/raw URL.
- Observed baseline: repository API says `has_pages: false`; Pages configuration GET returns 404. Exact-name web search for the repository returned no results. This is not proof of universal deindexing, and broader depression rankings or AI suggestion inclusion were not measured.
- Owner approval is still required for deployment. Main integration, actual public crawling, Search Console/Bing ownership/indexing and AI-search observation remain pending. No robots/training policy was changed.

## Actual publication record

PR #24 merged as `a37f254d17d63316e8f211005350645b8f1fe02c`, tree identical to checked head `961a4ee74d92612e0cc8a1c3a57bca95877d6339`. Owner enabled Pages with GitHub Actions after the integration received HTTP 403. Manual deployment run 43603795913 completed successfully. Actual Pages URL: https://janisp123.github.io/mental-health-questionnaire/ .

HTTPS page and sitemap returned 200; correct self-canonical; no HTML/header noindex; origin robots.txt returned 404 (no robots file at that origin, not a disallow). Simulated Googlebot/bingbot/OAI-SearchBot user-agent requests returned 200; these are not actual crawler observations. Download URLs point to the verified current Drive files. Live browser inspection found a long filename overflowing on narrow screens; a wrapping correction is included in the publication-record PR and must be deployed/verified before claiming that correction live. Search Console/Bing ownership verification and index requests remain owner-account steps; actual indexing, crawler visits, ranking and AI suggestions remain unverified.

## Stable public wording

The public download button and opening instructions deliberately omit release numbers, exact package filenames and a manual checked-on date. One stable Google Drive folder link provides both the questionnaire and PDF guide; there is no separate PDF or individual-file download action. The version-information link points to the tags index rather than a specific snapshot. New release artifacts still need the normal verified distribution update, but routine patches need no landing-page copy rewrite. Product facts such as supported languages and question coverage should be reviewed only when those facts change.


## Single-folder download delivery — 15 November 2026

README and the live page each use one “Download from Google Drive” link to the same folder. Removed separate raw-GitHub/individual-Drive PDF download links and aligned guide instructions. Source PR #42 merge `8063c261f1b33a23f3b78ade95a48178601cb6bf`; Pages run 43682403681 succeeded. Live index/sitemap bytes match the tested artifact, and main README bytes match the merged source. No product/guide/Drive-file update; v0.2.10 remains current. Current evidence: [download-link readback](../review/checks/2026-11-15-single-drive-download-links.json).


## Localized discovery update — 15 November 2026

Prepared English root, Latvian `/lv/` and Russian `/ru/` pages with visible language navigation, self-canonicals, reciprocal absolute hreflang alternatives and a sitemap listing every localized URL. Shared inline styling is reused; all content is readable without JavaScript. Each page has one stable Drive folder download action; no questionnaire, reports, progress or source-tree files enter the Pages artifact. Current source: English `index.html`, plus `lv.html` and `ru.html`; always inspect the builder output, which supplies shared styling/metadata.

The root link remains stable for sharing. Localized titles/descriptions and natural-language appointment/depression/anxiety questions improve content relevance; they do not guarantee indexing, ranking or AI recommendations. Existing bot/training policy is unchanged. Build/layout checks and required CI passed; PR #48 and successful Pages run 43706924365 published the update. Live English/Latvian/Russian pages and sitemap match builder bytes; current evidence is [localized delivery](../review/checks/2026-11-15-localized-discovery-live.json). Actual indexing/AI recommendations remain unverified. Older dated preparation/publication sections above are historical evidence.

Official guidance reviewed:
- [Google localized versions](https://developers.google.com/search/docs/specialty/international/localized-versions): alternatives must include self and other versions, use fully qualified URLs and link back reciprocally.
- [Google AI features](https://developers.google.com/search/docs/appearance/ai-features): supporting-link eligibility requires indexing and snippet eligibility; no additional AI-specific technical requirements.
- [OpenAI crawlers](https://developers.openai.com/api/docs/bots): OAI-SearchBot governs search discovery separately from GPTBot training. No bot-policy change was made.
