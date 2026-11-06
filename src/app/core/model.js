/* Question lookup, conditional visibility, active order, and progress queries. */
(function (root) {
"use strict";
root.QuestionnaireModel = {
 create(data) {
  const groups=new Map(data.groups.map(group=>[group.id,group]));
  const optionalIds=data.groups.filter(group=>!group.required).map(group=>group.id);
  const byId=Object.create(null),all=[];
  for(const group of data.groups){
   for(const question of group.questions){
    if(byId[question.id])throw Error("Duplicate question: "+question.id);
    byId[question.id]=question;all.push(question);
   }
  }
  function questionVisible(state,question){
   const context=question.context;
   if(!context||!context.id)return true;
   const parent=byId[context.id];
   if(!parent||!questionVisible(state,parent)||
      (!groups.get(parent.module).required&&!state.selected.includes(parent.module)))return false;
   const answer=state.answers[context.id];
   if(!answer||answer.kind!=="choice")return !Array.isArray(context.showValues);
   const chosen=new Set(answer.codes||[]);
   if(Array.isArray(context.showValues)&&!context.showValues.some(value=>chosen.has(value)))return false;
   if(Array.isArray(context.hideValues)&&context.hideValues.some(value=>chosen.has(value)))return false;
   return true;
  }
  const visibleQuestions=state=>all.filter(question=>questionVisible(state,question));
  return {
   groups,optionalIds,byId,all,
   questionVisible,
   reportQuestions:visibleQuestions,
   active(state){return all.filter(question=>(groups.get(question.module).required||state.selected.includes(question.module))&&questionVisible(state,question));},
   current(state){return byId[state.currentId]||null;},
   countGroup(state,groupId){
    const questions=all.filter(question=>question.module===groupId&&questionVisible(state,question));
    return {total:questions.length,done:questions.filter(question=>state.answers[question.id]).length,
     skipped:questions.filter(question=>state.answers[question.id]?.kind==="skip").length};
   },
   isSafety(question){return !!question.safetyRequired;}
  };
 }
};
})(globalThis);
