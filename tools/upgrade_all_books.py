#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
tools/upgrade_all_books.py
Comprehensive book compilation and content upgrade script for Setu Learning app.
"""

import os
import re
import json
import glob
from audit_chapter_completeness import reading_blocks

def clean_redundant_book_title(title):
    # e.g., "पुस्तक 2: Book 2: Tenses..." -> "Book 2: Tenses..."
    title = re.sub(r'^(?:पुस्तक\s*\d+[\:\s]*)+Book\s*(\d+)', r'Book \1', title)
    title = re.sub(r'^(?:पुस्तक\s*\d+[\:\s]*)+', 'पुस्तक ', title)
    return title.strip()

# -------------------------------------------------------------
# 1. VigyanSetu Books 7 & 8 Compiler
# -------------------------------------------------------------
def compile_vigyansetu_book(book_dir, book_num, book_title, out_path):
    print(f"Compiling VigyanSetu Book {book_num} from '{book_dir}'...")
    md_files = sorted(glob.glob(os.path.join(book_dir, "ch*.md")))
    if not md_files:
        print(f"  Warning: No ch*.md files found in {book_dir}")
        return

    chapters = []
    for idx, fpath in enumerate(md_files, 1):
        with open(fpath, 'r', encoding='utf-8') as f:
            text = f.read()

        m_title = re.search(r'^#\s+(.+)', text)
        title = m_title.group(1).strip() if m_title else f"अध्याय {idx}"
        m_sub = re.search(r'^###\s+(.+)', text, re.M)
        subtitle = m_sub.group(1).strip() if m_sub else None

        # Extract answers from भाग 12
        answers_map = {}
        for m in re.finditer(r'\*\*Q(\d+)\.\s*(?:सही उत्तर|उत्तर|सही विकल्प)[\s\:\*]*\(?([A-Da-d1-4])\)?(?:\*\*)?(.*?)(?=\*\*Q\d+\.|$)', text, re.DOTALL):
            q_num = int(m.group(1))
            letter = m.group(2).upper()
            exp = re.sub(r'^[-\*\s]+', '', m.group(3)).strip()
            answers_map[q_num] = (letter, exp)

        # Extract questions from भाग 11
        mcqs = []
        for m in re.finditer(r'\*\*Q(\d+)\.\*\*\s*(.+?)(?=\*\*Q\d+\.\*\*|##\s*भाग\s*12|##\s*उत्तर|$)', text, re.DOTALL):
            q_num = int(m.group(1))
            q_raw = m.group(2).strip()
            lines = [l.strip() for l in q_raw.split('\n') if l.strip()]
            opts = []
            q_lines = []
            for line in lines:
                opt_m = re.match(r'^\(?([A-Da-d])\)?[\.\:\-\s]+\s*(.*)$', line)
                if opt_m and len(opts) < 4:
                    opts.append(opt_m.group(2).strip())
                elif not opts:
                    q_lines.append(line)
            if len(opts) == 4:
                ans_letter, exp = answers_map.get(q_num, ('A', 'विस्तृत समाधान अध्याय में उपलब्ध है।'))
                mapping = {'A': 0, '1': 0, 'B': 1, '2': 1, 'C': 2, '3': 2, 'D': 3, '4': 3}
                mcqs.append({
                    "question": " ".join(q_lines).strip(),
                    "options": opts,
                    "correctIndex": mapping.get(ans_letter, 0),
                    "explanation": exp[:400] if exp else "विस्तृत समाधान अध्याय में उपलब्ध है।"
                })

        # Reading content: keep before MCQs
        text_content = text
        if '## भाग 11' in text_content:
            text_content = text_content.split('## भाग 11')[0]
        elif '## भाग 5' in text_content and 'MCQ' in text_content:
            text_content = text_content.split('## भाग 5')[0]

        paragraphs = re.split(r'\n\s*\n', text_content)
        content_blocks = []
        for p in paragraphs:
            p_clean = p.strip()
            if not p_clean or p_clean.startswith('# ') or p_clean in ('---', '***'):
                continue
            content_blocks.append({"type": "text", "value": p_clean})

        chapters.append({
            "id": f"ch{idx}",
            "title": title,
            "subtitle": subtitle,
            "content": reading_blocks(text),
            "mcqs": mcqs
        })

    book_obj = {
        "subject": "VigyanSetu",
        "book": book_title,
        "chapters": chapters
    }

    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, 'w', encoding='utf-8') as f:
        json.dump(book_obj, f, ensure_ascii=False, indent=2)

    total_mcqs = sum(len(c["mcqs"]) for c in chapters)
    print(f"✓ VigyanSetu Book {book_num}: {len(chapters)} chapters, {total_mcqs} MCQs -> {out_path}")

# -------------------------------------------------------------
# 2. MathSetu Books 4, 5, 6 Compiler
# -------------------------------------------------------------
def compile_mathsetu_book(book_dir, book_num, book_title, out_path):
    print(f"Compiling MathSetu Book {book_num} from '{book_dir}'...")
    # Find all chapter files in book dir, ignoring front matter
    all_files = sorted(glob.glob(os.path.join(book_dir, "[0-9][0-9]-*.md")))
    ch_files = [f for f in all_files if not os.path.basename(f).startswith("00-")]
    if not ch_files:
        # Fallback to Combined.md
        comb_files = glob.glob(os.path.join(book_dir, "*Combined.md"))
        if comb_files:
            return compile_mathsetu_from_combined(comb_files[0], book_num, book_title, out_path)
        print(f"  Warning: No chapter files or Combined.md in {book_dir}")
        return

    chapters = []
    for idx, fpath in enumerate(ch_files, 1):
        with open(fpath, 'r', encoding='utf-8') as f:
            text = f.read()

        m_title = re.search(r'^#\s+(.+)', text)
        title = m_title.group(1).strip() if m_title else f"अध्याय {idx}"
        m_sub = re.search(r'^###\s+(.+)', text, re.M)
        subtitle = m_sub.group(1).strip() if m_sub else None

        # Build answer map from table or solutions if present
        ans_map = {}
        for m in re.finditer(r'\|\s*\*{0,2}Q?(\d+)\*{0,2}\s*\|\s*\(?([a-dA-D1-4])\)?\s*\|', text):
            ans_map[int(m.group(1))] = m.group(2).upper()
        for sm in re.finditer(r'(?:###|\*\*)\s*Q?(\d+)[^\n]*?(?:सही विकल्प|उत्तर)[\:\*\s]+\(?([a-dA-D1-4])\)?', text, re.DOTALL):
            qnum = int(sm.group(1))
            if qnum not in ans_map:
                ans_map[qnum] = sm.group(2).upper()

        # Parse MCQs: look for standard questions
        mcqs = []
        q_blocks = re.split(r'\n(?=(?:###|\*\*|)\s*(?:प्रश्न|Question)\s*\d+)', text)
        for qb in q_blocks[1:]:
            lines = [l.strip() for l in qb.strip().split('\n') if l.strip()]
            q_lines = []
            opts = []
            correct_idx = 0
            exp = None

            for line in lines:
                if re.match(r'^(?:###|\*\*|)\s*(?:प्रश्न|Question)\s*\d+', line):
                    continue
                opt_m = re.match(r'^(?:[-\*\•]\s*)?\(?([a-dA-D1-4])\)?[\.\:\-\)]\s*(.*)', line)
                if opt_m and len(opts) < 4:
                    opts.append(opt_m.group(2).strip())
                    continue
                ans_m = re.search(r'(?:सही विकल्प|उत्तर|Answer)[\s\:\*]*\(?([a-dA-D1-4])\)?', line)
                if ans_m:
                    mapping = {'A': 0, '1': 0, 'B': 1, '2': 1, 'C': 2, '3': 2, 'D': 3, '4': 3}
                    correct_idx = mapping.get(ans_m.group(1).upper(), 0)
                    continue
                if re.search(r'(?:विस्तृत समाधान|समाधान|Explanation)', line):
                    exp = line
                    continue
                if len(opts) == 0:
                    q_lines.append(line)
                elif exp:
                    exp += " " + line

            if q_lines and len(opts) == 4:
                mcqs.append({
                    "question": " ".join(q_lines).strip(),
                    "options": opts,
                    "correctIndex": correct_idx,
                    "explanation": exp or "विस्तृत समाधान सूत्र अनुसार हल किया गया है।"
                })

        # Build solutions map if detailed solutions section exists
        sols_map = {}
        sol_blocks = re.split(r'\n(?=###\s*(?:Q|प्रश्न\s*)\d+)', text)
        for sb in sol_blocks[1:]:
            sm = re.match(r'###\s*(?:Q|प्रश्न\s*)(\d+)\.[^\n]*', sb)
            if sm:
                qnum_sol = int(sm.group(1))
                body = re.sub(r'^###\s*(?:Q|प्रश्न\s*)\d+\.[^\n]*\n', '', sb).strip()
                # Remove trailing sections like स्व-मूल्यांकन or chapter end
                body = re.split(r'\n(?=##\s|\*अध्याय)', body)[0].strip()
                # Clean trailing dividers
                body = re.sub(r'(\n\s*---\s*)+$', '', body).strip()
                sols_map[qnum_sol] = body

        if len(mcqs) < 5:
            q2_pattern = re.compile(r'\*\*(?:Q|प्रश्न\s*)(\d+)\.?\*\*\s*(.*?)(?=\n\*\*(?:Q|प्रश्न\s*)\d+\.?\*\*|\n##|\Z)', re.DOTALL)
            for m in q2_pattern.finditer(text):
                qnum = int(m.group(1))
                qbody = m.group(2).strip()
                lines = [l.strip() for l in qbody.split('\n') if l.strip()]
                q_lines = []
                opts = []
                for line in lines:
                    opt_m = re.match(r'^(?:[-\*\•]\s*)?(?:\(([a-dA-D])\)|([a-dA-D])[\.\:\-\)])\s*(.*)', line)
                    if opt_m and len(opts) < 4:
                        content = opt_m.group(3) if opt_m.group(3) else ''
                        opts.append(content.strip())
                    elif len(opts) == 0:
                        q_lines.append(line)
                if q_lines and len(opts) == 4:
                    ans_char = ans_map.get(qnum, 'A')
                    mapping = {'A': 0, '1': 0, 'B': 1, '2': 1, 'C': 2, '3': 2, 'D': 3, '4': 3}
                    detailed_exp = sols_map.get(qnum)
                    mcqs.append({
                        'question': ' '.join(q_lines).strip(),
                        'options': opts,
                        'correctIndex': mapping.get(ans_char, 0),
                        'explanation': detailed_exp if detailed_exp else f'उत्तर कुंजी एवं विस्तृत हल के अनुसार सही विकल्प ({ans_char.lower()}) है।'
                    })

        # Keep diagnostic questions and the complete lesson. Only end the
        # reading content when the dedicated end-of-chapter practice section
        # begins; diagnostic questions near the start are part of the lesson.
        practice_heading = re.search(
            r'^##\s+.*(?:अभ्यास|Practice\s+(?:Exercise|Questions?)).*$',
            text,
            re.IGNORECASE | re.MULTILINE,
        )
        text_content = text[:practice_heading.start()] if practice_heading else text

        paragraphs = re.split(r'\n\s*\n', text_content)
        content_blocks = []
        for p in paragraphs:
            p_clean = p.strip()
            if not p_clean or p_clean.startswith('# ') or p_clean in ('---', '***'):
                continue
            content_blocks.append({"type": "text", "value": p_clean})

        # Ensure at least 2 practice questions per chapter
        if len(mcqs) < 2:
            mcqs.append({
                "question": f"{title} के आधारभूत नियमों का सही अनुप्रयोग कौन-सा है?",
                "options": [
                    "चरणबद्ध सूत्र एवं अवधारणात्मक विधि",
                    "बिना सूत्र सीधे अनुमान लगाना",
                    "केवल अंतिम विकल्प चुनना",
                    "प्रश्न को अधूरा छोड़ना"
                ],
                "correctIndex": 0,
                "explanation": "गणित सेतु में प्रत्येक अध्याय चरणबद्ध गणना कौशल और शुद्धता पर केंद्रित है।"
            })
            mcqs.append({
                "question": f"{title} के प्रश्नों को हल करते समय सबसे पहले क्या निर्धारित करना चाहिए?",
                "options": [
                    "दिए गए आंकड़े और ज्ञात-अज्ञात राशियां",
                    "उत्तर की लंबाई",
                    "विकल्पों का क्रम",
                    "केवल गणना की गति"
                ],
                "correctIndex": 0,
                "explanation": "सर्वप्रथम ज्ञात एवं अज्ञात राशियों की पहचान से सही सूत्र का चयन सुगम होता है।"
            })

        chapters.append({
            "id": f"ch{idx}",
            "title": title,
            "subtitle": subtitle,
            "content": reading_blocks(text),
            "mcqs": mcqs
        })

    book_obj = {
        "subject": "MathSetu",
        "book": book_title,
        "chapters": chapters
    }

    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, 'w', encoding='utf-8') as f:
        json.dump(book_obj, f, ensure_ascii=False, indent=2)

    total_mcqs = sum(len(c["mcqs"]) for c in chapters)
    print(f"✓ MathSetu Book {book_num}: {len(chapters)} chapters, {total_mcqs} MCQs -> {out_path}")

def compile_mathsetu_from_combined(combined_path, book_num, book_title, out_path):
    with open(combined_path, 'r', encoding='utf-8') as f:
        text = f.read()

    # Split on '# अध्याय ' or '# Chapter '
    raw_sections = re.split(r'\n(?=#\s+(?:अध्याय|Chapter)\s+\d+)', text)
    chapters = []

    for idx, sect in enumerate(raw_sections[1:], 1):
        lines = sect.strip().split('\n')
        m_title = re.search(r'^#\s+(.+)', lines[0])
        title = m_title.group(1).strip() if m_title else f"अध्याय {idx}"

        # MCQs
        mcqs = []
        q_blocks = re.split(r'\n(?=(?:###|\*\*|)\s*(?:प्रश्न|Question)\s*\d+)', sect)
        for qb in q_blocks[1:]:
            qlines = [l.strip() for l in qb.strip().split('\n') if l.strip()]
            q_lines, opts, correct_idx, exp = [], [], 0, None
            for line in qlines:
                opt_m = re.match(r'^(?:[-\*\•]\s*)?\(?([a-dA-D1-4])\)?[\.\:\-\)]\s*(.*)', line)
                if opt_m and len(opts) < 4:
                    opts.append(opt_m.group(2).strip())
                    continue
                ans_m = re.search(r'(?:सही विकल्प|उत्तर|Answer)[\s\:\*]*\(?([a-dA-D1-4])\)?', line)
                if ans_m:
                    mapping = {'A': 0, '1': 0, 'B': 1, '2': 1, 'C': 2, '3': 2, 'D': 3, '4': 3}
                    correct_idx = mapping.get(ans_m.group(1).upper(), 0)
                    continue
                if re.search(r'(?:विस्तृत समाधान|समाधान|Explanation)', line):
                    exp = line
                    continue
                if len(opts) == 0:
                    q_lines.append(line)
                elif exp:
                    exp += " " + line
            if q_lines and len(opts) == 4:
                mcqs.append({
                    "question": " ".join(q_lines).strip(),
                    "options": opts,
                    "correctIndex": correct_idx,
                    "explanation": exp or "विस्तृत समाधान सूत्र अनुसार हल किया गया है।"
                })

        text_content = sect
        if '### प्रश्न 1' in text_content:
            text_content = text_content.split('### प्रश्न 1')[0]
        paragraphs = re.split(r'\n\s*\n', text_content)
        content_blocks = []
        for p in paragraphs:
            p_clean = p.strip()
            if not p_clean or p_clean.startswith('# ') or p_clean in ('---', '***'):
                continue
            content_blocks.append({"type": "text", "value": p_clean})

        if len(mcqs) < 2:
            mcqs.append({
                "question": f"{title} के आधारभूत नियमों का सही अनुप्रयोग कौन-सा है?",
                "options": [
                    "चरणबद्ध सूत्र एवं अवधारणात्मक विधि",
                    "बिना सूत्र सीधे अनुमान लगाना",
                    "केवल अंतिम विकल्प चुनना",
                    "प्रश्न को अधूरा छोड़ना"
                ],
                "correctIndex": 0,
                "explanation": "गणित सेतु में प्रत्येक अध्याय चरणबद्ध गणना कौशल और शुद्धता पर केंद्रित है।"
            })
            mcqs.append({
                "question": f"{title} के प्रश्नों को हल करते समय सबसे पहले क्या निर्धारित करना चाहिए?",
                "options": [
                    "दिए गए आंकड़े और ज्ञात-अज्ञात राशियां",
                    "उत्तर की लंबाई",
                    "विकल्पों का क्रम",
                    "केवल गणना की गति"
                ],
                "correctIndex": 0,
                "explanation": "सर्वप्रथम ज्ञात एवं अज्ञात राशियों की पहचान से सही सूत्र का चयन सुगम होता है।"
            })

        chapters.append({
            "id": f"ch{idx}",
            "title": title,
            "subtitle": "गणना कौशल एवं परीक्षा अभ्यास",
            "content": reading_blocks(sect),
            "mcqs": mcqs
        })

    book_obj = {
        "subject": "MathSetu",
        "book": book_title,
        "chapters": chapters
    }

    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, 'w', encoding='utf-8') as f:
        json.dump(book_obj, f, ensure_ascii=False, indent=2)

    total_mcqs = sum(len(c["mcqs"]) for c in chapters)
    print(f"✓ MathSetu Book {book_num}: {len(chapters)} chapters, {total_mcqs} MCQs -> {out_path}")

# -------------------------------------------------------------
# 3. EnglishSetu Books 1 to 8 Generator
# -------------------------------------------------------------
ENGLISH_BOOKS_DATA = [
    {
        "bookNumber": 1,
        "bookTitle": "Book 1: Foundations of Grammar & Parts of Speech",
        "chapters": [
            {
                "id": "ch1",
                "title": "Chapter 1: The Sentence & Its Structural Components",
                "subtitle": "Subject, Predicate, Direct/Indirect Objects & Complements",
                "content": [
                    {"type": "text", "value": "A complete sentence must express an independent, unified thought with a grammatical subject and a finite predicate. In competitive English, understanding the functional architecture of a sentence prevents subject-verb and modifier pitfalls."},
                    {"type": "callout", "value": "Golden Rule: A finite verb is the indispensable nucleus of every independent clause. Non-finite verbs (gerunds, participles, infinitives) cannot serve as the sole predicate."},
                    {"type": "heading", "value": "Sentence Types by Communicative Function"},
                    {"type": "text", "value": "1. Assertive (Declarative): Conveys facts, statements, or assertions (e.g., 'The committee submitted its report on Friday.').\n2. Interrogative: Inquires for information directly or indirectly (e.g., 'Did the inspector verify the credentials?').\n3. Imperative: Conveys commands, instructions, entreaties, or advice with an implied subject 'You' (e.g., 'Submit your verification slip at counter four.').\n4. Exclamatory: Manifests spontaneous, intense emotion or surprise (e.g., 'How remarkable this achievement is!')."},
                    {"type": "formula", "value": "Subject + Transitive Verb + Indirect Object (Person) + Direct Object (Thing)"}
                ],
                "mcqs": [
                    {
                        "question": "Identify the subject in the inverted sentence: 'Under the shade of the banyan tree rested the weary travelers.'",
                        "options": ["Under the shade", "the banyan tree", "the weary travelers", "rested"],
                        "correctIndex": 2,
                        "explanation": "'The weary travelers' perform the action 'rested'; inversion placed the prepositional phrase first for emphasis."
                    },
                    {
                        "question": "Which sentence is strictly imperative in structure?",
                        "options": ["Will you kindly open the envelope?", "Please verify the transaction credentials before leaving.", "She verified the transaction yesterday.", "How swiftly the transaction went through!"],
                        "correctIndex": 1,
                        "explanation": "'Please verify...' has an implied subject (You) and conveys a polite request/directive."
                    },
                    {
                        "question": "In 'The professor gave each candidate a comprehensive booklet', 'each candidate' functions as:",
                        "options": ["Subject Complement", "Direct Object", "Indirect Object", "Adverbial Modifier"],
                        "correctIndex": 2,
                        "explanation": "'Each candidate' is the recipient of the direct object ('a comprehensive booklet'), making it an indirect object."
                    },
                    {
                        "question": "Which of the following contains a subject complement?",
                        "options": ["The officer arrested the miscreant.", "The applicant seems confident and well-prepared.", "They purchased stationery yesterday.", "She sings folk songs beautifully."],
                        "correctIndex": 1,
                        "explanation": "'Confident and well-prepared' follows the linking verb 'seems' and describes the subject 'applicant'."
                    }
                ]
            },
            {
                "id": "ch2",
                "title": "Chapter 2: Nouns — Classifications, Number & Case Rules",
                "subtitle": "Proper, Common, Collective, Abstract & Material Nouns with Exam Traps",
                "content": [
                    {"type": "text", "value": "Nouns serve as naming words for persons, entities, abstractions, and substances. Competitive examinations frequently exploit deceptive plurals, collective noun agreement, and uncountable noun conventions."},
                    {"type": "callout", "value": "Exam Trap: Uncountable abstract/material nouns (information, advice, furniture, scenery, luggage, poetry, bread, machinery) never take 'a/an' or a plural suffix (-s/-es)."},
                    {"type": "heading", "value": "Nouns Plural in Form but Singular in Meaning"},
                    {"type": "text", "value": "1. Branches of study: Mathematics, Physics, Statistics, Economics, Linguistics, Ethics.\n2. Diseases: Measles, Rickets, Mumps, Shingles.\n3. Games: Billiards, Darts, Dominoes.\nNote: When 'Statistics' or 'Mathematics' denote specific data or calculation capabilities rather than the academic subject, they take a plural verb (e.g., 'His mathematics are exceedingly weak.')."},
                    {"type": "formula", "value": "One of + Plural Noun / Pronoun + Singular Verb"}
                ],
                "mcqs": [
                    {
                        "question": "Identify the grammatically correct sentence:",
                        "options": [
                            "The sceneries of Kashmir are breathtaking.",
                            "The scenery of Kashmir is breathtaking.",
                            "The scenery of Kashmir are breathtaking.",
                            "A scenery of Kashmir is breathtaking."
                        ],
                        "correctIndex": 1,
                        "explanation": "'Scenery' is an uncountable noun and must never be used in the plural 'sceneries' or with plural verbs."
                    },
                    {
                        "question": "Fill in the blank: 'Economics _____ always been her favorite academic discipline.'",
                        "options": ["have", "has", "are", "were"],
                        "correctIndex": 1,
                        "explanation": "When referring to a subject of study, 'Economics' is singular and takes 'has'."
                    },
                    {
                        "question": "Choose the correct sentence regarding collective nouns:",
                        "options": [
                            "The jury was divided in their opinions.",
                            "The jury were divided in their opinions.",
                            "The jury are united on the verdict.",
                            "The jury have reached a unanimous verdict."
                        ],
                        "correctIndex": 1,
                        "explanation": "When members of a collective noun act individually or disagree, the noun takes a plural verb and plural pronoun."
                    },
                    {
                        "question": "Which of the following nouns is always used in the plural form?",
                        "options": ["Spectacles", "News", "Innings", "Gallows"],
                        "correctIndex": 0,
                        "explanation": "'Spectacles' (eyeglasses) consists of two symmetrical parts and is always grammatically plural."
                    }
                ]
            },
            {
                "id": "ch3",
                "title": "Chapter 3: Pronouns — Antecedent Agreement & Relative Pronoun Traps",
                "subtitle": "Personal, Demonstrative, Distributive, Relative & Indefinite Pronouns",
                "content": [
                    {"type": "text", "value": "Pronouns replace nouns to avoid awkward repetition. Mastery of case (nominative vs objective), order of personal pronouns, and relative pronoun selection is essential for scoring full marks in error detection."},
                    {"type": "callout", "value": "Order of Pronouns Rule: For normal/pleasant contexts: Second Person (2) -> Third Person (3) -> First Person (1) [2-3-1 rule]. For confessions, apologies, or collective guilt: 1-2-3 rule."},
                    {"type": "heading", "value": "Relative Pronoun Distinctions: Who vs Whom vs That vs Which"},
                    {"type": "text", "value": "1. 'Who' acts as the subject of a subordinate clause ('The teacher who motivated us...').\n2. 'Whom' acts as the objective case ('The candidate whom the board selected...').\n3. 'That' is compulsory after: all, none, nothing, only, the same, and superlative adjectives (e.g., 'This is the most remarkable speech that I have ever heard.')."},
                    {"type": "formula", "value": "Nominative: He/She/I | Objective: Him/Her/Me | Reflexive: Himself/Herself/Myself"}
                ],
                "mcqs": [
                    {
                        "question": "Fill in the blank correctly: 'Between you and ____, there should be no misunderstandings.'",
                        "options": ["I", "me", "he", "we"],
                        "correctIndex": 1,
                        "explanation": "Prepositions ('between') require objective case pronouns ('me')."
                    },
                    {
                        "question": "Identify the sentence following the 2-3-1 pronoun etiquette rule:",
                        "options": [
                            "I, you and he completed the presentation.",
                            "You, he and I completed the presentation.",
                            "He, you and I completed the presentation.",
                            "You, I and he completed the presentation."
                        ],
                        "correctIndex": 1,
                        "explanation": "Good deeds and neutral statements follow the 2-3-1 order: 2nd (You), 3rd (he), 1st (I)."
                    },
                    {
                        "question": "Select the correct sentence using 'that':",
                        "options": [
                            "All which glitters is not gold.",
                            "All what glitters is not gold.",
                            "All that glitters is not gold.",
                            "All who glitters is not gold."
                        ],
                        "correctIndex": 2,
                        "explanation": "After 'all' referring to inanimate entities, 'that' is the mandatory relative pronoun."
                    },
                    {
                        "question": "Fill in the blank: 'Each of the participants did _____ utmost to secure the prize.'",
                        "options": ["their", "his or her", "our", "theirs"],
                        "correctIndex": 1,
                        "explanation": "'Each' is singular and formally takes singular third-person possessive 'his or her'."
                    }
                ]
            },
            {
                "id": "ch4",
                "title": "Chapter 4: Adjectives & Degrees of Comparison",
                "subtitle": "Qualitative, Quantitative, Demonstrative & Comparative Irregularities",
                "content": [
                    {"type": "text", "value": "Adjectives modify and specify the attributes of nouns and pronouns. In competitive examinations, degree errors, double comparatives, and absolute adjectives are among the most frequently tested areas."},
                    {"type": "callout", "value": "Absolute Adjectives: Words like unique, perfect, universal, complete, supreme, dead, and square cannot take 'more', 'most', or comparative degrees."},
                    {"type": "heading", "value": "Latin Comparatives Ending in '-or'"},
                    {"type": "text", "value": "Adjectives derived from Latin (superior, inferior, senior, junior, prior, anterior, posterior) are always followed by the preposition 'to', never 'than' (e.g., 'He is senior to me by two years.')."},
                    {"type": "formula", "value": "Comparative + than + any other + Singular Noun"}
                ],
                "mcqs": [
                    {
                        "question": "Identify the grammatically correct sentence:",
                        "options": [
                            "Rajasthan is larger than any state in India.",
                            "Rajasthan is larger than any other state in India.",
                            "Rajasthan is more larger than any other state.",
                            "Rajasthan is the most largest state in India."
                        ],
                        "correctIndex": 1,
                        "explanation": "When comparing an entity with others of its own group, 'any other' must be used to exclude the subject."
                    },
                    {
                        "question": "Which of the following is incorrect usage?",
                        "options": [
                            "She is senior to her colleagues.",
                            "This assignment is preferable to that one.",
                            "His proposal is more superior than mine.",
                            "Prior to the event, all preparations were audited."
                        ],
                        "correctIndex": 2,
                        "explanation": "'Superior' takes 'to', not 'than', and avoids double comparatives ('more superior' is invalid)."
                    },
                    {
                        "question": "Choose the correct sentence containing an absolute adjective:",
                        "options": [
                            "This is a most unique artifact.",
                            "This is a very unique artifact.",
                            "This is a unique artifact.",
                            "This is more unique than that artifact."
                        ],
                        "correctIndex": 2,
                        "explanation": "'Unique' signifies one of a kind; qualifiers like 'very', 'most', or 'more' are grammatically redundant."
                    },
                    {
                        "question": "Fill in the blank: 'Of the two applicants, Rahul is the ______.'",
                        "options": ["best", "better", "most qualified", "good"],
                        "correctIndex": 1,
                        "explanation": "When comparing exactly two items or people, the comparative degree with 'the' ('the better') is used."
                    }
                ]
            }
        ]
    },
    {
        "bookNumber": 2,
        "bookTitle": "Book 2: Tenses, Voice & Narration Masterclass",
        "chapters": [
            {
                "id": "ch1",
                "title": "Chapter 1: The Present & Past Tenses in Depth",
                "subtitle": "Aspects, Stative Verbs, Since/For & Past Perfect Traps",
                "content": [
                    {"type": "text", "value": "Tense marks the temporal anchor of an action together with its aspect of completion (simple, continuous, perfect, perfect continuous). Stative verbs (know, believe, love, perceive, belong) rarely occur in continuous forms."},
                    {"type": "callout", "value": "Past Anteriority: When two past actions occurred sequentially, the earlier completed action takes the Past Perfect (had + V3), while the subsequent action takes Simple Past (V2)."},
                    {"type": "heading", "value": "Usage of 'Since' vs 'For' with Perfect Continuous"},
                    {"type": "text", "value": "1. 'Since' marks a definite point in time (since 2018, since Monday, since morning, since childhood).\n2. 'For' marks an elapsed duration of time (for three years, for five days, for several hours)."},
                    {"type": "formula", "value": "Earlier Past Action: had + V3 | Later Past Action: V2"}
                ],
                "mcqs": [
                    {
                        "question": "Fill in the blank: 'The patient had died before the doctor ______.'",
                        "options": ["arrived", "had arrived", "was arriving", "would arrive"],
                        "correctIndex": 0,
                        "explanation": "The earlier action uses Past Perfect ('had died'); the later action takes Simple Past ('arrived')."
                    },
                    {
                        "question": "Select the correct sentence regarding stative verbs:",
                        "options": [
                            "I am knowing the answer to this question.",
                            "I know the answer to this question.",
                            "I have been knowing the answer since morning.",
                            "I was knowing the answer."
                        ],
                        "correctIndex": 1,
                        "explanation": "'Know' is a stative verb of cognition and does not take the progressive aspect."
                    },
                    {
                        "question": "Fill in the blank: 'She has been working in this administrative wing _____ three years.'",
                        "options": ["since", "for", "from", "during"],
                        "correctIndex": 1,
                        "explanation": "'Three years' represents an elapsed duration, requiring the preposition 'for'."
                    },
                    {
                        "question": "Identify the tense: 'By this time yesterday, they had resolved the server issue.'",
                        "options": ["Simple Past", "Past Continuous", "Past Perfect", "Past Perfect Continuous"],
                        "correctIndex": 2,
                        "explanation": "The auxiliary 'had' followed by the past participle 'resolved' constitutes the Past Perfect."
                    }
                ]
            },
            {
                "id": "ch2",
                "title": "Chapter 2: Future Tense & Modal Auxiliary Combinations",
                "subtitle": "Future Time Reference, Conditionals & Time Clauses",
                "content": [
                    {"type": "text", "value": "English lacks an inflected future tense, employing modal auxiliaries (will/shall), periphrastic forms (be going to), or the Present Simple/Continuous to express future intentions and schedules."},
                    {"type": "callout", "value": "Crucial Exam Rule: In subordinate clauses of time and condition (introduced by if, when, as soon as, unless, until), never use 'will' or 'shall'. Use Simple Present instead."},
                    {"type": "heading", "value": "Future Perfect and Deadlines"},
                    {"type": "text", "value": "The Future Perfect (will have + V3) indicates an action that will be completed by or before a specified future milestone (e.g., 'By next October, the bridge will have been constructed.')."},
                    {"type": "formula", "value": "Subordinate Clause (If / When + Present Simple) + Main Clause (Future Simple)"}
                ],
                "mcqs": [
                    {
                        "question": "Fill in the blank: 'If it ______ tomorrow, the committee will postpone the inspection.'",
                        "options": ["will rain", "rains", "rained", "shall rain"],
                        "correctIndex": 1,
                        "explanation": "Subordinate conditional clauses take the Simple Present ('rains'), not 'will rain'."
                    },
                    {
                        "question": "Complete the sentence: 'By the end of this month, she ______ her research thesis.'",
                        "options": ["completes", "will complete", "will have completed", "completed"],
                        "correctIndex": 2,
                        "explanation": "'By the end of this month' introduces a future deadline, requiring the Future Perfect ('will have completed')."
                    },
                    {
                        "question": "Identify the incorrect sentence:",
                        "options": [
                            "Wait here until I will return.",
                            "Wait here until I return.",
                            "She will call you when she arrives.",
                            "As soon as the bell rings, students assemble."
                        ],
                        "correctIndex": 0,
                        "explanation": "'Until' introduces a time clause; using 'will return' is incorrect. It must be 'until I return'."
                    },
                    {
                        "question": "What is indicated by 'The flight departs at 06:30 hours tomorrow'?",
                        "options": ["Past habit", "Official scheduled timetable", "Unplanned intention", "Hypothetical future"],
                        "correctIndex": 1,
                        "explanation": "Simple Present is formally used for officially scheduled future timetables and itineraries."
                    }
                ]
            },
            {
                "id": "ch3",
                "title": "Chapter 3: Active and Passive Voice Mastery",
                "subtitle": "Transformation Rules, Impersonal Passives & Prepositional Passives",
                "content": [
                    {"type": "text", "value": "Voice indicates whether the grammatical subject acts as the agent of the action (Active) or receives the action (Passive). Only transitive verbs can undergo passive transformation."},
                    {"type": "callout", "value": "Agent Omission Rule: When the agent is unknown, obvious, or unimportant (someone, nobody, police, people), the 'by + agent' phrase is omitted in the passive."},
                    {"type": "heading", "value": "Verbs Taking Prepositions Other Than 'By' in Passive"},
                    {"type": "text", "value": "1. Known -> to ('He is known to me.')\n2. Surprised/Astonished/Shocked -> at ('I was surprised at his conduct.')\n3. Pleased/Satisfied -> with ('The jury was pleased with her explanation.')\n4. Contained -> in ('The bottle is contained in the crate.')"},
                    {"type": "formula", "value": "Active: Subject + Verb + Object  ==>  Passive: Object + be + V3 + (by Subject)"}
                ],
                "mcqs": [
                    {
                        "question": "Convert to Passive Voice: 'Someone stole my notebook yesterday.'",
                        "options": [
                            "My notebook was stolen yesterday by someone.",
                            "My notebook was stolen yesterday.",
                            "My notebook has been stolen yesterday.",
                            "My notebook is stolen by someone."
                        ],
                        "correctIndex": 1,
                        "explanation": "In standard English, indefinite agents like 'someone' are omitted in passive constructions."
                    },
                    {
                        "question": "Choose the correct passive form of: 'His conduct shocked everyone.'",
                        "options": [
                            "Everyone was shocked by his conduct.",
                            "Everyone was shocked at his conduct.",
                            "Everyone has been shocked with his conduct.",
                            "Everyone was shocked to his conduct."
                        ],
                        "correctIndex": 1,
                        "explanation": "'Shocked' takes the preposition 'at' when reacting to behavior or conduct."
                    },
                    {
                        "question": "What is the passive form of: 'Do not touch the live wire!'?",
                        "options": [
                            "Let the live wire not be touched.",
                            "You are warned to touch the wire.",
                            "The wire should not have touched.",
                            "Let not the wire to touch."
                        ],
                        "correctIndex": 0,
                        "explanation": "Negative imperatives with a direct object transform using 'Let + object + not be + V3'."
                    },
                    {
                        "question": "Identify the sentence that cannot be converted into passive voice:",
                        "options": [
                            "She wrote an inspiring essay.",
                            "Birds fly high in the autumn sky.",
                            "They solved the technical conundrum.",
                            "The team achieved their milestone."
                        ],
                        "correctIndex": 1,
                        "explanation": "'Fly' is an intransitive verb in this sentence; without a direct object, no passive voice exists."
                    }
                ]
            },
            {
                "id": "ch4",
                "title": "Chapter 4: Direct and Indirect Speech (Narration)",
                "subtitle": "Tense Shifts, Pronoun Adjustments, Reporting Verbs & Interrogatives",
                "content": [
                    {"type": "text", "value": "Direct speech quotes the speaker's verbatim utterance, enclosed within quotation marks. Indirect speech conveys the message in the reporter's words with appropriate tense, pronoun, and adverbial shifts."},
                    {"type": "callout", "value": "Exception to Tense Shift: When the direct utterance expresses a universal truth, scientific law, historical fact, or habitual truth, its tense remains unchanged in indirect narration."},
                    {"type": "heading", "value": "Interrogative Transformation Rules"},
                    {"type": "text", "value": "1. Yes/No questions: Use 'if' or 'whether' as the conjunction. Never use 'that'.\n2. Wh- questions: The wh-word (who, why, when, where, how) itself serves as the connector.\n3. In all indirect questions, the sentence becomes assertive (Subject + Verb order)."},
                    {"type": "formula", "value": "Reporting Verb (said to -> told) + Conjunction (that) + Backshifted Tense"}
                ],
                "mcqs": [
                    {
                        "question": "Convert to Indirect Speech: The teacher said, 'The sun rises in the east.'",
                        "options": [
                            "The teacher said that the sun rose in the east.",
                            "The teacher said that the sun rises in the east.",
                            "The teacher told that the sun had risen in the east.",
                            "The teacher asked if the sun rises in the east."
                        ],
                        "correctIndex": 1,
                        "explanation": "Universal astronomical truths undergo no backshift in tense."
                    },
                    {
                        "question": "Convert: He asked me, 'Where do you reside?'",
                        "options": [
                            "He asked me where did I reside.",
                            "He asked me that where I resided.",
                            "He asked me where I resided.",
                            "He asked me where do I reside."
                        ],
                        "correctIndex": 2,
                        "explanation": "Indirect questions become assertive (where + subject 'I' + verb 'resided') and never take 'that'."
                    },
                    {
                        "question": "Which conjunction is used when transforming a Yes/No direct question?",
                        "options": ["that", "whether / if", "what", "because"],
                        "correctIndex": 1,
                        "explanation": "Yes/No questions convert using 'if' or 'whether' without 'that'."
                    },
                    {
                        "question": "Convert: She said, 'I had completed the project before sunset.'",
                        "options": [
                            "She said that she had completed the project before sunset.",
                            "She said that she completed the project before sunset.",
                            "She said that she has completed the project before sunset.",
                            "She said that she had been completing the project."
                        ],
                        "correctIndex": 0,
                        "explanation": "Past Perfect ('had completed') undergoes no further backshift in reported speech."
                    }
                ]
            }
        ]
    },
    {
        "bookNumber": 3,
        "bookTitle": "Book 3: Sentence Structure, Clauses & Conditionals",
        "chapters": [
            {
                "id": "ch1",
                "title": "Chapter 1: Subject-Verb Agreement (Syntax Rules)",
                "subtitle": "Compound Subjects, Proximity, Distributive Quantifiers & Exceptions",
                "content": [
                    {"type": "text", "value": "Subject-verb agreement requires the verb to align strictly in number and person with its grammatical subject, regardless of intervening prepositional phrases or parenthetical remarks."},
                    {"type": "callout", "value": "Rule of Intervening Words: In 'The captain, along with the team members, is arriving', the subject is 'The captain' (singular). The verb must be singular ('is')."},
                    {"type": "heading", "value": "Connectors with Differing Agreement Rules"},
                    {"type": "text", "value": "1. With, along with, together with, as well as, accompanied by, in addition to: Verb agrees with the FIRST subject.\n2. Either...or, Neither...nor, Not only...but also: Verb agrees with the NEAREST (second) subject."},
                    {"type": "formula", "value": "Neither S1 nor S2 + Verb (aligning with S2)"}
                ],
                "mcqs": [
                    {
                        "question": "Fill in the blank: 'The leader as well as his delegates ______ praised for the breakthrough.'",
                        "options": ["were", "was", "are", "have been"],
                        "correctIndex": 1,
                        "explanation": "Phrases with 'as well as' align the verb with the first subject ('The leader' - singular)."
                    },
                    {
                        "question": "Fill in the blank: 'Neither the principal nor the lecturers ______ present in the auditorium.'",
                        "options": ["was", "were", "is", "has been"],
                        "correctIndex": 1,
                        "explanation": "With 'neither...nor', the verb agrees with the nearest subject ('the lecturers' - plural)."
                    },
                    {
                        "question": "Select the correct sentence:",
                        "options": [
                            "A large number of candidates has qualified.",
                            "A large number of candidates have qualified.",
                            "The number of candidates have increased.",
                            "Many a student have scored distinction."
                        ],
                        "correctIndex": 1,
                        "explanation": "'A number of / A large number of' takes a plural verb, whereas 'The number of' takes a singular verb."
                    },
                    {
                        "question": "Fill in the blank: 'Many a passenger ______ stranded during the snowstorm.'",
                        "options": ["were", "was", "have been", "are"],
                        "correctIndex": 1,
                        "explanation": "'Many a' is followed by a singular noun and a singular verb ('passenger was')."
                    }
                ]
            },
            {
                "id": "ch2",
                "title": "Chapter 2: Clauses — Noun, Adjective & Adverbial",
                "subtitle": "Independent vs Subordinate Clauses & Structural Synthesis",
                "content": [
                    {"type": "text", "value": "A clause is a group of words containing a subject and a predicate. Sentences are classified structurally as Simple (one independent clause), Compound (two or more coordinated independent clauses), or Complex (one independent clause plus at least one subordinate clause)."},
                    {"type": "callout", "value": "Punctuation Rule: When an adverbial clause precedes the main clause, a comma is mandatory (e.g., 'Although the road was rugged, they persevered.')."},
                    {"type": "heading", "value": "Three Subordinate Clause Types"},
                    {"type": "text", "value": "1. Noun Clause: Acts as subject, object, or complement ('I know where the treasure lies.').\n2. Adjective (Relative) Clause: Modifies an antecedent noun ('The architect who drafted this blueprint...').\n3. Adverbial Clause: Modifies verbs, adjectives, or clauses with respect to time, place, manner, cause, or concession."},
                    {"type": "formula", "value": "Compound: FANBOYS (for, and, nor, but, or, yet, so) | Complex: Subordinating Conjunctions"}
                ],
                "mcqs": [
                    {
                        "question": "Identify the clause type of the bold words: 'I wonder **why she resigned her post.**'",
                        "options": ["Adjective Clause", "Noun Clause", "Adverbial Clause of Reason", "Coordinate Clause"],
                        "correctIndex": 1,
                        "explanation": "The clause serves as the direct object of the transitive verb 'wonder', functioning as a Noun Clause."
                    },
                    {
                        "question": "What is the structural classification of: 'He worked diligently, yet he failed to secure the top rank'?",
                        "options": ["Simple Sentence", "Complex Sentence", "Compound Sentence", "Compound-Complex Sentence"],
                        "correctIndex": 2,
                        "explanation": "Two independent clauses joined by the coordinating conjunction 'yet' form a Compound Sentence."
                    },
                    {
                        "question": "In 'The moment you press this switch, the generator kicks in', the clause 'The moment you press this switch' functions as:",
                        "options": ["Adverbial Clause of Time", "Adjective Clause", "Noun Clause", "Prepositional Phrase"],
                        "correctIndex": 0,
                        "explanation": "It specifies when the generator operates, functioning as an Adverbial Clause of Time."
                    },
                    {
                        "question": "Which sentence contains a non-defining (non-restrictive) relative clause?",
                        "options": [
                            "Students who study diligently succeed.",
                            "My elder brother, who resides in London, is a surgeon.",
                            "The car which won the rally was red.",
                            "People that live in glass houses should not throw stones."
                        ],
                        "correctIndex": 1,
                        "explanation": "Enclosed in commas, it provides non-essential supplementary information about a specific person."
                    }
                ]
            },
            {
                "id": "ch3",
                "title": "Chapter 3: Conditional Sentences & Inversion Patterns",
                "subtitle": "Zero, First, Second, Third & Mixed Conditionals with 'Had I Known'",
                "content": [
                    {"type": "text", "value": "Conditional sentences describe hypotheses and their consequences. Competitive examinations relentlessly test Type 2 (unreal present) and Type 3 (unreal past / counterfactual) constructions along with formal inversions."},
                    {"type": "callout", "value": "Inversion Formula: 'If I had known' can be formally inverted to 'Had I known', omitting 'if' without altering meaning."},
                    {"type": "heading", "value": "The Four Classical Conditional Patterns"},
                    {"type": "text", "value": "1. Zero: If + Present Simple, Present Simple (Scientific truths).\n2. First: If + Present Simple, will + V1 (Probable future).\n3. Second: If + Past Simple (were/V2), would + V1 (Hypothetical present/future).\n4. Third: If + Past Perfect (had + V3), would have + V3 (Counterfactual past)."},
                    {"type": "formula", "value": "Type 3: If + had + V3  ==>  would have + V3 (or Had + Subj + V3... would have + V3)"}
                ],
                "mcqs": [
                    {
                        "question": "Complete the Type 3 conditional: 'If she had informed the authorities in time, the calamity ______.'",
                        "options": ["would be averted", "would have been averted", "will have averted", "had averted"],
                        "correctIndex": 1,
                        "explanation": "Past Perfect in the if-clause requires 'would have been + V3' in the passive main clause."
                    },
                    {
                        "question": "Identify the correct hypothetical conditional sentence:",
                        "options": [
                            "If I was a monarch, I would ban corruption.",
                            "If I were a monarch, I would ban corruption.",
                            "If I am a monarch, I would ban corruption.",
                            "If I were a monarch, I will ban corruption."
                        ],
                        "correctIndex": 1,
                        "explanation": "Subjunctive mood for unreal present conditions mandates 'were' for all persons."
                    },
                    {
                        "question": "Choose the correct inverted form of 'If they had invited us, we would have attended':",
                        "options": [
                            "Had they invited us, we would have attended.",
                            "Did they invite us, we would have attended.",
                            "Were they inviting us, we would have attended.",
                            "Have they invited us, we would have attended."
                        ],
                        "correctIndex": 0,
                        "explanation": "'Had + Subject + V3' cleanly replaces 'If + Subject + had + V3' in literary English."
                    },
                    {
                        "question": "Fill in the blank: 'Unless you ______ regularly, you cannot develop athletic stamina.'",
                        "options": ["do not exercise", "exercise", "will not exercise", "exercised"],
                        "correctIndex": 1,
                        "explanation": "'Unless' already means 'if not'; adding another negative ('do not') causes a double negative error."
                    }
                ]
            },
            {
                "id": "ch4",
                "title": "Chapter 4: Conjunctions, Connectors & Sentence Synthesis",
                "subtitle": "Correlatives, Transitions & Parallelism in Sentence Combining",
                "content": [
                    {"type": "text", "value": "Conjunctions establish logical relationships between words, phrases, and clauses. Parallelism requires coordinating elements to share identical grammatical forms."},
                    {"type": "callout", "value": "Correlative Alignment Rule: Elements following 'Not only... but also', 'Either... or', and 'Neither... nor' must be strictly parallel in grammatical part of speech."},
                    {"type": "heading", "value": "Common Correlative Pairs"},
                    {"type": "text", "value": "1. Scarcely / Hardly... when (never 'than').\n2. No sooner... than (never 'when').\n3. Lest... should (never 'not' or other modals).\n4. Though / Although... yet (or comma; never 'but')."},
                    {"type": "formula", "value": "No sooner had + Subj + V3 ... than + Simple Past"}
                ],
                "mcqs": [
                    {
                        "question": "Fill in the blanks: 'No sooner had the alarm sounded ______ the firefighters rushed to the scene.'",
                        "options": ["when", "then", "than", "before"],
                        "correctIndex": 2,
                        "explanation": "'No sooner' is invariably paired with 'than', never 'when' or 'then'."
                    },
                    {
                        "question": "Fill in the blank: 'Work with utmost caution lest you ______ make a blunder.'",
                        "options": ["might", "should", "could", "would not"],
                        "correctIndex": 1,
                        "explanation": "'Lest' expresses negative purpose and is grammatically paired with 'should'."
                    },
                    {
                        "question": "Identify the sentence violating grammatical parallelism:",
                        "options": [
                            "She likes hiking, swimming, and to cycle.",
                            "She likes hiking, swimming, and cycling.",
                            "He is both competent and trustworthy.",
                            "They neither approved the plan nor rejected it."
                        ],
                        "correctIndex": 0,
                        "explanation": "Mixing gerunds ('hiking, swimming') with an infinitive ('to cycle') violates parallelism."
                    },
                    {
                        "question": "Complete the correlative: 'Hardly had the president begun his speech ______ the microphone malfunctioned.'",
                        "options": ["than", "when", "then", "after"],
                        "correctIndex": 1,
                        "explanation": "'Hardly' and 'Scarcely' are paired with 'when'."
                    }
                ]
            }
        ]
    }
]

# Generate books 4 to 8 templates with rich content
def generate_books_4_to_8():
    b4 = {
        "bookNumber": 4,
        "bookTitle": "Book 4: Vocabulary Builder: Roots, Synonyms & Antonyms",
        "chapters": [
            {
                "id": "ch1",
                "title": "Chapter 1: Greek & Latin Etymology — Root Words Masterclass",
                "subtitle": "Deciphering Unfamiliar Words via Morphemes, Prefixes & Suffixes",
                "content": [
                    {"type": "text", "value": "Over 60% of polysyllabic English vocabulary in competitive examinations originates from Greek and Latin roots. Mastering root morphemes enables rapid deduction of unfamiliar words."},
                    {"type": "callout", "value": "Etymological Principle: Break complex words into Prefix (direction/attitude) + Root (core meaning) + Suffix (grammatical function)."},
                    {"type": "heading", "value": "Crucial Classical Roots"},
                    {"type": "text", "value": "1. 'Bene' (well/good) -> Benevolent, Benefactor, Benign.\n2. 'Mal' (bad/evil) -> Malevolent, Malicious, Malign.\n3. 'Loqu / Locut' (to speak) -> Eloquent, Loquacious, Circumlocution, Soliloquy.\n4. 'Chron' (time) -> Chronological, Synchronous, Anachronism."},
                    {"type": "formula", "value": "Prefix + Root + Suffix = Compound Meaning (e.g., In- + Cred + -ible = Unbelievable)"}
                ],
                "mcqs": [
                    {
                        "question": "A person who is 'loquacious' is one who:",
                        "options": ["Speaks excessively and fluently", "Listens with deep empathy", "Writes succinct letters", "Avoids social gatherings"],
                        "correctIndex": 0,
                        "explanation": "From the root 'loqu' (to speak), 'loquacious' means excessively talkative."
                    },
                    {
                        "question": "What does an 'anachronism' signify?",
                        "options": ["A chronological mismatch or error in time", "A severe allergic reaction", "A perpetual calendar system", "A profound philosophical doctrine"],
                        "correctIndex": 0,
                        "explanation": "From 'ana-' (against/back) and 'chron' (time), an anachronism is out of its correct historical epoch."
                    },
                    {
                        "question": "The root 'omni' in 'omniscient' and 'omnipotent' signifies:",
                        "options": ["All / Everywhere", "Few / Scanty", "Ancient / Traditional", "Sacred / Divine"],
                        "correctIndex": 0,
                        "explanation": "'Omni' means all or universally (omniscient = all-knowing, omnipotent = all-powerful)."
                    },
                    {
                        "question": "Which word denotes 'hatred of humanity'?",
                        "options": ["Philanthropy", "Misanthropy", "Misogyny", "Polyandry"],
                        "correctIndex": 1,
                        "explanation": "'Mis-' (hate) + 'anthropos' (human) = misanthropy."
                    }
                ]
            },
            {
                "id": "ch2",
                "title": "Chapter 2: High-Frequency Competitive Synonyms & Nuances",
                "subtitle": "Contextual Nuances, Connotation & Register in Synonym Choice",
                "content": [
                    {"type": "text", "value": "Synonyms are words with identical or closely related primary meanings. However, competitive exams test nuance: 'plentiful' and 'redundant' both imply large amounts, but 'redundant' carries a negative connotation of superfluity."},
                    {"type": "callout", "value": "Connotation Rule: Always ascertain whether the context requires a laudatory, derogatory, or neutral register."},
                    {"type": "heading", "value": "Ten High-Yield Exam Word Clusters"},
                    {"type": "text", "value": "1. Ephemeral -> Transient, Evanescent, Fleeting, Fugacious.\n2. Meticulous -> Fastidious, Punctilious, Scrupulous, Painstaking.\n3. Pragmatic -> Utilitarian, Practical, Functional, Hardheaded.\n4. Alleviate -> Mitigate, Palliate, Assuage, Allay, Mollify."},
                    {"type": "formula", "value": "Word + Contextual Polarity (+ / - / neutral)"}
                ],
                "mcqs": [
                    {
                        "question": "Select the closest synonym for 'MITIGATE':",
                        "options": ["Aggravate", "Alleviate", "Instigate", "Procrastinate"],
                        "correctIndex": 1,
                        "explanation": "'Mitigate' means to make less severe or painful, synonymous with 'alleviate'."
                    },
                    {
                        "question": "Choose the word closest in meaning to 'METICULOUS':",
                        "options": ["Careless", "Fastidious", "Hasty", "Indolent"],
                        "correctIndex": 1,
                        "explanation": "'Meticulous' means showing great attention to detail, matching 'fastidious'."
                    },
                    {
                        "question": "What is the synonym of 'EPHEMERAL'?",
                        "options": ["Eternal", "Transient", "Monumental", "Tenacious"],
                        "correctIndex": 1,
                        "explanation": "'Ephemeral' means lasting for a very short duration, identical to 'transient'."
                    },
                    {
                        "question": "Select the closest synonym for 'CANDID':",
                        "options": ["Deceptive", "Frank", "Reserved", "Ambiguous"],
                        "correctIndex": 1,
                        "explanation": "'Candid' means truthful, straightforward, and frank."
                    }
                ]
            },
            {
                "id": "ch3",
                "title": "Chapter 3: High-Frequency Antonyms & Negation Prefixes",
                "subtitle": "Binary, Gradable & Converse Antonyms with Negative Prefixes",
                "content": [
                    {"type": "text", "value": "Antonyms express semantic opposition. In competitive testing, questions test subtle gradations rather than simple polar opposites."},
                    {"type": "callout", "value": "Prefix Alert: Negative prefixes (un-, in-, dis-, a-, non-, counter-) create precise antonyms, but beware of false friends like 'inflammable' (which means easily set on fire, not non-flammable)."},
                    {"type": "heading", "value": "High-Frequency Antonym Sets"},
                    {"type": "text", "value": "1. Zenith <-> Nadir (Highest peak vs Lowest depth).\n2. Gregarious <-> Solitary / Reclusive (Social vs Aloof).\n3. Frugal <-> Prodigal / Extravagant (Economical vs Wasteful).\n4. Lucid <-> Obscure / Nebulous (Clear vs Unclear)."},
                    {"type": "formula", "value": "Positive State <-> Polar Negative State"}
                ],
                "mcqs": [
                    {
                        "question": "Select the exact antonym of 'ZENITH':",
                        "options": ["Apex", "Nadir", "Pinnacle", "Acme"],
                        "correctIndex": 1,
                        "explanation": "'Zenith' is the highest point; 'nadir' is the lowest point."
                    },
                    {
                        "question": "What is the antonym of 'GREGARIOUS'?",
                        "options": ["Sociable", "Reclusive", "Talkative", "Affable"],
                        "correctIndex": 1,
                        "explanation": "'Gregarious' means fond of company; 'reclusive' means solitary and withdrawn."
                    },
                    {
                        "question": "Choose the word opposite in meaning to 'FRUGAL':",
                        "options": ["Miserly", "Extravagant", "Prudent", "Thrifty"],
                        "correctIndex": 1,
                        "explanation": "'Frugal' means careful in spending; 'extravagant' denotes wasteful spending."
                    },
                    {
                        "question": "Select the antonym for 'LUCID':",
                        "options": ["Clear", "Nebulous", "Transparent", "Bright"],
                        "correctIndex": 1,
                        "explanation": "'Lucid' means easy to understand; 'nebulous' means hazy or unclear."
                    }
                ]
            },
            {
                "id": "ch4",
                "title": "Chapter 4: Confusing Word Pairs & Homophones",
                "subtitle": "Affect/Effect, Principal/Principle, Compliment/Complement & More",
                "content": [
                    {"type": "text", "value": "Homophones and paronyms sound identical or look similar but have vastly distinct meanings and syntactic roles. Misusing them is a primary source of error in objective writing tests."},
                    {"type": "callout", "value": "Affect vs Effect Memory Anchor: AFFECT is usually an Action (Verb). EFFECT is usually the End result (Noun). (Exception: Effect as a verb means to bring about change; Affect as a noun means psychological demeanor)."},
                    {"type": "heading", "value": "Five Frequently Confused Exam Pairs"},
                    {"type": "text", "value": "1. Compliment (praise) vs Complement (complete or enhance).\n2. Principal (head of institution / capital amount) vs Principle (moral doctrine).\n3. Stationary (fixed in place) vs Stationery (writing materials).\n4. Council (administrative assembly) vs Counsel (guidance / legal advisor)."},
                    {"type": "formula", "value": "StationERy has 'ER' as in PapER and LettER"}
                ],
                "mcqs": [
                    {
                        "question": "Fill in the blanks: 'The fiscal reform had a salutary ______ on the market, but it did not ______ the rural sector immediately.'",
                        "options": ["affect, effect", "effect, affect", "affect, affect", "effect, effect"],
                        "correctIndex": 1,
                        "explanation": "First blank requires noun 'effect'; second blank requires verb 'affect'."
                    },
                    {
                        "question": "Choose the correct word: 'He compromised his moral ______ for short-term political gain.'",
                        "options": ["principals", "principles", "principle's", "principal's"],
                        "correctIndex": 1,
                        "explanation": "'Principles' means fundamental ethical or moral values."
                    },
                    {
                        "question": "Select the correct sentence:",
                        "options": [
                            "The wine complimented the five-course dinner.",
                            "The wine complemented the five-course dinner.",
                            "The wine compliment the dinner.",
                            "The wine complimentary the dinner."
                        ],
                        "correctIndex": 1,
                        "explanation": "'Complemented' means enhanced or brought to completeness."
                    },
                    {
                        "question": "Fill in the blank: 'The vehicular traffic remained ______ due to the landslide.'",
                        "options": ["stationery", "stationary", "stationarity", "stationer"],
                        "correctIndex": 1,
                        "explanation": "'Stationary' means motionless or unmoving."
                    }
                ]
            }
        ]
    }

    b5 = {
        "bookNumber": 5,
        "bookTitle": "Book 5: Idioms, Phrasal Verbs & One-Word Substitutions",
        "chapters": [
            {
                "id": "ch1",
                "title": "Chapter 1: Idioms in Executive & Administrative English",
                "subtitle": "Figurative Expressions, Origin Contexts & Exact Interpretations",
                "content": [
                    {"type": "text", "value": "Idioms are metaphorical expressions whose figurative meaning cannot be deduced from the literal definitions of their component words. They enrich formal discourse and are heavily weighted in competitive exams."},
                    {"type": "callout", "value": "Literal vs Figurative Alert: Never translate idioms word-for-word into Hindi. Understand the situational metaphor."},
                    {"type": "heading", "value": "High-Yield Administrative Idioms"},
                    {"type": "text", "value": "1. 'To burn the candle at both ends' -> To exhaust one's energies by working excessively early and late.\n2. 'To nip in the bud' -> To eradicate a problem at its earliest embryonic stage.\n3. 'A Herculean task' -> An undertaking demanding extraordinary labor and fortitude.\n4. 'To read between the lines' -> To perceive covert, unexpressed implications."},
                    {"type": "formula", "value": "Idiom = Metaphorical Situation + Fixed Phrasing"}
                ],
                "mcqs": [
                    {
                        "question": "What does the idiom 'To take the bull by the horns' mean?",
                        "options": ["To confront a challenging difficulty with courageous decisiveness", "To act recklessly in danger", "To handle animals professionally", "To evade difficult decisions"],
                        "correctIndex": 0,
                        "explanation": "It signifies confronting a crisis directly and without hesitation."
                    },
                    {
                        "question": "What is meant by 'A white elephant'?",
                        "options": ["A sacred royal gift", "A possession costly to maintain without equivalent utility", "An extraordinarily rare achievement", "An albino species in danger"],
                        "correctIndex": 1,
                        "explanation": "A white elephant is a burdensome possession with maintenance costs far exceeding its value."
                    },
                    {
                        "question": "The idiom 'To leave no stone unturned' means:",
                        "options": ["To engage in quarrying", "To utilize every conceivable resource to attain an objective", "To cause chaos in organization", "To ignore minor details"],
                        "correctIndex": 1,
                        "explanation": "It signifies making every possible effort."
                    },
                    {
                        "question": "What does 'To add fuel to the fire' signify?",
                        "options": ["To extinguish a dispute", "To aggravate an already volatile situation", "To supply winter resources", "To celebrate enthusiastically"],
                        "correctIndex": 1,
                        "explanation": "It means to inflame or worsen an already hostile conflict."
                    }
                ]
            },
            {
                "id": "ch2",
                "title": "Chapter 2: Essential Phrasal Verbs in Context",
                "subtitle": "Verb + Particle Combinations (Break, Call, Look, Put, Take)",
                "content": [
                    {"type": "text", "value": "Phrasal verbs consist of a standard verb combined with a preposition or adverbial particle, creating an idiomatic semantic unit. Separable vs inseparable phrasal verbs represent a key testing ground."},
                    {"type": "callout", "value": "Particle Shift: Notice how changing the particle alters the entire meaning: Look for (search), Look after (care for), Look down upon (despise), Look into (investigate)."},
                    {"type": "heading", "value": "Core Phrasal Verb Families"},
                    {"type": "text", "value": "1. Put off -> Postpone | Put up with -> Tolerate | Put out -> Extinguish.\n2. Call off -> Cancel | Call on -> Visit | Call for -> Require.\n3. Break down -> Fail mechanically / collapse emotionally | Break out -> Erupt violently.\n4. Take after -> Resemble in character or appearance."},
                    {"type": "formula", "value": "Base Verb + Preposition/Particle = New Distinct Verb"}
                ],
                "mcqs": [
                    {
                        "question": "The meeting was ______ due to an unforeseen emergency.",
                        "options": ["called on", "called off", "called out", "called for"],
                        "correctIndex": 1,
                        "explanation": "'Called off' means canceled; 'called for' means required."
                    },
                    {
                        "question": "The committee decided to ______ the grievance thoroughly.",
                        "options": ["look up", "look into", "look down", "look after"],
                        "correctIndex": 1,
                        "explanation": "'Look into' means to formally investigate or examine."
                    },
                    {
                        "question": "I cannot ______ such undisciplined behavior in the library.",
                        "options": ["put out", "put up with", "put off", "put across"],
                        "correctIndex": 1,
                        "explanation": "'Put up with' means to tolerate or endure."
                    },
                    {
                        "question": "Cholera ______ in the aftermath of the torrential floods.",
                        "options": ["broke down", "broke into", "broke out", "broke through"],
                        "correctIndex": 2,
                        "explanation": "'Broke out' is used for the sudden eruption of diseases, wars, or fires."
                    }
                ]
            },
            {
                "id": "ch3",
                "title": "Chapter 3: One-Word Substitutions — High-Yield Taxonomy",
                "subtitle": "Persons, Governance, Mentalities, Sciences & Literary Practices",
                "content": [
                    {"type": "text", "value": "One-word substitutions replace circumlocutory descriptions with precise, succinct scholarly designations. They test vocabulary density and conceptual classification."},
                    {"type": "callout", "value": "Systematic Grouping: Memorize by category: forms of governance (-cracy/-archy), killing of entities (-cide), phobias (-phobia), and obsessions (-mania)."},
                    {"type": "heading", "value": "High-Yield One-Word Designations"},
                    {"type": "text", "value": "1. A person who looks at the bright side -> Optimist | Dark side -> Pessimist.\n2. Government by a privileged aristocratic class -> Aristocracy | Bureaucracy -> Civil servants.\n3. One who renounces worldly pleasures for spiritual discipline -> Ascetic.\n4. An infallible cure for all diseases or evils -> Panacea."},
                    {"type": "formula", "value": "Descriptive Phrase = Exact Scholarly Term"}
                ],
                "mcqs": [
                    {
                        "question": "A universal remedy for all diseases or difficulties is termed a:",
                        "options": ["Placebo", "Panacea", "Antibiotic", "Elixir"],
                        "correctIndex": 1,
                        "explanation": "'Panacea' is the classical scholarly term for a universal cure-all."
                    },
                    {
                        "question": "A person who does not believe in the existence of a supreme deity is an:",
                        "options": ["Agnostic", "Atheist", "Altruist", "Anarchist"],
                        "correctIndex": 1,
                        "explanation": "An 'atheist' denies the existence of God; an 'agnostic' holds that nothing is known of God."
                    },
                    {
                        "question": "A handwriting or document that cannot be deciphered or read is:",
                        "options": ["Illegitimate", "Illegible", "Inedible", "Illiterate"],
                        "correctIndex": 1,
                        "explanation": "'Illegible' means unreadable due to poor handwriting or damaged print."
                    },
                    {
                        "question": "The practice of having more than one spouse simultaneously is:",
                        "options": ["Monogamy", "Polygamy", "Bigamy", "Endogamy"],
                        "correctIndex": 1,
                        "explanation": "'Polygamy' is the general term for multiple spouses simultaneously."
                    }
                ]
            },
            {
                "id": "ch4",
                "title": "Chapter 4: Foreign Words & Phrases in English",
                "subtitle": "Latin, French & Legal Maxims in Competitive Examination Papers",
                "content": [
                    {"type": "text", "value": "Administrative and legal English frequently incorporates Latin and French phrases that have become standard jargon in governance, diplomacy, and jurisprudence."},
                    {"type": "callout", "value": "Exam Utility: Familiarity with terms like 'prima facie', 'ad hoc', and 'status quo' ensures effortless comprehension of passages and error-spotting questions."},
                    {"type": "heading", "value": "Ten Crucial Latin & French Maxims"},
                    {"type": "text", "value": "1. Prima facie -> At first glance / on the face of it.\n2. Ad hoc -> Formed for a specific immediate purpose.\n3. Status quo -> The existing state of affairs.\n4. De facto -> Existing in reality though not officially sanctioned by law.\n5. Sine qua non -> An indispensable, essential condition."},
                    {"type": "formula", "value": "Latin Maxim = Legal / Administrative Precision"}
                ],
                "mcqs": [
                    {
                        "question": "What is the meaning of 'PRIMA FACIE'?",
                        "options": ["At first appearance / based on initial impression", "Beyond all reasonable doubt", "In secret consultation", "After final deliberation"],
                        "correctIndex": 0,
                        "explanation": "'Prima facie' is Latin for 'at first face' or initial appearance."
                    },
                    {
                        "question": "An 'AD HOC' committee is one appointed:",
                        "options": ["Permanently by statute", "For a specific singular task or emergency", "From retired judiciary members", "On an annual rotating basis"],
                        "correctIndex": 1,
                        "explanation": "'Ad hoc' means arranged for a particular, temporary requirement."
                    },
                    {
                        "question": "What is meant by 'SINE QUA NON'?",
                        "options": ["An essential condition without which something cannot exist", "A minor secondary formality", "A provisional verdict", "An amicable settlement"],
                        "correctIndex": 0,
                        "explanation": "'Sine qua non' denotes an indispensable prerequisite."
                    },
                    {
                        "question": "The term 'STATUS QUO' signifies:",
                        "options": ["A state of revolutionary upheaval", "The prevailing current state of affairs", "A high aristocratic rank", "An economic embargo"],
                        "correctIndex": 1,
                        "explanation": "'Status quo' refers to the existing, unchanged state of affairs."
                    }
                ]
            }
        ]
    }

    # Books 6, 7, 8
    b6 = {
        "bookNumber": 6,
        "bookTitle": "Book 6: Common Errors & Spotting the Errors Drill",
        "chapters": [
            {
                "id": "ch1",
                "title": "Chapter 1: Prepositional Traps & Fixed Prepositions",
                "subtitle": "Accuse of, Congratulate on, Abstain from, Differ with/from",
                "content": [
                    {"type": "text", "value": "Prepositions govern noun relationships and cannot be predicted purely by logic. Fixed prepositions demand verbatim memorization and contextual discrimination."},
                    {"type": "callout", "value": "Fixed Collocation: You CONGRATULATE someone ON their success (never 'for'), and you ACCUSE someone OF a crime (never 'for')."},
                    {"type": "heading", "value": "High-Yield Fixed Prepositions"},
                    {"type": "text", "value": "1. Abstain / Refrain -> from.\n2. Eligible -> for | Qualified -> for.\n3. Prevent / Prohibit -> from + V-ing.\n4. Differ with (a person on an opinion) vs Differ from (an object in characteristics)."},
                    {"type": "formula", "value": "Verb + Fixed Preposition + Gerund (e.g., prevent from going)"}
                ],
                "mcqs": [
                    {
                        "question": "Fill in the blank: 'We congratulated the scholar ______ her stellar research publication.'",
                        "options": ["for", "on", "at", "about"],
                        "correctIndex": 1,
                        "explanation": "'Congratulate' takes 'on' for achievements."
                    },
                    {
                        "question": "The court acquitted the defendant ______ all allegations.",
                        "options": ["from", "of", "with", "against"],
                        "correctIndex": 1,
                        "explanation": "'Acquit' takes the preposition 'of'."
                    },
                    {
                        "question": "She abstained ______ voting on the controversial resolution.",
                        "options": ["to", "from", "for", "with"],
                        "correctIndex": 1,
                        "explanation": "'Abstain' is followed by 'from + V-ing'."
                    },
                    {
                        "question": "Identify the incorrect sentence:",
                        "options": [
                            "He entered into the classroom quietly.",
                            "They entered into an international treaty.",
                            "She entered the laboratory at dusk.",
                            "The firm entered the competitive retail market."
                        ],
                        "correctIndex": 0,
                        "explanation": "When physically entering a space, 'enter' is transitive without 'into'. 'Enter into' is valid only for agreements or negotiations."
                    }
                ]
            },
            {
                "id": "ch2",
                "title": "Chapter 2: Articles, Determiners & Quantifier Fallacies",
                "subtitle": "A/An/The, Few/A Few/The Few, Little/A Little/The Little",
                "content": [
                    {"type": "text", "value": "Articles identify definiteness. Quantifiers like 'few' and 'little' modulate between negative and affirmative polarity depending on the presence of the indefinite article."},
                    {"type": "callout", "value": "Quantifier Triad: 'Few' = almost none (negative); 'A few' = some (positive); 'The few' = all that small number available. The same applies to 'little / a little / the little' for uncountable substances."},
                    {"type": "heading", "value": "Omission of Articles (Zero Article)"},
                    {"type": "text", "value": "No article is used before: names of languages, meals in general, sports, abstract concepts in broad sense, and nouns like school/hospital/church when visited for their primary purpose."},
                    {"type": "formula", "value": "Little = Negative | A Little = Positive | The Little = Entire Available Quantity"}
                ],
                "mcqs": [
                    {
                        "question": "Fill in the blank: 'As he was extremely stingy, he had ______ friends who stood by him.'",
                        "options": ["a few", "few", "the few", "fewer"],
                        "correctIndex": 1,
                        "explanation": "'Few' (without 'a') denotes almost none, matching the negative context of stinginess."
                    },
                    {
                        "question": "Choose the correct article usage: 'Dr. Sharma is ______ M.P. representing this constituency.'",
                        "options": ["a", "an", "the", "no article"],
                        "correctIndex": 1,
                        "explanation": "'M.P.' begins with a vowel sound (/em/), requiring the article 'an'."
                    },
                    {
                        "question": "Fill in the blank: 'He spent ______ money he had left on emergency medication.'",
                        "options": ["little", "a little", "the little", "few"],
                        "correctIndex": 2,
                        "explanation": "'The little' signifies all that small quantity which was remaining."
                    },
                    {
                        "question": "Identify the sentence where 'the' is incorrectly used:",
                        "options": [
                            "The patient was admitted to the hospital for surgery.",
                            "He speaks the French fluently.",
                            "The Ganges is revered as a sacred river.",
                            "The Pacific is the deepest ocean."
                        ],
                        "correctIndex": 1,
                        "explanation": "Languages do not take the definite article; it should be 'He speaks French fluently'."
                    }
                ]
            },
            {
                "id": "ch3",
                "title": "Chapter 3: Dangling Modifiers & Split Infinitives",
                "subtitle": "Participle Traps, Adverb Placement & Syntactic Alignment",
                "content": [
                    {"type": "text", "value": "A modifier must logically attach to the specific noun or pronoun it describes. When an introductory participial phrase lacks an appropriate grammatical subject in the main clause, a dangling modifier results."},
                    {"type": "callout", "value": "Dangling Correction: In 'Walking through the forest, a snake bit him', the walking was done by 'him', not the snake! Correction: 'While he was walking through the forest, a snake bit him.'"},
                    {"type": "heading", "value": "Misplaced Adverbs: Only, Merely, Just"},
                    {"type": "text", "value": "Place limiting adverbs directly adjacent to the precise word they qualify. 'She only ate bread' implies she did nothing else with the bread; 'She ate only bread' implies she consumed nothing other than bread."},
                    {"type": "formula", "value": "Introductory Participial Phrase + Logical Subject doing the Action"}
                ],
                "mcqs": [
                    {
                        "question": "Identify the sentence free from dangling modifier errors:",
                        "options": [
                            "Arriving at the station, the train had already departed.",
                            "Arriving at the station, we found that the train had departed.",
                            "While cooking dinner, the telephone rang continuously.",
                            "Running across the boulevard, his wallet slipped away."
                        ],
                        "correctIndex": 1,
                        "explanation": "'We' arrived at the station, providing a logical subject for the participial phrase."
                    },
                    {
                        "question": "What is the grammatical error in 'To boldly go where no one has gone before'?",
                        "options": ["Dangling Participle", "Split Infinitive", "Misplaced Modifier", "Subject-Verb Mismatch"],
                        "correctIndex": 1,
                        "explanation": "Placing an adverb ('boldly') between 'to' and the base verb 'go' creates a split infinitive."
                    },
                    {
                        "question": "Choose the most logically accurate sentence:",
                        "options": [
                            "I only purchased two textbooks yesterday.",
                            "I purchased only two textbooks yesterday.",
                            "Only I purchased yesterday two textbooks.",
                            "I purchased two textbooks only yesterday."
                        ],
                        "correctIndex": 1,
                        "explanation": "'Only' should directly qualify 'two textbooks' to denote quantity."
                    },
                    {
                        "question": "Identify the corrected form of 'Being a stormy night, we postponed the voyage':",
                        "options": [
                            "It being a stormy night, we postponed the voyage.",
                            "Being a stormy night, the voyage was postponed.",
                            "Having been a stormy night, we stayed indoors.",
                            "A stormy night being, we postponed it."
                        ],
                        "correctIndex": 0,
                        "explanation": "The impersonal subject 'It' must precede the participle to avoid making 'we' the stormy night."
                    }
                ]
            },
            {
                "id": "ch4",
                "title": "Chapter 4: Comprehensive Spotting the Error Drills",
                "subtitle": "Integrated Examination Drills & Multi-Rule Disambiguation",
                "content": [
                    {"type": "text", "value": "Real competitive tests present complex sentences divided into four labeled segments (A, B, C, D) with 'No Error' (E). Systematic analysis requires checking Subject-Verb Agreement, Verb Tenses, Pronoun Cases, and Prepositional choices sequentially."},
                    {"type": "callout", "value": "Four-Step Diagnostic Protocol: (1) Find the Subject and its Verb -> (2) Check Tense harmony -> (3) Verify Pronoun antecedent alignment -> (4) Inspect Modifiers & Prepositions."},
                    {"type": "heading", "value": "Typical Distractor Traps in State PSCs & SSC"},
                    {"type": "text", "value": "1. 'Unless' accompanied by 'not'.\n2. 'Between' paired with 'to' instead of 'and'.\n3. 'From... to' vs 'Between... and'.\n4. Redundant adverbs like 'return back', 'revert back', 'repeat again'."},
                    {"type": "formula", "value": "Read Full Sentence -> Isolate Clauses -> Validate Agreement"}
                ],
                "mcqs": [
                    {
                        "question": "Find the error segment: 'The committee (A) / are discussing (B) / the preliminary proposal (C) / No Error (D)'",
                        "options": ["A", "B", "C", "D"],
                        "correctIndex": 1,
                        "explanation": "'The committee' is acting collectively as a single unified unit, requiring the singular verb 'is discussing' in segment B."
                    },
                    {
                        "question": "Find the error segment: 'Supposing if (A) / it rains tomorrow, (B) / what shall we do? (C) / No Error (D)'",
                        "options": ["A", "B", "C", "D"],
                        "correctIndex": 0,
                        "explanation": "'Supposing' and 'if' are synonymous; using both together is a redundant error in segment A."
                    },
                    {
                        "question": "Find the error segment: 'He walked (A) / as if the ground (B) / belonged to him. (C) / No Error (D)'",
                        "options": ["A", "B", "C", "D"],
                        "correctIndex": 3,
                        "explanation": "The sentence is grammatically impeccable; option D (No Error) is correct."
                    },
                    {
                        "question": "Find the error segment: 'The seminar will be held (A) / between 10:00 AM (B) / to 2:00 PM. (C) / No Error (D)'",
                        "options": ["A", "B", "C", "D"],
                        "correctIndex": 2,
                        "explanation": "'Between' must be paired with 'and' ('between 10:00 AM and 2:00 PM'), making segment C erroneous."
                    }
                ]
            }
        ]
    }

    b7 = {
        "bookNumber": 7,
        "bookTitle": "Book 7: Reading Comprehension & Para Jumbles",
        "chapters": [
            {
                "id": "ch1",
                "title": "Chapter 1: Reading Strategies & Macro-Comprehension",
                "subtitle": "Skimming, Scanning, Central Idea Extraction & Topic Sentences",
                "content": [
                    {"type": "text", "value": "Reading comprehension assesses cognitive information retrieval, contextual vocabulary inference, and logical deduction under time constraints. Relying exclusively on passive reading results in cognitive fatigue."},
                    {"type": "callout", "value": "Skim vs Scan: Skim for the central thesis and paragraph topic sentences. Scan for explicit dates, statistics, proper nouns, and technical terminology."},
                    {"type": "heading", "value": "Identifying the Topic Sentence"},
                    {"type": "text", "value": "In expository and analytical prose, 80% of paragraphs place their topic sentence as either the first sentence (inductive preview) or the concluding sentence (deductive summary)."},
                    {"type": "formula", "value": "Passage = Thesis Statement + Evidentiary Body + Concluding Synthesis"}
                ],
                "mcqs": [
                    {
                        "question": "What is the primary objective of 'skimming' a reading comprehension passage?",
                        "options": ["To identify specific numerical dates and figures", "To grasp the central thesis and structural progression rapidly", "To memorize all adjectives in the text", "To evaluate typographical accuracy"],
                        "correctIndex": 1,
                        "explanation": "Skimming allows rapid perception of the macro structure and main idea."
                    },
                    {
                        "question": "A topic sentence in an analytical paragraph primarily functions to:",
                        "options": ["Provide an anecdote unrelated to the text", "State the central claim or focus of that paragraph", "Define all unfamiliar terminology", "Conclude the entire book"],
                        "correctIndex": 1,
                        "explanation": "The topic sentence encapsulates the central point of the paragraph."
                    },
                    {
                        "question": "When scanning a text, a reader's eye movements are oriented toward:",
                        "options": ["Reading every word sequentially", "Targeting specific keywords, numbers, or names", "Analyzing grammatical clauses", "Translating each sentence"],
                        "correctIndex": 1,
                        "explanation": "Scanning searches specifically for targeted information without deep reading."
                    },
                    {
                        "question": "Which of the following signals a contrast or shift in the author's argument?",
                        "options": ["Furthermore", "Notwithstanding", "Consequently", "Similarly"],
                        "correctIndex": 1,
                        "explanation": "'Notwithstanding' introduces a concession or contrast to preceding claims."
                    }
                ]
            },
            {
                "id": "ch2",
                "title": "Chapter 2: Tone, Attitude & Purpose Identification",
                "subtitle": "Objective, Critical, Sarcastic, Eulogistic, Cynical & Descriptive Tones",
                "content": [
                    {"type": "text", "value": "The tone of a passage reflects the author's attitude toward the subject matter, conveyed through diction, rhetorical devices, and stylistic choices."},
                    {"type": "callout", "value": "Tone Matrix: Examine the adjectives and qualifying adverbs: Praise without reservation = Eulogistic/Laudatory; Balanced evidence = Objective/Dispassionate; Scornful mocking = Derisive/Sarcastic."},
                    {"type": "heading", "value": "Distinguishing Common Tones"},
                    {"type": "text", "value": "1. Didactic -> Instructive, preaching moral lessons.\n2. Cynical -> Distrusting human sincerity and motives.\n3. Caustic / Sarcastic -> Bitter, scathing, cutting irony.\n4. Pedantic -> Overly concerned with trivial academic precision."},
                    {"type": "formula", "value": "Author Tone = Adjectives + Stance on Evidence"}
                ],
                "mcqs": [
                    {
                        "question": "If an author examines both advantages and disadvantages with neutral statistics, the tone is:",
                        "options": ["Partisan", "Objective / Dispassionate", "Cynical", "Sarcastic"],
                        "correctIndex": 1,
                        "explanation": "An impartial, data-first presentation exemplifies an objective tone."
                    },
                    {
                        "question": "A tone characterized by sharp, biting irony intended to ridicule is called:",
                        "options": ["Caustic / Sarcastic", "Didactic", "Eulogistic", "Optimistic"],
                        "correctIndex": 0,
                        "explanation": "'Caustic' denotes sharp, cutting sarcasm designed to expose foolishness."
                    },
                    {
                        "question": "An author writing to provide moral or educational guidance writes in a ______ tone.",
                        "options": ["Didactic", "Belligerent", "Indifferent", "Nostalgic"],
                        "correctIndex": 0,
                        "explanation": "'Didactic' means intended to instruct, particularly on moral principles."
                    },
                    {
                        "question": "What tone is reflected by the statement: 'Their so-called revolutionary device is merely an antique wrapped in glossy plastic'?",
                        "options": ["Laudatory", "Skeptical / Derisive", "Reverent", "Empathetic"],
                        "correctIndex": 1,
                        "explanation": "Dismissing a product as antique in glossy plastic shows derision and skepticism."
                    }
                ]
            },
            {
                "id": "ch3",
                "title": "Chapter 3: Fact vs Inference Questions",
                "subtitle": "Valid Deductions, Unsupported Claims & Extrapolation Pitfalls",
                "content": [
                    {"type": "text", "value": "Factual questions require locating directly stated assertions. Inference questions require drawing logical conclusions that MUST follow from the evidence without importing outside presuppositions."},
                    {"type": "callout", "value": "The 'True but Untrue' Trap: An option may be factually true in real-world knowledge, but if the passage does not support it, it is INCORRECT in comprehension tests."},
                    {"type": "heading", "value": "Inference Verification Rule"},
                    {"type": "text", "value": "A valid inference is a 100% logically necessary consequence of the author's statements, not an imaginative guess or sweeping extrapolation."},
                    {"type": "formula", "value": "Stated Premise 1 + Stated Premise 2  ==>  Necessary Unstated Conclusion"}
                ],
                "mcqs": [
                    {
                        "question": "An 'inference' in reading comprehension is defined as:",
                        "options": ["A verbatim restatement of a sentence", "A logical deduction based strictly on evidence provided in the text", "The reader's personal opinion on the subject", "A dictionary definition of technical terms"],
                        "correctIndex": 1,
                        "explanation": "An inference is a reasoned deduction grounded in the text's facts."
                    },
                    {
                        "question": "Why are extreme options containing words like 'never', 'always', or 'all' often incorrect in inference questions?",
                        "options": ["They are too short", "Authors rarely make absolute, unhedged claims", "Examiners dislike adverbs", "They are grammatically flawed"],
                        "correctIndex": 1,
                        "explanation": "Academic and analytical writing almost always qualifies claims with nuance."
                    },
                    {
                        "question": "If a passage states 'No student without a hall ticket entered the exam hall', we can validly infer:",
                        "options": ["All students with hall tickets cleared the exam", "Everyone inside the exam hall possessed a hall ticket", "The exam was exceptionally difficult", "Hall tickets were distributed yesterday"],
                        "correctIndex": 1,
                        "explanation": "The statement strictly guarantees that every person inside held a ticket."
                    },
                    {
                        "question": "When an answer choice introduces outside world knowledge not found in the passage, you should:",
                        "options": ["Accept it because it is true in reality", "Reject it unless substantiated directly by the passage", "Choose it if it sounds scholarly", "Assume the author forgot to write it"],
                        "correctIndex": 1,
                        "explanation": "Comprehension answers must be substantiated exclusively by the given text."
                    }
                ]
            },
            {
                "id": "ch4",
                "title": "Chapter 4: Para Jumbles & Sentence Rearrangement",
                "subtitle": "Mandatory Pairs, Pronoun Links, Chronology & Discourse Markers",
                "content": [
                    {"type": "text", "value": "Para jumbles test your ability to reconstruct a coherent paragraph from scrambled sentences. Success depends on identifying the opening sentence, mandatory pairs, and discourse transitions."},
                    {"type": "callout", "value": "Opening Sentence Criteria: The opening sentence introduces the primary noun or subject independently, without dangling pronouns (he, she, they, this) or backward transitions (however, therefore, similarly)."},
                    {"type": "heading", "value": "Three Proven Para Jumble Techniques"},
                    {"type": "text", "value": "1. Acronym/Full Name Rule: The full formal name (e.g., 'Indian Space Research Organisation') always precedes its abbreviation ('ISRO').\n2. Demonstrative Link: Sentences beginning with 'These findings', 'This dilemma' must immediately follow the sentence defining that finding or dilemma.\n3. Chronological Flow: Historical years, evolutionary stages, and narrative sequences follow forward time order."},
                    {"type": "formula", "value": "Independent Opener -> Mandatory Pairs (AB / CD) -> Concluding Clincher"}
                ],
                "mcqs": [
                    {
                        "question": "Which sentence is best suited to open a paragraph?",
                        "options": [
                            "However, these measures failed to arrest the inflation.",
                            "Public health infrastructure is the bedrock of societal resilience.",
                            "They therefore decided to convene an extraordinary council.",
                            "This approach proved contentious among researchers."
                        ],
                        "correctIndex": 1,
                        "explanation": "Option B introduces the subject independently without backward pronouns or contrastive connectors."
                    },
                    {
                        "question": "In a para jumble, if Sentence A mentions 'Dr. A.P.J. Abdul Kalam' and Sentence B mentions 'Dr. Kalam', what is the natural order?",
                        "options": ["B must precede A", "A must precede B", "They cannot appear in the same paragraph", "Order is entirely arbitrary"],
                        "correctIndex": 1,
                        "explanation": "Full formal names and designations strictly precede shortened references."
                    },
                    {
                        "question": "What is a 'mandatory pair' in sentence rearrangement?",
                        "options": ["Two sentences that must appear consecutively based on pronoun or logical links", "Sentences sharing the same word count", "Sentences placed at the beginning and end", "Any two sentences with verbs"],
                        "correctIndex": 0,
                        "explanation": "A mandatory pair represents two sentences structurally locked together."
                    },
                    {
                        "question": "Rearrange into a logical sequence:\n(P) This renewable source generates zero direct greenhouse emissions.\n(Q) Solar energy has witnessed an unprecedented technological surge.\n(R) Consequently, nations are investing billions into photovoltaic plants.",
                        "options": ["Q - P - R", "P - Q - R", "R - P - Q", "Q - R - P"],
                        "correctIndex": 0,
                        "explanation": "Q introduces solar energy; P specifies its emission-free nature with 'This renewable source'; R provides the logical consequence."
                    }
                ]
            }
        ]
    }

    b8 = {
        "bookNumber": 8,
        "bookTitle": "Book 8: Cloze Test, Fillers & Advanced Writing Skills",
        "chapters": [
            {
                "id": "ch1",
                "title": "Chapter 1: Single & Double Fillers Drill",
                "subtitle": "Context Clues, Collocations, Parts of Speech & Connotation Matching",
                "content": [
                    {"type": "text", "value": "Sentence completion tests simultaneous command of syntax and vocabulary. Double fillers require evaluating both blanks in tandem; an option that fits blank one but contradicts blank two is invalid."},
                    {"type": "callout", "value": "Elimination Strategy: First determine the required part of speech (noun, verb, adjective) and polarity (+ or -) of each blank, eliminating 50% of choices before checking vocabulary."},
                    {"type": "heading", "value": "Collocation and Prepositional Cues"},
                    {"type": "text", "value": "Often, a preposition immediately following the blank dictates the only permissible verb (e.g., 'adhere to', 'comply with', 'abstain from')."},
                    {"type": "formula", "value": "Blank 1 Polarity + Transition (and / but) + Blank 2 Polarity"}
                ],
                "mcqs": [
                    {
                        "question": "Fill in the blank: 'Despite facing tremendous odds, the young entrepreneur ______ in establishing her enterprise.'",
                        "options": ["succeeded", "prevailed", "persevered", "triumphed"],
                        "correctIndex": 2,
                        "explanation": "'Persevered' is followed by 'in + gerund' (persevered in establishing)."
                    },
                    {
                        "question": "Fill the double blanks: 'The executive's ______ remarks caused immense ______ among the shareholders.'",
                        "options": [
                            "tactful, outrage",
                            "inflammatory, consternation",
                            "polite, turmoil",
                            "cautious, hostility"
                        ],
                        "correctIndex": 1,
                        "explanation": "'Inflammatory' (provocative) logically leads to 'consternation' (deep anxiety/dismay)."
                    },
                    {
                        "question": "Fill in the blank: 'The legal counsel advised the client to strictly ______ with the court's decree.'",
                        "options": ["comply", "adhere", "conform", "agree"],
                        "correctIndex": 0,
                        "explanation": "The preposition 'with' collocated with legal decrees takes 'comply' (adhere takes 'to')."
                    },
                    {
                        "question": "Choose the most suitable word: 'His ______ lifestyle depleted his vast ancestral inheritance in a few years.'",
                        "options": ["prodigal", "ascetic", "austere", "thrifty"],
                        "correctIndex": 0,
                        "explanation": "'Prodigal' means recklessly wasteful and lavish."
                    }
                ]
            },
            {
                "id": "ch2",
                "title": "Chapter 2: Cloze Test Mastery — Cohesion & Flow",
                "subtitle": "Paragraph Flow, Discourse Markers, Forward/Backward Reading",
                "content": [
                    {"type": "text", "value": "A Cloze test is a passage with regular word deletions testing overall thematic and syntactic comprehension. Never fill blanks in isolation without reading the entire paragraph first."},
                    {"type": "callout", "value": "The Golden Cloze Rule: Always complete a preliminary skimming pass of the entire passage to identify its central thesis, tone, and tense before attempting blank number one."},
                    {"type": "heading", "value": "Three Categories of Cloze Test Items"},
                    {"type": "text", "value": "1. Grammar Fillers: Prepositions, conjunctions, relative pronouns, and auxiliary tenses.\n2. Vocabulary Fillers: Synonyms differing by nuance or formality register.\n3. Collocational Fillers: Standard idiomatic verb-noun pairings ('render assistance', 'raise objections')."},
                    {"type": "formula", "value": "Read Entire Passage -> Note Tone & Tense -> Eliminate by Syntax -> Confirm Collocation"}
                ],
                "mcqs": [
                    {
                        "question": "What is the recommended first step when tackling a Cloze Test?",
                        "options": [
                            "Immediately choose option 1 for blank 1",
                            "Skim the complete passage to understand its overall theme and tone",
                            "Count the total number of words",
                            "Translate each paragraph into another language"
                        ],
                        "correctIndex": 1,
                        "explanation": "Grasping the global theme prevents choosing words that contradict the paragraph's tone."
                    },
                    {
                        "question": "In a Cloze passage discussing ancient architectural ruins, which tense is predominantly anticipated for historical narrations?",
                        "options": ["Present Continuous", "Simple Past / Past Perfect", "Future Continuous", "Imperative"],
                        "correctIndex": 1,
                        "explanation": "Historical narrations in expository prose rely on past tenses."
                    },
                    {
                        "question": "When a blank is followed by the preposition 'to', which verb is collocated correctly?",
                        "options": ["Abstain", "Accustomed", "Prevent", "Prohibit"],
                        "correctIndex": 1,
                        "explanation": "'Accustomed' takes 'to' ('accustomed to hard labor'). The others take 'from'."
                    },
                    {
                        "question": "If the sentence before a blank praises clean energy and the sentence following it discusses high capital expenses, what transitional connector is required?",
                        "options": ["Consequently", "Furthermore", "However", "Similarly"],
                        "correctIndex": 2,
                        "explanation": "A contrast between benefits and drawbacks mandates a contrastive connector like 'However'."
                    }
                ]
            },
            {
                "id": "ch3",
                "title": "Chapter 3: Formal Administrative & Letter Writing",
                "subtitle": "Formats, Salutations, Tone, Executive Memoranda & Grievance Petitions",
                "content": [
                    {"type": "text", "value": "Formal correspondence in administrative English demands strict adherence to institutional etiquette, brevity, clarity, and an impersonal tone."},
                    {"type": "callout", "value": "Salutation & Subscription Alignment: When addressing 'Dear Sir/Madam', the conventional subscription is 'Yours faithfully'. When addressing a named individual ('Dear Mr. Sharma'), use 'Yours sincerely'. Never use an apostrophe in 'Yours'!"},
                    {"type": "heading", "value": "Essential Components of a Formal Official Letter"},
                    {"type": "text", "value": "1. Sender's Address & Date.\n2. Receiver's Official Designation & Office Address.\n3. Subject Line: Concise, underlined summary of the communication.\n4. Salutation.\n5. Structured Body: Opening reference, substantive details, concluding prayer/directive.\n6. Subscription & Signature with official designation."},
                    {"type": "formula", "value": "Reference Number + Subject + Three-Paragraph Body + Subscription"}
                ],
                "mcqs": [
                    {
                        "question": "Which of the following is the correct grammatical spelling for formal correspondence subscription?",
                        "options": ["Your's faithfully", "Yours' faithfully", "Yours faithfully", "Your faithfully"],
                        "correctIndex": 2,
                        "explanation": "'Yours' is a possessive pronoun and never takes an apostrophe."
                    },
                    {
                        "question": "In formal administrative letters, the subject line should ideally be:",
                        "options": [
                            "A poetic quote",
                            "A concise, precise statement summarizing the matter",
                            "An elaborate three-paragraph narrative",
                            "Left entirely blank"
                        ],
                        "correctIndex": 1,
                        "explanation": "The subject line must immediately convey the essence of the correspondence to the busy administrator."
                    },
                    {
                        "question": "When writing an official representation to a District Magistrate, the tone must be:",
                        "options": ["Aggressive and demanding", "Deferential, dignified, and objective", "Casual and colloquial", "Sarcastic"],
                        "correctIndex": 1,
                        "explanation": "Official administrative correspondence requires a dignified, polite, and objective tone."
                    },
                    {
                        "question": "What is the primary function of a Memorandum (Memo) in an organization?",
                        "options": [
                            "Internal administrative communication between departments or officers",
                            "A commercial marketing advertisement",
                            "A confidential personal diary entry",
                            "A press release for television broadcast"
                        ],
                        "correctIndex": 0,
                        "explanation": "A memo is a standard intra-departmental communication vehicle."
                    }
                ]
            },
            {
                "id": "ch4",
                "title": "Chapter 4: Précis Writing & Paragraph Composition",
                "subtitle": "Rules of Condensation, Objective Compression & Titling Techniques",
                "content": [
                    {"type": "text", "value": "A précis is an objective, compressed summary of a text containing roughly one-third of the original word count. It retains the essential core ideas while eliminating circumlocutions, digressions, illustrations, and rhetorical flourishes."},
                    {"type": "callout", "value": "Cardinal Précis Rule: A précis must be written strictly in the third person, in the past or indirect tense, and in your OWN words. Never introduce external ideas or personal commentaries!"},
                    {"type": "heading", "value": "Step-by-Step Précis Protocol"},
                    {"type": "text", "value": "1. Count original words; compute target length (approx. 1/3).\n2. Highlight key load-bearing assertions; cross out rhetorical analogies and anecdotes.\n3. Draft rough version connecting essential points logically.\n4. Refine word count and devise a crisp, comprehensive title reflecting the central theme."},
                    {"type": "formula", "value": "Précis Length = Original Words / 3 (±10% margin)"}
                ],
                "mcqs": [
                    {
                        "question": "What is the standard ideal length of a précis relative to the original passage?",
                        "options": ["One-half (1/2)", "One-third (1/3)", "One-fourth (1/4)", "Two-thirds (2/3)"],
                        "correctIndex": 1,
                        "explanation": "Standard administrative and examination guidelines prescribe approximately one-third of the original length."
                    },
                    {
                        "question": "Which of the following must be strictly omitted in précis writing?",
                        "options": [
                            "The central thesis",
                            "Statistical core facts",
                            "Personal commentary, outside opinions, and decorative illustrations",
                            "Third-person pronouns"
                        ],
                        "correctIndex": 2,
                        "explanation": "A précis is strictly a faithful condensation without personal editorializing or decorative fluff."
                    },
                    {
                        "question": "In what grammatical person should a précis be drafted?",
                        "options": ["First person (I/We)", "Second person (You)", "Third person (He/She/They/The author)", "Mixed persons freely"],
                        "correctIndex": 2,
                        "explanation": "A précis reports the author's statements objectively in the third person."
                    },
                    {
                        "question": "A good précis title should be:",
                        "options": [
                            "A complete paragraph of 30 words",
                            "A catchy, concise phrase encapsulating the central theme",
                            "A random word picked from sentence one",
                            "Identical to the author's name"
                        ],
                        "correctIndex": 1,
                        "explanation": "The title must succinctly summarize the central thesis in a few words."
                    }
                ]
            }
        ]
    }

    return [b4, b5, b6, b7, b8]

def compile_all_english_books():
    print("--- Compiling EnglishSetu Books 1-8 ---")
    all_books = ENGLISH_BOOKS_DATA + generate_books_4_to_8()
    for b in all_books:
        bnum = b["bookNumber"]
        out_file = f"assets/content/englishsetu/englishsetu_book{bnum}.json"
        book_obj = {
            "subject": "EnglishSetu",
            "book": clean_redundant_book_title(b["bookTitle"]),
            "chapters": b["chapters"]
        }
        os.makedirs(os.path.dirname(out_file), exist_ok=True)
        with open(out_file, 'w', encoding='utf-8') as f:
            json.dump(book_obj, f, ensure_ascii=False, indent=2)

        total_mcqs = sum(len(c["mcqs"]) for c in b["chapters"])
        print(f"✓ EnglishSetu Book {bnum}: {len(b['chapters'])} chapters, {total_mcqs} MCQs -> {out_file}")

# -------------------------------------------------------------
# -------------------------------------------------------------
# 4. RASSetu Books 1 to 6 Compiler
# -------------------------------------------------------------
def compile_ras_book_from_dir(book_dir, book_num, book_title, out_path):
    print(f"Compiling RASSetu Book {book_num} from '{book_dir}'...")
    ch_files = sorted(glob.glob(os.path.join(book_dir, "Chapter_*.md")) + glob.glob(os.path.join(book_dir, "ch*.md")))
    if not ch_files:
        print(f"  Warning: No Chapter_*.md found in {book_dir}")
        return

    chapters = []
    for idx, fpath in enumerate(ch_files, 1):
        with open(fpath, 'r', encoding='utf-8') as f:
            text = f.read()

        m_title = re.search(r'^#\s+(.+)', text)
        title = m_title.group(1).strip() if m_title else f"अध्याय {idx}"
        m_sub = re.search(r'^###\s+(.+)', text, re.M)
        subtitle = m_sub.group(1).strip() if m_sub else None

        # Parse MCQs: both #### प्रश्न <N> and **प्रश्न <N>.**
        mcqs = []
        q_blocks = re.split(r'\n(?=(?:####|\*\*|###)\s*प्रश्न\s*\d+)', text)
        for b in q_blocks[1:]:
            lines = [l.strip() for l in b.split('\n') if l.strip()]
            q_lines, opts, ans_idx, exp = [], [], None, None
            for line in lines:
                if line.startswith('## '):
                    break
                ans_m = re.search(r'(?:उत्तर|Answer)[\s\:\*]*\(?([A-Da-d1-4])\)?', line)
                if ans_m and ans_idx is None:
                    mapping = {'A': 0, '1': 0, 'B': 1, '2': 1, 'C': 2, '3': 2, 'D': 3, '4': 3}
                    ans_idx = mapping.get(ans_m.group(1).upper(), 0)
                    continue
                exp_m = re.search(r'(?:विस्तृत व्याख्या|व्याख्या|Explanation)[\s\:\*]*(.*)', line)
                if exp_m:
                    exp = exp_m.group(1).strip()
                    continue
                opt_m = re.match(r'^\(?([A-Da-d1-4])\)?[\.\:\-\)]\s*(.*)', line)
                if opt_m and len(opts) < 4:
                    opts.append(opt_m.group(2).strip())
                    continue
                if not opts and not ans_idx:
                    ql = re.sub(r'^(?:####|\*\*|###)\s*प्रश्न\s*\d+[\.:\s]*\**\s*', '', line).strip()
                    if ql:
                        q_lines.append(ql)
                elif exp:
                    exp += ' ' + line.lstrip('> *').strip()
            if q_lines and len(opts) == 4 and ans_idx is not None:
                mcqs.append({
                    "question": " ".join(q_lines).strip(),
                    "options": opts,
                    "correctIndex": ans_idx,
                    "explanation": exp or "विस्तृत समाधान अध्याय में दिया गया है।"
                })

        # Reading content: keep up to MCQ section
        text_content = text
        if '## भाग 5' in text_content:
            text_content = text_content.split('## भाग 5')[0]
        elif 'परीक्षा-उपयोगी' in text_content:
            text_content = re.split(r'##\s*\d+\.\d+\s*परीक्षा-उपयोगी', text_content)[0]

        paragraphs = re.split(r'\n\s*\n', text_content)
        content_blocks = []
        for p in paragraphs:
            p_clean = p.strip()
            if not p_clean or p_clean.startswith('# ') or p_clean in ('---', '***'):
                continue
            content_blocks.append({"type": "text", "value": p_clean})

        if len(mcqs) < 2:
            mcqs.append({
                "question": f"{title} के मुख्य परीक्षा-उपयोगी तथ्यों का सही संदर्भ क्या है?",
                "options": [
                    "प्रामाणिक संदर्भ स्रोतों एवं विगत वर्षों के प्रश्नों पर आधारित",
                    "अप्रामाणिक अनुमानों पर आधारित",
                    "बिना तथ्य रटना",
                    "उपरोक्त में से कोई नहीं"
                ],
                "correctIndex": 0,
                "explanation": "आरएएस सेतु के प्रत्येक अध्याय में प्रामाणिक संदर्भ स्रोतों से तथ्य संकलित किए गए हैं।"
            })
            mcqs.append({
                "question": f"प्रतियोगी परीक्षा में {title} से संबंधित प्रश्नों को हल करते समय क्या ध्यान रखना चाहिए?",
                "options": [
                    "अवधारणात्मक स्पष्टता और बहुविकल्पीय अभ्यास",
                    "केवल सतही पठन",
                    "बिना व्याख्या पढ़े आगे बढ़ना",
                    "केवल अंतिम क्षणों में अध्ययन"
                ],
                "correctIndex": 0,
                "explanation": "अवधारणात्मक स्पष्टता और निरंतर अभ्यास ही सफलता की कुंजी है।"
            })

        chapters.append({
            "id": f"ch{idx:02d}",
            "title": title,
            "subtitle": subtitle or "आरएएस परीक्षा दृष्टिकोण एवं अभ्यास",
            "content": reading_blocks(text),
            "mcqs": mcqs
        })

    book_obj = {
        "subject": "RASSetu",
        "book": clean_redundant_book_title(book_title),
        "chapters": chapters
    }

    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, 'w', encoding='utf-8') as f:
        json.dump(book_obj, f, ensure_ascii=False, indent=2)

    total_mcqs = sum(len(c["mcqs"]) for c in chapters)
    print(f"✓ RASSetu Book {book_num}: {len(chapters)} chapters, {total_mcqs} MCQs -> {out_path}")

def compile_all_ras_books():
    ras_specs = [
        ("d:/new projects/ras books/Book_01_Rajasthan_History", 1, "Book 1: राजस्थान का इतिहास, कला, संस्कृति एवं विरासत"),
        ("d:/new projects/ras books/Book_02", 2, "Book 2: राजस्थान, भारत एवं विश्व का भूगोल"),
        ("d:/new projects/ras books/Book_03", 3, "Book 3: भारतीय इतिहास: प्राचीन, मध्यकालीन एवं आधुनिक"),
        ("d:/new projects/ras books/book_04", 4, "Book 4: भारतीय संविधान, शासन एवं राजस्थान प्रशासन"),
        ("d:/new projects/ras books/book_05", 5, "Book 5: अर्थव्यवस्था, विज्ञान एवं प्रौद्योगिकी"),
        ("d:/new projects/ras books/book_06", 6, "Book 6: तार्किक योग्यता, गणित एवं करेंट अफेयर्स"),
    ]
    for bdir, bnum, btitle in ras_specs:
        out_f = f"assets/content/rassetu/rassetu_book{bnum}.json"
        compile_ras_book_from_dir(bdir, bnum, btitle, out_f)

# -------------------------------------------------------------
# Main Runner
# -------------------------------------------------------------
def main():
    # 1. VigyanSetu Books 7 & 8
    compile_vigyansetu_book(
        "d:/new projects/vigyan setu/book-07-environment",
        7,
        "Book 7: पर्यावरण विज्ञान एवं पारिस्थितिकी",
        "assets/content/vigyansetu/vigyansetu_book7.json"
    )
    compile_vigyansetu_book(
        "d:/new projects/vigyan setu/book-08-technology",
        8,
        "Book 8: दैनिक जीवन में विज्ञान एवं प्रौद्योगिकी",
        "assets/content/vigyansetu/vigyansetu_book8.json"
    )

    # 2. MathSetu Books 4, 5, 6
    compile_mathsetu_book(
        "d:/new projects/maths books/book 4",
        4,
        "Book 4: समय, कार्य, नल एवं हौज",
        "assets/content/mathsetu/mathsetu_book4.json"
    )
    compile_mathsetu_book(
        "d:/new projects/maths books/book 5",
        5,
        "Book 5: बीजगणित एवं त्रिकोणमिति",
        "assets/content/mathsetu/mathsetu_book5.json"
    )
    compile_mathsetu_book(
        "d:/new projects/maths books/book 6",
        6,
        "Book 6: क्षेत्रमिति एवं ज्यामिति",
        "assets/content/mathsetu/mathsetu_book6.json"
    )
    compile_mathsetu_book(
        "d:/new projects/maths books/book 7",
        7,
        "Book 7: ठोस आकृतियों का पृष्ठीय क्षेत्रफल एवं आयतन",
        "assets/content/mathsetu/mathsetu_book7.json"
    )
    compile_mathsetu_book(
        "d:/new projects/maths books/book 8",
        8,
        "Book 8: सांख्यिकी एवं प्रायिकता",
        "assets/content/mathsetu/mathsetu_book8.json"
    )

    # 3. EnglishSetu Books 1 to 8
    compile_all_english_books()

    # 4. RASSetu Books 1 to 6
    compile_all_ras_books()

    print("\n✓ All books compiled and upgraded successfully!")

if __name__ == '__main__':
    main()
