"""Check the RASSetu geography pilot files and unchanged-source hashes."""
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
manifest_path = ROOT / 'artifacts/rassetu_geography_pilot/manifest.json'
manifest = json.loads(manifest_path.read_text(encoding='utf-8'))
book_path = ROOT / manifest['asset']
book = json.loads(book_path.read_text(encoding='utf-8'))
errors = []
for entry in manifest['chapters']:
    chapter = next(c for c in book['chapters'] if c['id'] == entry['chapter'])
    image_blocks = [b for b in chapter['content'] if b.get('type') == 'image' and b.get('value') == entry['image']]
    image_indices = [i for i,b in enumerate(chapter['content']) if b.get('type') == 'image' and b.get('value') == entry['image']]
    note_indices = [i+1 for i in image_indices if i+1 < len(chapter['content']) and chapter['content'][i+1].get('type') == 'callout' and chapter['content'][i+1].get('value','').startswith('**चित्र से सीखें')]
    note_blocks = [chapter['content'][i] for i in note_indices]
    # Strip every image and only its adjacent graphics note. A source chapter
    # may itself contain a separate callout with the same introductory phrase.
    remove = set()
    for i, block in enumerate(chapter['content']):
        if block.get('type') != 'image':
            continue
        remove.add(i)
        for j in (i + 1, i - 1):
            if 0 <= j < len(chapter['content']):
                note = chapter['content'][j]
                if note.get('type') == 'callout' and note.get('value', '').startswith('**चित्र से सीखें'):
                    remove.add(j)
                    break
    original = [b for i, b in enumerate(chapter['content']) if i not in remove]
    digest = hashlib.sha256(json.dumps(dict(chapter, content=original), ensure_ascii=False,
        sort_keys=True, separators=(',', ':')).encode()).hexdigest()
    asset_path = ROOT / 'assets/images' / entry['image']
    if len(image_blocks) != 1 or len(note_blocks) != 1:
        errors.append(f"{entry['chapter']}: expected one image and note")
    if digest != entry['originalChapterSha256']:
        errors.append(f"{entry['chapter']}: source text or MCQs changed")
    if not asset_path.is_file() or asset_path.stat().st_size == 0:
        errors.append(f"Missing/empty image: {asset_path.name}")
    elif not asset_path.read_bytes().startswith(b'RIFF'):
        errors.append(f"Invalid WebP container: {asset_path.name}")
if errors:
    raise SystemExit('\n'.join(errors))
print(f"Verified {len(manifest['chapters'])} RASSetu image blocks and captions; original chapter text and MCQs unchanged")
