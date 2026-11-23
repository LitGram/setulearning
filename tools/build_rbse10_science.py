"""Build the chapter manuscripts and app asset without dropping post-quiz sections."""
from pathlib import Path
import importlib.util
import json
import re

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / '10th rbse/02_science'
LABELS = 'अबसद'
SYLLABUS = 'https://rajeduboard.rajasthan.gov.in/anudeshika-etc/10_2026.pdf'
PAPER = 'https://rajeduboard.rajasthan.gov.in/books/PAPERS-2025/Sec/S-07.pdf'

def rows(text, count=None):
    result = [line.split('|') for line in text.strip().splitlines() if line.strip()]
    if count is not None:
        assert len(result) == count, (len(result), count)
    return result

def build():
    spec = importlib.util.spec_from_file_location('science_source', SOURCE / 'source.py')
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    chapters = []
    stats = []
    for ch in module.CHAPTERS:
        n = ch['number']
        terms = rows(ch['terms'], 10)
        worked = rows(ch['worked'], 3)
        short = rows(ch['short'], 6)
        long = rows(ch['long'], 4)
        extended = rows(ch['extended'], 2)
        raw_mcqs = rows(ch['mcqs'], 15)
        mcqs = []
        for i, (question, correct, b, c, d, why) in enumerate(raw_mcqs):
            options = [correct, b, c, d]
            rotation = (i + n) % 4
            options = options[rotation:] + options[:rotation]
            mcqs.append(dict(question=question, options=options,
                             correctIndex=options.index(correct), explanation=why))
        blocks = []
        def add(kind, value, **kwargs):
            blocks.append(dict(type=kind, value=value.strip(), **kwargs))
        def heading(text):
            add('heading', text)
        heading('भाग 1: अध्याय प्रवेश एवं पाठ्यक्रम मैपिंग')
        add('callout', 'प्रथम संपादकीय प्रारूप। इस अध्याय का 2026–27 पाठ्यक्रम-क्षेत्र मिलाया गया है; NCERT के सभी प्रश्नों के हल तथा पूरा ऐतिहासिक PYQ संग्रह अभी स्रोत-परीक्षण में हैं।')
        add('text', f"**विषय कोड:** 07 · **श्रृंखला पुस्तक:** 2\n\n**सत्यापित आधार:** RBSE 2026–27 · **अध्याय भार:** {ch['marks']} अंक। यह आधिकारिक chapter weight है; वास्तविक प्रश्न-विभाजन की भविष्यवाणी नहीं।\n\n**सीखने के लक्ष्य:** {ch['goals']}")
        heading('भाग 2: शब्दावली एवं अवधारणा कैप्सूल')
        add('text', '| शब्द / सूत्र | अर्थ / उपयोग |\n|---|---|\n' + '\n'.join(f'| {t} | {v} |' for t, v in terms))
        heading('भाग 3: विस्तृत शिक्षण पाठ')
        for para in ch['theory'].strip().split('\n\n'):
            add('text', para)
        add('image', f'rbse10_sci_{n:02}.png', caption=ch['caption'])
        heading('भाग 4: पाठ्यपुस्तक-अवधारणाओं पर मौलिक हल किए उदाहरण')
        add('text', 'नीचे के प्रश्न लेखक के मौलिक मॉडल हैं। ये किसी NCERT edition के प्रश्न क्रमांक या संपूर्ण in-text/exercise solution bank होने का दावा नहीं करते।')
        for i, (q, a) in enumerate(worked, 1):
            add('text', f'**हल किया उदाहरण {i}: {q}**\n\n{a}')
        heading('भाग 5: सत्यापित बोर्ड प्रश्न एवं स्रोत-स्थिति')
        if ch.get('pyq'):
            add('text', ch['pyq'] + f'\n\n[RBSE 2025 मूल पेपर]({PAPER})। प्रश्न का संक्षिप्त विषय-संदर्भ है; शब्दशः पुनर्मुद्रण नहीं।')
        else:
            add('text', f'इस अध्याय का वर्षवार PYQ audit अभी पूरा नहीं है। अभ्यास प्रश्नों पर काल्पनिक परीक्षा-वर्ष नहीं लगाए गए हैं। [असली 2025 बोर्ड पेपर]({PAPER}) से प्रश्न, उपभाग और अंक मिलाकर ही नया PYQ जोड़ा जाए।')
        heading('भाग 6: खंडवार मौलिक अभ्यास बैंक')
        add('text', '**अभ्यास-अंक:** लेखक के स्व-अभ्यास के लिए हैं; RBSE की आधिकारिक marking scheme नहीं। उत्तर पहले स्वयं लिखें, फिर भाग 9 देखें।')
        heading('अ: बहुविकल्पीय प्रश्न — 15 × 1 अंक')
        for i, m in enumerate(mcqs, 1):
            add('text', f"**MCQ {i}. {m['question']}**\n\n" + '\n'.join(f'{LABELS[j]}) {o}  ' for j, o in enumerate(m['options'])))
        heading('आ: रिक्त स्थान — 6 × 1 अंक')
        blanks = [f'{definition} — इस शब्द/सूत्र का नाम है: ____।' for term, definition in terms[:6]]
        add('text', '\n'.join(f'{i}. {q}  ' for i, q in enumerate(blanks, 1)))
        heading('इ: अतिलघु उत्तर — 8 × 1 अंक')
        add('text', '\n'.join(f'{i}. {m[0]}  ' for i, m in enumerate(raw_mcqs[:8], 1)))
        heading('ई: लघु उत्तर — 6 × 2 अंक')
        add('text', '\n\n'.join(f'**B{i}.** {q}' for i, (q, _) in enumerate(short, 1)))
        heading('उ: दीर्घ उत्तर — 4 × 3 अंक')
        add('text', 'आंतरिक विकल्प अभ्यास: C1 अथवा C2, तथा C3 अथवा C4 चुनें। पुनरावृत्ति में बचा विकल्प भी हल करें। यह लेखक की अभ्यास व्यवस्था है।')
        add('text', '\n\n'.join(f'**C{i}.** {q}' for i, (q, _) in enumerate(long, 1)))
        heading('ऊ: विस्तृत उत्तर — 2 × 4 अंक')
        add('text', 'आंतरिक विकल्प अभ्यास: D1 अथवा D2 चुनें; बाद में दूसरा भी हल करें।')
        add('text', '\n\n'.join(f'**D{i}.** {q}' for i, (q, _) in enumerate(extended, 1)))
        heading('भाग 7: सावधानियाँ एवं परीक्षा-त्रुटियाँ')
        add('text', ch['traps'])
        heading('भाग 8: फटाफट पुनरावृत्ति — 25 बिंदु')
        revision = [f'{t}: {d}' for t, d in terms] + [m[-1] for m in raw_mcqs]
        add('text', '\n'.join(f'{i}. {v}  ' for i, v in enumerate(revision, 1)))
        heading('भाग 9: संपूर्ण अभ्यास उत्तर-कुंजी')
        heading('MCQ: सही विकल्प और कारण')
        add('text', '\n\n'.join(f"**{i}. {LABELS[m['correctIndex']]} — {m['options'][m['correctIndex']]}।** {m['explanation']}" for i, m in enumerate(mcqs, 1)))
        add('text', '**रिक्त स्थान:** ' + '; '.join(f'{i}. {t}' for i, (t, _) in enumerate(terms[:6], 1)))
        add('text', '**अतिलघु उत्तर:**\n\n' + '\n\n'.join(f'{i}. {m[1]}। {m[-1]}' for i, m in enumerate(raw_mcqs[:8], 1)))
        for code, questions in [('B', short), ('C', long), ('D', extended)]:
            for i, (q, a) in enumerate(questions, 1):
                add('text', f'**{code}{i}. {q}**\n\n{a}')
        heading('भाग 10: 10 मिनट / 10 अंक आत्म-मूल्यांकन एवं संदर्भ')
        add('text', f"समय: 10 मिनट। पहले पुस्तक बंद करें।\n\n1. MCQ 3 और 11 हल करें। (1 + 1)\n2. B2 और B5 के उत्तर लिखें। (2 + 2)\n3. D1 हल करें। (4)\n\n**कुंजी:** भाग 9 में संबंधित क्रमांक देखें। **स्व-मूल्यांकन:** 8–10: आगे बढ़ें; 5–7: छूटे कौशल का दोहराव; 0–4: भाग 2–4 फिर पढ़ें। यह अभ्यास-सुझाव है, बोर्ड grade नहीं।\n\n[सत्यापित RBSE 2026–27 पाठ्यक्रम]({SYLLABUS}) · [NCERT विज्ञान अध्याय {n}](https://ncert.nic.in/textbook/pdf/jesc1{n:02}.pdf)\n\n**आगे की कड़ी:** {ch['bridge']}")
        chapter = dict(id=f'sci_ch{n:02}', title=f"अध्याय {n}: {ch['title']}", subtitle=ch['english'], content=blocks, mcqs=mcqs)
        chapters.append(chapter)
        md = [f"# {chapter['title']} ({ch['english']})", '']
        for b in blocks:
            if b['type'] == 'heading': md.extend(['## ' + b['value'], ''])
            elif b['type'] == 'image': md.extend([f"![{b['caption']}](../../assets/images/{b['value']})", '', b['caption'], ''])
            elif b['type'] == 'callout': md.extend(['> ' + b['value'], ''])
            else: md.extend([b['value'], ''])
        path = SOURCE / f'ch{n:02}.md'
        path.write_text('\n'.join(md), encoding='utf-8')
        stats.append(dict(id=chapter['id'], file=str(path.relative_to(ROOT)), mcqs=len(mcqs), blocks=len(blocks), characters=sum(len(b['value']) for b in blocks), marks=ch['marks']))
    assert [c['id'] for c in chapters] == [f'sci_ch{i:02}' for i in range(1, 14)]
    assert sum(s['marks'] for s in stats) == 80
    from build_rbse10_science_pyq import create_chapter
    pyq_chapter, pyq_stats = create_chapter()
    chapters.append(pyq_chapter)
    stats.append(pyq_stats)
    asset = ROOT / 'assets/content/rbse10_science/science_book1.json'
    asset.parent.mkdir(parents=True, exist_ok=True)
    asset.write_text(json.dumps(dict(subject='RBSE 10th Science', book='कक्षा 10 विज्ञान: अध्यायवार गाइड (प्रारूप)', editorialStatus='first-draft', verifiedSyllabus='2026-27', chapters=chapters), ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    report = ROOT / 'artifacts/rbse10_science/completeness.json'
    report.parent.mkdir(parents=True, exist_ok=True)
    report.write_text(json.dumps(dict(chapters=stats, total_mcqs=sum(s['mcqs'] for s in stats), solved_pyqs=pyq_stats['solved_questions'], official_papers=pyq_stats['papers'], pending=['regular 2026-27 syllabus confirmation', 'exhaustive NCERT question coverage', 'unselected past-paper questions and image-only 2021 file', 'anatomical and full ray-diagram pack', 'independent teacher review']), ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    print(f'Built {len(chapters)} chapters / {sum(s["mcqs"] for s in stats)} MCQs.')

if __name__ == '__main__':
    build()
