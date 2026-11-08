# Reviewer build test plan

**Goal** Verify the LV, EN and RU offline reviewer package and record release blockers.

**Scope** The 712-question build on develop. Use synthetic answers only. Preserve the Latvian question bank, IDs, answer codes, branching and recovery compatibility. Follow docs/RELEASE_POLICY.md for release decisions.

## 1. Establish the baseline

- [x] Run tools/verify_project_index.py and every test script under tests/full_bank and tests/app. All 23 active checks passed on Windows. Node report tests require a working Python on the process PATH.
- [x] Rebuild the reviewer HTML in memory and compare bytes with the checked-in file. The file at c09987a matched SHA-256 9e93741ebbd74c83191e6c2c3dca59059d31713c5c8287946f5672935272a3d8.
- [x] Screen all question records for missing corresponding title, time or help fields, obvious cross-script text, broken Unicode and common inclusive-boundary errors. The automated screens found no confirmed mismatches in those categories. Continue with human review of meaning.
- [ ] Confirm the GitHub checks pass for the exact commit being shared. Keep the HTML and existing trilingual PDF together and compare the Drive HTML hash after copying.

## 2. Exercise riskier paths in the actual HTML

- [x] Open the packaged HTML offline in Chromium. Across 320, 390 and 844 CSS pixels, check five sensitive or long questions in each of LV, EN and RU. All 45 views matched the embedded title, set the document language and fit the viewport.
- [x] Confirm an emergency answer opens a focused support card with the emergency and support phone links. Import an invalid answer code and verify the existing session survives. Restore the valid backup in a fresh tab. No HTTP requests or JavaScript errors were observed in these checks.
- [x] Import a synthetic previous-layout backup, verify old module IDs map to one section, then change a parent answer to close a branch. The hidden answer stayed in recovery and was excluded from the clinician report.
- [x] Reuse the localized tools label for the toolbar landmark. The browser regression and packaged HTML check pass in LV, EN and RU.
- [ ] Check tab order, focus after choosing a locale, and support announcements in a screen reader.
- [ ] Clarify the retired pilot test locations. Five scripts under tests/pilot fail outside the active CI matrix. Four look for the old registry under src/pilot and one asserts against an obsolete runtime implementation.

## 3. Test on a physical Android device

- [x] Fix the touching Continue and Back buttons at the bottom of the section picker. Verified at 320 and 390 px in LV, EN and RU using Chromium.
- [ ] Confirm the section picker button spacing on the physical Android device.

- [ ] Download the exact reviewer HTML, enable airplane mode and open it from Files in Chrome. Verify the app works offline after closing Chrome and reopening the file. Record the phone model, Android version and browser version.
- [ ] Check narrow portrait and landscape, enlarged text, keyboard dismissal, double taps, navigating back, language switching, and readable LV/EN/RU choices.
- [ ] Fill a synthetic section, save a recovery file, close Chrome, reopen the HTML and import the file. Compare position, answers, skipped items, selected sections and locale. Reject a corrupt backup while keeping the open session intact.
- [ ] Produce the clinician report and separate project feedback. Check the A4 print preview or PDF in each locale for wrapping, accents, section order and page breaks. Verify the feedback export contains no synthetic name, answer or medicine values. Inspect the companion PDF guide against the current labels.

## 4. Review language and release readiness

- [ ] Have fluent reviewers compare EN and RU against LV. Start with immediate safety, negation, linked time windows, inclusive boundaries, and standardized screening questions. Log question ID, locale, field, observed wording and proposed change. Track clinician review separately.
- [ ] Retest every accepted fix on a rebuilt artifact. Record the build hash, date, device, tester, result and evidence per case. Resolve release blockers and obtain the release approval required by docs/RELEASE_POLICY.md.

## Performance baseline

One local Chromium run opened the 1.16 MB file and switched locale in about 134 ms. The measured model calls averaged about 0.03 ms for active question filtering and 0.08 ms for computing all section counts on this PC. Prioritize device timing and accessibility findings. If Android shows noticeable lag, profile load, section selection, navigation and report generation separately before changing the runtime.
