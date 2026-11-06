/* Section picker markup; the runtime supplies state and small query helpers. */
(function (root) {
"use strict";
const screens = root.QuestionnaireScreens = root.QuestionnaireScreens || {};
screens.sectionSelector = function ({state,data,countGroup,active,groups,escape,label,btn}) {
 const guide=state.screen==="guide";
 const rows=data.groups.map(g=>{
  const count=countGroup(g.id), title=escape((guide&&!g.required?g.concerns:g.titles)[state.lang]), progress=count.done+'/'+count.total;
  if(g.required)return '<p><strong>'+title+'</strong> — '+progress+'</p>';
  const checked=state.sectionDraft.includes(g.id);
  return '<label class="choice module-choice"><input type="checkbox" data-module="'+escape(g.id)+'" id="optional'+escape(g.id)+'"'+(checked?' checked':'')+'> <span><strong>'+title+'</strong><small>'+progress+' · '+label(checked?'selected':'notSelected')+'</small></span></label>'+(!guide&&state.selected.includes(g.id)&&!active().some(q=>groups.get(q.module).required&&!state.answers[q.id])?btn('jump', 'jump', '', 'data-jump="'+escape(g.id)+'"'):'');
 });
 return '<section class="card"><h2>'+label("selector")+'</h2><p>'+label(guide?"guideIntro":"selectIntro")+'</p>'+rows.join("")+ '<div class="actions">'+btn("all","chooseAll")+btn("clear","clearSections")+'</div>'+btn("confirm","confirmSections","primary")+btn("cancel","cancel")+'</section>';
};
})(globalThis);
