from pathlib import Path
import json, re, html, unicodedata
p = Path(__file__).resolve().parents[1]
old = json.loads((p / 'reference/knowledge-estimate-2026-09-12-round-54.json').read_text())
rows = old['countries']
lookup = {r['country']: r for r in rows}
recent = []
reverse = []
for r in rows:
    r['recent_forward'] = []
    r['recent_reverse'] = []
for n in range(164, 174):
    f, = (p / 'learning-records').glob(f'{n:04d}-*.md')
    t = f.read_text()
    rd = int(re.search(r'round (\d+)', t.splitlines()[0])[1])
    rev = 'reverse' in t.splitlines()[0]
    line = next(s for s in t.splitlines() if ' → ' in s and ';' in s)
    pairs = [s.split(' → ') for s in line.rstrip('.').split('; ')]
    assert len(pairs) == 12
    for a, b in pairs:
        c = re.sub(r' \(.*\)$', '', b if rev else a)
        r = lookup[c]
        e = {'record': n, 'round': rd, 'result': 'correct'}
        if rev:
            r['reverse_checks'] += 1
            r['reverse_correct'] += 1
            r['recent_reverse'].append(e)
            reverse.append(e)
        else:
            if (rd, c) in [(57, 'Burkina Faso'), (58, 'Madagascar')]:
                e['result'] = 'spelling'
                e['self_corrected_before_feedback'] = rd == 57
            r['events'].append(e)
            r['recent_forward'].append(e)
            recent.append(e)
labels = {1: 'Strongest demonstrated recall', 2: 'Good recall; less confirmation or still consolidating', 3: 'Association known; name accuracy inconsistent', 4: 'Forward recall still fragile'}
for r in rows:
    a = r['events']
    scored = [e for e in a if e['result'] != 'omission']
    streak = 0
    for e in reversed(scored):
        if e['result'] != 'correct': break
        streak += 1
    misses = sum(e['result'] == 'miss' for e in a)
    sp = sum(e['result'] == 'spelling' for e in a)
    level = 4 if any(e['result'] == 'miss' for e in scored[-2:]) else 3 if scored and (scored[-1]['result'] == 'spelling' or (sp >= 2 and streak < 3)) else 1 if streak >= 3 or (len(scored) >= 2 and not misses and not sp) else 2
    r.update(level=level, band=labels[level], forward_checks=len(a), correct=sum(e['result']=='correct' for e in a), spelling_slips=sp, recall_gaps=misses, forward_omissions=sum(e['result']=='omission' for e in a), consecutive_correct=streak)
    r['last_error_record'] = next((e['record'] for e in reversed(a) if e['result'] in ['miss', 'spelling']), None)
    notes = []
    if r['recent_forward']:
        notes.append('Recent forward: ' + ', '.join('R'+str(e['round'])+': '+('self-corrected spelling' if e.get('self_corrected_before_feedback') else e['result']) for e in r['recent_forward']) + '.')
    else: notes.append('No forward test in rounds 55–64; band carries earlier evidence.')
    if r['recent_reverse']: notes.append('Reverse correct in round 61.')
    special = {'Madagascar': 'Antananarivo spelling corrected in R58, correct in R60 and R64.', 'Burkina Faso': 'Ouagadougou self-corrected before feedback in R57, correct in R60; initial slip conservatively interrupts the streak.', 'South Africa': 'Capital roles combined; judicial capital correct in R62.', 'Sri Lanka': 'Jayawardenepura and Jayewardenepura are both correct.', 'Botswana': 'Earlier R53 omission resolved without answer exposure; excluded from streak.', 'Maldives': 'Earlier Mauritius confusion; Malé correct in R55 and R60.'}
    if r['country'] in special: notes.append(special[r['country']])
    r['note'] = r['evidence'] = ' '.join(notes)
rows.sort(key=lambda r: (r['level'], r['country'].casefold()))
bands = {labels[i]: sum(r['level']==i for r in rows) for i in labels}
summary = {'recent_forward_prompts':len(recent), 'recent_first_submission_exact':sum(e['result']=='correct' for e in recent), 'recent_associations_identified':len(recent), 'recent_self_corrected_spelling':1, 'recent_feedback_corrected_spelling':1, 'recent_reverse_correct':len(reverse), 'recent_unique_forward_countries':sum(bool(r['recent_forward']) for r in rows), 'recent_unique_countries_either_direction':sum(bool(r['recent_forward'] or r['recent_reverse']) for r in rows), 'total_forward_prompts':sum(r['forward_checks'] for r in rows), 'total_reverse_prompts':sum(r['reverse_checks'] for r in rows), 'bands':bands}
assert len(rows)==len(lookup)==195
assert summary['total_forward_prompts']==672 and summary['total_reverse_prompts']==96
assert len(recent)==108 and summary['recent_first_submission_exact']==106 and len(reverse)==12
method = """Snapshot through round 64, 12 September 2026. Round 65 is pending and excluded. All 195 countries are included, sorted by observed recall band and then alphabetically. Previous snapshots remain unchanged.

The user confirms a good sleep between rounds 54 and 55. Rounds 55–64 are therefore a confirmed post-sleep block. This updates earlier records that called these rounds within-session evidence because the break was not yet known. First encounters in this block provide evidence of recall after sleep; later repeats also include fresh practice. This cannot measure the causal effect of sleep or establish week-long retention.

Recent block: 108/108 forward associations identified, 106/108 exact on first submission (98.1%), one spelling slip self-corrected before feedback (Burkina Faso), and one corrected by feedback (Madagascar). Madagascar was subsequently spelled correctly twice. Reverse recall: 12/12. No association gaps. The accidental early submission in round 57 is not a recall omission. The spelling metric conservatively retains its spontaneously corrected typo.

Cumulative counts: 56 forward rounds, 672 prompts; 8 reverse rounds, 96 prompts. Immediate correction drills are excluded. Earlier lessons established coverage of all 195 countries in both directions, including corrections. A country not tested in the recent block has no new evidence of retention from that block.

Bands retain the previous heuristic: strongest requires three consecutive clean forward answers or at least two with no forward errors; a miss among the last two scored forward checks means fragile; a latest spelling slip or repeated slips without three subsequent clean answers means inconsistent name accuracy; others are good/consolidating. These are working categories, not validated probabilities. Self-corrected spelling slips conservatively interrupt the first-submission streak. Omission events are excluded from streak calculations. Reverse success is separate from forward success, and multi-capital countries combine tested roles. Case, accents and accepted spelling variants do not count as errors. Self-reported starting knowledge does not affect bands.
"""
out=p/'reference/knowledge-estimate-2026-09-12-round-64'
Path(str(out)+'.json').write_text(json.dumps({'method':method,'summary':summary,'countries':rows}, ensure_ascii=False, indent=2))
cols=['Band','Country','Exact forward / prompts','Spelling slips','Recall gaps','Omissions','Clean streak','Reverse correct / prompts','Recent evidence']
md='# Country-capital recall through round 64\n\n'+method+'\n'
md+='\n'.join(f'- {k}: {v}' for k,v in bands.items())+'\n\n'
md+='| '+' | '.join(cols)+' |\n|'+ '|'.join(['---']*len(cols))+'|\n'
trs=[]
for r in rows:
    vals=[r['level'],r['country'],f"{r['correct']}/{r['forward_checks']}",r['spelling_slips'],r['recall_gaps'],r['forward_omissions'],r['consecutive_correct'],f"{r['reverse_correct']}/{r['reverse_checks']}",r['note']]
    md+='| '+' | '.join(map(str,vals))+' |\n'
    history=', '.join(f"R{e['round']}: {e['result']}"+(' (self-corrected)' if e.get('self_corrected_before_feedback') else '') for e in r['events'])
    trs.append('<tr>'+''.join('<td>'+html.escape(str(v))+'</td>' for v in vals[:-1])+'<td><details><summary>'+html.escape(r['note'])+'</summary>'+html.escape(history)+'</details></td></tr>')
Path(str(out)+'.md').write_text(md)
page='<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Capital recall through round 64</title><link rel="stylesheet" href="../assets/style.css"><link rel="stylesheet" href="../assets/status-report.css"><script defer src="../assets/status-report.js"></script></head><body><main><p class="eyebrow">12 September 2026 · Round 64 · 195 countries</p><h1>Your capital recall</h1><p class="score">108/108 associations · 98.1% first-submission spelling · 12/12 reverse</p><p>Post-sleep practice: rounds 55–64. User confirms sleep between rounds 54 and 55.</p><p>'+str(summary['recent_unique_forward_countries'])+' countries tested forward in this block; '+str(summary['recent_unique_countries_either_direction'])+' in either direction. Earlier evidence is retained for the rest.</p><ul>'+''.join('<li>'+html.escape(k)+': <b>'+str(v)+'</b></li>' for k,v in bands.items())+'</ul><details><summary>Method and limits</summary>'+''.join('<p>'+html.escape(x)+'</p>' for x in method.split('\n\n'))+'</details><p><a href="knowledge-estimate-2026-09-12-round-54.html">Previous snapshot: round 54</a></p><label class="no-print">Find a country <input id="filter" type="search"></label><p id="count">195 countries</p><div class="scroll"><table><thead><tr>'+''.join('<th>'+s+'</th>' for s in cols)+'</tr></thead><tbody>'+''.join(trs)+'</tbody></table></div><p>Ask your teaching agent about any result or correction. Round 65 remains pending.</p></main></body></html>'
Path(str(out)+'.html').write_text(page)
print(json.dumps(summary,indent=2))
