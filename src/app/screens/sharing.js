/* Selectable public invitation and deliberate device/copy actions; hidden in print. */
(function(root){
"use strict";
const screens=root.QuestionnaireScreens=root.QuestionnaireScreens||{};
screens.sharing=function({text,canShare,label,btn,escape}){
 return '<section id="questionnaire-sharing" class="report-actions"><h3>'+label("shareQuestionnaire")+'</h3><p>'+label("sharePrivacy")+'</p>'+
  '<label for="questionnaire-share-copy">'+label("shareCopyHelp")+'</label><textarea id="questionnaire-share-copy" readonly rows="6">'+escape(text)+'</textarea>'+
  '<div class="actions">'+(canShare?btn("nativeShare","shareOnDevice"):"")+btn("copyQuestionnaire","copyShareMessage")+'</div>'+
  '<p id="questionnaire-share-status" role="status" aria-live="polite"></p></section>';
};
})(globalThis);
