/* Section picker markup; the runtime supplies state and small query helpers. */
(function (root) {
"use strict";
const screens = root.QuestionnaireScreens = root.QuestionnaireScreens || {};
screens.sectionSelector = function ({state,data,countGroup,active,groups,escape,label,btn}) {
 const rows=data.groups.map(g=>{
  const count=countGroup(g.id), title=escape(g.titles[state.lang]);
  const progress=label("sectionProgress").replace("{total}",String(g.questionCount)).replace("{completed}",String(count.done));
  if(g.required)return '<p><strong>'+title+'</strong> — '+progress+'</p>';
  const checked=state.sectionDraft.includes(g.id);
  return '<label class="choice module-choice"><input type="checkbox" data-module="'+escape(g.id)+'" id="optional'+escape(g.id)+'"'+(checked?' checked':'')+'> <span><strong>'+title+'</strong><small>'+progress+'</small></span></label>'+(state.selected.includes(g.id)&&!active().some(q=>groups.get(q.module).required&&!state.answers[q.id])?btn('jump', 'jump', '', 'data-jump="'+escape(g.id)+'"'):'');
 });
 return '<section class="card"><h2>'+label("selector")+'</h2><p>'+label("selectIntro")+'</p>'+btn("all","chooseAllAndContinue","primary")+rows.join("")+btn("confirm","continueSelected")+btn("cancel","cancel")+'</section>';
};
})(globalThis);
