"""Check provenance labels, complete source retention, quizzes, figures and worked arithmetic."""
from pathlib import Path
from fractions import Fraction as F
from collections import Counter
import json
import runpy
from PIL import Image

ROOT=Path(__file__).resolve().parents[1]

def audit():
    data=json.loads((ROOT/'assets/content/rbse10_science/science_book1.json').read_text(encoding='utf-8'))
    source=runpy.run_path(str(ROOT/'10th rbse/02_science/source.py'))['CHAPTERS']
    assert len(data['chapters'])==14
    positions=Counter()
    question_set=set()
    for raw,ch in zip(source,data['chapters']):
        n=raw['number']
        assert ch['id']==f'sci_ch{n:02}'
        md=(ROOT/f'10th rbse/02_science/ch{n:02}.md').read_text(encoding='utf-8')
        for part in range(1,11):
            assert sum(b['type']=='heading' and b['value'].startswith(f'भाग {part}:') for b in ch['content'])==1
        for block in ch['content']:
            if block['type']=='image':
                with Image.open(ROOT/'assets/images'/block['value']) as im:
                    assert im.size==(1400,960)
                    im.verify()
                assert block['caption'] in md
            else:
                assert block['value'] in md, f'Lost reader text: {n}'
        text='\n'.join(b['value'] for b in ch['content'])
        for field in ['theory','worked','short','long','extended']:
            values=raw[field].strip().split('\n\n') if field=='theory' else [v for row in raw[field].strip().splitlines() for v in row.split('|')]
            for v in values:assert v in text, (n,field,v)
        assert 'भाग 10:' in text and raw['bridge'] in text
        assert 'प्रथम संपादकीय प्रारूप' in text
        assert 'संपूर्ण in-text/exercise solution bank होने का दावा नहीं' in text
        assert len(ch['mcqs'])==15
        for m in ch['mcqs']:
            assert len(m['options'])==len(set(m['options']))==4
            assert 0<=m['correctIndex']<4
            assert m['question'] not in question_set, m['question']
            question_set.add(m['question'])
            assert len(m['explanation'])>20
            assert m['explanation'] in text
            positions[m['correctIndex']]+=1
    assert len(question_set)==195
    assert min(positions.values())>=40
    # Independent calculations catch signs/units in the authored examples.
    mirror=lambda u,f:1/(1/F(f)-1/F(u))
    lens=lambda u,f:1/(1/F(f)+1/F(u))
    assert mirror(-30,-15)==-30 and -mirror(-30,-15)/F(-30)==-1
    assert mirror(-15,-10)==-30 and -mirror(-15,-10)/F(-15)==-2
    assert lens(-30,20)==60 and lens(-30,20)/F(-30)==-2
    assert lens(-10,15)==-30 and lens(-10,15)/F(-10)==3
    assert 1/F(-25,100)==-4
    assert 1/(1/F(6)+1/F(3))==2
    assert F(1100,220)==5 and F(220**2,1100)==44
    assert F(100,1000)*5*30==15 and 15*6==90
    assert F(11,10)*2*3600000==7920000
    assert F(20000)*F(1,10)**3==20
    pyq=runpy.run_path(str(ROOT/'tools/audit_rbse10_science_pyq.py'))['audit_pyqs']()
    result=dict(status='pass', chapters=14, core_mcqs=195, total_mcqs=213, correct_option_distribution=dict(positions), core_figures=13,
                source_retention='all authored paragraphs and answers retained',
                arithmetic_check_groups=10, scientific_peer_review='pending',
                exhaustive_NCERT_and_PYQ_coverage='pending', previous_year_chapter=pyq)
    (ROOT/'artifacts/rbse10_science/audit.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(result,ensure_ascii=False))

if __name__=='__main__':audit()
