"""Recover complete English guides from Word XML, retaining document order.

No paragraph caps or broad copyright/author filters. Only a positively identified
leading introduction/chapter boundary excludes cover material. Existing keyed
practice is preserved; this recovery does not infer any new answer keys.
"""
import argparse
import hashlib
import json
import re
import posixpath
import zipfile
from pathlib import Path
from xml.etree import ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
W = '{http://schemas.openxmlformats.org/wordprocessingml/2006/main}'


def text_of(element):
    return ''.join(node.text or '' if node.tag == W + 't' else
                   '\n' if node.tag in (W + 'br', W + 'cr') else '\t'
                   for node in element.iter()
                   if node.tag in (W + 't', W + 'br', W + 'cr', W + 'tab'))


def escape(value):
    value = re.sub(r'([\\`*_\[\]<>#|])', r'\\\1', value)
    value = re.sub(r'(?m)^(\s*\d+)([.)])(?=\s)', r'\1\\\2', value)
    return re.sub(r'(?m)^(\s*)([-+])(?=\s)', r'\1\\\2', value)


def compact(value):
    return re.sub(r'\s+', '', value)


def digest(value):
    return hashlib.sha256(value.encode('utf-8')).hexdigest()


def source_blocks(path):
    with zipfile.ZipFile(path) as archive:
        body = ET.fromstring(archive.read('word/document.xml')).find(W + 'body')
        relationships = (ET.fromstring(archive.read('word/_rels/document.xml.rels'))
                         if 'word/_rels/document.xml.rels' in archive.namelist() else [])
        images = {}
        for relationship in relationships:
            if relationship.get('Type', '').endswith('/image'):
                target = posixpath.normpath('word/' + relationship.get('Target', ''))
                images[relationship.get('Id')] = (target, archive.read(target))
    blocks = []
    for element in body:
        if element.tag == W + 'p':
            value = text_of(element).strip()
            style = element.find(W + 'pPr/' + W + 'pStyle')
            style_name = style.get(W + 'val', '') if style is not None else ''
            heading = re.search(r'Heading([1-6])$', style_name, re.I)
            level = int(heading[1]) if heading else None
            if re.match(r'^(?:Chapter|Unit)\s+\d+\s*[:.\-–—]', value, re.I):
                level = 1
            if re.fullmatch(r'Set\s+\d+(?:\s*[:\-–].*)?', value, re.I):
                level = 1
            if value:
                blocks.append({'raw': value, 'value': ('#' * level + ' ' if level else '') + escape(value),
                               'level': level, 'kind': 'paragraph'})
            for drawing in element.iter('{http://schemas.openxmlformats.org/drawingml/2006/main}blip'):
                rid = drawing.get('{http://schemas.openxmlformats.org/officeDocument/2006/relationships}embed')
                if rid in images:
                    target, image_bytes = images[rid]
                    filename = 'docx_' + digest(path.name)[:12] + '_' + Path(target).name
                    blocks.append({'raw': '', 'value': filename, 'level': None,
                                   'kind': 'image', 'bytes': image_bytes})
        elif element.tag == W + 'tbl':
            rows = []
            for row in element.findall(W + 'tr'):
                cells = [' '.join(text_of(p).strip() for p in cell.findall(W + 'p'))
                         for cell in row.findall(W + 'tc')]
                if cells:
                    rows.append(cells)
            if not rows:
                continue
            width = max(len(row) for row in rows)
            lines = []
            for i, row in enumerate(rows):
                lines.append('| ' + ' | '.join(escape(value).replace('\n', ' ') for value in
                             row + [''] * (width - len(row))) + ' |')
                if i == 0:
                    lines.append('| ' + ' | '.join(['---'] * width) + ' |')
            blocks.append({'raw': '\n'.join(cell for row in rows for cell in row),
                           'value': '\n'.join(lines), 'level': None, 'kind': 'table'})
    return blocks


def recover(asset, source, write_images=True):
    old = (json.loads(asset.read_text(encoding='utf-8')) if asset.exists() else
           {'subject': 'EnglishSetu', 'book': source.stem, 'chapters': []})
    blocks = source_blocks(source)
    # Word's unstyled chapter headings are common in these originals.
    start = next((i for i, block in enumerate(blocks[:150])
                  if block['raw'].casefold() == 'introduction' or
                  re.match(r'^Chapter\s+1\s*[:.\-–—]', block['raw'], re.I)), 0)
    retained = blocks[start:]
    numbered_chapters = any(re.match(r'^Chapter\s+\d+(?:\s*[:.\-–—].*|\s*)$', b['raw'], re.I)
                            for b in retained if len(b['raw']) < 180)
    chapters = []
    raw_chapters = []
    body_seen = False
    for block in retained:
        chapter_heading = bool(re.match(r'^Chapter\s+\d+(?:\s*[:.\-–—].*|\s*)$', block['raw'], re.I)) and len(block['raw']) < 180
        boundary = chapter_heading if numbered_chapters else block['level'] == 1
        if not chapters or (boundary and body_seen):
            title = block['raw'] if block['level'] == 1 else 'Main study material'
            chapters.append({'id': f"docx_ch{len(chapters) + 1}", 'title': title,
                             'content': [], 'mcqs': []})
            raw_chapters.append([])
            body_seen = False
        chapters[-1]['content'].append({'type': 'image' if block['kind'] == 'image' else 'text', 'value': block['value']})
        raw_chapters[-1].append(block['raw'])
        if block['level'] is None:
            body_seen = True
    # Preserve a dangling source heading as context, not a phantom chapter.
    for index in range(len(chapters) - 1, 0, -1):
        brief = '\n'.join(raw_chapters[index])
        if (all(block['value'].startswith('#') for block in chapters[index]['content']) or
                (len(brief) < 80 and len(brief.split()) < 12)):
            if index + 1 < len(chapters):
                chapters[index]['content'].extend(chapters[index + 1]['content'])
                raw_chapters[index].extend(raw_chapters[index + 1])
                del chapters[index + 1]
                del raw_chapters[index + 1]
            else:
                chapters[index - 1]['content'].extend(chapters[index]['content'])
                raw_chapters[index - 1].extend(raw_chapters[index])
                del chapters[index]
                del raw_chapters[index]
    for index, chapter in enumerate(chapters, 1):
        chapter['id'] = f'docx_ch{index}'
    # Preserve previously supplied practice and answer keys exactly, once each.
    seen = set()
    preserved = []
    for chapter in old['chapters']:
        for question in chapter['mcqs']:
            signature = json.dumps(question, ensure_ascii=False, sort_keys=True)
            if signature not in seen:
                seen.add(signature)
                preserved.append(question)
    normalized = [compact('\n'.join(values)).casefold() for values in raw_chapters]
    for question in preserved:
        stem = compact(question['question']).casefold()
        index = next((i for i, value in enumerate(normalized) if stem in value), 0)
        chapters[index]['mcqs'].append(question)
    original = compact('\n'.join(block['raw'] for block in retained))
    recovered = compact('\n'.join(value for values in raw_chapters for value in values))
    assert original == recovered, 'Recovery changed source order or omitted text'
    new = {**old, 'chapters': chapters,
           'sourceImport': {'kind': 'ordered_docx', 'payloadSha256': digest(original)}}
    report = {'asset': asset.relative_to(ROOT).as_posix(), 'source': str(source),
              'sourceSha256': hashlib.sha256(source.read_bytes()).hexdigest(),
              'assetSha256': digest(json.dumps(new, ensure_ascii=False, indent=2) + '\n'),
              'sourceBlocks': len(blocks), 'excludedLeadingBlocks': start,
              'retainedBlocks': len(retained), 'retainedTables': sum(b['kind'] == 'table' for b in retained),
              'images': [{'file': b['value'], 'sha256': hashlib.sha256(b['bytes']).hexdigest()}
                         for b in retained if b['kind'] == 'image'],
              'chapterCount': len(chapters), 'preservedKeyedQuestions': len(preserved),
              'sourcePayloadSha256': digest(original), 'recoveredPayloadSha256': digest(recovered),
              'chapters': [{'id': c['id'], 'title': c['title'], 'blocks': len(c['content'])} for c in chapters]}
    for block in retained:
        if block['kind'] == 'image':
            target = ROOT / 'assets/images' / block['value']
            if not target.exists() or target.read_bytes() != block['bytes']:
                if not write_images:
                    raise AssertionError(f'Missing or changed original illustration: {target}')
                target.write_bytes(block['bytes'])
    return new, report, {c['id']: '\n'.join(values) for c, values in zip(chapters, raw_chapters)}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check', action='store_true')
    args = parser.parse_args()
    reports = []
    for line in (ROOT / 'tools/import_new_books.py').read_text(encoding='utf-8').splitlines():
        match = re.search(r'BookSpec\("englishsetu", "EnglishSetu", "([^"]+).*?NEW_PROJECTS / "([^"]+\.docx)"', line)
        if not match:
            continue
        asset = ROOT / 'assets/content/englishsetu' / match[1]
        source = Path('D:/new projects') / match[2]
        data, report, oracle = recover(asset, source, write_images=not args.check)
        text = json.dumps(data, ensure_ascii=False, indent=2) + '\n'
        if args.check:
            assert asset.read_text(encoding='utf-8') == text, asset
        else:
            asset.write_text(text, encoding='utf-8')
            report['assetSha256'] = hashlib.sha256(asset.read_bytes()).hexdigest()
            from format_mcq_books import markdown_book
            (ROOT / 'books_markdown/englishsetu' / asset.with_suffix('.md').name).write_text(markdown_book(data), encoding='utf-8')
            target = ROOT / 'artifacts/english_docx_expected_text' / asset.name
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_text(json.dumps(oracle, ensure_ascii=False, indent=2), encoding='utf-8')
        reports.append(report)
        print(f'{asset.name}: {len(data["chapters"])} complete sections; {report["retainedBlocks"]} source blocks; {report["retainedTables"]} tables in source order')
    if not args.check:
        (ROOT / 'artifacts/english_docx_recovery.json').write_text(json.dumps({'books': reports}, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
        catalog = ROOT / 'lib/services/content_service.dart'
        text = catalog.read_text(encoding='utf-8')
        for report in reports:
            filename = Path(report['asset']).name
            pattern = r"('" + re.escape(filename) + r"',\s*)\d+(\s*\))"
            text, changed = re.subn(pattern, lambda m: m[1] + str(report['chapterCount']) + m[2], text)
            assert changed == 1, filename
        catalog.write_text(text, encoding='utf-8')


if __name__ == '__main__':
    main()
