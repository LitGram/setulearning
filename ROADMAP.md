# Setu Learning — User-Experience Roadmap

Changes suggested from a student's point of view after reviewing the app
(23 Nov 2026). Work through them in order unless told otherwise. When an item
is finished, tick its box, add the date and the branch, and note anything left over.

Status key: `[ ]` not started · `[~]` in progress · `[x]` done

---

## Priority 1 — things that get in the way

### 1. [x] Group the home screen by learner type ("shelves") — done 2026-11-23
- **Problem:** Home shows ~19 subjects in one long list. A Class 10 student
  scrolls past UGC NET and M.Sc. Physics; a RAS aspirant scrolls past Punjabi.
- **Change:** Group subjects into shelves — कक्षा 10 (RBSE), प्रतियोगी परीक्षाएँ
  (MathSetu, EnglishSetu, VigyanSetu, RASSetu), UGC NET, कॉलेज व साहित्य
  (M.Sc. Physics, 100 Great Works). On first launch ask "आप किसकी तैयारी कर रहे
  हैं?"; remember the answer; keep a "सभी" (All) choice that shows every shelf
  with section headers. The choice can be changed any time from chips at the top.
- **Where:** `lib/screens/home_screen.dart` (`_SubjectHomeScreen`),
  subject → shelf mapping in a new `lib/models/shelf.dart`, saved with
  `shared_preferences`.
- **Branch:** `feature/home-shelves`

### 2. [ ] Smaller install — download books on demand (deferred)
- **Problem:** The APK is ~133 MB because ~190 MB of book JSON is bundled in
  `assets/content/`. Students on cheap phones / limited data struggle.
- **Change:** Ship a small app (maybe one starter book per shelf). Let the
  student download only the shelves/books they want; they stay offline after
  download. Alternatively use Play Asset Delivery / Android App Bundle splits.
- **Where:** `pubspec.yaml` asset list, `lib/services/content_service.dart`
  (`loadBookContent`), new download manager + storage under app documents dir.
- **Note:** Biggest effort item. Needs a hosting location for the JSON files.

### 3. [x] Remove "प्रथम प्रारूप" (first draft) labels shown to users — done 2026-11-23
- **Problem:** Science, Sanskrit and Punjabi taglines/titles say "प्रथम प्रारूप"
  / "(प्रारूप)", which makes students doubt the content.
- **Change:** Finish those books, or drop the label from user-facing text.
- **Where:** `lib/services/content_service.dart` (subject taglines, book titles).
- **Branch:** `feature/home-shelves` (small change, done on the current branch)

### 4. [ ] One interface language setting (Hindi / English)
- **Problem:** Buttons are English ("Previous", "Next", "Mark as read",
  "Choose a subject") while descriptions are Hindi.
- **Change:** Add a language choice in Settings and route all UI strings through
  it (Flutter `intl` / ARB files, or a simple strings map).
- **Where:** all of `lib/screens/` and `lib/widgets/`, `settings_screen.dart`.

## Priority 2 — missing features

### 5. [ ] Bookmarks, highlights and personal notes
- Mark a paragraph/formula/PYQ, add a short note, and see all bookmarks in one
  list (per book and global). Biggest everyday gap.
- **Where:** `chapter_screen.dart` (block-level long-press using the existing
  `_blockKeys` anchors), new table in `lib/services/database_helper.dart`,
  new "Bookmarks" screen reachable from the bottom navigation.

### 6. [ ] Full-text search inside chapters
- Search currently matches only book and chapter titles
  (`lib/screens/search_screen.dart`). Searching "Ohm's law" or "मेवाड़" should
  find the paragraph and open the chapter scrolled to it.
- **Where:** build a background index from loaded book JSON (isolate), reuse the
  block-anchor scrolling in `chapter_screen.dart`.

### 7. [ ] "My mistakes" revision deck
- Quiz results already list incorrect answers (`quiz_screen.dart`, "Review
  incorrect answers"). Persist wrong answers across all chapters and offer a
  practice mode of only those, removing a question once answered right twice.
- **Where:** `database_helper.dart`, `quiz_screen.dart`, new screen.

### 8. [ ] Timed full-length mock tests
- Practice is chapter-by-chapter and labelled "वैकल्पिक". RAS / UGC NET users
  need book- or subject-level timed papers with optional negative marking.
- **Where:** new mock-test screen pulling MCQs across chapters of a book/subject.

### 9. [ ] Automatic "read" marking and % progress per book
- Students forget to tap "Mark as read" at the bottom of a chapter. Mark it
  automatically when the end is reached (keep the manual button), and show a
  percentage bar on each book card.
- **Where:** `chapter_screen.dart` (scroll listener), `subject_screen.dart`,
  `book_screen.dart`, `progress_provider.dart`.

### 10. [ ] Daily goal / streak with optional reminder
- e.g. "आज 2 अध्याय". Show the streak on home; optional local notification.
- **Where:** `progress_provider.dart`, `home_screen.dart`, settings toggle;
  needs a local-notifications package.

## Priority 3 — polish

- [ ] Book cards show "B1", "B2" avatars — use a small cover image or subject
      icon instead (`subject_screen.dart`, `_buildBookCard`).
- [ ] At the last chapter "Next" just greys out — suggest the next book or a
      whole-book test (`chapter_screen.dart`, bottom stepper).
- [ ] Screenshots are blocked in chapters (FLAG_SECURE). Fine for protection,
      but bookmarks (#5) should cover the "save this formula" need.

---

## Log
- 2026-11-23 — Roadmap written. Started #1 on `feature/home-shelves`.
- 2026-11-23 — #1 done (not yet committed). New `lib/models/shelf.dart`; home
  screen asks once, saves the choice under the `home_shelf` preference, and
  shows chips to switch. Tests: `test/home_shelves_test.dart`. Screenshots in
  `docs/screenshots/`. Not yet tried on a real Android phone (checked in a web
  build at phone size).
- Known separately: 8 book-content tests fail on the current working tree
  (`all_books_schema_test` for RBSE 10 maths/social/hindi/english and RASSetu
  book 2, `rbse10_sanskrit_test` x2, `book_math_audit_test`). These come from
  the uncommitted book JSON changes, not from the shelf work.
- Tip: to preview the UI without an emulator, run `flutter build web` and serve
  `build/web` (e.g. `python -m http.server 8765 --directory build/web`). The
  progress database does not work on web, so treat it as a visual check only.
- 2026-11-23 — #2 (on-demand downloads) deferred by the user for later; it
  still needs a decision on where to host the book JSON.
- 2026-11-23 — #3 done (not yet committed). Dropped "प्रथम प्रारूप" / "(प्रारूप)"
  from the Science, Sanskrit and Punjabi taglines and book titles, and the
  "प्रथम संपादकीय प्रारूप।" prefix from every chapter note in those three books
  (bundled JSON and the Markdown sources in `10th rbse/`). The rest of each note
  stays, because it tells students honestly what is still missing (e.g. Science:
  NCERT solutions and full PYQs still being checked), so finishing those books
  is still open. New guard test: `test/no_draft_labels_test.dart`.
