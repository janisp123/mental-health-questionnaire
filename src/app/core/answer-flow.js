/* Navigation transitions shared by save, skip, and safety-review journeys. */
(function (root) {
"use strict";
root.QuestionnaireFlow = {
 next(state,questions){
  const index=questions.findIndex(question=>question.id===state.currentId),next=questions[index+1];
  return next?{id:next.id}:{screen:"results",currentId:state.currentId,clearDraft:true,clearNotice:true,scroll:true};
 },
 afterSave(state,questions){
  if(state.reviewQueue?.[0]===state.currentId){
   state.reviewQueue.shift();
   if(state.reviewQueue.length)return {id:state.reviewQueue[0]};
   const previous=state.reviewReturn;
   state.reviewQueue=null;state.reviewReturn=null;
   if(previous?.screen==="question"&&questions.some(question=>question.id===previous.id))return {id:previous.id};
   return {screen:previous?.screen||"results",currentId:previous?.id||null,clearDraft:true};
  }
  return this.next(state,questions);
 },
 previous(state,questions){
  const index=questions.findIndex(question=>question.id===state.currentId);
  return index>0?{id:questions[index-1].id}:{screen:"start"};
 }
};
})(globalThis);
