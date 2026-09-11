const config = JSON.parse(document.getElementById("lesson-data").textContent);
const items = config.items;
const $ = id => document.getElementById(id);
const normalize = s => s.normalize('NFD').replace(/[\u0300-\u036f]/g, '').trim().toLowerCase();
let order, index, results;
function showQuestion(){
 $('counter').textContent=`Question ${index+1} of ${order.length}`;
 $('prompt').textContent=`What is the capital of ${order[index].country}?`;
 $('answer-form').hidden=false; $('answer').value=''; $('answer').disabled=false;
 $('check').disabled=false; $('feedback').textContent=''; $('next').hidden=true; $('answer').focus();
}
function start(){
 order=[...items]; for(let i=order.length-1;i>0;i--){const j=Math.floor(Math.random()*(i+1));[order[i],order[j]]=[order[j],order[i]];}
 index=0; results=[]; $('study').hidden=true; $('results').hidden=true; $('quiz').hidden=false;showQuestion();
}
$('start').addEventListener('click',start);$('retry').addEventListener('click',start);
$('answer-form').addEventListener('submit',e=>{
 e.preventDefault();if($('check').disabled)return;
 const item=order[index], answer=$('answer').value.trim();if(!answer)return;
 const correct=[item.capital, ...(item.aliases || [])].some(value => normalize(answer)===normalize(value));results.push({...item,answer,correct});
 $('feedback').textContent=correct?`Correct. ${item.country} → ${item.capital}.`:`The capital of ${item.country} is ${item.capital}. Say the pair aloud before continuing.`;
 $('answer').disabled=true;$('check').disabled=true;$('next').hidden=false;
 $('next').textContent=index===order.length-1?'See results':'Next';$('next').focus();
});
$('next').addEventListener('click',()=>{
 index++;if(index<order.length){showQuestion();return;}
 $('quiz').hidden=true;$('results').hidden=false;
 $('score').textContent=`${results.filter(r=>r.correct).length} of ${order.length} correct this round.`;
 $('report').textContent='World capitals · Lesson '+config.number+' · '+new Date().toLocaleDateString()+'\n'+results.map(r=>`${r.country}: ${r.answer} — ${r.correct?'correct':'review: '+r.capital}`).join('\n');
});
