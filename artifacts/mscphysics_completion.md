# M.Sc. Physics import completion — 3 October 2026

Four complete English books are registered in the dedicated `mscphysics` section.

| Book | Chapters | Retained source lines |
|---|---:|---|
| Mathematical Physics | 67 | 109–2626 |
| Classical Mechanics | 48 | 98–1701 |
| Quantum Mechanics I | 52 | 103–1730 |
| Statistical Physics | 27 | 26–1332 |

All 194 chapters retain every non-presentation character after the first teaching unit, in source order (7,057 source lines). Only book-level front matter is omitted. Teaching, derivations, solved numericals, tables, diagrams/literal layouts, revision sheets, exam tips, question banks, educational appendices and references remain. Original source files are unchanged. No MCQs were invented: these sources contain open-answer practice without keyed multiple-choice options.

The repeatable importer is `tools/import_msc_physics.py`; clean copies are under `books_markdown/mscphysics/`, JSON assets under `assets/content/mscphysics/`, and generated catalog metadata is `lib/services/msc_physics_catalog.dart`. The existing catalog and Flutter asset declarations include the new section.

## Verification

- `python tools/import_msc_physics.py --check`: passes, including source hashes, deterministic outputs and complete retained-character coverage.
- EPUB comparison: every teaching heading and literal equation block in all four matching publication EPUBs is retained.
- `flutter test --no-pub --reporter expanded`: all 123 tests pass, including existing 100 Great Works schema/loading/navigation checks (six books, 600 lessons).
- All 194 Physics chapters pass independent visible-text comparisons through both Markdown parsing and actual Flutter widgets at 320px with 1.8× text. Wide equation/code blocks and tables use the existing horizontal scrolling.
- Physics library/section access, chapter search, reader opening, Next/Previous and return navigation pass. Chapter lists allow screenshots; reader routes request Android protection and restore capture on exit. Existing quiz protection and reading-session regressions pass.
- Full static analysis (`dart analyze`): no issues found.

Evidence: `artifacts/mscphysics_import.json`, `artifacts/mscphysics_verification.json`, `artifacts/mscphysics_all_tests.log`, and `artifacts/mscphysics_analysis_full.log`.

## Source and verification limits

Equations are supplied as Unicode and literal notation, not TeX, and were retained without speculative conversion. Mathematical Physics contains repeated/skipped topic numbers and a repeated Bessel generating formula beside a stray equation fence. Source numbering and both formula occurrences remain; the missing opening fence is repaired and recorded. Formatting escapes protect literal underscores, conjugation asterisks and angle brackets. Unrelated existing app changes and the Great Works assets were preserved.

Android screenshot checks use the native channel mock in widget tests; no new hardware-device capture test was run. The current app has no bookmark implementation to migrate; its existing reading progress, reading sessions, history, search and navigation remain in place.

**APK build deferred at the user's explicit instruction.** No updated APK was built, and packaged-APK asset verification awaits that build. Existing APK files are not the result of this import.
