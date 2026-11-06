/* First page markup, independent of questionnaire content. */
(function (root) {
"use strict";
const screens = root.QuestionnaireScreens = root.QuestionnaireScreens || {};
screens.start = function ({label, btn}) {
 return '<section class="card"><p>'+label("intro")+'</p><p class="muted">'+label("reviewNote")+'</p><p>'+label("noAuto")+'</p>'+btn("start","start","primary")+ '<div class="actions">'+btn("all","chooseAll")+btn("choose","chooseOwn")+btn("guide","chooseGuide")+'</div></section>';
};
})(globalThis);
