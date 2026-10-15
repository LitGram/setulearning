"""Download official regular Secondary Science papers with an auditable manifest."""
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path
from urllib.parse import urljoin
import hashlib
import json
import logging
import requests
from bs4 import BeautifulSoup
from pypdf import PdfReader

ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'artifacts/rbse10_science/papers'
BASE='https://rajeduboard.rajasthan.gov.in/books/'
logging.getLogger('pypdf').setLevel(logging.ERROR)

def fetch_year(year):
    index=urljoin(BASE,f'PAPERS-{year}/index.htm')
    result=[]
    try:
        r=requests.get(index,timeout=25);r.raise_for_status()
        soup=BeautifulSoup(r.content,'html.parser')
        for a in soup.find_all('a',href=True):
            label=a.get_text(' ',strip=True).upper()
            href=urljoin(index,a['href'])
            if 'SCIENCE' not in label or 'SECONDARY' not in label or any(s in label for s in ['SOCIAL','SR SECONDARY','SR.SECONDARY','PRAVESHIKA','D&D','D-D']):continue
            if '/sec/' not in href.lower() and '/secsup/' not in href.lower():continue
            session='supplementary' if '/secsup/' in href.lower() or '/supp/' in href.lower() else 'main'
            key=f'{year}_{session}'
            pdf=OUT/f'{key}.pdf'
            if not pdf.exists():
                response=requests.get(href,timeout=30);response.raise_for_status()
                if not response.content.startswith(b'%PDF'):raise ValueError('Not a PDF')
                pdf.write_bytes(response.content)
            reader=PdfReader(pdf)
            pages=[page.extract_text() or '' for page in reader.pages]
            (OUT/f'{key}.txt').write_text('\n\n'.join(f'=== PDF PAGE {i} ===\n{text}' for i,text in enumerate(pages,1)),encoding='utf-8')
            result.append(dict(id=key,year=year,session=session,url=href,index=index,pages=len(pages),sha256=hashlib.sha256(pdf.read_bytes()).hexdigest(),file=str(pdf.relative_to(ROOT)),text_file=str((OUT/f'{key}.txt').relative_to(ROOT))))
        if not result:result=[dict(year=year,status='no regular Secondary Science PDF found in index',index=index)]
    except Exception as e:result=[dict(year=year,status='fetch-failed',error=str(e),index=index)]
    return result

def main():
    OUT.mkdir(parents=True,exist_ok=True)
    manifest=[]
    with ThreadPoolExecutor(max_workers=4) as pool:
        for f in as_completed([pool.submit(fetch_year,y) for y in range(2014,2027)]):
            rows=f.result();manifest.extend(rows)
            print([(r.get('id',r['year']),r.get('status','downloaded')) for r in rows],flush=True)
    manifest.sort(key=lambda r:(-r['year'],r.get('session','')))
    (OUT/'manifest.json').write_text(json.dumps(manifest,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
    print('Downloaded',sum('id' in r for r in manifest),'official papers.')

if __name__=='__main__':main()
