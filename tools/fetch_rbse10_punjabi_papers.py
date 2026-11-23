"""Download official regular Secondary Punjabi (Code 75) papers with an auditable manifest."""
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
OUT = ROOT / 'artifacts/rbse10_punjabi/papers'
BASE = 'https://rajeduboard.rajasthan.gov.in/books/'
logging.getLogger('pypdf').setLevel(logging.ERROR)

EXTRA_SUPP = {
    2024: 'https://rajeduboard.rajasthan.gov.in/books/PAPERS-2024/SecSUP/S-75.pdf',
    2025: 'https://rajeduboard.rajasthan.gov.in/books/PAPERS-2025/SecSUP/S-75.pdf',
}


def save_paper(year, session, href, index):
    key = f'{year}_{session}'
    pdf = OUT / f'{key}.pdf'
    if not pdf.exists():
        response = requests.get(href, timeout=35)
        response.raise_for_status()
        if not response.content.startswith(b'%PDF'):
            raise ValueError('Not a PDF')
        pdf.write_bytes(response.content)
    reader = PdfReader(pdf)
    pages = [page.extract_text() or '' for page in reader.pages]
    (OUT / f'{key}.txt').write_text(
        '\n\n'.join(f'=== PDF PAGE {i} ===\n{text}' for i, text in enumerate(pages, 1)),
        encoding='utf-8',
    )
    return dict(
        id=key,
        year=year,
        session=session,
        url=href,
        index=index,
        pages=len(pages),
        sha256=hashlib.sha256(pdf.read_bytes()).hexdigest(),
        file=str(pdf.relative_to(ROOT)),
        text_file=str((OUT / f'{key}.txt').relative_to(ROOT)),
    )


def fetch_year(year):
    index = urljoin(BASE, f'PAPERS-{year}/index.htm')
    result = []
    seen_sessions = set()
    try:
        r = requests.get(index, timeout=25)
        r.raise_for_status()
        soup = BeautifulSoup(r.content, 'html.parser')
        for a in soup.find_all('a', href=True):
            label = a.get_text(' ', strip=True).upper()
            raw_href = a['href'].strip().replace('\\', '/')
            href = urljoin(index, quote(raw_href, safe='/:'))
            if ('PUNJABI' not in label and 'PNJABI' not in label and '75' not in raw_href) or 'SECONDARY' not in label:
                continue
            if any(s in label for s in ['SR SECONDARY', 'SR.SECONDARY', 'SR. SEC', 'PRAVESHIKA', 'VARISHTHA', 'D&D', 'D-D']):
                continue
            if 'D-D' in raw_href.upper() or 'D&D' in raw_href.upper():
                continue
            if '/sec/' not in href.lower() and '/secsup/' not in href.lower():
                continue
            session = 'supplementary' if '/secsup/' in href.lower() or '/supp/' in href.lower() else 'main'
            if session in seen_sessions:
                continue
            seen_sessions.add(session)
            result.append(save_paper(year, session, href, index))
        if year in EXTRA_SUPP and 'supplementary' not in seen_sessions:
            result.append(save_paper(year, 'supplementary', EXTRA_SUPP[year], index))
        if not result:
            result = [dict(year=year, status='no regular Secondary Punjabi PDF found in index', index=index)]
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
    print('Downloaded', sum('id' in r for r in manifest), 'official Punjabi papers.')


if __name__ == '__main__':
    main()
