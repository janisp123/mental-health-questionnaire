/* Delegated DOM event routing; questionnaire behavior is injected by the coordinator. */
(function (root) {
"use strict";
root.QuestionnaireEvents = {
 bind(app,handlers){
  app.addEventListener("click",event=>{
   const choice=event.target.closest(".choice");
   const radio=choice?.querySelector('input[name="answer"][type="radio"]');
   if(radio){event.preventDefault();if(event.detail<=1)handlers.singleAnswer(radio.value);return;}
   const element=event.target.closest("[data-act]");if(!element)return;
   event.preventDefault();
   if(element.dataset.act==="addMedicine"||element.dataset.act==="removeMedicine"){
    handlers.medicineAction(element.dataset.act,Number(element.dataset.medRemove));return;
   }
   if(element.dataset.jump)handlers.jump(element.dataset.jump);
   else handlers.action(element.dataset.act);
  });
  app.addEventListener("change",event=>{
   const element=event.target;
   if(element.id==="language"){handlers.language(element.value);return;}
   if(element.hasAttribute("data-med-field")){handlers.medicineChange();return;}
   if(element.hasAttribute("data-module")){handlers.moduleChange();return;}
   if(element.id==="restore"){handlers.restore(element.files[0]);return;}
   if(element.name==="answer")handlers.answerChange(event);
  });
  app.addEventListener("input",event=>{
   const element=event.target;
   if(element.id==="shortText")handlers.shortTextInput(element.value);
   if(element.hasAttribute("data-med-field"))handlers.medicineChange();
   if(element.id==="medicineDiscussion")handlers.medicineDiscussionInput(element.value);
  });
 }
};
})(globalThis);
