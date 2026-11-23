# Add the four M.Sc. Physics guides to Setu Learning

Work in `D:\new projects\setu learning android app` and add the following four complete English books from `D:\new projects\ras books\msc physics guide`:

1. **Mathematical Physics** — `Mathematical_Physics_MSc_Guide_English.md`
2. **Classical Mechanics** — `Classical Mechanics M.Sc Guide (English).md`
3. **Quantum Mechanics I** — `Quantum Mechanics I M.Sc Guide (English).md`
4. **Statistical Physics** — `Statistical Physics MSc Guide (PHY6.0-CC-104).md`

Matching publication EPUBs are available for comparison:

- `Mathematical_Physics_MSc_Guide_English.epub`
- `Classical_Mechanics_MSc_Guide_English.epub`
- `Quantum_Mechanics_I_MSc_Guide_English.epub`
- `Statistical_Physics_MSc_Guide_English.epub`

Create a dedicated **M.Sc. Physics** section with subject ID `mscphysics` and JSON assets under `assets/content/mscphysics/`. Register all four books in the catalog and Flutter asset declarations. Keep the original source folder read-only and preserve unrelated existing app changes.

Use the complete English Markdown manuscripts as the primary sources. The Hindi Mathematical Physics edition, individual `unit1.md`/`unit2.md`/`unit3.md` files, standalone Mathematical Physics Unit 2 guide, outline, and authoring instructions are alternate or partial materials; do not add them as extra books.

Remove only book-level front matter: covers/title pages, author/compiler credits, copyright, dedication, printed table of contents, and introductory pages before the first actual teaching unit. Start reading at the first teaching unit. Retain all teaching content, derivations, solved numericals, diagrams, examples, formula/revision sheets, chapter exam tips, model question banks, educational appendices, and references.

Create navigable chapters from actual units and topic headings, in source order. Statistical Physics uses a different heading hierarchy from the other books, so inspect each manuscript before splitting it. Derive chapter counts from the imported content; avoid arbitrary page chunks or artificial chapter counts.

Format content for the existing mobile Markdown/TeX renderer. Preserve equations, Greek symbols, subscripts/superscripts, matrices, vectors, operators, tables, lists, and derivation steps accurately. Check for broken math delimiters, visible formatting artifacts, missing text, duplicate lessons, and small-screen overflow. Keep existing practice questions and solutions; generate interactive MCQs only where the source supplies genuine choices and an explicit answer key.

Use the existing chapter and quiz screens so the app's Android screenshot protection applies automatically. Screenshots must remain enabled on the library, section, and chapter-list screens and blocked while chapter content or chapter quizzes are open. Preserve reading progress, bookmarks, search, and navigation.

Create a repeatable importer scoped to these four books, clean Markdown copies, and an import audit. Verify complete coverage against the sources, catalog/schema integrity, asset loading, math rendering, and navigation. Run relevant tests and static analysis, build a release APK containing both these books and the existing 100 Great Works section, verify the packaged assets, and provide the APK path with a concise completion report. Report any source or rendering limitation accurately.
