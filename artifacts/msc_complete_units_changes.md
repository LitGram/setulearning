# Complete M.Sc. teaching units — 5 October 2026

The old importer split unit introductions, theory subsections, solved examples, practice, exam strategy, and revision sheets into separate app chapters. Mathematical Physics started with a 363-character introduction presented as a standalone chapter, while the rest of Unit 1 appeared elsewhere in the chapter list.

All four guides now group each full teaching unit together. Individual source subsections remain small content blocks inside the unit, so long chapters render lazily while scrolling.

| Guide | Complete units | Separate appendices | Total chapters |
|---|---:|---:|---:|
| Mathematical Physics | 3 | 3 | 6 |
| Classical Mechanics | 3 | 3 | 6 |
| Quantum Mechanics I | 3 | 3 | 6 |
| Statistical Physics | 3 | 4 | 7 |

Every retained source character remains in its original order. The repeatable importer verifies both independent source payload hashes and publication headings/equation blocks. No source files were changed and no questions were invented.

Old subsection history links resolve to the corresponding full unit. Legacy subsection read flags remain stored but do not count as completion of a larger unit; units can be marked read after studying the complete content. Old section-specific reading offsets are not applied to the larger units.

Verification:

- All 1,694 current chapter records compared with available source files or verified import snapshots; zero remaining omissions in the completeness audit.
- All 133 Flutter tests passed, including independent rendered-text comparisons for every M.Sc. chapter, compact-screen rendering, reader navigation, both UGC NET books, and Skip/50–50 regressions.
- Changed Dart code passed static analysis with no issues.
- `python tools/import_msc_physics.py --check` passed.

Evidence: `artifacts/msc_complete_units_all_tests.log`, `artifacts/mscphysics_import.json`, and `artifacts/chapter_completeness_audit.json`.
