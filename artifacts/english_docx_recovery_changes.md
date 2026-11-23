# English source recovery — 5 October 2026

All 11 English Word imports were rebuilt from their original document XML. The old importer read paragraphs first and appended tables afterward; its cleanup could remove the entire opening group if any part contained cover or author material. That discarded teaching text in several books and left the Second Grade Complete Guide with only 36 table chapters.

The recovery preserves all retained teaching paragraphs, metadata about literary authors, source questions, explanations, tables, and illustrations in document order. Chapter boundaries follow source chapter headings; summaries and subordinate sections stay with their chapters. Heading-only fragments are merged with their material. No arbitrary paragraph or chapter-size cap is used.

- All 36 Second Grade guide tables are back beside their related text.
- All 23 original illustrations in the First Grade Literature MCQ book are restored and verified against source image bytes.
- Previously keyed practice questions and answer keys are preserved; exact duplicates appear once. No new keys are guessed. Other original questions remain in the reading content.
- Phonetics and the grammar glossary have no reliable source chapter divisions, so each remains a complete guide rather than being split at arbitrary paragraph counts.
- Rebuilt English chapters use new IDs. Old read flags and offsets are not applied to these larger sections; their records remain stored. Existing M.Sc., UGC NET, Skip, and 50–50 behavior remains covered by tests.

The repeatable recovery tool is `tools/recover_english_docx.py`. Its `--check` mode verifies deterministic source recovery and original images. The legacy Word import now uses the same ordered recovery, and the old broad cleanup skips verified Word books.

Verification:

- Independent original Word text versus Markdown visibility checks passed for every recovered section.
- Every original illustration decoded successfully; all 36 tables passed compact-phone rendering checks.
- All 146 Flutter tests passed; changed Dart code has no static-analysis issues.
- All 53 book files / 1,817 current chapter records passed the completeness audit.
- Release APK: `apk_output/SetuLearning-English-Content-Restored.apk`. All 53 packaged book files and 23 Word illustrations were checked against the recovered workspace/source hashes.

Evidence: `artifacts/english_docx_recovery.json`, `artifacts/english_recovery_all_tests.log`, `artifacts/chapter_completeness_audit.json`, and `artifacts/english_recovery_android_build.log`.
