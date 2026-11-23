"""Add three generated editorial illustrations beside their factual diagrams."""
import argparse
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / 'artifacts/rassetu_series/batch9_manifest.json'
NOTE = '**चित्र से सीखें — प्रतिनिधि चित्रण**'
PLACEMENTS = [
    (1, ['ch25', 'ch26'], '## 13.2 दुर्ग (किले) वास्तुकला — वर्गीकरण एवं प्रमुख दुर्ग',
     'rassetu_b1_fort_landscape_scene.webp', 'राजस्थान का पहाड़ी दुर्ग-परिदृश्य',
     'राजस्थान के पहाड़ी किलों और पथरीले भू-दृश्य से प्रेरित संयुक्त दृश्य। यह किसी नामित दुर्ग का सटीक ऐतिहासिक पुनर्निर्माण नहीं है।'),
    (1, ['ch31', 'ch32'], '## 16.2 शास्त्रीय एवं लोक नृत्य (Classical & Folk Dances of Rajasthan)',
     'rassetu_b1_folk_dance_scene.webp', 'घूमर-प्रेरित सामूहिक नृत्य दृश्य',
     'राजस्थानी सामूहिक नृत्य से प्रेरित प्रतिनिधि कला-दृश्य। परिधान और प्रस्तुति व्याख्यात्मक हैं; इसे किसी विशिष्ट समुदाय या प्रदर्शन का दस्तावेजी चित्र न मानें।'),
    (2, ['ch01'], '### 2.1 अरावली पर्वतमाला की भूगर्भिक उत्पत्ति',
     'rassetu_b2_aravalli_landscape_scene.webp', 'अरावली और जल-विभाजन का प्रतिनिधि भू-दृश्य',
     'अरावली की निम्न पहाड़ियों और दोनों ओर के जल-बहाव की संकल्पनात्मक कलात्मक झलक। यह सटीक स्थलाकृतिक/वर्षा मानचित्र या पैमाने पर बना अनुप्रस्थ काट नहीं है।'),
]

def digest(value):
    return hashlib.sha256(json.dumps(value, ensure_ascii=False, sort_keys=True,
        separators=(',', ':')).encode()).hexdigest()

def main(check=False):
    books = {}
    manifest = {'version': 1, 'batch': 'Generated representative scene illustrations', 'placements': []}
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
                for j in (i + 1,):
                    if 0 <= j < len(content) and content[j].get('type') == 'callout' and content[j].get('value', '').startswith(NOTE):
                        remove.add(j)
                        break
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
    print(f"{'Verified' if check else 'Applied'} batch 9: three generated illustrations across {len(manifest['placements'])} chapter records; original text and MCQs preserved")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check', action='store_true')
    main(parser.parse_args().check)
