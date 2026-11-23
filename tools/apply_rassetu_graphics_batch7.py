"""Apply a reviewed Preamble/constitutional-values concept diagram."""
import argparse
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BOOK_PATH = ROOT / 'assets/content/rassetu/rassetu_book4.json'
MANIFEST = ROOT / 'artifacts/rassetu_series/batch7_manifest.json'
CHAPTERS = ['ch03', 'ch04']
ANCHOR = '### 2.1 संविधान की प्रस्तावना (उद्देश्यिका): दार्शनिक आधार एवं मूल पाठ'
IMAGE = 'rassetu_b4_preamble_constitution.webp'
CAPTION = 'उद्देशिका के मूल्यों का संवैधानिक संबंध'
NOTE = '**चित्र से सीखें — प्रतिनिधि चित्रण**'
EXPLANATION = ('न्याय, स्वतंत्रता, समता और बंधुता को उद्देशिका से जुड़े मूल्यों के रूप में दिखाया गया है। '
               'चित्र केवल संबंध का संकल्पनात्मक सार है; संविधान के भागों और अनुच्छेदों की पूरी सूची नहीं।')

def digest(value):
    return hashlib.sha256(json.dumps(value, ensure_ascii=False, sort_keys=True,
        separators=(',', ':')).encode()).hexdigest()

def main(check=False):
    book = json.loads(BOOK_PATH.read_text(encoding='utf-8'))
    image_path = ROOT / 'assets/images' / IMAGE
    if not image_path.is_file() or not image_path.read_bytes().startswith(b'RIFF'):
        raise FileNotFoundError(image_path)
    manifest = {'version': 1, 'batch': 'Book 4 Preamble values', 'placements': []}
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
    print(f"{'Verified' if check else 'Applied'} batch 7: one Preamble-values graphic across {len(manifest['placements'])} paired chapters; source text and MCQs preserved")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check', action='store_true')
    main(parser.parse_args().check)
