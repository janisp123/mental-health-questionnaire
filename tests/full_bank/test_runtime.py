"""Offline browser regression for the complete questionnaire and its 15 user sections."""
import json
import tempfile
from pathlib import Path

from playwright.sync_api import sync_playwright
from browser_helpers import act, backup, choose, launch, open_page, qid, restore
import build_questionnaire as build


def skip_until(page, target):
    for _ in range(120):
        if qid(page) == target:
            return
        act(page, "skip")
    raise AssertionError(f"Could not reach {target} inside the selected section")


with tempfile.TemporaryDirectory() as tmp, sync_playwright() as pw:
    html_path = Path(tmp) / "questionnaire.html"
    html_path.write_text(build.make_html(), encoding="utf-8")
    browser = launch(pw)
    page, errors, network = open_page(browser, html_path)

    data = page.locator("#questionnaire-data").evaluate("el => JSON.parse(el.textContent)")
    assert "izlaid jautājumus, kas šķiet atbilstoši" in data["ui"]["lv"]["guideBody"].lower()
    assert "skip questions that seem fine" in data["ui"]["en"]["guideBody"].lower()
    assert "пропускайте подходящие вопросы" in data["ui"]["ru"]["guideBody"].lower()
    assert len(data["groups"]) == 15
    questions = [q for group in data["groups"] for q in group["questions"]]
    assert len(questions) == 712
    assert len({q["id"] for q in questions}) == 712
    question_by_id = {q["id"]: q for q in questions}
    assert question_by_id["M23_21"]["translations"]["en"]["choices"]["A"] == "A conversation and assessment"
    assert question_by_id["M23_21"]["translations"]["ru"]["choices"]["A"] == "Беседа и оценка состояния"
    assert question_by_id["M16_13"]["translations"]["en"]["choices"]["F"] == "Another activity"
    assert question_by_id["M16_13"]["translations"]["ru"]["choices"]["F"] == "Другой вид деятельности"
    assert question_by_id["M43_01"]["translations"]["ru"]["title"].startswith("Сколько дней за последние 28 дней")
    assert question_by_id["M43_04"]["translations"]["ru"]["choices"]["C"] == "Сон и отдых"
    assert question_by_id["M33_07"]["translations"]["en"]["choices"]["H"] == "I now have an opportunity to seek help or feel ready to do so."
    assert question_by_id["M33_07"]["translations"]["ru"]["choices"]["H"] == "Сейчас есть возможность или готовность обратиться за помощью."
    assert question_by_id["M33_08"]["translations"]["en"]["choices"]["C"] == "I don't think it would help, although I am experiencing difficulties."
    assert question_by_id["M23_25"]["translations"]["ru"]["choices"]["C"] == "Существенно не изменились"
    assert question_by_id["M33_05"]["translations"]["ru"]["choices"]["A"] == "Гетеросексуальная ориентация"
    first_section_russian = [
        text for q in questions if q["module"] == "S11"
        for text in q["translations"]["ru"].get("choices", {}).values()
    ]
    assert "Я не знаю / Я не уверен" not in first_section_russian
    assert "Я не уверен." not in first_section_russian

    s01_questions = [q for q in questions if q["module"] == "S01"]
    assert len(s01_questions) == 61
    assert question_by_id["M01_09"]["translations"]["en"]["choices"]["B"] == "More than 24 hours ago, but no more than 1 month ago"
    assert question_by_id["M01_17"]["translations"]["en"]["choices"]["M"] == "I have no diagnosis from this list."
    assert question_by_id["M01_17"]["translations"]["ru"]["choices"]["G"] == "Расстройство аутистического спектра"
    assert question_by_id["M01_25"]["translations"]["ru"]["title"] == "Почему завершился последний курс такой помощи?"
    assert question_by_id["M01_22"]["translations"]["ru"]["choices"]["E"] == "Самочувствие меняется"
    assert question_by_id["M14_17"]["translations"]["ru"]["title"] == "Как часто за последние 4 недели вы пропускали запланированный приём дозы регулярно принимаемого лекарства?"
    assert question_by_id["M14_18"]["translations"]["ru"]["choices"]["E"] == "Не чувствовал(а) необходимости или сомневался(ась) в пользе."
    assert question_by_id["M30_13"]["translations"]["ru"]["title"] == "Появились ли у вас внезапно прямо сейчас или только что слабость в лице или руке, нарушение речи либо выраженная потеря зрения?"
    assert question_by_id["M30_17"]["translations"]["en"]["time"] == "The past 28 days. New or worsening difficulties with hand movements should be assessed by a doctor. Sudden weakness, speech or vision changes require emergency help (112 or your local emergency number); do not wait to finish."
    assert question_by_id["M30_20"]["translations"]["ru"]["choices"]["C"] == "Более 24 часов назад, но не более месяца назад"
    assert question_by_id["M30_25"]["translations"]["en"]["title"] == "Is the person now barely moving or not speaking, staying frozen for a long time, or unable to take in fluids, with these symptoms starting suddenly?"

    s09_questions = [q for q in questions if q["module"] == "S09"]
    assert len(s09_questions) == 50
    assert question_by_id["M11_17"]["translations"]["en"]["title"] == "On work or study days compared with days off, does your usual sleep onset or wake-up time differ by more than two hours?"
    assert question_by_id["M11_17"]["translations"]["ru"]["title"] == "Обычно ли время, когда вы засыпаете или просыпаетесь, отличается более чем на два часа в рабочие или учебные дни по сравнению с выходными?"
    assert question_by_id["M12_11"]["translations"]["en"]["choices"]["B"] == "More than 24 hours ago, but no more than 1 month ago"
    assert question_by_id["M12_11"]["translations"]["ru"]["choices"]["B"] == "Более 24 часов назад, но не более 1 месяца назад"
    assert question_by_id["M13_10"]["translations"]["en"]["time"] == "At any point in your life."
    assert question_by_id["M13_10"]["translations"]["ru"]["time"] == "Когда-либо в жизни."
    assert question_by_id["M13_10"]["translations"]["ru"]["choices"]["C"] == "Не знаю / трудно сказать."
    assert question_by_id["M13_15"]["translations"]["ru"]["choices"]["F"] == "По-разному / не знаю"
    s09_russian_answers = [
        answer for q in s09_questions
        for answer in q["translations"]["ru"].get("choices", {}).values()
    ]
    assert "Я не знаю / Я не уверен" not in s09_russian_answers
    assert "Я не уверен." not in s09_russian_answers
    s01_russian_answers = [
        answer for q in s01_questions
        for answer in q["translations"]["ru"].get("choices", {}).values()
    ]
    assert "Я не знаю / Я не уверен" not in s01_russian_answers
    assert "Я не уверен." not in s01_russian_answers

    # Start opens a short section picker; select-all chooses every group and continues.
    page.locator('[data-act="start"]').click()
    assert page.locator(".question-nav").count() == 0
    assert page.locator("input[data-module]").count() == 15
    assert all(group["questionCount"] >= 30 for group in data["groups"])
    page.locator('[data-act="all"]').click()
    assert qid(page) == "M23_11"
    assert len(backup(page)["selected"]) == 15

    # Multi-select is manually saved; single-select saves once even on a double tap.
    assert qid(page) == "M23_11"
    page.locator('input[name="answer"][value="A"]').check()
    choose(page, "B")
    assert backup(page)["answers"] == {}
    act(page, "save")
    assert qid(page) == "M23_01"
    page.locator('input[name="answer"][value="B"]').locator("..").dblclick(delay=40)
    page.wait_for_timeout(1400)
    assert qid(page) == "M23_02"
    assert backup(page)["answers"]["M23_01"]["codes"] == ["B"]

    # Feedback is separate from a saved medical answer and survives recovery.
    act(page, "previous")
    act(page, "feedback")
    page.locator('[data-feedback-reason="question"]').check()
    page.locator("#feedback-comment").fill("Synthetic question note")
    act(page, "feedbackContinue")
    saved = backup(page)
    assert saved["answers"]["M23_01"]["codes"] == ["B"]
    assert saved["feedback"]["M23_01"]["reasons"] == ["question"]
    assert saved["feedback"]["M23_01"]["comment"] == "Synthetic question note"
    restore(page, saved)
    round_trip = backup(page)
    assert round_trip["answers"] == saved["answers"]
    assert round_trip["feedback"] == saved["feedback"]

    # A real conditional follow-up appears for an applicable parent answer.
    act(page, "sections")
    page.locator('[data-jump="S01"]').click()
    skip_until(page, "M01_01")
    for question_number in range(1, 8):
        choose(page, "A")
        assert qid(page) == f"M01_{question_number + 1:02d}"
    choose(page, "B")
    assert qid(page) == "M01_09"
    choose(page, "A")
    assert qid(page) == "M01_10"

    # The full-bank safety rules still produce the gentle support message.
    act(page, "sections")
    page.locator('[data-jump="S03"]').click()
    skip_until(page, "M06_01")
    assert qid(page) == "M06_01"
    choose(page, "B")
    assert page.locator("#support-message").is_visible()
    assert page.locator('#support-message a[href="tel:116123"]').is_visible()
    support_text = page.locator("#support-message").inner_text()
    assert "116123" in support_text and "116 123" not in support_text
    act(page, "dismissSupport")

    # Reach the real medication-list item via ordinary section navigation.
    act(page, "sections")
    page.locator('[data-jump="S01"]').click()
    skip_until(page, "M14_01")
    choose(page, "B")
    assert qid(page) == "M14_02", f"Expected medication form next, got {qid(page)}"
    page.locator('[data-med-index="0"][data-med-field="name"]').fill("SYNTHETIC MEDICINE")
    act(page, "save")
    assert backup(page)["answers"]["M14_02"]["kind"] == "medicine"

    # Text questions are manually saved and remain in the clinician report.
    act(page, "sections")
    page.locator('[data-jump="S11"]').click()
    skip_until(page, "M33_01")
    page.locator("#shortText").fill("SYNTHETIC NAME")
    act(page, "save")
    assert qid(page) == "M33_02"
    skip_box = page.locator('.question-nav [data-act="skip"]').bounding_box()
    assert abs(skip_box["x"] + skip_box["width"] / 2 - 195) < 2
    assert page.evaluate("document.documentElement.scrollWidth <= innerWidth")
    act(page, "skip")
    assert qid(page) != "M33_02"
    assert backup(page)["answers"]["M33_02"]["kind"] == "skip"
    act(page, "previous")
    assert qid(page) == "M33_02"
    act(page, "results")
    page.evaluate('window.__copied=null;Object.defineProperty(navigator,"clipboard",{value:{writeText:async t=>{window.__copied=t}},configurable:true})')
    act(page, "copyFeedback")
    page.wait_for_function("window.__copied!==null")
    project_feedback = page.evaluate("window.__copied")
    assert "Synthetic question note" in project_feedback
    assert "SYNTHETIC NAME" not in project_feedback
    assert "SYNTHETIC MEDICINE" not in project_feedback
    act(page, "doctor")
    report = page.locator(".report-preview").evaluate("(el) => el.textContent")
    assert "SYNTHETIC NAME" in report
    assert "SYNTHETIC MEDICINE" in report
    report_locale = page.locator("html").get_attribute("lang")
    assert report.index("SYNTHETIC NAME") < report.index(data["ui"][report_locale]["feedbackSectionHeading"])
    assert data["ui"][report_locale]["reportCountSelected"] in report
    assert data["ui"][report_locale]["reportCountDone"] in report
    assert data["ui"][report_locale]["reportCountSkip"] in report
    assert "Synthetic question note" in report
    assert page.locator("#reportText").count() == 0
    assert page.locator('[data-act="print"]').count() == 1
    assert page.locator('[data-act="back"]').count() == 1
    assert page.locator('[data-act="sections"]').count() == 1
    assert page.locator('[data-act="copyDoctor"],[data-act="downloadReport"]').count() == 0
    page.emulate_media(media="print")
    assert page.locator(".report-preview").is_visible()
    assert not page.locator("footer").is_visible()
    pdf_path = Path(tmp) / "doctor-report.pdf"
    page.pdf(path=str(pdf_path), format="A4")
    assert pdf_path.stat().st_size > 1000
    page.emulate_media(media="screen")
    assert not page.locator('[data-act="ai"]').count()
    assert not errors, errors
    assert not network, network

    # Saving is user-initiated; ten ordinary skips must not trigger a download.
    recovery_page, recovery_errors, recovery_network = open_page(browser, html_path)
    recovery_downloads = []
    recovery_page.on("download", lambda download: recovery_downloads.append(download.suggested_filename))
    recovery_page.locator('[data-act="start"]').click()
    recovery_page.locator('[data-act="all"]').click()
    first = questions[0]
    for language in ("lv", "ru", "en"):
        recovery_page.select_option("#language", language)
        assert recovery_page.locator(".question h2").inner_text() == first["translations"][language]["title"]
    for _ in range(10):
        act(recovery_page, "skip")
    assert recovery_downloads == [], recovery_downloads
    ten_skips = backup(recovery_page)
    assert recovery_downloads == ["questionnaire-recovery.json"]
    assert len(ten_skips["answers"]) == 10
    assert all(answer["kind"] == "skip" for answer in ten_skips["answers"].values())
    restore(recovery_page, ten_skips)
    assert backup(recovery_page)["answers"] == ten_skips["answers"]
    assert not recovery_errors, recovery_errors
    assert not recovery_network, recovery_network
    recovery_page.close()
    browser.close()

print("PASS: full offline runtime includes selection, answer types, conditions, support, feedback/recovery, skip/back, copy/print, three locales, and manual progress saving. Android device UNVERIFIED.")

