/* Editorial report order only. No diagnostic/risk score, triage or answer mutation. */
(function(root){
"use strict";
function responsePriority(question,answer,policy){
 const rule=policy.questions[question.id];
 if(answer.kind!=="choice")return rule.default;
 return Math.max(...answer.codes.map(code=>rule.answers[code]));
}
function sortEntries(entries,questions,answers,policy){
 if(!policy)return entries;
 const byId=new Map(questions.map(q=>[q.id,q]));
 const explicit=new Map(Object.entries(policy.relatedGroups).flatMap(([group,ids])=>ids.map(id=>[id,"named:"+group])));
 function family(id){
  const visited=new Set();
  while(!visited.has(id)){
   if(explicit.has(id))return explicit.get(id);
   visited.add(id);
   const parent=byId.get(id)?.context?.id;
   if(!parent)return "question:"+id;
   if(!byId.has(parent))return explicit.get(parent)||"question:"+parent;
   id=parent;
  }
  return "question:"+id;
 }
 const groups=new Map(),families=new Map();
 entries.forEach((entry,index)=>{
  const key=family(entry.id),priority=responsePriority(byId.get(entry.id),answers[entry.id],policy);
  families.set(entry.id,key);
  const group=groups.get(key);
  if(group)group.priority=Math.max(group.priority,priority);
  else groups.set(key,{priority,index});
 });
 // The highest included response positions its context family; original order breaks ties.
 return [...entries].sort((a,b)=>{
  const left=groups.get(families.get(a.id)),right=groups.get(families.get(b.id));
  return right.priority-left.priority||left.index-right.index;
 });
}
root.QuestionnaireReviewPriority={responsePriority,sortEntries};
})(typeof window!=="undefined"?window:globalThis);
