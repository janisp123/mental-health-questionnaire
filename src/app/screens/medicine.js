/* Medication-entry form markup, independent from answer-flow handling. */
(function (root) {
"use strict";
const screens = root.QuestionnaireScreens = root.QuestionnaireScreens || {};
screens.medicine = function ({medicine,draft,medicineFields,escape}) {
 function select(index,key,value,options,labels){
  return '<label class="field-label">'+escape(medicine.fields[key])+'<select data-med-index="'+index+'" data-med-field="'+key+'"><option value="">—</option>'+options.map(code=>'<option value="'+code+'"'+(value===code?' selected':'')+'>'+escape(labels[code])+'</option>').join("")+'</select></label>';
 }
 return '<p class="help">'+escape(medicine.help)+'</p>'+draft.records.map((record,i)=>'<fieldset class="medicine-card"><legend>'+escape(medicine.entry)+' '+(i+1)+'</legend>'+medicineFields.map(key=>{
  const value=record[key]||"";
  if(key==="status")return select(i,key,value,["current","past","unknown"],medicine.status);
  if(key==="benefit")return select(i,key,value,Object.keys(medicine.benefits),medicine.benefits);
  return '<label class="field-label">'+escape(medicine.fields[key])+'<input type="text" maxlength="1000" data-med-index="'+i+'" data-med-field="'+key+'" value="'+escape(value)+'"></label>';
 }).join("")+ '<button type="button" data-act="removeMedicine" data-med-remove="'+i+'">'+escape(medicine.remove)+'</button></fieldset>').join("")+
 '<button type="button" data-act="addMedicine" class="secondary">'+escape(medicine.add)+'</button><label class="field-label">'+escape(medicine.discussion)+'<textarea id="medicineDiscussion" maxlength="3000">'+escape(draft.discussion||"")+'</textarea></label><p class="muted">'+escape(medicine.select)+'</p>';
};
})(globalThis);
