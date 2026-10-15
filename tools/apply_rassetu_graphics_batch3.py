"""Apply a reviewed Book 1 set with paired-chapter source guards."""
import argparse
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BOOK_PATH = ROOT / 'assets/content/rassetu/rassetu_book1.json'
MANIFEST = ROOT / 'artifacts/rassetu_series/batch3_manifest.json'

PLACEMENTS = [
    (['ch25', 'ch26'], '## 13.2 दुर्ग (किले) वास्तुकला — वर्गीकरण एवं प्रमुख दुर्ग',
     'rassetu_b1_fort_architecture.webp', 'दुर्ग स्थापत्य: रक्षा के प्राकृतिक आधार',
     'गिरि, वन, जल और धन्वन दुर्ग के प्राकृतिक परिवेश का सरलीकृत वर्गीकरण-सह-कार्य मॉडल। ऐतिहासिक किलों की बनावट और वर्गीकरण में भिन्नताएं हैं; आरेख पैमाने पर नहीं है।'),
    (['ch27', 'ch28'], '## 14.2 मेवाड़ स्कूल ऑफ पेंटिंग्स (Mewar School)',
     'rassetu_b1_painting_schools.webp', 'राजस्थानी चित्रशैली: तुलनात्मक अध्ययन',
     'मेवाड़, मारवाड़, किशनगढ़ और बूंदी–कोटा से जुड़े चुने हुए शैलीगत विषयों का प्रतिनिधि तुलनात्मक मॉडल। प्रत्येक परंपरा के भीतर समय और कलाकार के अनुसार विविधता मिलती है।'),
    (['ch31', 'ch32'], '## 16.2 शास्त्रीय एवं लोक नृत्य (Classical & Folk Dances of Rajasthan)',
     'rassetu_b1_folk_dance_regions.webp', 'राजस्थान के लोकनृत्य: चुने हुए उदाहरण',
     'घूमर, गैर, कालबेलिया और तेरहताली के संक्षिप्त परीक्षा-स्मरण संकेत। समुदाय और क्षेत्र के संबंध को अध्याय के विस्तृत विवरण के साथ पढ़ें; यह नृत्य-प्रदर्शन का हूबहू चित्र नहीं है।'),
]
NOTE = '**चित्र से सीखें — प्रतिनिधि चित्रण**'

def digest(value):
    return hashlib.sha256(json.dumps(value, ensure_ascii=False, sort_keys=True,
        separators=(',', ':')).encode()).hexdigest()

def main(check=False):
    book = json.loads(BOOK_PATH.read_text(encoding='utf-8'))
    manifest = {'version': 1, 'batch': 'Book 1 heritage and culture', 'placements': []}
    for chapter_ids, anchor, image, label, explanation in PLACEMENTS:
        image_path = ROOT / 'assets/images' / image
        if not image_path.is_file() or not image_path.read_bytes().startswith(b'RIFF'):
            raise FileNotFoundError(f'Missing or invalid WebP: {image_path}')
        for chapter_id in chapter_ids:
            chapter = next(c for c in book['chapters'] if c['id'] == chapter_id)
            content = chapter['content']
            image_ids = [i for i, b in enumerate(content)
                         if b.get('type') == 'image' and b.get('value') == image]
            remove = set(image_ids)
            for i in image_ids:
                for j in (i + 1, i - 1):
                    if (0 <= j < len(content) and content[j].get('type') == 'callout'
                        and content[j].get('value', '').startswith(NOTE)):
                        remove.add(j)
                        break
            original = [b for i, b in enumerate(content) if i not in remove]
            matches = [i for i, b in enumerate(original)
                       if b.get('type') == 'text' and b.get('value', '').startswith(anchor)]
            if len(matches) != 1:
                raise ValueError(f'{chapter_id}: expected one anchor {anchor!r}, found {len(matches)}')
            image_block = {'type': 'image', 'value': image, 'caption': label}
            note_block = {'type': 'callout', 'value': NOTE + '\n\n' + explanation
                + '\n\nप्रतिनिधि चित्रण — केवल शैक्षिक समझ हेतु; इसे वास्तविक दृश्य का हूबहू चित्र न मानें।'}
            expected = original[:matches[0] + 1] + [image_block, note_block] + original[matches[0] + 1:]
            if check and content != expected:
                raise ValueError(f'Unexpected or missing placement at {chapter_id}')
            if not check:
                chapter['content'] = expected
            manifest['placements'].append({'chapter': chapter_id,
                'originalChapterSha256': digest(dict(chapter, content=original)),
                'anchor': anchor, 'image': image, 'caption': label,
                'explanation': explanation})
    if not check:
        BOOK_PATH.write_text(json.dumps(book, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
        MANIFEST.write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    print(f"{'Verified' if check else 'Applied'} batch 3: {len(PLACEMENTS)} graphics across {len(manifest['placements'])} paired chapters; source text and MCQs preserved")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check', action='store_true')
    main(parser.parse_args().check)
