# Chapter completeness and practice improvements

## Reading content

Restored omitted source paragraphs while preserving existing lesson edits, chapter IDs, questions, and answer keys. RAS Book 2 Chapter 1 now contains 50 reading blocks, compared with the previous 35, including the missing geography sections and final revision material.

Removed the 15/35/40-block caps from the old importers. Shared reading extraction recognizes dedicated quiz headings, retains worked examples and mentions of MCQs in teaching prose, and resumes reading content for revision sections after practice.

`tools/audit_chapter_completeness.py` audits every chapter JSON in the content directory, including the unregistered UGC NET English collection. Its default is read-only; `--repair` restores confirmed omissions. The final audit compared all 1,863 records with sources or verified import snapshots and found zero remaining omissions. Results are saved in `artifacts/chapter_completeness_audit.json`. Source folders can be supplied with `--source-root`.

## Practice

- Skip clears an unchecked selection, awards no credit, and advances to the next question. Previous allows the learner to revisit it. Skipping the last question opens results.
- 50–50 hides exactly two incorrect options, always keeps the correct answer, and can be used once per question. Questions with fewer than four options omit the lifeline.
- Hidden options and skipped questions persist when practice is resumed. A restart resets both. If the lifeline removes a selected option, that selection is cleared.
- Results show skipped/unanswered questions separately and provide their answer explanations for review. The score remains correct checked answers divided by all questions.

## Verification

- Full Flutter suite: 130 tests passed (`artifacts/chapter_quiz_all_tests.log`).
- Chapter, lifeline, and learning-flow regressions: 25 tests passed (`artifacts/chapter_quiz_tests.log`).
- Import extraction: 2 Python regression tests passed.
- Static analysis of the changed Dart screen and new tests: no issues.
- Original M.Sc. Physics imports independently rechecked with `python tools/import_msc_physics.py --check`.
- Release Android APK built successfully: `apk_output/SetuLearning-Chapters-Skip-50-50.apk`. Packaged book JSON files were checked byte-for-byte against the updated workspace.
