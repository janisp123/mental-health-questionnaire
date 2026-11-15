/* Public questionnaire invitation only. No session, report or saved-data inputs. */
(function(root){
"use strict";
const url="https://janisp123.github.io/mental-health-questionnaire/";
function content(ui){return {title:ui.shareTitle,text:ui.shareMessage,url};}
function copyText(ui){return ui.shareMessage+"\n"+url;}
async function deliver(kind,ui,{field,status}){
 const select=()=>{field.focus();field.select();};
 try{
  if(kind==="share"){
   if(typeof root.navigator.share!=="function")throw Error("Share unavailable");
   await root.navigator.share(content(ui));status.textContent=ui.shareReady;
  }else{
   select();
   if(typeof root.navigator.clipboard?.writeText!=="function")throw Error("Clipboard unavailable");
   await root.navigator.clipboard.writeText(copyText(ui));status.textContent=ui.shareCopied;
  }
 }catch(error){
  if(kind==="share"&&error?.name==="AbortError"){status.textContent=ui.shareCancelled;return;}
  select();status.textContent=ui.shareCopyHelp;
 }
}
root.QuestionnaireSharing={content,copyText,deliver};
})(globalThis);
