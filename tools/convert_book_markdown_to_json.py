#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Setu Learning: Markdown-to-JSON Book Converter
Converts book Markdown files into offline-first JSON assets for the Setu Learning Flutter app.

Usage:
  # Single file conversion:
  python tools/convert_book_markdown_to_json.py --input mathsetu_book3.md --output assets/content/mathsetu/mathsetu_book3.json

  # Batch conversion:
  python tools/convert_book_markdown_to_json.py --input-dir path/to/markdowns --output-dir assets/content/mathsetu

  # Overriding subject & book title:
  python tools/convert_book_markdown_to_json.py --input mathsetu_book3.md --subject "MathSetu" --book "Book 3"
"""

import argparse
import glob
import json
import os
import re
import shutil
import sys

# Regular expressions for parsing
IMAGE_PATTERN = re.compile(r'!\[(.*?)\]\((.*?)\)')
MCQ_BLOCK_PATTERN = re.compile(r'<!--\s*mcq\s*-->([\s\S]*?)<!--\s*/mcq\s*-->', re.IGNORECASE)
OPTION_PREFIX_PATTERN = re.compile(r'^\s*(?:[A-Da-d][\)\.\:\-]|[1-4][\)\.\:\-]|\([A-Da-d]\)|\([1-4]\))\s*')

def infer_subject_and_book(filename_or_path, default_subject=None, default_book=None):
    """
    Infers Subject and Book name from filename, e.g.:
    mathsetu_book3.md -> MathSetu, Book 3
    englishsetu_book1.md -> EnglishSetu, Book 1
    vigyansetu_book2.md -> VigyanSetu, Book 2
    MathSetu_Book_01_Combined.md -> MathSetu, Book 1
    """
    base = os.path.splitext(os.path.basename(filename_or_path))[0]
    
    subject = default_subject
    book = default_book

    # 1. Infer subject
    if not subject:
        lower = base.lower()
        if 'math' in lower:
            subject = 'MathSetu'
        elif 'english' in lower:
            subject = 'EnglishSetu'
        elif 'vigyan' in lower or 'science' in lower:
            subject = 'VigyanSetu'
        else:
            subject = base.split('_')[0].capitalize()

    # 2. Infer book
    if not book:
        # Match book number like book3, book_03, b3, etc.
        m = re.search(r'book_?0?(\d+)', base, re.IGNORECASE)
        if m:
            book_num = int(m.group(1))
            book = f"Book {book_num}"
        else:
            book = base

    return subject, book

def parse_mcq_comment_block(block_text, file_ref, chapter_title):
    """
    Parses a single <!-- mcq --> block:
    Q: Question text
    A) Option 1
    B) Option 2
    C) Option 3
    D) Option 4
    Correct: B
    """
    lines = [line.strip() for line in block_text.strip().split('\n') if line.strip()]
    question = ""
    options = []
    correct_index = None
    explanation = None

    for line in lines:
        # Question line
        if re.match(r'^(?:Q|Question|प्रश्न)\s*[\:\.]\s*', line, re.IGNORECASE):
            question = re.sub(r'^(?:Q|Question|प्रश्न)\s*[\:\.]\s*', '', line, flags=re.IGNORECASE).strip()
            continue

        # Correct answer line
        correct_match = re.match(r'^(?:Correct|Answer|उत्तर)\s*[\:\.]\s*\(?([A-Da-d1-4])\)?', line, re.IGNORECASE)
        if correct_match:
            letter = correct_match.group(1).upper()
            mapping = {'A': 0, '1': 0, 'B': 1, '2': 1, 'C': 2, '3': 2, 'D': 3, '4': 3}
            correct_index = mapping.get(letter)
            continue

        # Explanation line (optional)
        exp_match = re.match(r'^(?:Explanation|Exp|व्याख्या|स्पष्टीकरण)\s*[\:\.]\s*(.*)', line, re.IGNORECASE)
        if exp_match:
            explanation = exp_match.group(1).strip()
            continue

        # Options lines (A), B), C), D) or A. B. C. D.)
        if re.match(r'^(?:[A-Da-d][\)\.\:\-]|\([A-Da-d]\)|[1-4][\)\.\:\-]|\([1-4]\))\s+', line):
            cleaned_opt = OPTION_PREFIX_PATTERN.sub('', line).strip()
            options.append(cleaned_opt)
            continue

        # If question not yet assigned and line is before options
        if not question and not options:
            question = line
        elif not correct_index and len(options) == 4 and not explanation:
            # Might be continuation or explanation
            if explanation:
                explanation += " " + line
            else:
                explanation = line

    # Validation and error reporting
    warnings = []
    if not question:
        warnings.append("Missing question text in MCQ block")
    if len(options) != 4:
        warnings.append(f"Expected exactly 4 options, found {len(options)} (Options: {options})")
    if correct_index is None:
        warnings.append("Missing or unrecognized 'Correct: [A-D]' line in MCQ block")

    if warnings:
        warn_msg = f"  ⚠️  [MALFORMED MCQ WARNING] File '{file_ref}', Chapter '{chapter_title}':\n"
        for w in warnings:
            warn_msg += f"      - {w}\n"
        warn_msg += f"      Raw block snippet: {block_text.strip()[:100]}...\n"
        print(warn_msg, file=sys.stderr)
        return None

    mcq_dict = {
        "question": question,
        "options": options,
        "correctIndex": correct_index
    }
    if explanation:
        mcq_dict["explanation"] = explanation

    return mcq_dict

def parse_fallback_question_block(q_block_text, file_ref, chapter_title):
    """
    Fallback parser for books using native markdown questions like:
    ### प्रश्न 1
    24 × 25 बराबर है:
    (a) 500
    (b) 600
    (c) 650
    (d) 700
    उत्तर: सही विकल्प (b) है।
    """
    lines = [line.strip() for line in q_block_text.strip().split('\n') if line.strip()]
    question_lines = []
    options = []
    correct_index = 0
    explanation = None

    for line in lines:
        if re.match(r'^(?:###|\*\*|)\s*(?:प्रश्न|Question)\s*\d+', line):
            continue
        opt_match = re.match(r'^\(?([a-dA-D1-4])\)?[\.\:\-\)]\s*(.*)', line)
        if opt_match and len(options) < 4:
            options.append(opt_match.group(2).strip())
            continue

        ans_match = re.search(r'(?:सही विकल्प|उत्तर|Answer)[\s\:\*]*\(?([a-dA-D1-4])\)?', line)
        if ans_match:
            let = ans_match.group(1).upper()
            mapping = {'A': 0, '1': 0, 'B': 1, '2': 1, 'C': 2, '3': 2, 'D': 3, '4': 3}
            if let in mapping:
                correct_index = mapping[let]
            continue

        if re.search(r'(?:विस्तृत समाधान|समाधान|Explanation)', line):
            explanation = line
            continue

        if len(options) == 0:
            question_lines.append(line)
        elif explanation:
            explanation += "\n" + line

    q_text = " ".join(question_lines).strip()
    if q_text and len(options) == 4:
        item = {
            "question": q_text,
            "options": options,
            "correctIndex": correct_index
        }
        if explanation:
            item["explanation"] = explanation
        return item
    return None

def split_into_chapters(markdown_text):
    """
    Splits markdown file into chapters.
    - If the markdown contains '# अध्याय ' or '# Chapter ', those mark the true chapters.
    - Otherwise, standard convention: '## ' starts a new chapter.
    """
    lines = markdown_text.split('\n')
    
    # Check if '# अध्याय ' or '# Chapter ' is used for chapters
    has_adhya_h1 = any(re.match(r'^#\s+(?:अध्याय|Chapter)\s+\d+', line, re.IGNORECASE) for line in lines)
    
    chapters_raw = []
    current_title = None
    current_lines = []

    if has_adhya_h1:
        ch_regex = re.compile(r'^#\s+((?:अध्याय|Chapter)\s+\d+.*)$', re.IGNORECASE)
    else:
        # Standard convention per user specification: ## starts a new chapter
        ch_regex = re.compile(r'^##\s+(.+)$')

    for line in lines:
        m = ch_regex.match(line)
        if m:
            heading_candidate = m.group(1).strip()
            # Save previous chapter
            if current_title is not None and current_lines:
                chapters_raw.append((current_title, current_lines))
                current_lines = []
            current_title = heading_candidate
        else:
            if current_title is not None:
                current_lines.append(line)

    if current_title is not None and current_lines:
        chapters_raw.append((current_title, current_lines))

    # If no heading was matched at all, treat whole text as single chapter
    if not chapters_raw and lines:
        chapters_raw.append(("Chapter 1", lines))

    return chapters_raw

def parse_chapter_content_and_mcqs(chapter_title, chapter_lines, file_ref, referenced_images):
    """
    Parses chapter content preserving reading order:
    - Paragraphs -> text blocks
    - Images -> image blocks
    - MCQs -> extracted into chapter's mcqs list
    """
    full_text = "\n".join(chapter_lines)
    mcqs = []

    # 1. Parse fenced <!-- mcq --> blocks first
    for match in MCQ_BLOCK_PATTERN.finditer(full_text):
        raw_mcq = match.group(1)
        mcq_obj = parse_mcq_comment_block(raw_mcq, file_ref, chapter_title)
        if mcq_obj:
            mcqs.append(mcq_obj)

    # 2. Check for VigyanSetu style MCQs: **Q<N>.** with answers in भाग 12
    if not mcqs and '**Q1.**' in full_text:
        # Extract answers first
        answers_map = {}
        for m in re.finditer(r'\*\*Q(\d+)\.\s*(?:सही उत्तर|उत्तर|सही विकल्प)[\s\:\*]*\(?([A-Da-d1-4])\)?(?:\*\*)?(.*?)(?=\*\*Q\d+\.|$)', full_text, re.DOTALL):
            q_num = int(m.group(1))
            letter = m.group(2).upper()
            exp = m.group(3).strip()
            # Clean explanation markdown artifacts
            exp_clean = re.sub(r'^[-\*\s]+', '', exp).strip()
            answers_map[q_num] = (letter, exp_clean)

        # Extract questions
        for m in re.finditer(r'\*\*Q(\d+)\.\*\*\s*(.+?)(?=\*\*Q\d+\.\*\*|##\s*भाग\s*12|##\s*उत्तर|$)', full_text, re.DOTALL):
            q_num = int(m.group(1))
            q_raw = m.group(2).strip()
            lines = [l.strip() for l in q_raw.split('\n') if l.strip()]
            opts = []
            q_lines = []
            for line in lines:
                opt_match = re.match(r'^\(?([A-Da-d])\)?[\.\:\-\s]+\s*(.*)$', line)
                if opt_match and len(opts) < 4:
                    opts.append(opt_match.group(2).strip())
                elif not opts:
                    q_lines.append(line)

            if len(opts) == 4:
                ans_letter, exp = answers_map.get(q_num, ('A', ''))
                mapping = {'A': 0, '1': 0, 'B': 1, '2': 1, 'C': 2, '3': 2, 'D': 3, '4': 3}
                mcqs.append({
                    "question": " ".join(q_lines).strip(),
                    "options": opts,
                    "correctIndex": mapping.get(ans_letter, 0),
                    "explanation": exp[:400] if exp else None
                })

    # 3. Check for native markdown MCQs (MathSetu style) if no MCQs found yet
    if not mcqs:
        # Look for ### प्रश्न blocks
        q_blocks = re.split(r'\n(?=###\s*(?:प्रश्न|Question)\s*\d+)', full_text)
        for qb in q_blocks[1:]:
            parsed_q = parse_fallback_question_block(qb, file_ref, chapter_title)
            if parsed_q:
                mcqs.append(parsed_q)

    # Remove the MCQ blocks and quiz sections from the text flow so raw quiz code doesn't clutter the reader
    text_for_reading = MCQ_BLOCK_PATTERN.sub('', full_text)
    
    # If questions were found in a dedicated section, truncate the reading text before the quiz/answer section
    cutoff_patterns = [
        r'##\s*भाग\s*(?:11|12|5)\s*[\:\-]\s*(?:बहुविकल्पीय|उच्च-प्रतिफल|उत्तर|अभ्यास)',
        r'##\s*(?:अभ्यास MCQs|उत्तर कुंजी तालिका|प्रश्न एवं 6-चरणीय विस्तृत समाधान)',
        r'###\s*प्रश्न\s*1\b',
        r'\*\*Q1\.\*\*'
    ]
    for cp in cutoff_patterns:
        if re.search(cp, text_for_reading):
            text_for_reading = re.split(cp, text_for_reading)[0]
            break

    # 3. Parse content blocks (text and images in exact visual order)
    content_blocks = []
    
    # Split paragraphs by double newline
    paragraphs = re.split(r'\n\s*\n', text_for_reading)

    for para in paragraphs:
        para_clean = para.strip()
        if not para_clean:
            continue
        
        # Skip horizontal dividers
        if para_clean in ('---', '***', '___'):
            continue

        # Check for image references
        img_match = IMAGE_PATTERN.search(para_clean)
        if img_match:
            alt_text = img_match.group(1).strip()
            img_path = img_match.group(2).strip()
            img_filename = os.path.basename(img_path)
            referenced_images.add(img_filename)

            # If there was text before the image
            pre_text = para_clean[:img_match.start()].strip()
            if pre_text:
                content_blocks.append({"type": "text", "value": pre_text})

            content_blocks.append({
                "type": "image",
                "value": img_filename
            })

            # If there was text after the image
            post_text = para_clean[img_match.end():].strip()
            if post_text:
                content_blocks.append({"type": "text", "value": post_text})
        else:
            # Regular text paragraph
            content_blocks.append({
                "type": "text",
                "value": para_clean
            })

    # Warning for zero MCQs
    if len(mcqs) == 0:
        print(f"  ⚠️  [ZERO MCQs WARNING] File '{file_ref}', Chapter '{chapter_title}' has 0 practice questions.", file=sys.stderr)

    return content_blocks, mcqs

def convert_markdown_file(input_file, output_file, subject_override=None, book_override=None):
    """
    Converts a single markdown file into the target JSON schema.
    """
    if not os.path.exists(input_file):
        raise FileNotFoundError(f"Input Markdown file not found: {input_file}")

    with open(input_file, 'r', encoding='utf-8') as f:
        markdown_text = f.read()

    subject, book = infer_subject_and_book(input_file, subject_override, book_override)
    file_ref = os.path.basename(input_file)
    referenced_images = set()

    raw_chapters = split_into_chapters(markdown_text)
    chapters_json = []

    for idx, (ch_title, ch_lines) in enumerate(raw_chapters):
        ch_id = f"ch{idx + 1}"
        content_blocks, mcqs = parse_chapter_content_and_mcqs(
            ch_title, ch_lines, file_ref, referenced_images
        )
        
        # Build chapter entry
        chapters_json.append({
            "id": ch_id,
            "title": ch_title,
            "content": content_blocks,
            "mcqs": mcqs
        })

    result = {
        "subject": subject,
        "book": book,
        "chapters": chapters_json
    }

    # Ensure output directory exists
    os.makedirs(os.path.dirname(os.path.abspath(output_file)), exist_ok=True)
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(result, f, ensure_ascii=False, indent=2)

    total_mcqs = sum(len(c["mcqs"]) for c in chapters_json)
    print(f"✓ Converted '{input_file}' ➔ '{output_file}'")
    print(f"  Subject: {subject} | Book: {book} | Chapters: {len(chapters_json)} | Total MCQs: {total_mcqs}")
    if referenced_images:
        print(f"  Referenced Images ({len(referenced_images)}): {', '.join(sorted(referenced_images))}")

    return result, referenced_images

def main():
    parser = argparse.ArgumentParser(description="Convert Setu Book Markdown files to in-app JSON schema.")
    parser.add_argument('--input', '-i', help="Path to a single Markdown file.")
    parser.add_argument('--output', '-o', help="Output path for the JSON file.")
    parser.add_argument('--input-dir', help="Directory containing multiple Markdown files for batch conversion.")
    parser.add_argument('--output-dir', help="Output directory for generated JSON files.")
    parser.add_argument('--subject', help="Explicit subject name (e.g., MathSetu).")
    parser.add_argument('--book', help="Explicit book title (e.g., Book 3).")

    args = parser.parse_args()

    if args.input:
        output_file = args.output
        if not output_file:
            base_name = os.path.splitext(os.path.basename(args.input))[0]
            output_file = f"{base_name}.json"
        convert_markdown_file(args.input, output_file, args.subject, args.book)

    elif args.input_dir:
        output_dir = args.output_dir or "assets/content"
        md_files = sorted(glob.glob(os.path.join(args.input_dir, "*.md")))
        if not md_files:
            print(f"No markdown files found in directory: {args.input_dir}", file=sys.stderr)
            sys.exit(1)

        print(f"Starting batch conversion of {len(md_files)} Markdown files from '{args.input_dir}'...")
        all_referenced_images = set()

        for md_path in md_files:
            base_name = os.path.splitext(os.path.basename(md_path))[0]
            out_json = os.path.join(output_dir, f"{base_name}.json")
            _, images = convert_markdown_file(md_path, out_json, args.subject, args.book)
            all_referenced_images.update(images)

        print(f"\n✓ Batch conversion finished. Converted {len(md_files)} files into '{output_dir}'.")
        if all_referenced_images:
            print(f"Total Unique Images Referenced Across Books: {len(all_referenced_images)}")
            for img in sorted(all_referenced_images):
                print(f"  - {img}")
    else:
        parser.print_help()

if __name__ == '__main__':
    main()
