"""Integrate representative image scenes alongside Book 1 vector teaching diagrams."""
import argparse
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BOOK_PATH = ROOT / 'assets/content/rassetu/rassetu_book1.json'
MANIFEST = ROOT / 'artifacts/rassetu_series/book1_scene_manifest.json'
NOTE = '**चित्र से सीखें — प्रतिनिधि चित्रण**'
REPRESENTATIVE = ('प्रतिनिधि चित्रण — केवल शैक्षिक समझ हेतु; इसे वास्तविक दृश्य का हूबहू चित्र न मानें।\n'
                  'Representative illustration — for learning purposes; not a literal depiction.')
PLACEMENTS = [
    (['ch01', 'ch02'], '## 1.4 कांस्य युगीन सिंधु-सरस्वती सभ्यता',
     'rassetu_b1x_prehistory_scene.webp', 'पूर्व-ऐतिहासिक बस्ती: प्रतिनिधि पुनर्निर्माण',
     'अरावली के निकट नदी-तट पर मिट्टी के घर, बर्तन-निर्माण और पशुपालन की एक शैक्षिक कल्पना। यह किसी नामित पुरातात्विक स्थल या उत्खनन का हूबहू चित्रण नहीं है।'),
    (['ch27', 'ch28'], '## 14.2 मेवाड़ स्कूल ऑफ पेंटिंग्स',
     'rassetu_b1x_painting_scene.webp', 'लघुचित्र निर्माण की प्रतिनिधि कार्यशाला',
     'सूक्ष्म चित्रांकन और रंग-तैयारी से प्रेरित प्रतिनिधि दृश्य; इसे किसी विशिष्ट चित्रशाला, कलाकार, समय या शैली का दस्तावेजी चित्र न मानें।'),
    (['ch29', 'ch30'], '## 15.4 वस्त्र शिल्प, छपाई एवं बंधेज कला',
     'rassetu_b1x_craft_scene.webp', 'हाथ से ब्लॉक-प्रिंटिंग: प्रतिनिधि दृश्य',
     'कपड़े पर लकड़ी के ठप्पे से छपाई की प्रतिनिधि कार्यशाला; यह किसी खास केंद्र या कारीगर का सटीक चित्र नहीं है।'),
    (['ch31', 'ch32'], '## 16.4 लोक संगीत एवं गायकी परंपराएं',
     'rassetu_b1x_folk_music_scene.webp', 'लोकसंगीत का सामूहिक आयोजन: प्रतिनिधि दृश्य',
     'तार, वायु और ताल वाद्यों के साथ एक प्रतिनिधि संगीत-संगत; किसी विशिष्ट समुदाय, आयोजन या स्थान का दावा नहीं।'),
]

def canon(value):
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(',', ':')).encode('utf-8')

def digest(value):
    return hashlib.sha256(canon(value)).hexdigest()

def source_hashes(chapter):
    retained = [b for b in chapter['content'] if b.get('type') not in ('image', 'callout')]
    return digest(retained), digest(chapter.get('mcqs', []))

def run(check=False):
    book = json.loads(BOOK_PATH.read_text(encoding='utf-8'))
    chapters = {c['id']: c for c in book['chapters']}
    names = {p[2] for p in PLACEMENTS}
    if not check:
        for chapter in chapters.values():
            cleaned, skip_note = [], False
            for block in chapter['content']:
                if block.get('type') == 'image' and block.get('value') in names:
                    skip_note = True
                    continue
                if skip_note and block.get('type') == 'callout' and block.get('value', '').startswith(NOTE):
                    skip_note = False
                    continue
                skip_note = False
                cleaned.append(block)
            chapter['content'] = cleaned

    changes, rows = {}, []
    for chapter_ids, anchor, image, caption, explanation in PLACEMENTS:
        asset = ROOT / 'assets/images' / image
        if not asset.is_file() or not asset.read_bytes().startswith(b'RIFF'):
            raise FileNotFoundError(f'Missing/invalid WebP: {asset}')
        asset_hash = hashlib.sha256(asset.read_bytes()).hexdigest()
        for chapter_id in chapter_ids:
            chapter = chapters[chapter_id]
            content = changes.get(chapter_id, chapter['content'])
            matches = [i for i, b in enumerate(content)
                       if b.get('type') == 'text' and b.get('value', '').startswith(anchor)]
            if len(matches) != 1:
                raise ValueError(f'{chapter_id}: expected one exact anchor {anchor!r}, found {len(matches)}')
            index = matches[0]
            image_block = {'type': 'image', 'value': image, 'caption': caption}
            callout = {'type': 'callout', 'value': NOTE + '\n\n' + explanation + '\n\n' + REPRESENTATIVE}
            changes[chapter_id] = content[:index+1] + [image_block, callout] + content[index+1:]
            text_hash, mcq_hash = source_hashes(chapter)
            rows.append({'chapter': chapter_id, 'anchor': anchor, 'image': image,
                         'assetSha256': asset_hash, 'caption': caption,
                         'explanation': explanation, 'sourceTextSha256': text_hash,
                         'sourceMcqSha256': mcq_hash})

    if check:
        manifest = json.loads(MANIFEST.read_text(encoding='utf-8'))
        for row in manifest['placements']:
            chapter = chapters[row['chapter']]
            if source_hashes(chapter) != (row['sourceTextSha256'], row['sourceMcqSha256']):
                raise ValueError(f'Source hash mismatch: {row["chapter"]}')
            asset = ROOT / 'assets/images' / row['image']
            if not asset.is_file() or hashlib.sha256(asset.read_bytes()).hexdigest() != row['assetSha256']:
                raise ValueError(f'Asset missing/changed: {row["image"]}')
            content = chapter['content']
            idx = next((i for i, b in enumerate(content)
                        if b.get('type') == 'image' and b.get('value') == row['image']), None)
            if idx is None or idx == 0 or content[idx-1].get('type') != 'text' or not content[idx-1].get('value', '').startswith(row['anchor']):
                raise ValueError(f'Anchor/image mismatch: {row["chapter"]}/{row["image"]}')
        print(f'Verified {len(manifest["placements"])} scene placements; source text, MCQs and asset hashes match')
        return

    for chapter_id, content in changes.items():
        chapters[chapter_id]['content'] = content
    MANIFEST.write_text(json.dumps({'version': 1, 'batch': 'RAS Book 1 representative image scenes',
                                    'distinctImages': len(PLACEMENTS), 'placements': rows},
                                   ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    BOOK_PATH.write_text(json.dumps(book, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    print(f'Applied {len(PLACEMENTS)} representative images across {len(changes)} paired chapter records')

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--check', action='store_true')
    run(parser.parse_args().check)
