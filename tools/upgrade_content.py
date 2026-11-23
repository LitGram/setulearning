#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
tools/upgrade_content.py
Batch script to fix, enrich, and validate content for:
1. RASSetu Books 1-6 (extract embedded MCQs from content into mcqs array, clean reading content)
2. VigyanSetu Books 7-8 (compile full 27 and 28 chapter books from source markdowns)
3. MathSetu Books 4-6 (compile complete 20+ chapters from source markdowns)
4. EnglishSetu Books 1-8 (expand full grammar and vocabulary books with complete 4-option MCQs)
"""

import os
import re
import json
import glob

OPT_RE = re.compile(r'^\(?([A-Da-d1-4])\)?[\.\:\-\)]\s*(.*)$')
ANS_RE = re.compile(r'(?:उत्तर|Answer|Correct)[\s\:\*]*\(?([A-Da-d1-4])\)?', re.IGNORECASE)
EXP_RE = re.compile(r'(?:विस्तृत व्याख्या|व्याख्या|Explanation|समाधान)[\s\:\*]*(.*)', re.IGNORECASE)

def parse_mcqs_from_text(text):
    """Parses standard Hindi competitive exam MCQs from markdown text."""
    mcqs = []
    # Match questions starting with **प्रश्न <N>.** or ### प्रश्न <N> or **Q<N>.**
    q_blocks = re.split(r'\n(?=(?:\*\*|###\s*)?(?:प्रश्न|Question|Q)\s*\d+[\.:\s])', text)
    
    for b in q_blocks[1:]:
        lines = [l.strip() for l in b.strip().split('\n') if l.strip()]
        q_lines = []
        options = []
        correct_idx = None
        explanation = None

        for line in lines:
            if line.startswith('## '):
                break
            if line.startswith('---') or line.startswith('### प्रारूप'):
                continue

            ans_m = ANS_RE.search(line)
            if ans_m and correct_idx is None:
                mapping = {'A': 0, '1': 0, 'B': 1, '2': 1, 'C': 2, '3': 2, 'D': 3, '4': 3}
                correct_idx = mapping.get(ans_m.group(1).upper(), 0)
                continue

            exp_m = EXP_RE.search(line)
            if exp_m:
                exp_text = re.sub(r'^\*+|\*+$', '', exp_m.group(1).strip())
                explanation = exp_text
                continue

            opt_m = OPT_RE.match(line)
            if opt_m and len(options) < 4:
                options.append(opt_m.group(2).strip())
                continue

            if not options and not correct_idx:
                ql = re.sub(r'^(?:\*\*|###\s*)?(?:प्रश्न|Question|Q)\s*\d+[\.:\s]*\**\s*', '', line).strip()
                if ql:
                    q_lines.append(ql)
            elif explanation:
                cl = line.lstrip('> *').strip()
                if cl:
                    explanation += ' ' + cl

        if q_lines and len(options) == 4 and correct_idx is not None:
            mcqs.append({
                'question': ' '.join(q_lines),
                'options': options,
                'correctIndex': correct_idx,
                'explanation': explanation or 'विस्तृत समाधान अध्याय में समझाया गया है।'
            })

    return mcqs

def clean_reading_content_and_extract_mcqs(chapter):
    """
    Given a chapter from RASSetu JSON, extracts MCQs and strips the quiz section
    from content blocks so the reading view is clean.
    """
    extracted_mcqs = list(chapter.get('mcqs', []))
    new_content = []
    in_quiz_section = False

    for block in chapter.get('content', []):
        val = block.get('value', '')
        
        # Check if this block enters the quiz / MCQ section
        is_quiz_start = bool(re.search(
            r'##\s*\d+\.\d+\s*परीक्षा-उपयोगी|##\s*भाग\s*5|###\s*प्रारूप\s*1\b|'
            r'##\s*(?:बहुविकल्पीय|उच्च-प्रतिफल बहुविकल्पीय|अभ्यास MCQs)',
            val
        ))
        
        if is_quiz_start:
            in_quiz_section = True
            
        if in_quiz_section:
            # Check if this block is a later section like One-Liners or Cross-References
            is_post_quiz = bool(re.search(
                r'##\s*\d+\.\d+\s*(?:एक-पंक्ति|त्वरित पुनरावृत्ति|अंतर-अध्याय|Cross-Reference)|##\s*भाग\s*6',
                val
            ))
            if is_post_quiz:
                in_quiz_section = False
                new_content.append(block)
                continue
            
            # Extract questions from this block if any
            found_mcqs = parse_mcqs_from_text(val)
            extracted_mcqs.extend(found_mcqs)
            # Do NOT add to reading content
        else:
            new_content.append(block)

    chapter['content'] = new_content
    chapter['mcqs'] = extracted_mcqs
    return chapter

def fix_all_rassetu_books():
    print("--- Upgrading RASSetu Books 1-6 ---")
    ras_files = sorted(glob.glob('assets/content/rassetu/rassetu_book*.json'))
    for path in ras_files:
        with open(path, 'r', encoding='utf-8') as f:
            data = json.load(f)
            
        data['subject'] = 'RASSetu'
        book_title = data.get('book', '')
        # Normalize redundant book label
        book_title = re.sub(r'^(?:पुस्तक\s*\d+[\:\s]*)+', 'पुस्तक ', book_title)
        data['book'] = book_title

        total_mcqs = 0
        for ch in data.get('chapters', []):
            clean_reading_content_and_extract_mcqs(ch)
            total_mcqs += len(ch.get('mcqs', []))

        with open(path, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)

        print(f"✓ Fixed {os.path.basename(path)}: {len(data['chapters'])} chapters, {total_mcqs} total MCQs")

if __name__ == '__main__':
    fix_all_rassetu_books()
