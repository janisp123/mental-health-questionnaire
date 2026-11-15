# One public Google Drive download link

**Goal:** README and live GitHub Pages offer one Google Drive folder link for obtaining both the questionnaire and PDF guide. Remove separate PDF/file download links and keep instructions aligned.

**Scope:** README, discovery-page source, public-link preference and release records only. Current app/guide package stays v0.2.10; no Drive file/content change. Technical source/provenance links remain distinct from downloads, with README linking the application source directory instead of the packaged HTML.

**Target:** `https://drive.google.com/drive/folders/1BUlc5W7tRw06JOUE250wCuTe-1ick9xb`.

- [x] Replace the README's two download links and the page's two-button choice with one folder link each; explain the guide is in that same folder.
- [x] Validate both link sets, run the existing isolated artifact checks and inspect JavaScript-disabled phone/desktop rendering. Record the single-folder preference for future edits.
- [x] Integrate a checked PR, dispatch the existing manual Pages workflow, then verify live bytes/links/canonical/sitemap and the main README.
- [x] Record actual deployment/readback, update checkpoint and close queued-only PR #27 as fulfilled (without merging a completed TD entry). Preserve current product version and unrelated TD work.

- Source checks: two existing artifact tests passed. README/generated-page link validation confirms exactly one download destination each and no individual HTML/PDF artifact links. JavaScript-disabled 320/390/1280 layouts and keyboard skip link passed; phone CTA and opening instructions visually inspected. Independent review found no Critical/Important or minor concerns. Drive folder listing confirms the current clean-named v0.2.10 pair. Previous successful Pages run: 43607264240 (`bee1b93cb0d72043b12b678c62210fb4b15a060f`).

- Published: PR #42 merge `8063c261f1b33a23f3b78ade95a48178601cb6bf`, checked head `d4192daa760b707889d14a5493b2bc52eea1b761`, Pages run 43682403681. Live page/sitemap bytes and main README verified; one identical folder CTA each. Queued-only PR #27 closed as fulfilled. Delivery records/checkpoint are integrated through the checked documentation follow-up; product package stays v0.2.10.
