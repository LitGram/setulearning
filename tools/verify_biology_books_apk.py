"""Verify both biology books, their original baselines and all 110 packaged figures."""
import hashlib
import json
import sys
import zipfile
from pathlib import Path
from apply_biology_graphics import digest

ROOT = Path(__file__).resolve().parents[1]

def verify(apk):
    manifest = json.loads((ROOT/'assets/biology_graphics_manifest.json').read_text(encoding='utf-8'))
    report = dict(apk=str(apk.resolve()), bytes=apk.stat().st_size,
                  sha256=hashlib.sha256(apk.read_bytes()).hexdigest(), books=[])
    with zipfile.ZipFile(apk) as archive:
        assert archive.testzip() is None, 'Corrupt APK entry'
        prefix = 'assets/flutter_assets/'
        for number, expected_chapters, expected_figures in [(5,16,46),(6,24,64)]:
            asset = f'assets/content/vigyansetu/vigyansetu_book{number}.json'
            entries = [e for e in manifest['chapters'] if e['asset']==asset]
            bundled = json.loads(archive.read(prefix+asset))
            local = json.loads((ROOT/asset).read_text(encoding='utf-8'))
            assert bundled == local, f'Packaged book differs from source: {asset}'
            figures = 0
            image_bytes = 0
            for entry in entries:
                chapter = next(c for c in bundled['chapters'] if c['id']==entry['chapter'])
                original = [b for b in chapter['content'] if b not in entry['blocks']]
                assert digest(dict(chapter,content=original))==entry['originalChapterSha256'], chapter['id']
                for block in entry['blocks']:
                    assert chapter['content'].count(block)==1, block
                    if block['type']!='image': continue
                    image_asset = 'assets/images/'+block['value']
                    payload = archive.read(prefix+image_asset)
                    assert payload==(ROOT/image_asset).read_bytes(), image_asset
                    figures += 1
                    image_bytes += len(payload)
            assert len(entries)==expected_chapters
            assert figures==expected_figures
            report['books'].append(dict(book=number-4,chapters=len(entries),figures=figures,
                figure_bytes=image_bytes,bundled_book_matches_source=True,original_text_and_mcqs_preserved=True))
        report['zip_integrity_verified'] = True
    (ROOT/'artifacts/biology_books1_2_apk_verification.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(report,indent=2))

if __name__=='__main__': verify(Path(sys.argv[1]))
