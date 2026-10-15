"""Promote the three-figure pilot to all 46 Book 1 placements."""
import json
from pathlib import Path
from apply_biology_graphics import digest
ROOT = Path(__file__).resolve().parents[1]
manifest_path = ROOT / 'assets/biology_graphics_manifest.json'
old = json.loads(manifest_path.read_text(encoding='utf-8'))
asset = 'assets/content/vigyansetu/vigyansetu_book5.json'
book_path = ROOT / asset
book = json.loads(book_path.read_text(encoding='utf-8'))
briefs = json.loads((ROOT / 'artifacts/biology_book1_figure_briefs.json').read_text(encoding='utf-8'))
entries = []
for c in book['chapters']:
    previous = next((e for e in old['chapters'] if e['asset'] == asset and e['chapter'] == c['id']), None)
    original = [b for b in c['content'] if not previous or b not in previous['blocks']]
    sha = digest(dict(c, content=original))
    if previous:
        assert sha == previous['originalChapterSha256'], c['id']
    placements = []
    for f in briefs:
        if f['chapter'] != c['id']:
            continue
        blocks = [{'type':'image', 'value':f"bio1_{f['id']}.webp", 'caption':f['caption']},
                  {'type':'callout', 'value':'**चित्र से सीखें — '+f['caption']+'**\n\n'+f['note']}]
        placements.append({'anchor':f['anchor'], 'blocks':blocks})
    assert placements, c['id']
    entries.append({'asset':asset, 'chapter':c['id'], 'originalChapterSha256':sha,
                    'placements':placements, 'blocks':[b for p in placements for b in p['blocks']]})
    c['content'] = original
entries += [e for e in old['chapters'] if e['asset'] != asset]
assert sum(len(e['placements']) for e in entries if e['asset'] == asset) == 46
manifest = {'version':2, 'generator':'Reviewed original illustrations and editable scientific schematics', 'chapters':entries}
# Original pilot blocks are removed only after every chapter baseline is verified.
book_path.write_text(json.dumps(book,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
manifest_path.write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print('Prepared 46 placements across 16 chapters; original chapter hashes verified')
