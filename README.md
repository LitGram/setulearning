# Setu Learning (सेतु लर्निंग) Android App

**Setu Learning** is a modern, offline-first educational Flutter application built for school and competitive exam students using the **Setu book series** (MathSetu, EnglishSetu, VigyanSetu).

---

## 🌟 Key Architectural Highlights

1. **100% Offline-First Architecture**:
   - Zero dependence on a live backend server for core reading and practice.
   - All 24 books (8 books per subject across MathSetu, EnglishSetu, and VigyanSetu) are bundled as clean JSON assets in `assets/content/`.
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
│   │   ├── mathsetu/          # mathsetu_book1.json to book8.json
│   │   ├── englishsetu/       # englishsetu_book1.json to book8.json
│   │   └── vigyansetu/        # vigyansetu_book1.json to book8.json
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
