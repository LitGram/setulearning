"""Add three representative scene illustrations alongside precise diagrams."""
import argparse
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / 'artifacts/rassetu_series/batch10_manifest.json'
NOTE = '**चित्र से सीखें — प्रतिनिधि चित्रण**'
PLACEMENTS = [
    (3, ['ch35', 'ch36'], '## 18.1 अध्याय परिचय एवं परीक्षा दृष्टिकोण',
     'rassetu_b3_salt_march_scene.webp', 'नमक सत्याग्रह से प्रेरित दृश्य',
     '1930 के नमक सत्याग्रह से प्रेरित प्रतिनिधि दृश्य। यह किसी विशेष दिन, स्थान या ऐतिहासिक व्यक्ति का दस्तावेजी पुनर्निर्माण नहीं है।'),
    (4, ['ch01', 'ch02'], '### 2.2 संविधान सभा का गठन, चुनाव एवं संरचना (कैबिनेट मिशन 1946)',
     'rassetu_b4_constituent_assembly_scene.webp', 'संविधान सभा की चर्चा: प्रतिनिधि दृश्य',
     'संविधान सभा की सामूहिक विचार-प्रक्रिया का व्याख्यात्मक दृश्य। प्रतिनिधि और सभा-कक्ष किसी विशिष्ट बैठक का सटीक चित्रण नहीं हैं।'),
    (5, ['ch11', 'ch12'], '### 2.1 भारतीय कृषि का संरचनात्मक ढांचा',
     'rassetu_b5_agriculture_market_scene.webp', 'खेत से स्थानीय बाजार तक: प्रतिनिधि कृषि दृश्य',
     'खेती, कटाई और स्थानीय विपणन से प्रेरित प्रतिनिधि दृश्य। फसल, मौसम, क्षेत्र और मूल्य की सटीक जानकारी इस चित्र से न निकालें।'),
]

def digest(value):
    return hashlib.sha256(json.dumps(value, ensure_ascii=False, sort_keys=True,
        separators=(',', ':')).encode()).hexdigest()

def main(check=False):
    books = {}
    manifest = {'version': 1, 'batch': 'Representative historical and agriculture scenes', 'placements': []}
    for book_num, chapter_ids, anchor, image, label, explanation in PLACEMENTS:
        if book_num not in books:
            p = ROOT / f'assets/content/rassetu/rassetu_book{book_num}.json'
            books[book_num] = (p, json.loads(p.read_text(encoding='utf-8')))
        _, book = books[book_num]
        image_path = ROOT / 'assets/images' / image
        if not image_path.is_file() or not image_path.read_bytes().startswith(b'RIFF'):
            raise FileNotFoundError(f'Missing or invalid WebP: {image_path}')
        for chapter_id in chapter_ids:
            chapter = next(c for c in book['chapters'] if c['id'] == chapter_id)
            content = chapter['content']
            indexes = [i for i, b in enumerate(content)
                       if b.get('type') == 'image' and b.get('value') == image]
            remove = set(indexes)
            for i in indexes:
                if i + 1 < len(content) and content[i + 1].get('type') == 'callout' and content[i + 1].get('value', '').startswith(NOTE):
                    remove.add(i + 1)
            original = [b for i, b in enumerate(content) if i not in remove]
            matches = [i for i, b in enumerate(original)
                       if b.get('type') == 'text' and b.get('value', '').startswith(anchor)]
            if len(matches) != 1:
                raise ValueError(f'{chapter_id}: expected one anchor, found {len(matches)}: {anchor}')
            additions = [
                {'type': 'image', 'value': image, 'caption': label},
                {'type': 'callout', 'value': NOTE + '\n\n' + explanation + '\n\nप्रतिनिधि चित्रण — केवल शैक्षिक समझ हेतु; इसे वास्तविक दृश्य का हूबहू चित्र न मानें।'},
            ]
            expected = original[:matches[0] + 1] + additions + original[matches[0] + 1:]
            if check and content != expected:
                raise ValueError(f'Unexpected or missing placement at Book {book_num}/{chapter_id}')
            if not check:
                chapter['content'] = expected
            manifest['placements'].append({'book': book_num, 'chapter': chapter_id,
                'originalChapterSha256': digest(dict(chapter, content=original)),
                'anchor': anchor, 'image': image, 'caption': label,
                'explanation': explanation})
    if not check:
        for asset, book in books.values():
            asset.write_text(json.dumps(book, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
        MANIFEST.write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    print(f"{'Verified' if check else 'Applied'} batch 10: three scene illustrations across {len(manifest['placements'])} chapter records; source text and MCQs preserved")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check', action='store_true')
    main(parser.parse_args().check)
