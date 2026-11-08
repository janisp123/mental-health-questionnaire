# Mental health questionnaire

Free offline questionnaire to help adults organize information before an appointment with a mental-health professional. Anyone can use it for free, including clinicians during paid appointments. It is not a diagnostic tool, screening score, or substitute for professional assessment.

## Current development build

The working application assembles all 48 original modules and 712 questions into 15 optional user-facing sections of 36–70 questions each, in one self-contained HTML file. Latvian is the reference language. English and Russian are unreviewed drafts.

The file runs offline and sends no data. Answers remain in the open session unless the user downloads a recovery file, copies a report, prints it, or otherwise chooses to share it. Question feedback is separate from medical answers. The doctor report shows recorded answers and feedback without calculating a diagnosis or score.

## Build and checks

Run `python tools/build_questionnaire.py` to build `dist/QUESTIONNAIRE_LV_EN_RU_NOT_RELEASED.html`. Run `python tools/verify_project_index.py` and the tests listed in [Questionnaire architecture](docs/QUESTIONNAIRE_ARCHITECTURE.md) to check source fidelity and behavior.

Desktop Chromium checks pass in GitHub Actions. Native Android testing, human review of EN/RU and interface wording, and clinical review have not been completed. Technical testing is not clinical validation.

## Review and contribution

Professionals can help by reviewing question wording, navigation, report usefulness, and privacy behavior. Do not submit real patient information. Contact: janis.paegle.email@gmail.com.

The project is non-commercial. No general license has been selected; obtain permission before including externally copyrighted contributions. The professional-review candidate is in [this Google Drive folder](https://drive.google.com/drive/folders/1BUlc5W7tRw06JOUE250wCuTe-1ick9xb). The frozen v16 files remain in `reference/baseline/`; the older Drive copies were removed from the shared folder. This candidate is not a final or clinically validated release.
