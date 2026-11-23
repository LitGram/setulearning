#!/usr/bin/env python3
"""Repeatable, read-only source import of exactly four English Physics guides.

Run: python tools/import_msc_physics.py [--check]
No external packages. --check verifies saved outputs without rewriting them.
The complete manuscript is retained, including author, prerequisites and appendices.
"""
from __future__ import annotations

import argparse
import hashlib
import html
import json
import re
import shutil
import zipfile
from pathlib import Path
from xml.etree import ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
BOOKS = (
    ('mathematical_physics', 'Mathematical Physics',
     'Mathematical_Physics_MSc_Guide_English.md', 'Mathematical_Physics_MSc_Guide_English.epub'),
    ('classical_mechanics', 'Classical Mechanics',
     'Classical Mechanics M.Sc Guide (English).md', 'Classical_Mechanics_MSc_Guide_English.epub'),
    ('quantum_mechanics_i', 'Quantum Mechanics I',
     'Quantum Mechanics I M.Sc Guide (English).md', 'Quantum_Mechanics_I_MSc_Guide_English.epub'),
    ('statistical_physics', 'Statistical Physics',
     'Statistical Physics MSc Guide (PHY6.0-CC-104).md', 'Statistical_Physics_MSc_Guide_English.epub'),
)
ANCHOR = re.compile(r'^\s*<div id="[^"]+"></div>\s*$')
HEADING = re.compile(r'^(#{1,6}) (.+)$')
SEPARATOR = re.compile(r'^\s*\|(?:\s*:?-+:?\s*\|)+\s*$')
IMAGE = re.compile(r'^!\[([^\]]*)\]\(([^)]+)\)$')
IMAGE_SOURCES = {}
APPENDIX_START = {'mathematical_physics': 65, 'classical_mechanics': 46,
                  'quantum_mechanics_i': 50, 'statistical_physics': 24}


def digest(value: str | bytes) -> str:
    return hashlib.sha256(value.encode('utf-8') if isinstance(value, str) else value).hexdigest()


def compact(value: str) -> str:
    return re.sub(r'\s+', '', value)


def visible_text(source: str) -> str:
    """Independent visibility oracle for the source's limited Markdown dialect.

    Equation fences are literal: every symbol, including *, _, |, is retained.
    Outside fences remove only presentation syntax, never mathematical operators.
    """
    result, code, table = [], False, False
    lines = source.splitlines()
    for index, line in enumerate(lines):
        if line.strip().startswith('```'):
            code = not code
            continue
        if code:
            result.append(line)
            continue
        if SEPARATOR.fullmatch(line) or re.fullmatch(r'\s*---\s*', line):
            continue
        if index + 1 < len(lines) and SEPARATOR.fullmatch(lines[index + 1]):
            table = True
        if not line.lstrip().startswith('|'):
            table = False
        if table and line.strip().startswith('|') and line.strip().endswith('|'):
            # Every pipe in these tables is a column boundary unless escaped.
            line = ' '.join(re.split(r'(?<!\\)\|', line)[1:-1])
        line = re.sub(r'^\s*(?:>\s?)+', '', line)
        if re.match(r'^\s*#{1,6}\s+', line):
            line = re.sub(r'^\s*#{1,6}\s+', '', line)
        else:
            line = re.sub(r'^\s*(?:[-+] |\d+[.)] )', '', line)
        line = re.sub(r'\[([^\]]+)\]\(([^)]+)\)', r'\1', line)
        line = re.sub(r'(?<!\\)\*\*(.*?)(?<!\\)\*\*', r'\1', line)
        line = re.sub(r'(?<![\w\\*])\*([^*\n]+)(?<!\\)\*(?![\w*])', r'\1', line)
        line = re.sub(r'`([^`]+)`', r'\1', line)
        line = re.sub(r'\\([\\`*_{}\[\]()#+.!<>|$-])', r'\1', line)
        result.append(html.unescape(line))
    assert not code, 'Unbalanced equation fences'
    return '\n'.join(result)


def clean(lines: list[str], book_id: str, offset: int) -> tuple[list[str], list[dict]]:
    result, repairs, code = [], [], False
    for index, original in enumerate(lines):
        line = original
        if ANCHOR.fullmatch(line):
            repairs.append({'sourceLine': offset + index + 1, 'kind': 'remove empty HTML navigation anchor'})
            continue
        if IMAGE.fullmatch(line) and not code:
            result.append(line)
            continue
        # The published Markdown has a stray closing fence after a repeated
        # generating formula. Supply its missing opening fence; keep both formulas.
        if (book_id == 'mathematical_physics' and not code
                and line.startswith('exp[ (x / 2) (t - 1/t) ]')
                and index > 0 and not lines[index - 1].strip()
                and index + 1 < len(lines) and lines[index + 1].strip() == '```'):
            result.append('```')
            code = True
            repairs.append({'sourceLine': offset + index + 1, 'kind': 'insert missing opening equation fence'})
        if line.strip().startswith('```'):
            code = not code
        elif not code:
            if line.lstrip().startswith('|'):
                line = line.replace('|λ|', r'\|λ\|')
            # Retain a leading blockquote marker; escape mathematical comparisons.
            quote = re.match(r'^(>\s*)', line)
            prefix = quote[0] if quote else ''
            line = line[len(prefix):].replace('_', r'\_').replace('<', '&lt;').replace('>', '&gt;')
            line = prefix + line
            if book_id in {'mathematical_physics', 'quantum_mechanics_i'}:
                # Single asterisks are conjugation signs, except *Example:*.
                line = line.replace('*Example:*', '\x00EXAMPLE\x00')
                line = re.sub(r'(?<!\*)\*(?!\*)', r'\\*', line)
                line = line.replace('\x00EXAMPLE\x00', '*Example:*')
            # A bold delimiter touching whitespace leaks ** in CommonMark.
            line = re.sub(r'\*\*(.*?)\*\*',
                          lambda m: ('**' + m[1].strip() + '**' if m[1].strip() else '')
                          + (' ' if m[1].endswith(' ') else ''), line)
        if line != original:
            repairs.append({'sourceLine': offset + index + 1, 'kind': 'protect literal math symbols / normalize emphasis',
                            'before': original, 'after': line})
        result.append(line)
    assert not code, 'Unclosed equation fence in source'
    return result, repairs


def chapter_markdown(chapter: dict) -> str:
    return '\n'.join(block['value'] if block['type'] == 'text' else
                     f"![{block['caption']}]({IMAGE_SOURCES[block['value']]})"
                     for block in chapter['content'])


def chapters_from(lines: list[str], book_id: str) -> list[dict]:
    # Only top-level teaching units delimit units. Headings such as
    # '## Unit 1: Quick Revision' remain inside the corresponding unit.
    boundaries = [(0, 'Start Here: Basics and Study Guide', 'preface')]
    code = False
    for i, line in enumerate(lines):
        if line.strip().startswith('```'):
            code = not code
        if code:
            continue
        unit = re.match(r'^# Unit ([123]):', line)
        appendix = re.match(r'^#{1,2} Appendix (\d+):', line)
        if unit:
            boundaries.append((i, HEADING.fullmatch(line)[2], 'unit'+unit[1]))
        elif appendix:
            # Preserve existing appendix IDs as well as unit IDs and book IDs.
            boundaries.append((i, HEADING.fullmatch(line)[2],
                               'ch'+str(APPENDIX_START[book_id]+int(appendix[1])-1)))
    result=[]
    for number,(start,title,chapter_id) in enumerate(boundaries):
        end=boundaries[number+1][0] if number+1<len(boundaries) else len(lines)
        blocks=[]; chunk=[]; code=False
        def flush():
            if chunk:
                blocks.append({'type':'text','value':'\n'.join(chunk)})
                chunk.clear()
        for line in lines[start:end]:
            image=IMAGE.fullmatch(line)
            if image and not code:
                flush()
                filename=next(name for name,path in IMAGE_SOURCES.items() if path==image[2])
                blocks.append({'type':'image','value':filename,'caption':image[1]})
            else:
                if not code and re.match(r'^#{2,3} ',line):flush()
                chunk.append(line)
                if line.strip().startswith('```'):code=not code
        flush()
        result.append({'id':chapter_id,'title':title,'subtitle':'Shiwali Sharma' if chapter_id=='preface' else title,
                       'content':blocks,'mcqs':[]})
    assert '\n'.join(map(chapter_markdown,result))=='\n'.join(lines), 'Lost or duplicated manuscript content'
    assert len({ch['id'] for ch in result})==len(result)
    assert {ch['id'] for ch in result if ch['id'].startswith('unit')}=={'unit1','unit2','unit3'}
    return result


def epub_comparison(path: Path, chapters: list[dict]) -> dict:
    """Compare publication teaching pages, never title/front matter pages."""
    headings, literal_blocks, pages = [], [], []
    with zipfile.ZipFile(path) as archive:
        for name in archive.namelist():
            if re.search(r'/(unit[123]|appendix)\.xhtml$', name):
                doc = ET.fromstring(archive.read(name))
                pages.append(name)
                for el in doc.iter():
                    tag = el.tag.rsplit('}', 1)[-1]
                    value = ''.join(el.itertext()).strip()
                    if re.fullmatch(r'h[1-6]', tag):
                        headings.append(value)
                    elif tag == 'pre':
                        literal_blocks.append(value)
    raw = '\n'.join(block['value'] for ch in chapters for block in ch['content'])
    visible = compact(visible_text(raw))
    # A malformed publication fence can put Markdown headings in a <pre>.
    # Also compare the literal retained source, ignoring presentation escapes.
    literal_source = compact(html.unescape(re.sub(r'\\([_*])', r'\1', raw)).replace('```', ''))
    missing_headings = [h for h in headings if compact(h) not in visible
                        and compact(h) not in literal_source]
    missing_literals = [b for b in literal_blocks if compact(b) not in visible
                        and compact(b) not in literal_source]
    return {'file': path.name, 'sha256': digest(path.read_bytes()), 'teachingPages': pages,
            'headingCount': len(headings), 'literalEquationBlocks': len(literal_blocks),
            'headingsNotInMarkdown': missing_headings,
            'literalBlocksNotInMarkdown': missing_literals,
            'note': 'Markdown is authoritative. Publication differences are recorded, not substituted.'}


def save(path: Path, value: str, check: bool) -> None:
    if check:
        assert path.read_text(encoding='utf-8') == value, f'Stale output: {path}'
    else:
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(value, encoding='utf-8', newline='\n')


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--source-root', type=Path, default=Path(r'D:\new projects\ras books\msc physics guide'))
    parser.add_argument('--check', action='store_true')
    args = parser.parse_args()
    audits, catalog = [], []
    for number, (book_id, title, manuscript, epub) in enumerate(BOOKS, 1):
        path = args.source_root / manuscript
        source_bytes = path.read_bytes()
        source = source_bytes.decode('utf-8-sig')
        lines = source.splitlines()
        first = next(i for i, line in enumerate(lines) if re.match(r'^# Unit 1:', line))
        assert '**Author:** Shiwali Sharma' in source
        # App credit is a small line, not a printed title page. Retain the
        # complete teaching introduction and prerequisite bridge after it.
        intro=next(i for i,line in enumerate(lines) if re.match(r'^## (Preface|A Note)',line))
        app_lines=[f'{title} · Shiwali Sharma','']+lines[intro:]
        cleaned, repairs = clean(app_lines, book_id, intro-2)
        IMAGE_SOURCES.clear()
        images=[]
        for line in cleaned:
            image=IMAGE.fullmatch(line)
            if not image:
                continue
            image_path=(args.source_root/image[2]).resolve()
            assert image_path.is_relative_to(args.source_root.resolve())
            filename='msc_'+book_id+'_'+image_path.name
            IMAGE_SOURCES[filename]=image[2]
            destination=ROOT/'assets/images'/filename
            if args.check:
                assert destination.read_bytes()==image_path.read_bytes(), f'Stale figure: {filename}'
            else:
                shutil.copy2(image_path,destination)
            images.append({'file':filename,'source':image[2],'sha256':digest(image_path.read_bytes())})
        chapters = chapters_from(cleaned,book_id)
        data = {'subject': 'M.Sc. Physics', 'book': title, 'author': 'Shiwali Sharma', 'chapters': chapters}
        asset = f'assets/content/mscphysics/{book_id}.json'
        markdown = f'books_markdown/mscphysics/{book_id}.md'
        save(ROOT / asset, json.dumps(data, ensure_ascii=False, indent=2) + '\n', args.check)
        save(ROOT / markdown, '\n'.join(cleaned) + '\n', args.check)
        # Prove all non-presentation source characters survive the transformations.
        def payload(text: str) -> str:
            text = re.sub(r'^\s*<div id="[^"]+"></div>\s*$', '', text, flags=re.M)
            text = re.sub(r'\\([_*|])', r'\1', html.unescape(text))
            return compact(text.replace('```', ''))
        retained = '\n'.join(app_lines)
        imported = '\n'.join(map(chapter_markdown,chapters))
        assert payload(retained) == payload(imported), f'Coverage failure: {title}'
        # Source files must still have their exact original bytes.
        assert path.read_bytes() == source_bytes
        oracle = {ch['id']: visible_text('\n'.join(block['value'] for block in ch['content'] if block['type']=='text')) for ch in chapters}
        save(ROOT / f'artifacts/mscphysics_expected_text/{book_id}.json',
             json.dumps(oracle, ensure_ascii=False, indent=2) + '\n', args.check)
        audit = {'id': book_id, 'title': title, 'source': str(path), 'sourceSha256': digest(source_bytes),
                 'sourceLines': len(lines), 'firstTeachingLine': first + 1,
                 'excludedFrontMatterLines': intro, 'retainedSourceLines': len(lines)-intro,
                 'appCredit': f'{title} · Shiwali Sharma',
                 'omittedPublicationHeader': '\n'.join(lines[:intro]),
                 'chapterCount': len(chapters), 'interactiveMcqCount': 0,
                 'coverage': 'Small book/author credit replaces publication header; complete teaching preface, prerequisites, units and appendices retained in order; diagrams copied byte for byte',
                 'author': 'Shiwali Sharma', 'images':images,
                 'retainedPayloadSha256': digest(payload(retained)),
                 'importedPayloadSha256': digest(payload(imported)),
                 'asset': asset, 'assetSha256': digest((ROOT / asset).read_bytes()),
                 'cleanMarkdown': markdown, 'formatRepairs': repairs,
                 'chapters': [{'id': ch['id'], 'title': ch['title'],
                               'visibleTextSha256': digest(compact(oracle[ch['id']]))} for ch in chapters],
                 'publicationComparison': epub_comparison(args.source_root / epub, chapters)}
        audits.append(audit)
        catalog.append(f"      Book(id: 'mscphysics_{book_id}', subjectId: 'mscphysics', bookNumber: {number},\n"
                       f"          title: '{title}', description: 'Shiwali Sharma · English with Hindi support',\n"
                       f"          jsonAssetPath: '{asset}', expectedChapterCount: {len(chapters)}),")
        print(f'{title}: {len(chapters)} chapters, {len(images)} diagrams; full manuscript, author Shiwali Sharma')
    generated = """// Generated by tools/import_msc_physics.py; chapter counts follow source headings.
import 'package:flutter/material.dart';
import '../models/book.dart';
import '../models/subject.dart';

Subject createMscPhysicsSubject() => Subject(
    id: 'mscphysics',
    name: 'M.Sc. Physics',
    hindiName: 'एम.एससी. भौतिकी',
    tagline: 'Mathematical Physics, Classical Mechanics, Quantum Mechanics & Statistical Physics',
    seedColor: const Color(0xFF0369A1),
    icon: Icons.science_outlined,
    books: [
""" + '\n'.join(catalog) + '\n    ],\n  );\n'
    save(ROOT / 'lib/services/msc_physics_catalog.dart', generated, args.check)
    save(ROOT / 'artifacts/mscphysics_import.json', json.dumps({
        'subject': 'mscphysics', 'books': audits,
        'limitations': [
            'Source equations use Unicode and literal notation, not TeX. Preserved without speculative conversion.',
            'Explained manuscript MCQs remain in the reading content; no duplicate interactive quiz is generated.',
            'Book, unit and existing appendix IDs are preserved. Start Here retains the learning introduction with a small book/author credit in place of the print publication header.',
            'Mathematical Physics repeats a Bessel generating formula beside a stray fence; both formula occurrences are retained, with the missing opening fence repaired.',
        ]}, ensure_ascii=False, indent=2) + '\n', args.check)


if __name__ == '__main__':
    main()
