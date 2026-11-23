"""Insert reviewed biology figures without removing source text or changing MCQs.

Run after a future book import to reapply figures. --check is read-only.
"""
import argparse
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / 'assets/biology_graphics_manifest.json'


def digest(value):
    return hashlib.sha256(json.dumps(value, ensure_ascii=False,
        sort_keys=True, separators=(',', ':')).encode()).hexdigest()


def apply(check=False):
    manifest = json.loads(MANIFEST.read_text(encoding='utf-8'))
    books = {}
    for entry in manifest['chapters']:
        path = ROOT / entry['asset']
        if path not in books:
            books[path] = json.loads(path.read_text(encoding='utf-8'))
        book = books[path]
        chapter = next(c for c in book['chapters'] if c['id'] == entry['chapter'])
        additions = entry['blocks']
        original = [b for b in chapter['content'] if b not in additions]
        # Check the full pre-pilot chapter, including title and quiz answers.
        payload = dict(chapter, content=original)
        if digest(payload) != entry['originalChapterSha256']:
            raise ValueError(f"Source chapter changed: {path.name}/{chapter['id']}; review anchors before reapplying")
        for block in additions:
            if block['type'] == 'image':
                image = ROOT / 'assets/images' / block['value']
                if not image.exists():
                    raise ValueError(f'Missing image: {image}')
        placements = entry.get('placements', [{'anchor': entry.get('anchor'), 'blocks': additions}])
        insertions = {}
        for placement in placements:
            matches = [i for i, b in enumerate(original) if b['value'].startswith(placement['anchor'])]
            if len(matches) != 1:
                raise ValueError(f"Expected one insertion anchor in {chapter['id']}: {placement['anchor']}")
            insertions.setdefault(matches[0], []).extend(placement['blocks'])
        expected = []
        for i, block in enumerate(original):
            expected.append(block)
            expected.extend(insertions.get(i, []))
        if check:
            if chapter['content'] != expected:
                raise ValueError(f"Figures missing or out of order: {path.name}/{chapter['id']}")
        else:
            chapter['content'] = expected
    if not check:
        for path, book in books.items():
            path.write_text(json.dumps(book, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    print(f"{'Verified' if check else 'Applied'} biology graphics: {len(manifest['chapters'])} chapters; original text and MCQs preserved")


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check', action='store_true')
    apply(parser.parse_args().check)
