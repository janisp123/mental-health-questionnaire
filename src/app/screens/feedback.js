/* Per-question feedback controls, separate from medical answer controls. */
(function (root) {
"use strict";
const screens = root.QuestionnaireScreens = root.QuestionnaireScreens || {};
screens.feedback = function ({q,t,state,ui,label,escape,btn}) {
 if(!state.feedbackOpen)return "";
 const saved=(state.feedbackDraft?.forId===q.id?state.feedbackDraft:state.feedback[q.id])||{reasons:[],comment:""},selected=new Set(saved.reasons||[]);
 const choices=[["question",label("feedbackQuestion")],["language",label("feedbackLanguage")],
  ...q.choiceCodes.map(code=>["answer:"+code,escape(ui.feedbackAnswerPrefix+" "+code+" — "+(t.choices[code]||code))]),
  ["other",label("feedbackOther")]];
 return '<fieldset id="question-feedback" class="feedback-panel"><legend>'+label("feedbackTitle")+'</legend>'+choices.map(([key,text])=>
  '<label class="choice feedback-choice"><input type="checkbox" data-feedback-reason="'+escape(key)+'"'+(selected.has(key)?' checked':'')+'> <span>'+text+'</span></label>'
 ).join("")+'<label class="field-label">'+label("feedbackComment")+' <textarea id="feedback-comment" aria-describedby="feedback-privacy" maxlength="500">'+escape(saved.comment||"")+'</textarea></label><p class="muted">'+label("optionalText")+'</p><p id="feedback-privacy" class="muted">'+label("feedbackPrivacy")+'</p>'+btn("feedbackContinue","feedbackContinue","primary-inline")+(state.feedback[q.id]?btn("removeFeedback","removeFeedback"):"")+'</fieldset>';
};
})(globalThis);
