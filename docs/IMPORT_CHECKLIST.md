# Migration acceptance checklist

**Status: ORIGINAL SOURCE MIGRATION VERIFIED COMPLETE (79/79 on `develop`).** Active task log: GitHub [`docs/CHANGELOG.md`](CHANGELOG.md); latest version pointers: [`project-manifest.json`](../project-manifest.json) and [`docs/FILE_INDEX.md`](FILE_INDEX.md). Google Drive distributes LV only.

- [x] Public GitHub repository reachable with write permissions
- [x] Isolated `develop` branch created
- [x] Disposable test create / read / edit / verify / delete succeeded
- [x] Development scaffold read back from GitHub and verified
- [x] Existing Drive changelog archived as immutable copy under `docs/drive-original/`
- [x] Public-bound sources inspected for personal or private medical information (not a guarantee; never commit real responses)
- [x] Complete original-source baseline indexed with Git blob SHA1 and file size; module SHA256s in source module index
- [x] 48/48 multilingual modules imported and verified
- [x] 712 question IDs and original BANK reconstruction checked (full dependency/safety audit still required for release)
- [x] Existing source tools / release-evidence policy migrated (CI remains absent)
- [x] Original LV/EN/RU HTML references preserved and verified
- [x] Historical Drive changelog imported separately and GitHub changelog made authoritative
- [ ] Single shared application engine extracted, tested and documented
- [ ] English/Russian questions and UI/documentation fully translated and reviewed
- [ ] One self-contained offline HTML candidate built
- [ ] Structural, behavior, translation, privacy and release gates run on candidate
- [ ] Qualified clinical review recorded where required
- [ ] Explicit approved release published to `main` and Google Drive
