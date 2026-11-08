/* First page markup, independent of questionnaire content. */
(function (root) {
"use strict";
const screens = root.QuestionnaireScreens = root.QuestionnaireScreens || {};
screens.start = function ({label, btn}) {
 return '<section class="card"><p>'+label("intro")+'</p>'+btn("start","start","primary")+'</section>';
};
})(globalThis);
