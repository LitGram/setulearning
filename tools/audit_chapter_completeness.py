"""Audit every bundled chapter and restore omitted reading paragraphs from sources.

Existing lesson edits, IDs, and MCQs are preserved. Run with --repair to write
repairs; the default is a read-only audit. Source roots may be overridden.
"""
import argparse
import difflib
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def reading_blocks(text):
    """Keep teaching sections, including revision after a dedicated quiz section.

    Only section headings trigger quiz exclusion: references to MCQs in prose
    and worked/PYQ examples must never cut off the teaching material.
    """
    text = text.replace('\x0crac', r'\frac').replace('\x0c', '')
    text = text.replace(r'\night)', r'\right)')
    text = re.sub(r'<!--\s*mcq\s*-->.*?<!--\s*/mcq\s*-->', '', text,
                  flags=re.DOTALL | re.IGNORECASE)
    kept = []
    excluded_level = None
    fenced = False
    question_bank = bool(re.search(r'^#\s+.*MCQs?', text, re.MULTILINE | re.IGNORECASE))
    for line in text.splitlines():
        if line.strip().startswith('```'):
            fenced = not fenced
        heading = None if fenced else re.match(r'^(#{1,6})\s+(.+)', line)
        if question_bank and re.match(r'^###\s*(?:प्रश्न|Question)\s*\d+', line):
            excluded_level = 2
        if heading:
            level, title = len(heading[1]), heading[2]
            if excluded_level is not None and level <= excluded_level:
                excluded_level = None
            quiz = (level == 2 and re.search(
                r'अभ्यास.*(?:MCQ|प्रश्न|प्रश्नमाला)|बहुविकल्प|प्रश्नोत्तरी|'
                r'भाग\s*12\s*[:\-]|उत्तर[-\s]*कुंजी|विस्तृत हल|संक्षिप्त हल|'
                r'उत्तर\s*(?:कुंजी|एवं विस्तृत|व विस्तृत)|प्रश्न एवं.*समाधान|'
                r'^विस्तृत समाधान|^समाधान|Detailed.*Solutions|'
                r'परीक्षा[-\s]*उपयोगी.*प्रश्न|Practice Question Bank',
                title, re.IGNORECASE))
            if quiz:
                excluded_level = level
        if excluded_level is None:
            kept.append(line)
    blocks = []
    for paragraph in re.split(r'\n\s*\n', '\n'.join(kept)):
        value = paragraph.strip()
        if value and not value.startswith('# ') and value not in ('---', '***', '___'):
            blocks.append({'type': 'text', 'value': value})
    return blocks


def normalize(value):
    return re.sub(r'[\s#*>`_]+', '', value).casefold()


def source_for(asset, index, chapter, source_root):
    subject = asset.parent.name
    if subject == 'englishsetu' and asset.stem in ('book59', 'book60'):
        folder = source_root / 'short books' / {
            'book59': 'Book_59_High_Frequency_Vocab',
            'book60': 'Book_60_Literary_Terms',
        }[asset.stem]
        files = sorted(folder.glob('Chapter_[0-9][0-9].md'))
        if index < len(files):
            return files[index], None
    if subject == 'rassetu_supplementary':
        folders = {
            'book52': 'short books/Book_52_Flagship_Schemes',
            'book53': 'short books/Book_53_Rajasthan_Economy',
            'book55': 'short books/Book_55_Administrative_Hindi',
            'mains_answer_writing': 'ras books/book_ras_mains_answer_writing',
            'paper4_language_essay': 'ras books/book_paper4_language_essay',
            'general_science': 'ras books/general science book',
        }
        folder = source_root / folders[asset.stem]
        files = sorted(folder.glob('Chapter_[0-9][0-9].md'))
        if not files:
            files = sorted(p for p in folder.glob('[0-9][0-9]-*.md') if not p.name.startswith('00-'))
        if index < len(files):
            return files[index], None
    number = re.search(r'_book(\d+)', asset.stem)
    if number and subject in ('mathsetu', 'vigyansetu', 'rassetu'):
        n = int(number[1])
        if subject == 'mathsetu':
            folder = source_root / 'maths books' / f'book {n}'
            files = sorted(p for p in folder.glob('[0-9][0-9]-*.md')
                           if not p.name.startswith('00-'))
        elif subject == 'vigyansetu':
            folders = list((source_root / 'vigyan setu').glob(f'book-{n:02d}-*'))
            files = sorted(folders[0].glob('ch[0-9][0-9]*.md')) if folders else []
            source_number = re.search(r'अध्याय\s*(\d+)', chapter['title'])
            if source_number:
                matching = [p for p in files if p.name.startswith(f'ch{int(source_number[1]):02d}')]
                if len(matching) == 1:
                    return matching[0], None
        else:
            folders = list((source_root / 'ras books').glob(f'Book_{n:02d}*'))
            folder = folders[0] if folders else source_root / 'ras books' / f'book_{n:02d}'
            files = sorted(set(folder.glob('Chapter_[0-9][0-9].md')) |
                           set(folder.glob('ch[0-9][0-9]*.md')))
            # The original RAS importer emitted each chapter twice under odd/even IDs.
            index //= 2
        return (files[index], None) if index < len(files) else (None, None)
    # Later imported books carry their complete chapter Markdown in the repo.
    matches = list((ROOT / 'books_markdown').rglob(asset.stem + '.md'))
    if not matches and subject == 'greatworks':
        matches = list((ROOT / 'books_markdown/great_works').glob(asset.stem + '.md'))
    if matches:
        text = matches[0].read_text(encoding='utf-8')
        sections = re.split(r'(?m)^# (?=(?:अध्याय|Chapter)\s+\d+)', text)
        if len(sections) > 1 and index + 1 < len(sections):
            return matches[0], '# ' + sections[index + 1]
        # Match title headings to avoid guessing boundaries in literature imports.
        lines = text.splitlines()
        title = normalize(chapter['title'])
        for start, line in enumerate(lines):
            match = re.match(r'^(#{1,2})\s+(.+)', line)
            if match and normalize(match[2]) == title:
                level = len(match[1])
                end = next((i for i in range(start + 1, len(lines))
                            if re.match(r'^#{1,' + str(level) + r'}\s+', lines[i])), len(lines))
                return matches[0], '\n'.join(lines[start:end])
    return None, None


def audit(repair=False, source_root=Path('D:/new projects')):
    report = {'chaptersChecked': 0, 'sourceMatched': 0, 'restoredChapters': 0,
              'restoredParagraphs': 0, 'books': []}
    for asset in sorted((ROOT / 'assets/content').rglob('*.json')):
        data = json.loads(asset.read_text(encoding='utf-8'))
        snapshot_verified = False
        if asset.parent.name == 'englishsetu':
            from format_mcq_books import markdown_book
            snapshot = ROOT / 'books_markdown/englishsetu' / (asset.stem + '.md')
            snapshot_verified = snapshot.exists() and normalize(snapshot.read_text(encoding='utf-8')) == normalize(markdown_book(data))
            recovery_path = ROOT / 'artifacts/english_docx_recovery.json'
            if data.get('sourceImport', {}).get('kind') == 'ordered_docx' and recovery_path.exists():
                import hashlib
                records = json.loads(recovery_path.read_text(encoding='utf-8'))['books']
                snapshot_verified = any(
                    record['asset'] == asset.relative_to(ROOT).as_posix() and
                    record['assetSha256'] == hashlib.sha256(asset.read_bytes()).hexdigest() and
                    record['sourceSha256'] == hashlib.sha256(Path(record['source']).read_bytes()).hexdigest() and
                    record['sourcePayloadSha256'] == record['recoveredPayloadSha256']
                    for record in records)
        if asset.parent.name == 'mscphysics':
            manifest = json.loads((ROOT / 'artifacts/mscphysics_import.json').read_text(encoding='utf-8'))
            import hashlib
            snapshot_verified = any(b['asset'] == asset.relative_to(ROOT).as_posix() and
                b['assetSha256'] == hashlib.sha256(asset.read_bytes()).hexdigest() for b in manifest['books'])
        if asset.parent.name.startswith('ugcnet_'):
            original = source_root / 'ugc net for setu app' / asset.parent.name / 'json' / asset.name
            snapshot_verified = original.exists() and json.loads(original.read_text(encoding='utf-8')) == data
        book_report = {'asset': asset.relative_to(ROOT).as_posix(), 'chapters': []}
        changed = False
        for index, chapter in enumerate(data.get('chapters', [])):
            report['chaptersChecked'] += 1
            path, section = source_for(asset, index, chapter, source_root)
            row = {'id': chapter['id'], 'readingBlocks': len(chapter['content']),
                   'status': 'source unavailable for comparison'}
            if snapshot_verified:
                report['sourceMatched'] += 1
                row['status'] = 'complete against import snapshot'
            elif path:
                source = section if section is not None else path.read_text(encoding='utf-8')
                expected = reading_blocks(source)
                current = [normalize(b['value']) for b in chapter['content']]
                joined = ''.join(current)
                # Validate source mapping with actual lesson text, not just position.
                anchors = sum(normalize(b['value']) in joined for b in expected[:8])
                if anchors >= 2 or all(normalize(b['value']) in joined for b in expected):
                    report['sourceMatched'] += 1
                    missing = []
                    for block in expected:
                        value = normalize(block['value'])
                        if value in joined:
                            continue
                        # Preserve edited formulas and paragraphs in the current app.
                        if any(value in c or c in value or
                               (value[:24] == c[:24] and
                                .8 < len(value) / len(c) < 1.2 and
                                difflib.SequenceMatcher(None, value, c).ratio() > .85)
                               for c in current if c):
                            continue
                        missing.append(block)
                    row.update(source=str(path), missingParagraphs=len(missing),
                               status='omitted source paragraphs' if missing else 'complete against source')
                    if missing:
                        report['restoredChapters'] += 1
                        report['restoredParagraphs'] += len(missing)
                        if repair and asset.parent.name in ('mathsetu', 'vigyansetu', 'rassetu', 'rassetu_supplementary'):
                            chapter['content'].extend(missing)
                            changed = True
                else:
                    row.update(source=str(path), status='source mapping requires review')
            if not chapter['content']:
                row['status'] = 'empty reading content'
            book_report['chapters'].append(row)
        if changed:
            asset.write_text(json.dumps(data, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
        report['books'].append(book_report)
    return report


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--repair', action='store_true')
    parser.add_argument('--source-root', type=Path, default=Path('D:/new projects'))
    parser.add_argument('--report', type=Path, default=ROOT / 'artifacts/chapter_completeness_audit.json')
    args = parser.parse_args()
    result = audit(args.repair, args.source_root)
    args.report.parent.mkdir(parents=True, exist_ok=True)
    args.report.write_text(json.dumps(result, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    print(json.dumps({k: v for k, v in result.items() if k != 'books'}))
