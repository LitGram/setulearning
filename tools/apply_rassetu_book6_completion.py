"""Integrate the final eight source-matched figures across all Book 6 lessons."""
import argparse
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / 'artifacts/rassetu_series/batch11_manifest.json'
NOTE = '**चित्र से सीखें — प्रतिनिधि चित्रण**'
ILLUSTRATION_NOTE = 'प्रतिनिधि शैक्षिक चित्रण — यह आरेख/उदाहरण सांकेतिक है; इसे वास्तविक दृश्य, डेटा या आधिकारिक परीक्षा-निर्देश का हूबहू रूप न मानें।'

# Each paired lesson uses the same visual in both app chapter records.
LESSONS = [
    ('course_of_action_filter', 'उचित कार्यवाही: तीन प्रश्नों की निर्णय-कसौटी',
     '### 2.2 30-सेकंड शॉर्ट-ट्रिक बॉक्स (Decision Flowchart)',
     'तीन प्रश्नों की फिल्टर प्रक्रिया; किसी प्रश्न पर विफल विकल्प हटाएं।'),
    ('argument_cause_effect', 'कारण–प्रभाव तर्क: दावे की कड़ी परखें',
     '### 2.1 पैराग्राफ-आधारित तर्क का तीन-चरणीय मॉडल',
     'सांकेतिक दावा, प्रमाण और वैकल्पिक कारण; X/Y किसी वास्तविक घटना के बारे में नहीं हैं।'),
    ('coding_alphabet_map', 'कोडिंग–डिकोडिंग: वर्णमाला और चक्रीय शिफ्ट',
     '### 2.1 अंग्रेजी वर्णमाला के स्थान-मान एवं याद रखने के सूत्र',
     'A–Z स्थान, विपरीत-अक्षर योग 27 और चक्रीय +2 उदाहरण।'),
    ('data_interpretation_reading', 'आंकड़ा व्याख्या: चार कदम में चार्ट पढ़ें',
     '### 2.1 आंकड़ा विश्लेषण के चार प्रमुख प्रारूप एवं डेटा पठन तकनीक',
     'स्पष्ट रूप से काल्पनिक दो-बार अभ्यास चार्ट और तुलना प्रक्रिया।'),
    ('permutation_combination', 'क्रमचय और संचय: व्यवस्था बनाम चयन',
     '### 2.1 गणना के मूलभूत सिद्धांत (Fundamental Counting Principles)',
     'तीन व्यक्तियों में से दो: क्रम-निरपेक्ष चयन के 3 और क्रमबद्ध व्यवस्थाओं के 6 तरीके।'),
    ('current_affairs_verification', 'समसामयिकी: स्रोत से परीक्षा-संबंध तक',
     '### 2.1 नीतियां, अधिनियम एवं बड़े नीतिगत निर्णय 2026',
     'तथ्य-सत्यापन का स्थिर कार्यप्रवाह; इसमें कोई समय-संवेदी दावा नहीं जोड़ा गया।'),
    ('omr_fifth_option_workflow', 'पांचवां विकल्प: OMR भरने की सुरक्षित जांच',
     '### 3.2 RPSC 5वां विकल्प ओएमआर अंकन मास्टर प्रोटोकॉल',
     'OMR जांच-सूची; विकल्प, ऋणात्मक अंकन और समय-सीमा वर्तमान आधिकारिक अधिसूचना से मिलाएं।'),
    ('question_bank_review_loop', 'मास्टर प्रश्न बैंक: हल करें, जांचें, सुधारें',
     '## 22.1 अध्याय परिचय एवं अभ्यास निर्देश',
     'प्रश्न हल करने, उत्तर-कुंजी और व्याख्या से सीखने तथा त्रुटि-पुनरावृत्ति का अभ्यास-चक्र।'),
]

def digest(value):
    return hashlib.sha256(json.dumps(value, ensure_ascii=False, sort_keys=True,
        separators=(',', ':')).encode()).hexdigest()

def main(check=False):
    path = ROOT / 'assets/content/rassetu/rassetu_book6.json'
    book = json.loads(path.read_text(encoding='utf-8'))
    chapters = {c['id']: c for c in book['chapters']}
    placements = []
    for fig, caption, anchor, explanation in LESSONS:
        image = f'rassetu_b6_{fig}.webp'
        image_path = ROOT / 'assets/images' / image
        if not image_path.is_file() or not image_path.read_bytes().startswith(b'RIFF'):
            raise FileNotFoundError(f'Missing or invalid WebP: {image_path}')
        # Paired chapters are sequential (05/06, 07/08, ... 43/44).
        first = int(next(row['id'][2:] for row in chapters.values()
                         if any(b.get('type') == 'text' and b.get('value', '').startswith(anchor)
                                for b in row['content'])))
        for chapter_number in (first, first + 1):
            chapter_id = f'ch{chapter_number:02}'
            chapter = chapters[chapter_id]
            content = chapter['content']
            old = [i for i,b in enumerate(content)
                   if b.get('type') == 'image' and b.get('value') == image]
            remove = set(old)
            for i in old:
                if i + 1 < len(content) and content[i+1].get('type') == 'callout' and content[i+1].get('value','').startswith(NOTE):
                    remove.add(i+1)
            original = [b for i,b in enumerate(content) if i not in remove]
            matches = [i for i,b in enumerate(original)
                       if b.get('type') == 'text' and b.get('value','').startswith(anchor)]
            if len(matches) != 1:
                raise ValueError(f'{chapter_id}: expected exactly one anchor, found {len(matches)}: {anchor}')
            additions = [
                {'type':'image','value':image,'caption':caption},
                {'type':'callout','value':NOTE + '\n\n' + explanation + '\n\n' + ILLUSTRATION_NOTE},
            ]
            expected = original[:matches[0]+1] + additions + original[matches[0]+1:]
            if check and content != expected:
                raise ValueError(f'Unexpected or missing placement at Book 6/{chapter_id}')
            if not check:
                chapter['content'] = expected
            placements.append({'book':6,'chapter':chapter_id,
                'originalChapterSha256':digest(dict(chapter,content=original)),
                'anchor':anchor,'image':image,'caption':caption,'explanation':explanation})
    if not check:
        path.write_text(json.dumps(book,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
        MANIFEST.write_text(json.dumps({'version':1,'batch':'Book 6 complete lesson coverage','placements':placements},ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print(f"{'Verified' if check else 'Applied'} Book 6 completion: {len(LESSONS)} lesson pairs, {len(placements)} chapter records; original source hashes preserved")

if __name__ == '__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check',action='store_true')
    main(parser.parse_args().check)
