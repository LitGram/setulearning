# Setu Learning UI improvement plan

Prepared 1 October 2026 using mobile-app-ui-design, mobile-app-ux-auditor, ui-ux-pro-max, and flutter-expert.

## Findings and priorities

This is a code-based audit of the current working tree, not a verified device walkthrough. Setu is an offline-first, Hindi/English learning library for school, college, and exam preparation. The main job is finding a relevant chapter, reading comfortably, practicing, and returning to unfinished learning.

| Priority | Screen or flow | Evidence | Impact | Planned change |
| --- | --- | --- | --- | --- |
| P1 | Reading progress | `lib/screens/chapter_screen.dart:42` marks a chapter read immediately on opening; `lib/providers/progress_provider.dart:111` also marks it read after a quiz. | Completion totals can describe opened or practiced chapters as completed reading. | Separate started, reading completed, and practiced states. Offer an explicit “पढ़ लिया” action near the chapter ending. Decide how legacy read flags are labeled before migrating them. |
| P1 | Continue reading | `LastPosition` in `lib/models/user_progress.dart` stores chapter identity, but no position inside it. The reader scroll controller does not persist its position. | Returning learners restart long chapters at the top. | Save a content-block anchor and intra-block position per chapter; restore after layout. Keep a pixel offset as fallback, clamp invalid positions, and handle changed text size or content. |
| P1 | Quiz interruption | Answers and score live only in `QuizScreen` state; there is no exit guard or persisted attempt. | Back navigation or process loss can discard an unfinished practice session. | Persist the current attempt locally; resume or restart explicitly. Add an exit dialog when an attempt is unfinished, with a clear save-and-exit action. |
| P1 | Progress recovery | `ProgressProvider.loadProgress` catches database errors and only prints them; Home and Progress do not represent the loading/error state. | A failed load can look like no previous study. | Distinguish loading, true empty, loaded, and failed states; offer retry without preventing offline reading. Show score-save failure and retry before claiming results were saved. |
| P2 | Home hierarchy | `home_screen.dart` places a repeated brand hero before Continue Reading and repeats offline information below the subjects. | Useful next actions receive less prominence. | Keep compact branding in the app bar. Put Continue Reading first for returning learners; show subject selection first for new learners. Reduce repeated offline copy to one quiet indicator. |
| P2 | Discovery | Subject and book screens list the full catalog without search or filters. | Finding a specific book or chapter requires scanning long lists. | Add offline book/chapter title search with Hindi and English matching, clear scope, recent queries, useful no-results guidance, and optional Unread/In progress filters. Index metadata first; avoid parsing every full book on each keystroke. |
| P2 | Reader controls | Two text-size actions compete with long titles in the app bar; practice is placed after all content. | Limited title space and poor visibility of available practice. | Consolidate reader settings into an “Aa” sheet with size preview, theme, and reset. Keep visible Previous/Next controls and add a labeled practice shortcut when questions exist. |
| P2 | Adaptive layout | Home switches to a navigation rail at 600 logical pixels; reader/content widths and action rows still need device verification. | Wide reading lines and large-text overflow remain risks. | Bound reading width to roughly 640–720 logical pixels; use available space for chapter navigation on wide layouts. Wrap or stack action rows when content does not fit. |
| P2 | Accessibility | Meaningful content images lack a semantic label in `content_block_widget.dart`; quiz cards describe selection but not explicit correct/incorrect semantic state. | Diagrams and answer feedback may be incomplete with TalkBack. | Add useful diagram descriptions, exclude decorative images, announce checked-answer feedback, and expose selected/disabled states without duplicate labels. |
| P3 | Visual consistency | Screens use repeated custom containers, variable spacing, mixed bilingual button labels, and raw subject seed colors. | A less coherent interface and possible dark-theme contrast issues. | Introduce shared spacing/surface/type tokens and semantic subject colors; use concise Hindi action labels with English support in secondary copy. Validate actual contrast before replacing colors. |

No P0 issue was established in this static review.

## Proposed visual direction

Use a calm, study-focused Material 3 interface. Preserve the indigo brand, recognizable subject accents, bottom navigation/large-screen rail, offline operation, and existing light/dark choices. Prioritize readable Hindi and English over decorative typography.

- Use theme roles for surfaces and text, reserving strong accents for the primary action and progress feedback.
- Standardize spacing around 4/8/12/16/24/32; keep compact phone card padding around 16–20 and radius roles around 12/16/20.
- Define four principal text roles (screen title, section title, body, supporting label), with content-specific headings where needed. Preserve system scaling and check its interaction with the existing in-app font multiplier.
- Use a single consistent Material icon family and labeled unfamiliar actions.
- Use brief state transitions only when they clarify selection or completion; honor reduced motion. Avoid decorative animation during reading.
- Preview long Hindi titles, English literature titles, equations, tables, and MCQ explanations before choosing final typography.

The UI/UX Pro Max generator was run. Its education preset suggested child-oriented fonts, a marketing showcase structure, and avoiding dark mode. Those suggestions do not fit this exam-preparation reader; use its interaction/accessibility guidance while retaining Setu’s identity and dark mode.

## Flow changes

New learner, current: Home → Subject → Book → Chapter → Practice.

New learner, proposed: Same direct route, with clearer subject/book hierarchy and optional search → Chapter → explicitly finish reading or Practice. No extra onboarding gate.

Returning learner, current: Home → Continue Reading → chapter beginning.

Returning learner, proposed: Home → prominent Continue Reading → saved content location. An unfinished quiz offers Resume practice separately.

Quiz, proposed: Select option → Check answer → labeled feedback/explanation → Next → results with saved status → Review incorrect answers, retry, or return to chapter. Saving failures retain the attempt and provide retry.

Progress, proposed: Meaningful completion totals → subject/book detail → continue unfinished reading or review weaker quiz chapters. Move Reset All Progress to Settings, preserving its confirmation dialog.

## Implementation sequence

1. **Establish a visual baseline and design tokens.** Capture current Home, book list, reader, quiz, results, Progress, and Settings on a compact phone. Produce proposed Home/reader/quiz previews, then centralize tokens in `lib/theme/app_theme.dart` and shared widgets. Acceptance: readable long titles and coherent light/dark variants.
2. **Fix continuity and progress semantics.** Update `chapter_screen.dart`, `user_progress.dart`, `progress_provider.dart`, and `database_helper.dart`. Add migration handling for existing data and loading/error states. Acceptance: opening a chapter does not imply completion; relaunch restores the correct chapter and location; existing progress remains available.
3. **Improve Home and discovery.** Update Home, Subject, Book, and `content_service.dart`. Introduce a shared search/list presentation, simple metadata, and distinct empty/no-results states. Acceptance: returning users resume with one tap; known Hindi or English titles are findable offline; first-time users see the subjects immediately.
4. **Polish the reading experience.** Add reader settings, bounded content width, accessible diagram descriptions, chapter navigation, and the practice shortcut. Acceptance: tables and formulas remain usable, title/context stay understandable, and font changes do not lose the reading location.
5. **Make practice recoverable and actionable.** Update Quiz and local persistence. Separate selected answers from checked answers, save drafts, show save feedback, and add incorrect-answer review. Acceptance: back/relaunch preserves unfinished work, revisiting checked questions does not inflate scores, and failed saves can be retried safely.
6. **Refine Progress and Settings; verify the whole journey.** Add useful empty-state guidance and links back to learning. Check large text, TalkBack, dark theme, layout changes, local-storage failures, and process restoration.

Keep Provider, Navigator, SQLite, and the current content model unless an individual requirement demonstrates a need to change them. Build reusable `ResumeStudyCard`, `StudyStatusBadge`, `ReaderSettingsSheet`, and state panels rather than duplicating screen styling. Prefer lazy lists for expanding catalogs and avoid rebuilding all reading content for unrelated progress changes.

## Verification and acceptance

- Test a compact phone around 360 logical pixels wide, a larger phone, landscape, and a tablet/wide window. Include Hindi/English long strings and Android system text scale up to 200%, combined with the app’s maximum font setting.
- Use TalkBack to complete Home → Book → Reader → Quiz → Results; verify focus order, selected/correct/incorrect feedback, meaningful images, and no duplicated announcements.
- Check 48×48 logical-pixel Android tap targets and normal-text contrast of at least 4.5:1 in actual light/dark surfaces.
- Add targeted widget tests for layout/semantics and state transitions; persistence tests for reading anchors, quiz drafts, migrations, and failure recovery. Use Flutter’s accessibility guideline APIs where applicable.
- Run `flutter analyze` and the existing tests after implementation. Capture before/after screenshots and perform a real offline/background/process-restart walkthrough. Do not regard passing unit tests as visual approval.
- Measure usability through task success: find a known chapter, resume a long chapter, finish practice, and understand the next useful action. Do not invent engagement targets without a baseline.

Flutter references: [adaptive best practices](https://docs.flutter.dev/ui/adaptive-responsive/best-practices), [accessible styling](https://docs.flutter.dev/ui/accessibility/ui-design-and-styling), and [accessibility testing](https://docs.flutter.dev/ui/accessibility/accessibility-testing).

## Audit evidence and limitations

The focused static scan inspected 22 files under `lib` and produced 57 P1 and 2 P2 heuristic flags, saved in `ux-static-scan.json`. It misclassified Flutter `Icon` usages as Android Compose and requested `contentDescription`; those are false-positive framework recommendations, not 57 confirmed severe issues. Flutter images and semantic-state concerns were reviewed separately.

Reviewed the seven screens, navigation, theme, progress model/provider, reader controls, and shared content/accessibility widgets. Ran the skill’s design-system and Flutter guideline searches. No emulator, rendered current screenshots, TalkBack session, contrast measurement, or runtime performance profiling was performed. Adaptive issues are verification risks until reproduced. This task creates a plan and scan report only; app source and pre-existing working-tree edits are untouched.
