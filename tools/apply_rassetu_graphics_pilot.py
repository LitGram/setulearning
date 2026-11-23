"""Insert the reviewed Book 2 geography pilot without changing source text or MCQs."""
import argparse
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BOOK = ROOT / 'assets/content/rassetu/rassetu_book2.json'
MANIFEST = ROOT / 'artifacts/rassetu_geography_pilot/manifest.json'

CAPTIONS = {
    'watershed': 'अरावली के दोनों ओर जल-विभाजन की प्रतिनिधि संकल्पनात्मक आकृति। वास्तविक भू-दृश्य का हूबहू चित्र नहीं; सांकेतिक, पैमाने पर नहीं।',
    'drainage': 'बंगाल की खाड़ी, अरब सागर और आंतरिक अपवाह प्रणालियों के चुनिंदा उदाहरण। अरावली महत्वपूर्ण जल-विभाजक है, लेकिन नदी-बेसिनों की सीमाएं अधिक जटिल हैं। सांकेतिक अवधारणा-चित्र; पूरा नदी-मानचित्र नहीं।',
    'monsoon': 'मानसून, अरावली की दिशा और वर्षा-छाया का सरलीकृत प्रतिनिधि मॉडल। वास्तविक मानसून-वर्षा वितरण अधिक जटिल है।',
    'crop_belts': 'फसल और जलवायु संबंध के व्यापक उदाहरण। प्रतिनिधि चित्रण; जिला-सीमा या सटीक फसल-वितरण मानचित्र नहीं।',
    'water_harvesting': 'टांका, जोहड़ और खडीन की कार्य-विधि के सांकेतिक अनुप्रस्थ मॉडल। प्रतिनिधि चित्रण; स्थानीय संरचनाओं में विविधता होती है।',
}
PLACEMENTS = [
    ('ch01', '### 2.1 अरावली पर्वतमाला की भूगर्भिक उत्पत्ति', 'rassetu_b2_watershed.webp', 'watershed',
     'अरावली पर्वतमाला: राजस्थान का महान जल-विभाजक'),
    ('ch03', '### 2.1 अरावली पर्वतमाला: राजस्थान का महान जल-विभाजक', 'rassetu_b2_drainage.webp', 'drainage',
     'राजस्थान के अपवाह तंत्र'),
    ('ch05', '### 2.2 अरावली पर्वतमाला और राजस्थान में वर्षा की क्षेत्रीय विषमता', 'rassetu_b2_monsoon.webp', 'monsoon',
     'मानसून और अरावली का प्रभाव'),
    ('ch11', '### 2.1 राजस्थान में कृषि की प्रकृति', 'rassetu_b2_crop_belts.webp', 'crop_belts',
     'राजस्थान में फसल और जलवायु संबंध'),
    ('ch15', '### 2.8 पारंपरिक जल संरक्षण तकनीकें', 'rassetu_b2_water_harvesting.webp', 'water_harvesting',
     'राजस्थान की पारंपरिक जल-संचयन संरचनाएं'),
]

def digest(value):
    return hashlib.sha256(json.dumps(value, ensure_ascii=False, sort_keys=True,
        separators=(',', ':')).encode()).hexdigest()

def find_anchor(content, anchor):
    matches = [i for i, block in enumerate(content)
               if block.get('type') == 'text' and block.get('value', '').startswith(anchor)]
    if len(matches) != 1:
        raise ValueError(f'Expected one anchor {anchor!r}; found {len(matches)}')
    return matches[0]

def main(check=False):
    book = json.loads(BOOK.read_text(encoding='utf-8'))
    manifest = {'version': 1, 'asset': 'assets/content/rassetu/rassetu_book2.json', 'chapters': []}
    for chapter_id, anchor, image, caption_key, label in PLACEMENTS:
        chapter = next(c for c in book['chapters'] if c['id'] == chapter_id)
        image_block = {'type': 'image', 'value': image, 'caption': label}
        note_prefix = '**चित्र से सीखें — प्रतिनिधि चित्रण**'
        note_block = {'type': 'callout', 'value': note_prefix + '\n\n' + CAPTIONS[caption_key]}
        additions = [image_block, note_block]
        # Remove the image and its nearby owned note. This also repairs an older
        # caption if the graphic wording is refined later.
        content = chapter['content']
        image_indices = [i for i, b in enumerate(content)
                         if b.get('type') == 'image' and b.get('value') == image]
        remove = set(image_indices)
        for i in image_indices:
            for j in (i + 1, i - 1):
                if 0 <= j < len(content) and content[j].get('type') == 'callout' and content[j].get('value', '').startswith(note_prefix):
                    remove.add(j)
                    break
        original = [b for i, b in enumerate(content) if i not in remove]
        sha = digest(dict(chapter, content=original))
        index = find_anchor(original, anchor)
        expected = original[:index + 1] + additions + original[index + 1:]
        if check and chapter['content'] != expected:
            raise ValueError(f'Unexpected or missing pilot placement at {chapter_id}/{anchor}')
        for block in additions[:1]:
            if not (ROOT / 'assets/images' / block['value']).is_file():
                raise FileNotFoundError(block['value'])
        if not check:
            chapter['content'] = expected
        manifest['chapters'].append({
            'chapter': chapter_id,
            'originalChapterSha256': sha,
            'anchor': anchor,
            'caption': label,
            'image': image,
            'illustrationNote': CAPTIONS[caption_key],
        })
    MANIFEST.parent.mkdir(parents=True, exist_ok=True)
    if not check:
        BOOK.write_text(json.dumps(book, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
        MANIFEST.write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    print(f"{'Verified' if check else 'Applied'} {len(PLACEMENTS)} RASSetu geography graphics; original source text and MCQs preserved")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check', action='store_true')
    main(parser.parse_args().check)
