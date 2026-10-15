"""Install all 64 Biology II placements while preserving full chapter baselines."""
import json
from pathlib import Path
from apply_biology_graphics import digest, apply

ROOT=Path(__file__).resolve().parents[1]

def main():
    manifest_path=ROOT/'assets/biology_graphics_manifest.json'
    old=json.loads(manifest_path.read_text(encoding='utf-8'))
    asset='assets/content/vigyansetu/vigyansetu_book6.json'
    book_path=ROOT/asset
    book=json.loads(book_path.read_text(encoding='utf-8'))
    briefs=json.loads((ROOT/'artifacts/biology_book2_figure_briefs.json').read_text(encoding='utf-8'))
    entries=[]
    baselines=[]
    for c in book['chapters']:
        prev=next((e for e in old['chapters'] if e['asset']==asset and e['chapter']==c['id']),None)
        original=[b for b in c['content'] if not prev or b not in prev['blocks']]
        sha=digest(dict(c,content=original))
        if prev:
            assert sha==prev['originalChapterSha256'],c['id']
        placements=[]
        for f in briefs:
            if f['chapter']!=c['id']: continue
            assert (ROOT/'assets/images'/f"bio2_{f['id']}.webp").exists(),f['id']
            assert sum(b['value'].startswith(f['anchor']) for b in original)==1,f['id']
            blocks=[{'type':'image','value':f"bio2_{f['id']}.webp",'caption':f['caption']},
                    {'type':'callout','value':'**चित्र से सीखें — '+f['caption']+'**\n\n'+f['note']}]
            placements.append({'anchor':f['anchor'],'blocks':blocks})
        assert placements,c['id']
        entries.append(dict(asset=asset,chapter=c['id'],originalChapterSha256=sha,
                            placements=placements,blocks=[b for p in placements for b in p['blocks']]))
        baselines.append(dict(chapter=c['id'],sha256=sha,originalBlocks=len(original),mcqs=len(c.get('mcqs',[])),figures=len(placements)))
        c['content']=original
    assert len(entries)==24
    assert sum(len(e['placements']) for e in entries)==64
    combined=[e for e in old['chapters'] if e['asset']!=asset]+entries
    manifest=dict(old,version=3,chapters=combined)
    # All baselines, anchors and image files were verified before writing.
    book_path.write_text(json.dumps(book,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    manifest_path.write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    apply()
    apply(check=True)
    (ROOT/'artifacts/biology_book2_completeness.json').write_text(json.dumps(baselines,indent=2)+'\n',encoding='utf-8')
    print('Installed 64 graphics in all 24 Biology II chapters; text and MCQs preserved')

if __name__=='__main__': main()
