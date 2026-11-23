"""Apply a reviewed, non-numeric economic-indicator comparison to Book 5."""
import argparse
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BOOK_PATH = ROOT / 'assets/content/rassetu/rassetu_book5.json'
MANIFEST = ROOT / 'artifacts/rassetu_series/batch8_manifest.json'
CHAPTERS = ['ch01', 'ch02']
ANCHOR = '### 2.1 आर्थिक संवृद्धि (Economic Growth): सैद्धांतिक एवं गणितीय आयाम'
IMAGE = 'rassetu_b5_gdp_price_indicators.webp'
CAPTION = 'आर्थिक एवं मानव-विकास संकेतक: क्या मापते हैं?'
NOTE = '**चित्र से सीखें — प्रतिनिधि चित्रण**'
EXPLANATION = ('GDP, मुद्रास्फीति, बेरोजगारी और मानव विकास अलग पहलुओं को मापते हैं। '
               'चित्र के वर्णन संक्षिप्त हैं; औपचारिक परिभाषा और गणना प्रयुक्त सांख्यिकीय श्रृंखला पर निर्भर करती है। इसमें आंकड़े नहीं हैं।')

def digest(value):
    return hashlib.sha256(json.dumps(value, ensure_ascii=False, sort_keys=True,
        separators=(',', ':')).encode()).hexdigest()

def main(check=False):
    book = json.loads(BOOK_PATH.read_text(encoding='utf-8'))
    image_path = ROOT / 'assets/images' / IMAGE
    if not image_path.is_file() or not image_path.read_bytes().startswith(b'RIFF'):
        raise FileNotFoundError(image_path)
    manifest = {'version': 1, 'batch': 'Book 5 economic indicators', 'placements': []}
    for chapter_id in CHAPTERS:
        chapter = next(c for c in book['chapters'] if c['id'] == chapter_id)
        content = chapter['content']
        indexes = [i for i, b in enumerate(content)
                   if b.get('type') == 'image' and b.get('value') == IMAGE]
        remove = set(indexes)
        for i in indexes:
            for j in (i - 1, i + 1):
                if 0 <= j < len(content) and content[j].get('type') == 'callout' and content[j].get('value', '').startswith(NOTE):
                    remove.add(j)
                    break
        original = [b for i, b in enumerate(content) if i not in remove]
        matches = [i for i, b in enumerate(original)
                   if b.get('type') == 'text' and b.get('value', '').startswith(ANCHOR)]
        if len(matches) != 1:
            raise ValueError(f'{chapter_id}: expected one anchor, found {len(matches)}')
        additions = [
            {'type': 'image', 'value': IMAGE, 'caption': CAPTION},
            {'type': 'callout', 'value': NOTE + '\n\n' + EXPLANATION + '\n\nप्रतिनिधि चित्रण — केवल शैक्षिक समझ हेतु; इसे वास्तविक दृश्य का हूबहू चित्र न मानें।'},
        ]
        expected = original[:matches[0] + 1] + additions + original[matches[0] + 1:]
        if check and content != expected:
            raise ValueError(f'Unexpected or missing placement at {chapter_id}')
        if not check:
            chapter['content'] = expected
        manifest['placements'].append({'chapter': chapter_id,
            'originalChapterSha256': digest(dict(chapter, content=original)),
            'anchor': ANCHOR, 'image': IMAGE, 'caption': CAPTION,
            'explanation': EXPLANATION})
    if not check:
        BOOK_PATH.write_text(json.dumps(book, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
        MANIFEST.write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    print(f"{'Verified' if check else 'Applied'} batch 8: one indicator graphic across {len(manifest['placements'])} paired chapters; source text and MCQs preserved")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check', action='store_true')
    main(parser.parse_args().check)
