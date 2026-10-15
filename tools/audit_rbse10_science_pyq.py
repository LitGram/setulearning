"""Verify the final chapter's source integrity, solutions, scope and numerical results."""
from pathlib import Path
from collections import Counter
from fractions import Fraction as F
from PIL import Image
import hashlib
import json
import runpy

ROOT=Path(__file__).resolve().parents[1]

def audit_pyqs():
    raw=runpy.run_path(str(ROOT/'10th rbse/02_science/pyq_source.py'))
    provenance=json.loads((ROOT/'10th rbse/02_science/pyq_provenance.json').read_text(encoding='utf-8'))
    manifest=json.loads((ROOT/'artifacts/rbse10_science/papers/manifest.json').read_text(encoding='utf-8'))
    papers={p['id']:p for p in manifest}
    book=json.loads((ROOT/'assets/content/rbse10_science/science_book1.json').read_text(encoding='utf-8'))
    chapter=book['chapters'][-1]
    assert len(book['chapters'])==14 and chapter['id']=='sci_ch14'
    assert len(provenance['questions'])==len(raw['QUESTIONS'])==361
    text='\n'.join(b['value'] for b in chapter['content'])
    md=(ROOT/'10th rbse/02_science/ch14_previous_year_exams.md').read_text(encoding='utf-8')
    seen=set();perpaper=Counter();source_words=Counter();figures=set()
    for q in provenance['questions']:
        identity=(q['paper'],q['ref']);assert identity not in seen,identity;seen.add(identity)
        p=papers[q['paper']]
        assert 'rajeduboard.rajasthan.gov.in/books/' in q['url'] and '/S-07' in q['url']
        assert q['url']==p['url'] and q['source_sha256']==p['sha256']
        assert 1<=q['page']<=p['pages']
        assert q['answer']==raw['ANSWERS'][q['key']]['answer']
        assert q['answer'] in text and q['answer'] in md and q['prompt'] in md
        assert f"#page={q['page']}" in md
        assert float(q['marks'])>0 if q['marks']!='-' else True
        if q['topic']==0:assert '**पुराना पाठ्यक्रम:** **हल:** '+q['answer'] in text
        perpaper[q['paper']]+=1;source_words[q['paper']]+=len(q['prompt'].split())
    assert len(perpaper)==18 and '2021_main' not in perpaper
    for pid in perpaper:
        p=papers[pid]
        assert hashlib.sha256((ROOT/p['file']).read_bytes()).hexdigest()==p['sha256']
    for b in chapter['content']:
        if b['type']=='image':
            with Image.open(ROOT/'assets/images'/b['value']) as im:
                assert im.size==(1400,960);im.verify()
            figures.add(b['value'])
        else:assert b['value'] in md
    assert len(figures)==12
    assert len(chapter['mcqs'])==18
    for m in chapter['mcqs']:
        assert len(m['options'])==len(set(m['options']))==4
        assert 0<=m['correctIndex']<4 and m['explanation'] in text
        assert '[' in m['question'] and 'Q ' in m['question']
        # Account for repeated summaries in the revision quiz as well.
        for q in raw['QUESTIONS']:
            p=papers[q['paper']]
            if m['question'].endswith(q['prompt']) and f"[{p['year']} " in m['question'] and f"Q {q['ref']}]" in m['question']:
                source_words[q['paper']]+=len(q['prompt'].split());break
    assert max(source_words.values())<=200,source_words
    # Independently solve all authored numerical cases; compare result tokens
    # to the teaching solutions, avoiding a quiz-key-only consistency check.
    expected={
        'q300':(F(300,5*60),'1 A'),
        'lamps100':(F(60+40,220),'5/11'),
        'bulbs11':(F(220*5,100),'11 bulbs'),
        'q025':(F(25,100)*20*60,'300 C'),
        'iron840':(F(220**2,840),'1210/21'),
        'bill576':(F(600,1000)*8*30*4,'₹576'),
        'power110':(F(220)*F(1,2),'110 W'),
        'q30':(F(1)*30,'30 C'),
        'power2':(1/F(1,2),'2 D'),
        'speed2':(F(300000000)/F(3,2),'2×10⁸'),
        'res4':(F(2)/F(1,2),'4 Ω'),
        'heat5184':(F(12**2*15*60,25),'5184 J'),
        'qsmall':(F(4,1000)*F(5,100),'2×10⁻⁴'),
        'heat4320':(F(6**2*3600,30),'4320 J'),
        'half5':(F(5,2),'2.5 Ω'),
        'double3':(F(3)*2,'6 Ω'),
        'plane6':(F(3)*2,'6 m'),
        'plane10':(F(5)*2,'10 m'),
        'seriesR2':(F(12,2)-4,'2 Ω'),
        'voltage12':(F(24,2),'12 V'),
        'mechanics60':(F(1,2)*40*(2**2-1**2),'60 J'),
        'spring08':(F(1,2)*4000*F(2,100)**2,'0.8 J'),
        'mechanics1500':(F(1,2)*40*(10**2-5**2),'1500 J'),
        'force20':(F(200,10),'20 N'),
    }
    values=[1,F(5,11),11,300,F(1210,21),576,110,30,2,200000000,4,5184,F(1,5000),4320,F(5,2),6,6,10,2,12,60,F(4,5),1500,20]
    for (key,(value,token)),reference in zip(expected.items(),values):
        assert value==reference and token in raw['ANSWERS'][key]['answer'],key
    assert abs(3e8/1.33-2.26e8)<5e5
    out=dict(status='pass',solved_occurrences=361,official_papers=18,by_paper=dict(perpaper),unique_solution_concepts=len({q['key'] for q in provenance['questions']}),revision_mcqs=18,figures=12,new_figures=10,numerical_checks=25,max_summary_words_per_source=max(source_words.values()),coverage='selected questions and subparts; not every full paper',omitted='2021 image-only PDF; unreadable/ambiguous diagram-dependent and unselected parts')
    (ROOT/'artifacts/rbse10_science/pyq_audit.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    return out

if __name__=='__main__':print(json.dumps(audit_pyqs(),ensure_ascii=False))
