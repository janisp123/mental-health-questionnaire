"""Render every current question/locale at phone widths using the real screen renderer."""
import tempfile
from pathlib import Path
from playwright.sync_api import sync_playwright
from browser_helpers import launch, open_page
import build_questionnaire as build

with tempfile.TemporaryDirectory() as tmp, sync_playwright() as pw:
    path = Path(tmp) / "questionnaire.html"
    path.write_text(build.make_html(), encoding="utf-8")
    browser = launch(pw)
    page, errors, requests = open_page(browser, path)
    tested = 0
    for width in (320, 390):
        page.set_viewport_size({"width": width, "height": 844})
        result = page.evaluate("""() => {
            const data=JSON.parse(document.querySelector('#questionnaire-data').textContent);
            const questions=data.groups.flatMap(g=>g.questions),esc=QuestionnaireReports.esc;
            const main=document.querySelector('main');let failures=[],tested=0;
            for(const lang of Object.keys(data.ui))for(const q of questions){
                const u=data.ui[lang];
                const draft=q.type==='medicineList'?{records:[Object.fromEntries(Object.keys(u.medicine.fields).map(k=>[k,k==='status'?'current':'']))],discussion:''}:{codes:[],value:''};
                const label=k=>esc(u[k]||k),btn=(act,key,cls)=>'<button class="'+(cls||'')+'">'+label(key)+'</button>';
                main.innerHTML=QuestionnaireScreens.question({q,state:{lang,draft,feedback:{},feedbackOpen:false},ui:u,queue:questions,group:data.groups.find(g=>g.id===q.module).titles[lang],escape:esc,label,btn,renderFeedback:()=>'',renderMedicine:()=>QuestionnaireScreens.medicine({medicine:u.medicine,draft,medicineFields:Object.keys(u.medicine.fields),escape:esc})});
                const card=main.querySelector('.question');
                if(card.scrollWidth>card.clientWidth+1)failures.push({lang,id:q.id,width:card.clientWidth,content:card.scrollWidth});
                tested++;
            }
            return {tested,failures};
        }""")
        assert not result["failures"], {"viewport": width, "failures": result["failures"]}
        tested += result["tested"]
    assert not errors and not requests, (errors, requests)
    browser.close()
print(f"PASS: {tested} question/locale/phone-width layouts fit; no network or JavaScript errors.")
