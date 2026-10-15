from pathlib import Path
import re
ROOT=Path(__file__).resolve().parents[1]
folder=ROOT/'artifacts/rbse10_science/papers'
parts=[]
for path in sorted(folder.glob('*.txt')):
    if path.name=='english_index.txt':continue
    lines=[]
    original=path.read_text(encoding='utf-8')
    decoded=re.sub(r'/G(\d+)',lambda m:chr(int(m.group(1))),original)
    if decoded!=original:
        (folder/(path.stem+'_decoded.txt')).write_text(decoded,encoding='utf-8')
    for line in decoded.splitlines():
        words=re.findall(r'\b[A-Za-z]{3,}\b',line)
        if line.startswith('===') or (len(words)>=3 and len(re.findall(r'[^\x00-\x7F]',line))<6):
            lines.append(line)
    parts.append('===== '+path.stem+' =====\n'+'\n'.join(lines))
(folder/'english_index.txt').write_text('\n\n'.join(parts),encoding='utf-8')
print('English index written')
