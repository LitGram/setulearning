"""Download official regular Secondary Sanskrit (Code 71) papers with an auditable manifest."""
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path
from urllib.parse import urljoin, quote
import hashlib
import json
import logging
import requests
from bs4 import BeautifulSoup
from pypdf import PdfReader

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'artifacts/rbse10_sanskrit/papers'
BASE = 'https://rajeduboard.rajasthan.gov.in/books/'
logging.getLogger('pypdf').setLevel(logging.ERROR)

def fetch_year(year):
    index = urljoin(BASE, f'PAPERS-{year}/index.htm')
    result = []
    try:
        r = requests.get(index, timeout=25)
        r.raise_for_status()
        soup = BeautifulSoup(r.content, 'html.parser')
        for a in soup.find_all('a', href=True):
            label = a.get_text(' ', strip=True).upper()
            raw_href = a['href'].strip()
            href = urljoin(index, quote(raw_href, safe='/:'))
            if ('SANSKRIT' not in label and 'SANKRIT' not in label and '71' not in raw_href) or 'SECONDARY' not in label:
                continue
            if any(s in label for s in ['SR SECONDARY', 'SR.SECONDARY', 'SR. SEC', 'PRAVESHIKA', 'VARISHTHA', 'D&D', 'D-D']):
                continue
            if '/sec/' not in href.lower() and '/secsup/' not in href.lower():
                continue
            session = 'supplementary' if '/secsup/' in href.lower() or '/supp/' in href.lower() else 'main'
            key = f'{year}_{session}'
            pdf = OUT / f'{key}.pdf'
            if not pdf.exists():
                response = requests.get(href, timeout=35)
                if response.status_code == 404 and 'S-71-Sankrit-TL-14.pdf' in href:
                    href = href.replace('S-71-Sankrit-TL-14.pdf', 'S-71-Sankrit-14.pdf')
                    response = requests.get(href, timeout=35)
                response.raise_for_status()
                if not response.content.startswith(b'%PDF'):
                    raise ValueError('Not a PDF')
                pdf.write_bytes(response.content)
            elif 'S-71-Sankrit-TL-14.pdf' in href:
                href = href.replace('S-71-Sankrit-TL-14.pdf', 'S-71-Sankrit-14.pdf')
            reader = PdfReader(pdf)
            pages = [page.extract_text() or '' for page in reader.pages]
            (OUT / f'{key}.txt').write_text(
                '\n\n'.join(f'=== PDF PAGE {i} ===\n{text}' for i, text in enumerate(pages, 1)),
                encoding='utf-8',
            )
            result.append(dict(
                id=key,
                year=year,
                session=session,
                url=href,
                index=index,
                pages=len(pages),
                sha256=hashlib.sha256(pdf.read_bytes()).hexdigest(),
                file=str(pdf.relative_to(ROOT)),
                text_file=str((OUT / f'{key}.txt').relative_to(ROOT)),
            ))
        if not result:
            result = [dict(year=year, status='no regular Secondary Sanskrit PDF found in index', index=index)]
    except Exception as e:
        result = [dict(year=year, status='fetch-failed', error=str(e), index=index)]
    return result

def main():
    OUT.mkdir(parents=True, exist_ok=True)
    manifest = []
    with ThreadPoolExecutor(max_workers=4) as pool:
        for f in as_completed([pool.submit(fetch_year, y) for y in range(2014, 2027)]):
            rows = f.result()
            manifest.extend(rows)
            print([(r.get('id', r['year']), r.get('status', 'downloaded')) for r in rows], flush=True)
    manifest.sort(key=lambda r: (-r['year'], r.get('session', '')))
    (OUT / 'manifest.json').write_text(json.dumps(manifest, indent=2, ensure_ascii=False) + '\n', encoding='utf-8')
    print('Downloaded', sum('id' in r for r in manifest), 'official Sanskrit papers.')

if __name__ == '__main__':
    main()
