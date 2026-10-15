# Setu Learning (सेतु लर्निंग) Android App

**Setu Learning** is an offline-first educational Flutter application for school, college, and competitive exam preparation. Its library contains MathSetu, EnglishSetu, VigyanSetu, RASSetu, **100 Great Works of All Time**, and **M.Sc. Physics**. Each subject can contain as many complete, well-formatted books as its catalog needs.

---

## 🌟 Key Architectural Highlights

1. **100% Offline-First Architecture**:
   - Zero dependence on a live backend server for core reading and practice.
   - Books are bundled as JSON assets in `assets/content/`; the catalog supports a different number of books for every subject.
   - Clean Markdown source copies of the formatted MCQ books are kept in `books_markdown/`; the app uses their cleaned JSON versions.
   - SQLite database (`sqflite`) locally persists read chapters, quiz scores, and the user's last reading position.

2. **Material 3 Design System**:
   - Uses `useMaterial3: true`.
   - Distinct dynamic subject palettes using `ColorScheme.fromSeed()`:
     - **MathSetu**: Royal Indigo (`#1E40AF`)
     - **EnglishSetu**: Emerald Teal (`#0F766E`)
     - **VigyanSetu**: Rust Amber (`#C2410C`)
   - Standard typography (`textTheme.titleLarge`, `bodyLarge`, `labelMedium`) conforming to Google's Material 3 standard.

3. **Strict Accessibility Standards (Section 6.4)**:
   - **Minimum 48×48 dp Tap Targets**: All buttons, cards, and list tiles maintain a minimum hit boundary with at least 8dp spacing.
   - **Contrast Compliance**: Strict ≥ 4.5:1 text-to-background contrast ratio (≥ 3:1 for large headings).
   - **Multimodal Status Indicators**: Status is never indicated by color alone; every badge includes both an icon and text (e.g. `[✓] पठित`, `[★] स्कोर`).
   - **Font Scaling Support**: Responsive layouts that respect Android system text size adjustments, plus an in-app font scale slider (85% to 135%).
   - **Semantic Labels**: All interactive icons and cards include screen-reader (`Semantics`) descriptions for TalkBack support.
   - **Explicit Navigation**: Physical, visible buttons for "Previous", "Next", and "Back" — never reliant on gesture-only navigation.

4. **Interactive Practice Quizzes**:
   - Multiple choice questions (MCQs) with instant tactile ripple feedback.
   - Automated score recording to SQLite database.
   - Detailed result summaries with explanations for every question.
   - Retake quiz and return-to-chapter flows.

---

## 📂 Project Directory Structure

```
setu learning android app/
├── android/                   # Native Android wrapper & Manifest
│   └── app/src/main/
│       ├── AndroidManifest.xml # com.setulearning.app
│       └── kotlin/.../MainActivity.kt
├── assets/
│   ├── content/               # Bundled JSON books
│   │   ├── mathsetu/
│   │   ├── englishsetu/
│   │   ├── vigyansetu/
│   │   ├── rassetu/
│   │   ├── rassetu_supplementary/
│   │   ├── greatworks/
│   │   └── mscphysics/
│   ├── icons/
│   └── images/
├── lib/
│   ├── main.dart              # App entry point, MultiProvider setup
│   ├── models/                # Subject, Book, Chapter, MCQ, UserProgress
│   ├── providers/             # ThemeProvider, ProgressProvider
│   ├── screens/               # Home, Subject, Book, Chapter, Quiz, Progress, Settings
│   ├── services/              # ContentService (JSON loader), DatabaseHelper (sqflite)
│   ├── theme/                 # AppTheme (Material 3 with ColorScheme.fromSeed)
│   └── widgets/               # AccessibleCard, StatusBadge, ContentBlockWidget
├── test/                      # Model & schema unit tests
└── pubspec.yaml               # Dependencies & asset declarations
```

---

## 📖 Chapter JSON Schema

The **M.Sc. Physics** section (`mscphysics`) contains four complete English guides:
Mathematical Physics (67 chapters), Classical Mechanics (48), Quantum Mechanics I
(52), and Statistical Physics (27). Chapter boundaries follow the manuscripts'
actual units, topics, exam/revision sections, and educational appendices. Reading
begins at Unit 1; book-level title/author pages, prefaces, introductory syllabus
pages and printed contents are excluded. All subsequent teaching content and
references are retained. Existing open-answer questions and worked solutions
remain reading content; the sources do not supply keyed MCQs.

Regenerate only these four assets, their clean Markdown copies and generated
catalog with `python tools/import_msc_physics.py`. Use `--source-root` if the source
folder moves and `--check` to verify repeatability without rewriting outputs.
Original sources in `D:\new projects\ras books\msc physics guide` are read only.
Clean copies are in `books_markdown/mscphysics/`; hashes, excluded line ranges,
formatting repairs, chapter inventory, complete retained-character coverage and
publication EPUB comparisons are in `artifacts/mscphysics_import.json`.

The manuscripts use Unicode equations and literal notation, not TeX. The import
preserves those equations and matrix/derivation layouts without speculative
conversion. Fenced equations and wide tables scroll horizontally in the existing
offline Markdown reader. A stray equation fence in Mathematical Physics is
repaired; the repeated formula beside it is retained. All chapters are tested for
visible text preservation and overflow at 320px with enlarged text. Run
`flutter test test/msc_physics_test.dart` for Physics asset, rendering, chapter
search, Next/Previous and screenshot-protection verification.

The **100 Great Works of All Time** section contains six critical guides covering
novels, plays, poems, short stories, essays, and literary criticism. Each has 100
lessons, in the source book's reading order. Publication title pages, author credit
pages, copyright, dedications, introductory notes, printed contents, and part
divider pages are excluded; the app supplies its own chapter navigation. Literary
authors, work details, quotations, and source references within lessons are retained.
These are reading guides and contain no invented practice quizzes.

Regenerate only these six assets with `python tools/import_great_works.py`. The
importer reads the publication EPUBs in `D:\new projects\100 great works\manuscript`
(including the revised short stories edition), preserving Markdown headings,
emphasis, quotations, verse line breaks, and lists. Clean Markdown copies are in
`books_markdown/great_works/`; source hashes and excluded pages are recorded in
`artifacts/great_works_import.json`. To check every retained character through the
app's Markdown parser, run:

```powershell
dart run tools/audit_great_works.dart > artifacts/great_works_rendered_text.json
python tools/import_great_works.py --verify-render artifacts/great_works_rendered_text.json
```

On Android, chapter readers and chapter quizzes enable `FLAG_SECURE` while open.
Screenshots and screen recordings remain available on the library, subject, and
chapter-list screens. Capture is restored after the last protected route finishes
closing; content waits for Android to confirm protection before being displayed.

Each book file (e.g., `mathsetu_book1.json`) follows this schema:

```json
{
  "subject": "MathSetu",
  "book": "पुस्तक 1: गणना कौशल, संख्या पद्धति एवं सरलीकरण",
  "chapters": [
    {
      "id": "ch1",
      "title": "अध्याय 1: गणना की तैयारी और मानसिक गणित",
      "subtitle": "Calculation Readiness and Mental Mathematics",
      "content": [
        {
          "type": "text",
          "value": "अवधारणात्मक व्याख्या..."
        },
        {
          "type": "callout",
          "value": "महत्वपूर्ण परीक्षा बिंदु या सूत्र..."
        },
        {
          "type": "formula",
          "value": "n × 25 = (n ÷ 4) × 100",
          "caption": "त्वरित गणना सूत्र"
        },
        {
          "type": "image",
          "value": "diagram_name.png",
          "caption": "चित्र विवरण"
        }
      ],
      "mcqs": [
        {
          "question": "24 × 25 का मान क्या होगा?",
          "options": ["500", "600", "550", "625"],
          "correctIndex": 1,
          "explanation": "24 ÷ 4 = 6; 6 × 100 = 600"
        }
      ]
    }
  ]
}
```

---

## 🚀 How to Run and Build

### Prerequisites
- Flutter SDK (≥ 3.0.0)
- Android Studio / Android SDK (Platform 34, Build-Tools)

### Commands

1. **Install Dependencies**:
   ```bash
   flutter pub get
   ```

2. **Run on Device or Emulator**:
   ```bash
   flutter run
   ```

3. **Run Unit & Schema Tests**:
   ```bash
   flutter test
   ```

4. **Build Release APK (Direct Install)**:
   ```bash
   flutter build apk --release
   ```

5. **Build Release Android App Bundle (Google Play Store)**:
   ```bash
   flutter build appbundle --release
   ```

## Release to Indus Appstore

Setu Learning is already listed on Indus Appstore with package name `com.litgram.setulearning`. The GitHub Actions workflow at `.github/workflows/release-indus.yml` builds a release AAB and submits updates to that existing listing.

Before running it:

1. In the Indus Developer Platform, open **Tools & Resources** and enable the **Indus App Update API**. Keep the generated API token private.
2. In this GitHub repository, open **Settings → Secrets and variables → Actions** and add these repository secrets:
   - `INDUS_APP_STORE_API_TOKEN` — the token from Indus.
   - `KEYSTORE_BASE64` — the base64-encoded JKS keystore used to sign the already-published Android app.
   - `KEYSTORE_PASSWORD`, `KEY_ALIAS`, and `KEY_PASSWORD` — the matching signing credentials.
3. Open **Actions → Build and release to Indus Appstore → Run workflow**. Enter a version name and a version code greater than the one currently published. The workflow runs only when started manually.

The first app submission must be completed manually in the Indus Developer Platform. Never commit the API token, keystore, or signing passwords to this repository. AAB updates must use the same signing key as the published app.
