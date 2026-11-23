"""Verify integrated RAS graphics against their saved source-chapter hashes."""
import hashlib
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MANIFESTS = [
    ROOT / 'artifacts/rassetu_geography_pilot/manifest.json',
    *(ROOT / f'artifacts/rassetu_series/batch{n}_manifest.json' for n in range(2, 12)),
]
NOTE_PREFIX = '**चित्र से सीखें — प्रतिनिधि चित्रण**'

def digest(value):
    return hashlib.sha256(json.dumps(value, ensure_ascii=False, sort_keys=True,
        separators=(',', ':')).encode()).hexdigest()

def main():
    indexed = []
    asset_by_chapter = {}
    for rank, path in enumerate(MANIFESTS, start=1):
        manifest = json.loads(path.read_text(encoding='utf-8'))
        if 'placements' in manifest:
            records = manifest['placements']
            if all('book' in row for row in records):
                path_for = lambda row: ROOT / 'assets/content/rassetu' / f"rassetu_book{row['book']}.json"
            else:
                match = re.match(r'Book (\d+)', manifest.get('batch', ''))
                if match:
                    book_num = int(match.group(1))
                    path_for = lambda row: ROOT / 'assets/content/rassetu' / f'rassetu_book{book_num}.json'
                else:
                    path_for = lambda row: ROOT / manifest['asset']
        else:
            records = manifest['chapters']
            path_for = lambda row: ROOT / manifest['asset']
        for row in records:
            book_path = path_for(row)
            key = (str(book_path), row['chapter'])
            entry = {'rank': rank, 'manifest': path, 'bookPath': book_path, 'row': row}
            indexed.append(entry)
            asset_by_chapter.setdefault(key, []).append((rank, row['image']))

    verified_by_manifest = {path: 0 for path in MANIFESTS}
    for entry in indexed:
        path, row = entry['manifest'], entry['row']
        book_path = entry['bookPath']
        book = json.loads(book_path.read_text(encoding='utf-8'))
        chapter = next(c for c in book['chapters'] if c['id'] == row['chapter'])
        image = row['image']
        image_path = ROOT / 'assets/images' / image
        if not image_path.is_file() or not image_path.read_bytes().startswith(b'RIFF'):
            raise ValueError(f'{path.name}: missing/invalid asset {image}')
        content = chapter['content']
        key = (str(book_path), row['chapter'])
        # Later batches can add another figure to an already-illustrated lesson.
        # Strip those later additions as well to reconstruct the exact chapter
        # state against which this manifest's original hash was recorded.
        remove_assets = {name for rank, name in asset_by_chapter[key] if rank >= entry['rank']}
        remove = set()
        for i, block in enumerate(content):
            if block.get('type') == 'image' and block.get('value') in remove_assets:
                remove.add(i)
                for j in (i + 1,):
                    if (0 <= j < len(content) and content[j].get('type') == 'callout'
                        and content[j].get('value', '').startswith(NOTE_PREFIX)):
                        remove.add(j)
                        break
        if not any(content[i].get('type') == 'image' and content[i].get('value') == image for i in remove):
            raise ValueError(f'{path.name}: missing {image} image block in {row["chapter"]}')
        original = [b for i, b in enumerate(content) if i not in remove]
        source_hash = digest(dict(chapter, content=original))
        if source_hash != row['originalChapterSha256']:
            raise ValueError(f'{path.name}: source text/MCQs changed for {row["chapter"]}')
        verified_by_manifest[path] += 1

    total = 0
    for path, count in verified_by_manifest.items():
        total += count
        print(f'{path.name}: {count} placements and source hashes verified')
    print(f'All {total} declared placements retain their original chapter text and MCQs.')

if __name__ == '__main__':
    main()
