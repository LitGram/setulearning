"""Append the independently solved official-paper selections as chapter 14."""
from pathlib import Path
from collections import Counter
import json
import runpy

ROOT=Path(__file__).resolve().parents[1]
SOURCE=ROOT/'10th rbse/02_science'
LABELS='अबसद'

def create_chapter():
    d=runpy.run_path(str(SOURCE/'pyq_source.py'))
    answers,questions=d['ANSWERS'],d['QUESTIONS']
    manifest=json.loads((ROOT/'artifacts/rbse10_science/papers/manifest.json').read_text(encoding='utf-8'))
    papers={p['id']:p for p in manifest if 'id' in p}
    source=runpy.run_path(str(SOURCE/'source.py'))['CHAPTERS']
    topics={c['number']:c['title'] for c in source}
    topics[0]='पुराना पाठ्यक्रम / enrichment: वर्तमान core से बाहर'
    blocks=[]
    def add(kind,value,**kw):blocks.append(dict(type=kind,value=value.strip(),**kw))
    add('heading','अध्याय का उपयोग और स्रोत सीमा')
    counts=Counter(q['paper'] for q in questions)
    add('callout',f'{len(questions)} स्रोत-संदर्भित हल किए प्रश्न/उपभाग, {len(counts)} आधिकारिक मुख्य/पूरक पेपरों से। प्रश्नों के संक्षिप्त हिंदी सार और मौलिक solutions हैं; पूरे पेपरों का शब्दशः पुनर्मुद्रण या official answer key नहीं।')
    add('text','प्रश्न का year, main/supplementary, original question/subpart और PDF viewer page दिया है। Printed page और PDF page अलग हो सकते हैं। बड़े प्रश्न का selected part ही लिया गया हो तो उसका संक्षिप्त focus दिखता है; इसे पूरे प्रश्न का exhaustive solution न मानें। अंक source में दिए selected scope के हैं; अलग अंक स्पष्ट न हो तो “अलग सत्यापित नहीं” लिखा है।\n\nRepeated exam occurrences अलग source references के साथ रखे हैं; यह distinct concepts की count नहीं। मुख्य अध्याय 1–13 के 80-अंक chapter weightage में यह अभ्यास अध्याय अलग अतिरिक्त weightage नहीं जोड़ता। 2021 archive PDF image-based है और यहाँ verified question source नहीं माना गया।')
    add('heading','वर्षवार स्रोत रजिस्टर')
    lines=['| वर्ष / परीक्षा | चुने प्रश्न/उपभाग | मूल स्रोत |','|---|---:|---|']
    ids=sorted(counts,key=lambda k:(-papers[k]['year'],papers[k]['session']))
    for pid in ids:
        p=papers[pid];session='मुख्य' if p['session']=='main' else ('विशेष पूरक' if pid=='2017_supplementary' else 'पूरक')
        lines.append(f"| {p['year']} / {session} | {counts[pid]} | [S-07 मूल पेपर]({p['url']}) |")
    add('text','\n'.join(lines))
    add('heading','लिखित उत्तर का तरीका')
    add('text','पहले source का पूरा प्रश्न पढ़ें, फिर answer छिपाकर हल करें। Numerical में given quantities → SI conversion → formula → substitution → result/unit लिखें। Diagram में labels, arrow direction और requested part दें। यहाँ दिए solutions लेखक के शिक्षण उत्तर हैं; अंक-वितरण का आधिकारिक मूल्यांकन दावा नहीं।')
    provenance=[]
    figures={'electrolysis':'pyq_water.png','uniformfield':'pyq_uniform.png','budding':'pyq_budding.png','slab':'pyq_slab.png','dispersion':'pyq_dispersion.png','solenoid':'pyq_solenoid.png','fieldprops':'pyq_barfield.png','insidefield':'pyq_barfield.png','sexdetermination':'pyq_sex.png','graphRA':'pyq_ra.png','ohm':'pyq_vi.png','reflex':'rbse10_sci_06.png','foodenergy':'rbse10_sci_13.png'}
    # Show each useful diagram once; subsequent solutions point to the same
    # concept figure instead of inflating a long chapter with duplicate assets.
    shown=set()
    order={}
    for pid in ids:
        p=papers[pid];session='मुख्य' if p['session']=='main' else ('विशेष पूरक' if pid=='2017_supplementary' else 'पूरक')
        add('heading',f"{p['year']} — {session} परीक्षा")
        add('text',f"[{p['year']} {session}: पूरा आधिकारिक प्रश्न-पत्र]({p['url']})")
        for q in [q for q in questions if q['paper']==pid]:
            answer=answers[q['key']];topic=answer['topic'];number=len(provenance)+1
            uid=f"pyq_{pid}_{number:03}"
            order[(pid,q['ref'])]=number
            mark=q['marks']+' अंक' if q['marks']!='-' else 'अलग अंक सत्यापित नहीं'
            tag='**पुराना पाठ्यक्रम:** ' if topic==0 else ''
            add('heading',f"{number}. {q['prompt']}")
            add('text',f"**स्रोत:** {p['year']} {session}, प्रश्न {q['ref']}, PDF पृष्ठ {q['page']} · **अंक:** {mark}\n\n**अध्याय-संबंध:** {topics[topic]}\n\n{tag}**हल:** {answer['answer']}\n\n[मूल प्रश्न देखें]({p['url']}#page={q['page']})")
            if q['key'] in figures:
                fig=figures[q['key']]
                if fig not in shown:
                    add('image',fig,caption=f"मौलिक शिक्षण schematic: {q['prompt']} — source paper का scan नहीं।")
                    shown.add(fig)
                else:
                    add('text','चित्र सहायता: इसी अध्याय में इस अवधारणा का पहले दिया नामांकित schematic देखें।')
            provenance.append(dict(id=uid,**q,year=p['year'],session=p['session'],url=p['url'],source_sha256=p['sha256'],topic=topic,answer=answer['answer'],scope='selected original subquestion / concise paraphrase',solution_author='Setu Learning; not official marking key'))
    # Adapted revision MCQs: one sourced prompt per selected paper, with
    # author-created distractors and transparent source reference.
    quiz_specs=[
        ('2026_main','1(i)','Pancreas',['Thyroid','Pituitary','Adrenal']),
        ('2026_supplementary','1(ii)','Hydra',['Amoeba','Spirogyra','Rhizopus']),
        ('2025_main','1(v)','1:2:1',['3:1','1:1','9:3:3:1']),
        ('2025_supplementary','1(x)','12 V',['6 V','24 V','48 V']),
        ('2024_main','1(x)','6 m',['3 m','1.5 m','9 m']),
        ('2024_supplementary','1(x)','10 m',['5 m','2.5 m','20 m']),
        ('2023_main','1(ii)','Cerebellum',['Medulla','Cerebrum','Spinal cord']),
        ('2022_main','1(ix)','लगभग 2.26×10⁸ m/s',['3×10⁸ m/s','1.33×10⁸ m/s','3.99×10⁸ m/s']),
        ('2020_main','25','440 Ω; 110 W',['110 Ω; 440 W','220 Ω; 220 W','440 Ω; 55 W']),
        ('2020_supplementary','25(b)','4320 J',['120 J','72 J','3600 J']),
        ('2019_main','20(b)','CH₄',['C₂H₆','C₂H₄','C₂H₂']),
        ('2018_main','25(b)','5184 J',['144 J','129600 J','25 J']),
        ('2018_supplementary','25(b)','2×10⁻⁴ C',['2×10⁻³ C','0.2 C','200 C']),
        ('2017_main','24','30 C',['1 C','30 A','0.033 C']),
        ('2017_supplementary','1','Brass',['Bronze','Steel','Solder']),
        ('2016_main','24','₹576',['₹144','₹240','₹57.60']),
        ('2015_main','7','11',['5','10','22']),
        ('2014_main','8','1 A',['60 A','0.2 A','300 A']),
    ]
    lookup={(q['paper'],q['ref']):q for q in questions}
    mcqs=[]
    add('heading','PYQ आधारित पुनरावृत्ति क्विज़ — 18 प्रश्न')
    add('text','वर्ष-संदर्भ वास्तविक हैं। नीचे प्रश्न-सार और distractor विकल्प लेखक द्वारा पुनर्गठित हैं; इन्हें मूल पेपर के option letters का पुनर्मुद्रण न मानें।')
    for i,(pid,ref,correct,distractors) in enumerate(quiz_specs):
        q=lookup[(pid,ref)];choices=[correct]+distractors;rotation=i%4
        choices=choices[rotation:]+choices[:rotation]
        m=dict(question=f"[{papers[pid]['year']} {'मुख्य' if papers[pid]['session']=='main' else 'पूरक'}, Q {ref}] {q['prompt']}",options=choices,correctIndex=choices.index(correct),explanation=answers[q['key']]['answer']+f" स्रोत: प्रश्न {ref}, PDF पृष्ठ {q['page']}।",sourceQuestionId=next(r['id'] for r in provenance if r['paper']==pid and r['ref']==ref))
        mcqs.append(m)
        add('text',f"**क्विज़ {i+1}. {m['question']}**\n\n"+'\n'.join(f'{LABELS[j]}) {v}  ' for j,v in enumerate(choices))+f"\n\n**उत्तर: {LABELS[m['correctIndex']]} — {correct}।** {m['explanation']}")
    add('heading','अंतिम अभ्यास और आगे की कड़ी')
    add('text','किसी एक year का source paper खोलकर timer के साथ पूरा paper attempt करें। Selected solutions से covered parts check करें; unselected questions को इस bank के नाम पर solved न मानें। पुराने/removed topics को current syllabus से मिलाएँ। गलत उत्तरों को chemical equations, biology terms, optics signs और electrical units की चार lists में रखें।\n\n**आगे की कड़ी:** मुख्य अध्याय 1–13 में कमजोर concept पर लौटें। यह अंतिम अभ्यास अध्याय है।')
    # MCQ parser ignores unknown metadata; keep provenance in a separate file
    # so model round-trip equality remains exact.
    for m in mcqs:m.pop('sourceQuestionId')
    chapter=dict(id='sci_ch14',title='अध्याय 14: पिछले वर्षों के हल किए परीक्षा प्रश्न',subtitle='Solved Previous-Year Examination Questions (2014–2026 selections)',content=blocks,mcqs=mcqs)
    markdown=['# '+chapter['title'],'',f"**चयनित हल:** {len(provenance)} · **आधिकारिक पेपर:** {len(ids)}",'']
    for b in blocks:
        if b['type']=='heading':markdown.extend(['## '+b['value'],''])
        elif b['type']=='image':markdown.extend([f"![{b['caption']}](../../assets/images/{b['value']})",''])
        elif b['type']=='callout':markdown.extend(['> '+b['value'],''])
        else:markdown.extend([b['value'],''])
    (SOURCE/'ch14_previous_year_exams.md').write_text('\n'.join(markdown),encoding='utf-8')
    (SOURCE/'pyq_provenance.json').write_text(json.dumps(dict(verified_date='2026-10-12',solved_occurrences=len(provenance),papers=len(ids),unique_solution_concepts=len({q['key'] for q in questions}),questions=provenance),ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    return chapter,dict(id='sci_ch14',file='10th rbse/02_science/ch14_previous_year_exams.md',mcqs=len(mcqs),blocks=len(blocks),characters=sum(len(b['value']) for b in blocks),marks=0,solved_questions=len(provenance),papers=len(ids))

if __name__=='__main__':
    chapter,stats=create_chapter()
    print(stats)
