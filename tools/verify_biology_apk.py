"""Inspect the delivered APK's bundled Book 1 figures and original lessons."""
import hashlib
import json
import sys
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
apk = Path(sys.argv[1])
manifest = json.loads((ROOT / 'assets/biology_graphics_manifest.json').read_text(encoding='utf-8'))
book_asset = 'assets/content/vigyansetu/vigyansetu_book5.json'
entries = [e for e in manifest['chapters'] if e['asset'] == book_asset]
with zipfile.ZipFile(apk) as archive:
    assert archive.testzip() is None, 'Corrupt APK entry'
    prefix = 'assets/flutter_assets/'
    bundled = json.loads(archive.read(prefix + book_asset))
    local = json.loads((ROOT / book_asset).read_text(encoding='utf-8'))
    assert bundled == local, 'APK book differs from reviewed source'
    figure_count = 0
    figure_bytes = 0
    for entry in entries:
        chapter = next(c for c in bundled['chapters'] if c['id'] == entry['chapter'])
        for block in entry['blocks']:
            assert chapter['content'].count(block) == 1
            if block['type'] != 'image':
                continue
            asset = 'assets/images/' + block['value']
            payload = archive.read(prefix + asset)
            assert payload == (ROOT / asset).read_bytes(), asset
            figure_count += 1
            figure_bytes += len(payload)
    assert figure_count == 46
    assert len(entries) == 16
    assert prefix + 'assets/images/biology_cells.png' not in archive.namelist()
    assert prefix + 'assets/images/biology_mitosis.png' not in archive.namelist()
report = {'apk':str(apk.resolve()), 'bytes':apk.stat().st_size,
          'sha256':hashlib.sha256(apk.read_bytes()).hexdigest(),
          'book1_chapters':len(entries), 'book1_figures':figure_count,
          'book1_figure_bytes':figure_bytes, 'bundled_book_matches_reviewed_source':True,
          'zip_integrity_verified':True}
(ROOT / 'artifacts/biology_book1_apk_verification.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
print(json.dumps(report,indent=2))
