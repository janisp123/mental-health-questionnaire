# Multilanguage mental health questionnaire

**[Open questionnaire in your browser](https://janisp123.github.io/mental-health-questionnaire/questionnaire/)**

A free, multilanguage questionnaire for adults preparing for a mental-health appointment, with **over 700 questions in more than 10 sections**. It helps you organize what you want to discuss with a healthcare professional. **It is not a diagnostic or validated screening tool.** It does not calculate a screening score.

This is a hobby project by Janis Paegle, developed with ChatGPT and Codex assistance while exploring what AI can help build. It is available to try, with its review limitations described below.

**Current version: v0.2.19.** The browser version and offline download use the same questionnaire. Save a progress file manually before closing or reloading if you want to continue later.

[![Multilanguage checks](https://github.com/janisp123/mental-health-questionnaire/actions/workflows/questionnaire-checks.yml/badge.svg?branch=main)](https://github.com/janisp123/mental-health-questionnaire/actions/workflows/questionnaire-checks.yml)

## Download and open

**[Download from Google Drive](https://drive.google.com/drive/folders/1BUlc5W7tRw06JOUE250wCuTe-1ick9xb)**

1. In the Drive folder, choose **Download** for the file ending in **`.html`**. The Drive preview and GitHub source viewer do not run the questionnaire.
2. Open the downloaded HTML file in a browser. On a phone, find it in **Files → Downloads** and use **Open with → browser** if offered.
3. Choose your language and begin. To continue later, use the app's progress-file download and keep the saved file.

The same Drive folder contains the **`.pdf`** guide. Download it there and open it in a PDF viewer.

If the HTML appears as code, it is open in a source/text viewer. Choose a browser instead. If your phone offers no browser for local HTML files, use a desktop browser; physical-phone compatibility testing remains pending.

The questionnaire runs offline and sends no answers. Clinician reports and project-feedback PDFs are separate. Downloaded progress files may contain sensitive information; keep and share them carefully.

![Current questionnaire in English, showing its offline introduction and language selector](docs/images/questionnaire-current.png)

## What you can do

- Choose relevant sections, skip questions and add context in your own words.
- Switch languages within one application. Latvian is the reference and initial language; English, Russian and Ukrainian are also included.
- Download a progress file and import it later, including supported older progress files.
- Prepare a clinician PDF report in a language chosen independently of the questionnaire language. Provided negative, uncertain and declined responses remain in the report.
- Keep project feedback separate from medical answers. Feedback email drafts, copying and sending remain under your control.

Clinician reports use a draft review order, which is not a clinical risk score. See the [change history](docs/CHANGELOG.md) for individual updates and [release policy](docs/RELEASE_POLICY.md) for verification limits.

Landing page languages: [English](https://janisp123.github.io/mental-health-questionnaire/) · [Latviešu](https://janisp123.github.io/mental-health-questionnaire/lv/) · [Русский](https://janisp123.github.io/mental-health-questionnaire/ru/).

## Questions about depression before an appointment

If you are looking for a free offline questionnaire to help describe low mood before seeing a psychiatrist or therapist, this tool includes questions about mood, interest, sleep, energy, concentration and daily-life impact. You can choose relevant sections and prepare a PDF summary.

It is an appointment-preparation aid, **not a validated depression screening test**. It does not diagnose depression, calculate a depression score or rule out a condition. Its diagnostic accuracy has not been established. You can seek professional help without completing it.

**[Read the public questionnaire overview](https://janisp123.github.io/mental-health-questionnaire/)** for depression-related appointment questions, download instructions and privacy details. [Publication/indexing instructions](docs/discovery-preview/LAUNCH.md) record the hosting and search-verification limits.

## Technical overview

| Area | Technologies and approach |
|---|---|
| Application | Plain HTML, CSS and JavaScript; focused screens, state transitions and report renderers. |
| Content and languages | JSON question data and validated translation packs, with stable question IDs and answer codes. |
| Build and packaging | Python, ReportLab, embedded fonts and checksum manifests; one self-contained offline HTML plus a PDF guide and ZIP. |
| Verification | JavaScript component tests, Python source/package checks, Playwright/Chromium browser journeys and responsive layout sweeps. |
| Delivery | GitHub Actions, short-lived branches/PRs, versioned review snapshots and readback-verified Drive updates. |

The technical work addresses three practical problems: keeping sensitive answers on the user's device, maintaining consistent question/answer identity across languages, and preserving older progress files while the interface evolves. Separate answer and feedback reports help keep reviewer comments out of the clinician document. Repeatable packaging and current-source verification help prevent distributing stale files.

## About this project

I'm [Janis](https://github.com/janisp123), and I'm curious about AI and what I can make with it. I shape the idea, decide what to work on, review generated results and test changes. ChatGPT and Codex help generate and revise the code, tooling, tests and documentation.

The [source history](https://github.com/janisp123/mental-health-questionnaire/commits/main/) and [module contracts](docs/FEATURE_DEVELOPMENT.md) show how the project has developed. Automated checks help catch technical problems; human language and clinical review and physical-device testing remain separate requirements.

Another experiment: [Language Learning App](https://github.com/janisp123/language-learning-app), a separate project for everyday vocabulary and pronunciation.

## Source and package records

- [Browse the application source](src/app/)
- [Current package files, source revision and checksums](MH_Public_version/manifest.json)
- [Version snapshot](https://github.com/janisp123/mental-health-questionnaire/tree/review/v0.2.19)

## Development

`main` is the only active product source. Create short-lived branches from main. Older develop/candidate branches and [archived packages](archive/three-language/v0.2.0/README.md) are historical. Legacy `downloads/` paths remain for existing links.

```sh
python -m pip install -r tools/review-requirements.txt playwright
python -m playwright install chromium
python tools/run_checks.py
python tools/build_questionnaire.py
python tools/build_review_package.py --output-dir dist/review-0.2.19
python tools/verify_review_package.py dist/review-0.2.19 --with-zip
```

The normal HTML output is `dist/QUESTIONNAIRE_LV_EN_RU_UK_NOT_RELEASED.html`. Package destinations are never overwritten. CI runs the same checks on PRs to main and on main, then uploads the matching multilanguage package.

Read [feature/module contracts](docs/FEATURE_DEVELOPMENT.md), [architecture](docs/QUESTIONNAIRE_ARCHITECTURE.md), [release policy](docs/RELEASE_POLICY.md) and [current checkpoint](docs/WORK_CHECKPOINT.md) before working. For a managed browser that blocks file navigation, explicitly use `--load-mode memory` and record that limitation.

## Review and contribution

This is a technical-review project. Human language review, clinical review and physical-device verification remain separate requirements. Main adoption does not establish clinical validation. Anyone may use the questionnaire for free, including clinicians during appointments. Source/content reuse terms are separate: no general license has been granted.

Use synthetic data in public issues/tests; never post patient answers or recovery files. Project feedback: janis.paegle.email@gmail.com. See [contribution guidance](CONTRIBUTING.md) and the [future-ideas parking lot](docs/FUTURE_IDEAS.md), which is not an approved feature roadmap.

## Developer coordination

Agent entrypoint: [AGENTS.md](AGENTS.md). Active tasks: [TD list](docs/TD_LIST.md). See the [shared agent protocol](docs/AGENT_PROTOCOL.md), [current checkpoint](docs/WORK_CHECKPOINT.md), [decision log](docs/DECISIONS.md) and [new-project setup](docs/NEW_PROJECT_SETUP.md). These files describe development, not the questionnaire's medical purpose.
