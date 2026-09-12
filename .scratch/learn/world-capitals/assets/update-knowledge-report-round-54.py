from pathlib import Path
import json,re,unicodedata,html
p=Path('.scratch/learn/world-capitals'); old=json.loads((p/'reference/knowledge-estimate-2026-09-12.json').read_text()); rows=old['countries']
norm=lambda s: ''.join(c for c in unicodedata.normalize('NFD',s.casefold()) if not unicodedata.combining(c)).replace('’',"'")
base=lambda s: re.sub(r' \(.*\)$','',s).strip()
lookup={norm(r['country']):r for r in rows}
def get(s):
 s=base(s)
 if s=='Micronesia':s='Federated States of Micronesia'
 if s=='Czech Republic':s='Czechia'
 return lookup[norm(s)]
errors={36:{'Mali':'miss','Brunei':'spelling'},37:{'Nauru':'miss','Kiribati':'spelling'},43:{'South Africa':'spelling'},45:{'Jamaica':'spelling','Maldives':'miss'},53:{'Botswana':'omission'}}
recent=[]
for f in sorted((p/'learning-records').glob('*.md')):
 n=int(f.name[:4])
 if not 140<=n<=162 or n in [141,143,152,161]:continue
 t=f.read_text(); head=t.splitlines()[0]; m=re.search(r'round (\d+)',head)
 if not m:continue
 rd=int(m[1]); reverse='reverse' in head
 if rd in [36,37]:
  prompts=re.search(r'Prompt order: (.*?)\.',t)[1].split(', ')
 else:
  paragraph=next(line for line in t.splitlines() if ' → ' in line and ';' in line)
  pairs=[x.split(' → ') for x in paragraph.rstrip('.').split('; ')]
  assert len(pairs)==12,(n,pairs)
  prompts=[b if reverse else a for a,b in pairs]
 for c in prompts:
  r=get(c)
  if reverse:
   r['reverse_checks']+=1;r['reverse_correct']+=1
  else:
   result=errors.get(rd,{}).get(r['country'],'correct')
   event={'record':n,'round':rd,'result':result}
   if result=='omission':event['resolved_without_answer_exposure']=True
   r['events'].append(event);recent.append(event)
labels={1:'Strongest demonstrated recall',2:'Good recall; less confirmation or still consolidating',3:'Association known; name accuracy inconsistent',4:'Forward recall still fragile'}
for r in rows:
 a=r['events']; scored=[x for x in a if x['result']!='omission']; streak=0
 for x in scored[::-1]:
  if x['result']!='correct':break
  streak+=1
 misses=sum(x['result']=='miss' for x in a);sp=sum(x['result']=='spelling' for x in a)
 level=4 if any(x['result']=='miss' for x in scored[-2:]) else 3 if scored and (scored[-1]['result']=='spelling' or (sp>=2 and streak<3)) else 1 if streak>=3 or (len(scored)>=2 and not misses and not sp) else 2
 r.update(level=level,band=labels[level],forward_checks=len(a),correct=sum(x['result']=='correct' for x in a),spelling_slips=sp,recall_gaps=misses,forward_omissions=sum(x['result']=='omission' for x in a),consecutive_correct=streak)
 r['note']={1:'Repeated clean forward retrieval; current evidence is stable.',2:'Correct association demonstrated; fewer confirming checks or still consolidating.',3:'Association available; exact name needs more consistency.',4:'Recall gap among the last two scored forward checks.'}[level]
 if r['country']=='Botswana':r['note']+=' Round 53 omission resolved correctly without answer exposure; omission excluded from streak calculation.'
 if r['country']=='Maldives':r['note']+=' Port Louis confusion in round 45; Malé correct in rounds 47 and 50.'
 if r['country']=='South Africa':r['note']+=' All three roles combined; Bloemfontein slip in round 43, correct in rounds 45 and 53.'
 if r['country']=='Sri Lanka':r['note']+=' Jayawardenepura and Jayewardenepura both fully correct.'
 r['evidence']=r['note'];r['last_error_record']=next((x['record'] for x in a[::-1] if x['result'] in ['miss','spelling']),None)
rows.sort(key=lambda r:(r['level'],norm(r['country'])))
assert len(rows)==195 and sum(r['forward_checks'] for r in rows)==564
assert sum(r['reverse_checks'] for r in rows)==84
assert len(recent)==204
method='''Snapshot through round 54, 12 September 2026. Round 55 is pending and excluded. All 195 countries are sorted by demonstrated recall band, then alphabetically. Only observed testing evidence is used; self-reported prior knowledge is excluded.

Counts cover 47 cumulative forward rounds (564 prompts) and 7 reverse rounds (84 prompts). Earlier lessons establish coverage of all 195 countries in both directions, including corrections. Immediate correction drills are excluded from mixed-check counts. This measures capital recall, not wider country knowledge or retention after a known break.

Bands use the same working rules as the previous report: strongest requires three consecutive clean forward answers, or at least two with no recorded forward errors. A recall gap among the last two scored forward checks gives the fragile band. A latest spelling slip, or repeated slips without three subsequent clean answers, gives the name-accuracy band. Remaining countries are in the good/consolidating band. These are practical heuristics, not validated probabilities. Fewer tests means less evidence, not necessarily less knowledge.

Recognizable spelling slips and recall gaps are separate. Both Sri Jayawardenepura Kotte and Sri Jayewardenepura Kotte count as correct. Botswana's round 53 omission is counted as an omission, subsequently resolved without answer exposure; it is excluded from clean-streak calculations rather than treated as a recall error or first-pass success. Reverse evidence is separate and does not establish forward recall. Multi-capital countries combine their tested roles. Intervening reverse questions can refresh an answer; longer forward intervals do not necessarily mean no exposure.
'''
out=p/'reference/knowledge-estimate-2026-09-12-round-54'
Path(str(out)+'.json').write_text(json.dumps({'method':method,'countries':rows},ensure_ascii=False,indent=2))
legend=''.join(f'<li><b>{labels[i]}</b>: {sum(r["level"]==i for r in rows)} countries</li>' for i in labels)
md='# Country-capital recall through round 54\n\n'+method+'\n| Band | Country | Exact forward / prompts | Spelling slips | Recall gaps | Omissions | Clean streak | Reverse correct / prompts | Current state |\n|---|---|---:|---:|---:|---:|---:|---:|---|\n'
trs=[]
for r in rows:
 vals=[r['level'],r['country'],f"{r['correct']}/{r['forward_checks']}",r['spelling_slips'],r['recall_gaps'],r['forward_omissions'],r['consecutive_correct'],f"{r['reverse_correct']}/{r['reverse_checks']}",r['note']]
 md+='| '+' | '.join(map(str,vals))+' |\n'
 history=', '.join(f"R{x['round']}: {x['result']}" for x in r['events'])
 trs.append('<tr data-search="'+html.escape(norm(r['country']))+'">'+''.join('<td>'+html.escape(str(v))+'</td>' for v in vals[:-1])+'<td><details><summary>'+html.escape(r['note'])+'</summary>'+html.escape(history)+'</details></td></tr>')
Path(str(out)+'.md').write_text(md)
page='''<!doctype html><html lang="en"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Country-capital recall — round 54</title><style>body{font:16px/1.5 system-ui;margin:30px;background:#faf9f6;color:#24313c}main{max-width:1500px;margin:auto}td,th{padding:10px;text-align:left;border-bottom:1px solid #ddd;vertical-align:top}table{border-collapse:collapse;font-size:14px}thead{background:#eaece8}input{font:inherit;padding:10px}summary{cursor:pointer}.scroll{overflow:auto}@media print{input{display:none}}</style><main><h1>Your country-capital recall</h1><p>12 September 2026 · Through round 54 · 195 countries · Strongest first, alphabetical within each band</p><ol>'''+legend+'</ol><details><summary>Method and limits</summary>'+''.join('<p>'+html.escape(x)+'</p>' for x in method.split('\n\n'))+'</details><p><label>Find a country <input id="filter" type="search"></label></p><p id="count">195 countries</p><div class="scroll"><table><thead><tr>'+''.join('<th>'+s+'</th>' for s in ['Band','Country','Exact forward / prompts','Spelling slips','Recall gaps','Omissions','Clean streak','Reverse correct / prompts','Current state and forward history'])+'</tr></thead><tbody>'+''.join(trs)+'''</tbody></table></div></main><script>document.querySelector('#filter').addEventListener('input',e=>{const q=e.target.value.normalize('NFD').replace(/[\u0300-\u036f]/g,'').toLowerCase().replace(/’/g,"'");let n=0;document.querySelectorAll('tbody tr').forEach(r=>{r.hidden=!r.dataset.search.includes(q);if(!r.hidden)n++});document.querySelector('#count').textContent=n+' countries'})</script></html>'''
Path(str(out)+'.html').write_text(page)
print('Bands:',{labels[i]:sum(r['level']==i for r in rows) for i in labels})
print('Rounds36–54 forward:',{s:sum(x['result']==s for x in recent) for s in ['correct','spelling','miss','omission']})
print('Last ten forward rounds:',{s:sum(x['result']==s for x in recent if x['round']>=44) for s in ['correct','spelling','miss','omission']})
print('Validated: 195 unique countries, 564 forward prompts, 84 reverse prompts; HTML, MD, JSON generated.')
