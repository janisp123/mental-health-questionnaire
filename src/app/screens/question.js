/* Question card markup; state transitions stay in the runtime. */
(function (root) {
"use strict";
const screens = root.QuestionnaireScreens = root.QuestionnaireScreens || {};
screens.question = function ({q,state,ui,queue,group,escape,label,btn,renderFeedback,renderMedicine}) {
 const t=q.translations[state.lang],idx=queue.findIndex(x=>x.id===q.id);
 const time=t.time?'<p class="muted">'+escape(t.time)+'</p>':"";
 const help=t.help?'<p class="help">'+escape(t.help)+'</p>':"";
 const selectionHint=q.multi?'<p class="muted selection-hint">'+label(q.maxChoices?"multiMaxHint":"multiHint").replace("{count}",escape(q.maxChoices))+'</p>':"";
 let options="";
 if(q.type==="medicineList")options=renderMedicine();
 else if(q.type==="shortText")options='<label class="field-label">'+label("enterText")+' <input id="shortText" autocomplete="off" type="text" maxlength="200" value="'+escape(state.draft.value||"")+'"></label><p class="muted">'+label("optionalText")+'</p>';
 else options='<fieldset><legend class="sr-only">'+escape(t.title)+'</legend>'+
  q.choiceCodes.map(key=>{
    const checked=(state.draft.codes||[]).includes(key),kind=q.multi?"checkbox":"radio";
    return '<label class="choice"><input type="'+kind+'" name="answer" value="'+escape(key)+'"'+(checked?" checked":"")+'> <span>'+escape(t.choices[key]||key)+'</span>'+(checked?'<span class="choice-checkmark" aria-hidden="true">✓</span>':"")+'</label>';
  }).join("")+'</fieldset>';
 const flagged=!!state.feedback[q.id];
 const feedbackControl='<div class="question-title-row"><h2 tabindex="-1" id="question-heading">'+escape(t.title)+'</h2><button type="button" class="feedback-flag" data-act="feedback" aria-label="'+label("feedbackFlag")+'" aria-expanded="'+state.feedbackOpen+'" title="'+label("feedbackFlag")+'">⚑</button></div>';
 return '<section class="card question" data-question="'+escape(q.id)+'"><div class="muted">'+escape(group)+' · '+(idx+1)+'/'+queue.length+(flagged?' · '+label("feedbackFlagged"):"")+'</div>'+feedbackControl+renderFeedback()+time+help+selectionHint+options+
 '<p class="muted">'+label(q.multi||q.type==="shortText"||q.type==="medicineList"?"saveWarning":"autoHint")+'</p>'+(q.multi||q.type==="shortText"||q.type==="medicineList"?btn("save","next","primary"):"")+
 '<div class="actions">'+btn("skipSection","skipSection")+btn("end","skipRest")+'</div></section>';
};
})(globalThis);
