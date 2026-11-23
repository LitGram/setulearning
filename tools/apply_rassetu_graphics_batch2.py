"""Apply reviewed Book 4–6 RAS graphics with paired-chapter source guards."""
import argparse
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / 'artifacts/rassetu_series/batch2_manifest.json'

# Each RAS topic is stored twice in adjacent, identical app chapters. Insert into
# both copies so students see the same lesson regardless of chapter navigation.
PLACEMENTS = [
    (6, ['ch01','ch02'], '### 2.1 निगमनात्मक तर्क', 'rassetu_b6_deduction_induction.webp', 'निगमन और आगमन', 'सामान्य से विशिष्ट निगमन और उदाहरणों से सामान्यीकरण करने वाला आगमन तर्क अलग प्रक्रियाएं हैं। चित्र में दिए गए वाक्य केवल नमूना रूप हैं।'),
    (6, ['ch03','ch04'], '### 2.1 कथन एवं पूर्वधारणाएं', 'rassetu_b6_flow_कथन_म_ल_य_कन.webp', 'कथन का मूल्यांकन', 'तर्क, पूर्वधारणा और निष्कर्ष पहचानने का अभ्यास मॉडल। किसी वास्तविक प्रश्न का उत्तर उसके पूरे कथन पर निर्भर है।'),
    (6, ['ch09','ch10'], '### 2.1 संख्या श्रृंखला के 8 प्रमुख मास्टर पैटर्न', 'rassetu_b6_number_series.webp', 'संख्या-श्रृंखला के चरण', 'श्रृंखला में अंतर, अनुपात और वैकल्पिक पदों को जांचने का अभ्यास क्रम। हर प्रश्न में एक ही पैटर्न लागू नहीं होता।'),
    (6, ['ch13','ch14'], '### 2.1 रक्त संबंध: वंशवृक्ष', 'rassetu_b6_family_tree.webp', 'वंशवृक्ष संकेत', 'वंशवृक्ष में वृत्त और वर्ग प्रचलित परीक्षा-प्रतीक हैं। वास्तविक संबंध वही मानें जो प्रश्न में दिए हों।'),
    (6, ['ch15','ch16'], '### 2.1 वेन आरेख के 10 मानक प्रारूप', 'rassetu_b6_venn_models.webp', 'समुच्चय और प्रतिच्छेद', 'दो समुच्चयों और उनके साझा भाग का प्रतिनिधि वेन मॉडल। कौन-सा क्षेत्र छायांकित होगा, यह प्रश्न के कथन पर निर्भर है।'),
    (6, ['ch17','ch18'], '### 2.1 क्रम परीक्षण', 'rassetu_b6_ranking_formula.webp', 'क्रम-स्थान सूत्र', 'एक पंक्ति में कुल स्थान निकालने का नमूना: बाएं से स्थान + दाएं से स्थान − 1। प्रश्न की व्यवस्था पहले जांचें।'),
    (6, ['ch19','ch20'], '### 2.1 दर्पण एवं जल प्रतिबिंब', 'rassetu_b6_mirror_water.webp', 'दर्पण और जल प्रतिबिंब', 'सामान्य दर्पण-प्रतिबिंब में पार्श्व उलटाव और जल-प्रतिबिंब में ऊर्ध्व उलटाव का सरलीकृत मॉडल।'),
    (6, ['ch21','ch22'], '### 2.1 संख्याओं का पदानुक्रम एवं वर्गीकरण', 'rassetu_b6_number_system.webp', 'संख्या समुच्चयों का संबंध', 'वास्तविक संख्याओं में परिमेय और अपरिमेय उपसमुच्चय अलग हैं। पूर्णांक, पूर्ण संख्याओं और प्राकृतिक संख्याओं की परिभाषा भी देखें।'),
    (6, ['ch23','ch24'], '### 2.1 अनुपात एवं समानुपात', 'rassetu_b6_ratio_proportion.webp', 'अनुपात और समानुपात', 'समानुपात a:b = c:d में b और d शून्य नहीं होते; क्रॉस-गुणन से ad = bc मिलता है।'),
    (6, ['ch25','ch26'], '### 2.1 प्रतिशत एवं मानक भिन्न रूपांतरण तालिका', 'rassetu_b6_percent_fraction.webp', 'भिन्न, प्रतिशत और दशमलव', 'समान मान के कुछ प्रतिनिधि रूपांतरण। अन्य भिन्नों के लिए अंश को हर से भाग देकर प्रतिशत निकालें।'),
    (6, ['ch27','ch28'], '### 2.1 साधारण ब्याज', 'rassetu_b6_simple_compound_interest.webp', 'साधारण और चक्रवृद्धि ब्याज', 'सूत्र में वार्षिक दर और वार्षिक चक्रवृद्धि की मूल धारणा है; अन्य चक्र-अवधि पर दर और समय को समायोजित करें।'),
    (6, ['ch29','ch30'], '### 2.1 त्रिभुज', 'rassetu_b6_geometry_shapes.webp', 'त्रिभुज: क्षेत्रफल और कोण', 'त्रिभुज का क्षेत्रफल ½ × आधार × लंबवत ऊंचाई और आंतरिक कोणों का योग 180° होता है। आकृतियां पैमाने पर नहीं हैं।'),
    (6, ['ch31','ch32'], '### 2.1 केंद्रीय प्रवृत्ति के माप', 'rassetu_b6_mean_median_mode.webp', 'माध्य, माध्यिका और बहुलक', 'केंद्रीय प्रवृत्ति के तीन अलग माप; कौन-सा उपयोगी है, यह डेटा और प्रश्न पर निर्भर करता है।'),
    (6, ['ch37','ch38'], '### 2.1 शास्त्रीय प्रायिकता', 'rassetu_b6_probability.webp', 'शास्त्रीय प्रायिकता', 'सूत्र समान-संभावित परिणामों की धारणा पर है। उदाहरण निष्पक्ष छह-पक्षीय पासे का है।'),
    (4, ['ch11','ch12'], '### 2.4 विधायी प्रक्रिया एवं विधेयकों के प्रकार', 'rassetu_b4_bill_to_act.webp', 'विधेयक से अधिनियम तक', 'यह साधारण विधेयक के मार्ग का संक्षिप्त मॉडल है। धन विधेयक और संविधान संशोधन विधेयक की प्रक्रिया अलग हो सकती है।'),
    (5, ['ch11','ch12'], '### 2.1 भारतीय कृषि का संरचनात्मक ढांचा', 'rassetu_b5_agriculture_value_chain.webp', 'कृषि उत्पाद की मूल्य-शृंखला', 'उत्पादक से उपभोक्ता तक के कुछ सामान्य चरण। वास्तविक विपणन मार्ग, संस्थाएं और मूल्य-वितरण अलग-अलग होते हैं।'),
    (5, ['ch41','ch42'], '### 2.3 आनुवंशिक अभियांत्रिकी एवं पुनर्योजक डीएनए तकनीक', 'rassetu_b5_biotechnology_steps.webp', 'जैव-प्रौद्योगिकी का सामान्य कार्य-प्रवाह', 'विभिन्न तकनीकों में चरण, जांच और नियमन अलग होते हैं; यह किसी खास जीन-संपादन या उत्पाद की प्रक्रिया नहीं है।'),
]

def digest(value):
    return hashlib.sha256(json.dumps(value, ensure_ascii=False, sort_keys=True,
        separators=(',', ':')).encode()).hexdigest()

def load_book(book_num):
    asset = ROOT / f'assets/content/rassetu/rassetu_book{book_num}.json'
    return asset, json.loads(asset.read_text(encoding='utf-8'))

def main(check=False):
    books = {}
    manifest = {'version': 1, 'batch': 'Book 4–6 reasoning, governance, economy and technology', 'placements': []}
    for book_num, chapter_ids, anchor, image, label, explanation in PLACEMENTS:
        asset, book = books.setdefault(book_num, load_book(book_num))
        for chapter_id in chapter_ids:
            chapter = next(c for c in book['chapters'] if c['id'] == chapter_id)
            image_block = {'type':'image','value':image,'caption':label}
            prefix = '**चित्र से सीखें — प्रतिनिधि चित्रण**'
            note_block = {'type':'callout','value':prefix+'\n\n'+explanation+'\n\nप्रतिनिधि चित्रण — केवल शैक्षिक समझ हेतु; इसे वास्तविक दृश्य का हूबहू चित्र न मानें।'}
            additions = [image_block, note_block]
            indices = [i for i,b in enumerate(chapter['content']) if b.get('type')=='image' and b.get('value')==image]
            remove = set(indices)
            for i in indices:
                for j in (i+1,i-1):
                    if 0 <= j < len(chapter['content']) and chapter['content'][j].get('type')=='callout' and chapter['content'][j].get('value','').startswith(prefix):
                        remove.add(j); break
            original = [b for i,b in enumerate(chapter['content']) if i not in remove]
            matches = [i for i,b in enumerate(original) if b.get('type')=='text' and b.get('value','').startswith(anchor)]
            if len(matches) != 1:
                raise ValueError(f'{asset.name}/{chapter_id}: anchor expected once, found {len(matches)}: {anchor}')
            expected = original[:matches[0]+1] + additions + original[matches[0]+1:]
            image_path = ROOT / 'assets/images' / image
            if not image_path.is_file() or not image_path.read_bytes().startswith(b'RIFF'):
                raise ValueError(f'Missing or invalid WebP: {image_path}')
            if check and chapter['content'] != expected:
                raise ValueError(f'Placement missing/changed: {asset.name}/{chapter_id}')
            source_hash = digest(dict(chapter, content=original))
            if not check:
                chapter['content'] = expected
            manifest['placements'].append({'book':book_num,'chapter':chapter_id,'originalChapterSha256':source_hash,'anchor':anchor,'image':image,'caption':label,'explanation':explanation})
    if not check:
        for asset, book in books.values():
            asset.write_text(json.dumps(book,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
        MANIFEST.parent.mkdir(parents=True,exist_ok=True)
        MANIFEST.write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print(f"{'Verified' if check else 'Applied'} batch 2: {len(PLACEMENTS)} graphics across {len(manifest['placements'])} paired chapters; source text and MCQs preserved")

if __name__ == '__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check',action='store_true')
    main(parser.parse_args().check)
