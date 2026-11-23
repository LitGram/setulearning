"""Integrate the reviewed completion set for the RAS Book 1 graphics plan."""
import argparse
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BOOK_PATH = ROOT / 'assets/content/rassetu/rassetu_book1.json'
MANIFEST = ROOT / 'artifacts/rassetu_series/book1_completion_manifest.json'
NOTE = '**चित्र से सीखें — अवधारणा आरेख**'

# Every anchor is an exact, source-text heading in the chapter JSON.
PLACEMENTS = [
    (['ch01', 'ch02'], '## 1.8 तुलनात्मक मास्टर तालिकाएं एवं विभेदन विश्लेषण',
     'rassetu_b1x_archaeology_locator.webp', 'राजस्थान के पुरातात्विक स्थल',
     'प्रागैतिहासिक एवं ऐतिहासिक केंद्रों को दिशा-सूचक क्षेत्र और नदी-संकेत के साथ देखने का schematic।'),
    (['ch01', 'ch02'], '## 1.2 पाषाण काल एवं प्रारंभिक प्रागैतिहासिक अनुसंधान',
     'rassetu_b1x_prehistoric_sequence.webp', 'राजस्थान: सांस्कृतिक क्रम',
     'पाषाण से लौह युग तक का क्रम और अध्याय में दिए औजार, बसावट तथा स्थल-संकेत।'),
    (['ch01', 'ch02'], '## 1.5 ताम्र-पाषाण युगीन बनास-बेड़च संस्कृति',
     'rassetu_b1x_kalibanga_ahar_compare.webp', 'कालीबंगा और आहड़–बनास',
     'अध्याय में वर्णित जुते खेत, नगर-खंड, अग्निवेदी, ताम्र औजार और मृद्भांड के प्रमुख भेद।'),
    (['ch15', 'ch16'], '## 8.7 मास्टर राजवंश तुलनात्मक मैट्रिक्स',
     'rassetu_b1x_dynasty_parallel_timeline.webp', 'राजस्थान के राजवंश: समानांतर काल-रेखाएं',
     'वंशों और उनसे जुड़े क्षेत्रीय केंद्रों का विषय-आधारित अवलोकन; पट्टियां अवधि का अनुपात नहीं दिखातीं।'),
    (['ch15', 'ch16'], '## 8.2 जैसलमेर का भाटी राजवंश',
     'rassetu_b1x_kingdoms_schematic_locator.webp', 'क्षेत्रीय राजवंश: स्थान और पहचान',
     'पुस्तक में दिए क्षेत्रीय नामों और राजवंशों का दिशात्मक स्मरण मॉडल; सीमाएं नहीं दर्शाई गई हैं।'),
    (['ch05', 'ch06'], '### 1. प्रारंभिक संस्थापक एवं राजधानी परिवर्तन',
     'rassetu_b1x_mewar_capital_sequence.webp', 'मेवाड़: सत्ता-केंद्र और शाखा क्रम',
     'मेवाड़ के वृत्तांत में वर्णित प्रमुख केंद्र, शाखा परिवर्तन और चुने हुए पड़ाव।'),
    (['ch25', 'ch26'], '## 13.6 तुलनात्मक विश्लेषण एवं विभेदीकरण तालिकाएं',
     'rassetu_b1x_fort_capital_schematic.webp', 'दुर्ग और क्षेत्रीय केंद्र',
     'पुस्तक में वर्णित दुर्गों और भू-आकृतिक संदर्भ का schematic; मार्ग और दूरियां नहीं दर्शाई गई हैं।'),
    (['ch21', 'ch22'], '## 11.5 तुलनात्मक मास्टर तालिका एवं विभेदन विश्लेषण',
     'rassetu_b1x_people_movements_timeline.webp', 'किसान और जनजातीय आंदोलनों के पड़ाव',
     'आंदोलनों, स्थानों और काल-संकेतों का चुनिंदा पुनरावृत्ति क्रम; पूर्ण सूची नहीं।'),
    (['ch23', 'ch24'], '### 2. राजस्थान के एकीकरण के 7 चरणों का संपूर्ण रोडमैप',
     'rassetu_b1x_integration_seven_stages.webp', 'राजस्थान एकीकरण: सात चरण',
     'अध्याय में दिए सात चरणों के नाम और तिथियां; सहभागी रियासतों की पूरी सूची मूल पाठ में है।'),
    (['ch29', 'ch30'], '## 15.2 मृण्मय एवं पॉटरी शिल्प',
     'rassetu_b1x_craft_material_process.webp', 'राजस्थानी शिल्प: सामग्री से पहचान',
     'शिल्प-सामग्री, तकनीक और अध्याय में दिए उत्पाद-उदाहरणों का वैचारिक संबंध।'),
    (['ch39', 'ch40'], '### 1. राजस्थानी त्योहार चक्र का दार्शनिक आधार',
     'rassetu_b1x_festival_month_cycle.webp', 'राजस्थान: त्योहार और मेले का वार्षिक चक्र',
     'विक्रम संवत के मासों के साथ चुने हुए सांस्कृतिक उदाहरण; चंद्र तिथियां हर वर्ष बदलती हैं।'),
    (['ch39', 'ch40'], '## 20.6 त्वरित स्मरण हेतु 60 एक-पंक्ति पुनरावृत्ति पत्रक',
     'rassetu_b1x_heritage_concept_web.webp', 'राजस्थान विरासत: पुनरावृत्ति संकल्पना-जाल',
     'इतिहास, पुरातत्व, कला और सांस्कृतिक परंपराओं को जोड़ने वाला अध्ययन-संगठन मॉडल।'),
    (['ch39', 'ch40'], '## 20.4 तुलनात्मक तालिकाएं व भ्रामक युगलों का निवारण',
     'rassetu_b1x_heritage_recall_grid.webp', 'विरासत पुनरावृत्ति: मिलान-अभ्यास',
     'स्थल, काल, पहचान और साक्ष्य को जोड़ने का नमूना retrieval अभ्यास; प्रत्येक जोड़ी मूल पाठ से जांचें।'),
]

def canonical(value):
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(',', ':')).encode('utf-8')

def source_digest(chapter):
    text = [b for b in chapter['content'] if b.get('type') not in ('image', 'callout')]
    return hashlib.sha256(canonical(text)).hexdigest()

def mcq_digest(chapter):
    return hashlib.sha256(canonical(chapter.get('mcqs', []))).hexdigest()

def apply(check=False):
    book = json.loads(BOOK_PATH.read_text(encoding='utf-8'))
    chapters = {c['id']: c for c in book['chapters']}
    batch_images = {entry[2] for entry in PLACEMENTS}
    if not check:
        for chapter in chapters.values():
            cleaned = []
            skip_note = False
            for block in chapter['content']:
                if block.get('type') == 'image' and block.get('value') in batch_images:
                    skip_note = True
                    continue
                if skip_note and block.get('type') == 'callout' and block.get('value', '').startswith(NOTE):
                    skip_note = False
                    continue
                skip_note = False
                cleaned.append(block)
            chapter['content'] = cleaned
    placements, expected_updates = [], {}
    for chapter_ids, anchor, image, caption, explanation in PLACEMENTS:
        image_path = ROOT / 'assets/images' / image
        if not image_path.is_file() or not image_path.read_bytes().startswith(b'RIFF'):
            raise FileNotFoundError(f'Missing/invalid WebP: {image_path}')
        image_sha = hashlib.sha256(image_path.read_bytes()).hexdigest()
        for chapter_id in chapter_ids:
            chapter = chapters[chapter_id]
            original = expected_updates.get(chapter_id, chapter['content'])
            matches = [i for i, b in enumerate(original)
                       if b.get('type') == 'text' and b.get('value', '').startswith(anchor)]
            if len(matches) != 1:
                raise ValueError(f'{chapter_id}: expected one exact anchor {anchor!r}, found {len(matches)}')
            at = matches[0]
            image_block = {'type': 'image', 'value': image, 'caption': caption}
            note = {'type': 'callout', 'value': NOTE + '\n\n' + explanation}
            expected = original[:at + 1] + [image_block, note] + original[at + 1:]
            if not check:
                expected_updates[chapter_id] = expected
            placements.append({
                'chapter': chapter_id, 'anchor': anchor, 'image': image,
                'assetSha256': image_sha, 'caption': caption,
                'explanation': explanation,
                'sourceTextSha256': source_digest(chapter),
                'sourceMcqSha256': mcq_digest(chapter),
            })
    if check:
        manifest = json.loads(MANIFEST.read_text(encoding='utf-8'))
        for item in manifest['placements']:
            c = chapters[item['chapter']]
            if item['sourceTextSha256'] != source_digest(c) or item['sourceMcqSha256'] != mcq_digest(c):
                raise ValueError(f'Source content hash mismatch at {item["chapter"]}')
            asset = ROOT / 'assets/images' / item['image']
            if not asset.is_file() or hashlib.sha256(asset.read_bytes()).hexdigest() != item['assetSha256']:
                raise ValueError(f'Asset missing or changed: {item["image"]}')
            blocks = c['content']
            idx = next((i for i, b in enumerate(blocks) if b.get('type') == 'image' and b.get('value') == item['image']), None)
            if idx is None or idx == 0 or blocks[idx-1].get('type') != 'text' or not blocks[idx-1].get('value','').startswith(item['anchor']):
                raise ValueError(f'Anchor/image mismatch at {item["chapter"]}: {item["image"]}')
        print(f"Verified {len(manifest['placements'])} chapter records across {len(PLACEMENTS)} Book 1 graphics; source text and MCQs match hashes")
        return
    for chapter_id, content in expected_updates.items():
        chapters[chapter_id]['content'] = content
    BOOK_PATH.write_text(json.dumps(book, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    MANIFEST.write_text(json.dumps({'version': 1, 'batch': 'RAS Book 1 planned coverage completion',
                                    'distinctGraphics': len(PLACEMENTS), 'placements': placements},
                                   ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    print(f'Applied {len(PLACEMENTS)} Book 1 graphics to {len(expected_updates)} paired chapter records')

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--check', action='store_true')
    apply(parser.parse_args().check)
