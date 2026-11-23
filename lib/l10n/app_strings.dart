import 'package:flutter/widgets.dart';

/// Interface languages the app can show its buttons, labels and messages in.
/// Book content (chapter text, subject names) is not translated.
enum AppLanguage {
  hi('hi', 'हिंदी'),
  en('en', 'English');

  const AppLanguage(this.code, this.nativeName);

  final String code;

  /// The language's own name, shown in Settings so it is always readable.
  final String nativeName;

  static AppLanguage? fromCode(String? code) {
    for (final language in AppLanguage.values) {
      if (language.code == code) return language;
    }
    return null;
  }
}

/// Every user-facing interface string, in Hindi and English side by side.
///
/// Add new strings here as `_t('हिंदी', 'English')` so both languages stay
/// next to each other and neither can be forgotten.
class AppStrings {
  const AppStrings._(this.language);

  final AppLanguage language;

  static const hindi = AppStrings._(AppLanguage.hi);
  static const english = AppStrings._(AppLanguage.en);

  static AppStrings of(AppLanguage language) =>
      language == AppLanguage.hi ? hindi : english;

  String _t(String hi, String en) => language == AppLanguage.hi ? hi : en;

  // ── Common ────────────────────────────────────────────────────────────
  String get retry => _t('फिर कोशिश करें', 'Retry');
  String get cancel => _t('रद्द करें', 'Cancel');
  String get previous => _t('पिछला', 'Previous');
  String get next => _t('अगला', 'Next');
  String get practice => _t('अभ्यास', 'Practice');
  String get read => _t('पठित', 'Read');
  String get unread => _t('अपठित', 'Unread');
  String get book => _t('पुस्तक', 'Book');
  String get progressSaved => _t('प्रगति सहेजी गई', 'Progress saved');
  String get couldNotSaveProgress => _t(
      'प्रगति सहेजी नहीं जा सकी। फिर कोशिश करें।',
      'Could not save progress. Try again.');
  String bookNumber(Object n) => _t('पुस्तक $n', 'Book $n');
  String booksCount(int n) => _t(n == 1 ? '1 पुस्तक' : '$n पुस्तकें',
      n == 1 ? '1 Book' : '$n Books');
  String chaptersDone(int n) =>
      _t('$n अध्याय पूर्ण', n == 1 ? '1 chapter done' : '$n chapters done');
  String chaptersCount(int n) =>
      _t('$n अध्याय', n == 1 ? '1 chapter' : '$n chapters');

  // ── Navigation ───────────────────────────────────────────────────────
  String get navSubjects => _t('विषय', 'Subjects');
  String get navProgress => _t('प्रगति', 'Progress');
  String get navSettings => _t('सेटिंग्स', 'Settings');

  // ── Home ─────────────────────────────────────────────────────────────
  String get appTagline => _t('पढ़ाई, जब चाहो', 'Study whenever you like');
  String get searchBooksAndChapters =>
      _t('पुस्तकें और अध्याय खोजें', 'Search books and chapters');
  String get offlineTitle => _t('पूर्णतः ऑफलाइन अध्ययन', 'Fully offline study');
  String get offlineBody => _t(
      'सभी पुस्तकें एवं अभ्यास प्रश्न बिना इंटरनेट के उपलब्ध हैं।',
      'All books and practice questions work without internet.');
  String get shelfQuestion =>
      _t('आप किसकी तैयारी कर रहे हैं?', 'What are you preparing for?');
  String get shelfQuestionHint => _t(
      'हम आपकी पुस्तकें सबसे ऊपर दिखाएँगे। इसे कभी भी बदल सकते हैं।',
      "We'll show your books first. You can change this any time.");
  String get showAllSubjects => _t('सभी विषय देखें', 'Show all subjects');
  String get chooseShelf =>
      _t('पुस्तकों की श्रेणी चुनें', 'Choose a book category');
  String get allShelves => _t('सभी', 'All');
  String continueChapterSemantics(String title) =>
      _t('अंतिम पठित अध्याय जारी रखें: $title', 'Continue last chapter: $title');
  String get couldNotOpenChapter => _t(
      'अध्याय नहीं खुल सका। कृपया फिर कोशिश करें।',
      'Could not open the chapter. Please try again.');
  String get continueReading => _t('पढ़ना जारी रखें', 'Continue reading');
  String subjectCardSemantics(String name, String hindiName, int books) => _t(
      '$name, $hindiName, ${books == 1 ? '1 पुस्तक' : '$books पुस्तकें'} उपलब्ध',
      '$name, $hindiName, ${books == 1 ? '1 book' : '$books books'} available');

  // ── Subject ──────────────────────────────────────────────────────────
  String booksAvailable(int n) => _t(
      n == 1 ? '1 पुस्तक उपलब्ध' : '$n पुस्तकें उपलब्ध',
      n == 1 ? '1 book available' : '$n books available');
  String get subjectBlurb => _t(
      'अलग-अलग विषयों और परीक्षाओं के लिए अध्ययन सामग्री।',
      'Study material for different subjects and exams.');
  String get chooseBook => _t('पुस्तक चुनें', 'Choose a book');
  String bookSemantics(String title) =>
      _t('$title, विषय-आधारित पुस्तक', '$title, subject book');
  String chaptersRead(int n) =>
      _t('$n अध्याय पठित', n == 1 ? '1 chapter read' : '$n chapters read');

  // ── Book ─────────────────────────────────────────────────────────────
  String get loadingContents =>
      _t('विषय सूची लोड हो रही है...', 'Loading contents...');
  String get bookLoadError =>
      _t('पुस्तक लोड करने में समस्या आई', 'There was a problem loading the book');
  String syllabusPart(Object n) => _t('पाठ्यक्रम खंड $n', 'Syllabus part $n');
  String totalChapters(int n) => _t('कुल अध्याय: $n', 'Total chapters: $n');
  String get chapters => _t('अध्याय', 'Chapters');
  String get searchChapters => _t('अध्याय खोजें', 'Search chapters');
  String get noMatchingChapters => _t(
      'कोई अध्याय नहीं मिला। कोई दूसरा शब्द आज़माएँ या फ़िल्टर हटाएँ।',
      'No matching chapters. Try another word or clear the filter.');
  String chapterSemantics(int index, String title, bool isRead) => _t(
      'अध्याय $index: $title, ${isRead ? 'पठित' : 'अपठित'}',
      'Chapter $index: $title, ${isRead ? 'read' : 'unread'}');
  String quizScore(int score, int total, String percent) =>
      _t('स्कोर: $score/$total ($percent%)', 'Score: $score/$total ($percent%)');
  String practiceQuestionsCount(int n) => _t('$n अभ्यास प्रश्न',
      n == 1 ? '1 practice question' : '$n practice questions');

  // ── Chapter ──────────────────────────────────────────────────────────
  String get readingPositionNotSaved => _t(
      'पढ़ने का स्थान सहेजा नहीं जा सका।', 'Reading position could not be saved.');
  String get readingHistoryNotSaved => _t(
      'पढ़ने का इतिहास सहेजा नहीं जा सका।', 'Reading history could not be saved.');
  String get endOfChapterPractice =>
      _t('अध्याय-अंत अभ्यास (वैकल्पिक)', 'End-of-chapter practice (optional)');
  String chapterPracticeSummary(int n) => _t(
      'कुल प्रश्न: $n • अध्याय पढ़ने के बाद कभी भी हल करें',
      'Total questions: $n • Solve any time after reading');
  String get startOptionalPractice =>
      _t('वैकल्पिक अभ्यास शुरू करें', 'Start optional practice');
  String get readingSettings => _t('पढ़ने की सेटिंग्स', 'Reading settings');
  String get readingCompleted => _t('पढ़ना पूरा हुआ', 'Reading completed');
  String get markAsRead => _t('पढ़ लिया', 'Mark as read');

  // ── Quiz ─────────────────────────────────────────────────────────────
  String get quizTitle => _t('प्रश्नोत्तरी', 'Quiz');
  String get resumePracticeTitle =>
      _t('अभ्यास फिर से शुरू करें?', 'Resume practice?');
  String get resumePracticeBody => _t(
      'आपके अधूरे उत्तर इस डिवाइस पर सहेजे गए हैं।',
      'Your unfinished answers are saved on this device.');
  String get startAgain => _t('नए सिरे से शुरू करें', 'Start again');
  String get resume => _t('जारी रखें', 'Resume');
  String get leavePracticeTitle => _t('अभ्यास छोड़ें?', 'Leave practice?');
  String get leavePracticeBody => _t(
      'अपने उत्तर सहेजें और बाद में जारी रखें।',
      'Save your answers and resume later.');
  String get keepPracticing => _t('अभ्यास जारी रखें', 'Keep practicing');
  String get saveAndExit => _t('सहेजें और बाहर जाएँ', 'Save & exit');
  String get noQuestions =>
      _t('इस अध्याय में कोई प्रश्न नहीं हैं।', 'This chapter has no questions.');
  String get goBack => _t('वापस जाएँ', 'Go back');
  String get answersNotSaved =>
      _t('उत्तर सहेजे नहीं जा सके।', 'Answers could not be saved.');
  String questionOf(int i, int n) => _t('प्रश्न $i / $n', 'Question $i of $n');
  String score(int n) => _t('स्कोर: $n', 'Score: $n');
  String get fiftyFiftyUsed => _t('50–50 उपयोग हो चुका', '50–50 used');
  String get fiftyFiftyLifeline => _t('50–50 सहायता', '50–50 lifeline');
  String get twoOptionsRemoved =>
      _t('दो गलत विकल्प हटा दिए गए।', 'Two incorrect options removed.');
  String option(String letter) => _t('विकल्प $letter', 'Option $letter');
  String get selected => _t('चुना गया', 'Selected');
  String get correctAnswer => _t('सही उत्तर', 'Correct answer');
  String get incorrectAnswer => _t('गलत उत्तर', 'Incorrect answer');
  String notQuite(String letter) => _t('सही नहीं। सही उत्तर $letter है।',
      'Not quite. The correct answer is $letter.');
  String get explanation => _t('व्याख्या', 'Explanation');
  String get skip => _t('छोड़ें', 'Skip');
  String get checkAnswer => _t('उत्तर जाँचें', 'Check answer');
  String get nextQuestion => _t('अगला प्रश्न', 'Next question');
  String get viewResults => _t('परिणाम देखें', 'View results');
  String get practiceResults => _t('अभ्यास परिणाम', 'Practice results');
  String get greatPerformance => _t('शानदार प्रदर्शन!', 'Great work!');
  String get keepGoing => _t('अभ्यास जारी रखें!', 'Keep practising!');
  String practiceComplete(String title) =>
      _t('$title अभ्यास पूर्ण', '$title practice complete');
  String get questions => _t('प्रश्न', 'Questions');
  String get correctAnswers => _t('सही उत्तर', 'Correct answers');
  String get scoreLabel => _t('स्कोर', 'Score');
  String skippedCount(int n) =>
      _t('$n छोड़े गए / अनुत्तरित', '$n skipped / unanswered');
  String get reviewSkipped =>
      _t('छोड़े गए प्रश्न देखें', 'Review skipped questions');
  String correctAnswerIs(String answer) =>
      _t('सही उत्तर: $answer', 'Correct answer: $answer');
  String get savingProgress => _t('प्रगति सहेजी जा रही है…', 'Saving progress…');
  String get progressNotSaved => _t('प्रगति सहेजी नहीं गई', 'Progress not saved');
  String get retrySaving => _t('फिर से सहेजें', 'Retry saving');
  String get reviewIncorrect => _t('गलत उत्तर देखें', 'Review incorrect answers');
  String get backToChapter => _t('अध्याय पर लौटें', 'Back to chapter');
  String get tryAgain => _t('फिर से हल करें', 'Try again');

  // ── Search ───────────────────────────────────────────────────────────
  String get searchFieldLabel =>
      _t('हिंदी या अंग्रेज़ी शीर्षक', 'Hindi or English title');
  String get clearSearch => _t('खोज साफ़ करें', 'Clear search');
  String get preparingSearch =>
      _t('अध्याय खोज तैयार हो रही है', 'Preparing chapter search');
  String get someChaptersNotLoaded => _t(
      'कुछ अध्याय लोड नहीं हो सके। आप फिर भी पुस्तकें खोज सकते हैं।',
      'Some chapters could not be loaded. You can still search books.');
  String get searchHint => _t(
      'किसी पुस्तक या अध्याय के शीर्षक का कोई भी शब्द खोजें। बिना इंटरनेट के काम करता है।',
      'Search any word from a book or chapter title. Works offline.');
  String get recentSearches => _t('हाल की खोजें', 'Recent searches');
  String get noResults => _t(
      'कोई परिणाम नहीं। छोटा शब्द या हिंदी/अंग्रेज़ी शीर्षक आज़माएँ।',
      'No results. Try a shorter word or a Hindi or English title.');

  // ── Progress ─────────────────────────────────────────────────────────
  String get myProgress => _t('मेरी प्रगति', 'My progress');
  String get progressEmpty => _t(
      'अपना पहला अध्याय पढ़ें और अंत में “पढ़ लिया” चुनें। अभ्यास स्कोर अलग सहेजे जाते हैं।',
      'Read your first chapter and tap “Mark as read” at the end. Practice scores are saved separately.');
  String get totalChaptersDone => _t('कुल पूर्ण अध्याय', 'Chapters completed');
  String get bySubject => _t('विषयवार', 'By subject');

  // ── Settings ─────────────────────────────────────────────────────────
  /// Always bilingual, so someone who picked the wrong language can find it.
  String get languageHeader => 'भाषा / Language';
  String get readingSection => _t('पढ़ना', 'Reading');
  String get textSize => _t('अक्षर का आकार', 'Text size');
  String get textPreview => _t(
      'पूर्वावलोकन: सेतु श्रृंखला से अपनी परीक्षा तैयारी को सहज और प्रभावी बनाएं।',
      'Preview: make your exam preparation easy and effective with the Setu series.');
  String get appearance => _t('रूप-रंग', 'Appearance');
  String get systemDefault => _t('सिस्टम के अनुसार', 'System default');
  String get lightMode => _t('लाइट मोड', 'Light mode');
  String get darkMode => _t('डार्क मोड', 'Dark mode');
  String get aboutApp => _t('सेतु लर्निंग के बारे में', 'About Setu Learning');
  String get versionLabel => _t('संस्करण 1.0.0', 'Version 1.0.0');
  String get aboutBody => _t(
      'सेतु लर्निंग स्कूली, कॉलेज और प्रतियोगी परीक्षा के विद्यार्थियों के लिए विषयवार अध्ययन सामग्री उपलब्ध कराता है। MathSetu, VigyanSetu, EnglishSetu, RASSetu और अन्य विषयों की पुस्तकें ऑफ़लाइन पढ़ी जा सकती हैं।',
      'Setu Learning offers subject-wise study material for school, college and competitive-exam students. Books for MathSetu, VigyanSetu, EnglishSetu, RASSetu and other subjects can be read offline.');
  String get worksOffline => _t('ऑफ़लाइन चलता है', 'Works offline');
  String get resetAllProgress => _t('सारी प्रगति मिटाएँ', 'Reset all progress');
  String get resetAllProgressSubtitle => _t(
      'पढ़ने का इतिहास, अभ्यास स्कोर और अधूरे प्रयास मिटाएँ',
      'Clear reading history, quiz scores, and unfinished attempts');
  String get resetConfirmTitle => _t('सारी प्रगति मिटाएँ?', 'Reset all progress?');
  String get resetConfirmBody => _t(
      'इससे आपकी सहेजी गई पढ़ाई की प्रगति और अभ्यास स्कोर हट जाएँगे। इसे वापस नहीं लाया जा सकता।',
      'This removes your saved reading progress and practice scores. This cannot be undone.');
  String get reset => _t('मिटाएँ', 'Reset');
  String get progressReset => _t('प्रगति मिटा दी गई', 'Progress reset');
  String get couldNotReset => _t('प्रगति नहीं मिटाई जा सकी। फिर कोशिश करें।',
      'Could not reset progress. Try again.');

  // ── Reader settings sheet ────────────────────────────────────────────
  String textSizePercent(int p) =>
      _t('अक्षर का आकार: $p%', 'Text size: $p%');
  String get comfortableReading =>
      _t('पढ़ने का आरामदायक अनुभव।', 'A comfortable reading experience.');
  String get theme => _t('थीम', 'Theme');
  String get system => _t('सिस्टम', 'System');
  String get light => _t('लाइट', 'Light');
  String get dark => _t('डार्क', 'Dark');
  String get resetTextSize =>
      _t('अक्षर का आकार पहले जैसा करें', 'Reset text size');

  // ── Widgets ──────────────────────────────────────────────────────────
  String get enlargeDiagram => _t('चित्र बड़ा करें', 'Enlarge diagram');
  String get educationalDiagram => _t('शैक्षिक चित्र', 'Educational diagram');
  String get imageUnavailable => _t('चित्र उपलब्ध नहीं है', 'Image not available');
  String get tapToEnlarge => _t('बड़ा देखने के लिए टैप करें', 'Tap to enlarge');
  String get diagramTitle => _t('चित्र', 'Diagram');
  String get closeDiagram => _t('चित्र बंद करें', 'Close diagram');
  String get zoomOut => _t('छोटा करें', 'Zoom out');
  String get zoomIn => _t('बड़ा करें', 'Zoom in');
  String get resetZoom => _t('मूल आकार', 'Reset zoom');
  String get pinchToZoom => _t('दो उँगलियों से ज़ूम करें • खिसकाकर देखें',
      'Pinch to zoom • Drag to explore');
  String equation(String source) => _t('समीकरण: $source', 'Equation: $source');
  String get loadingProgress => _t('प्रगति लोड हो रही है', 'Loading progress');
  String get progressLoadFailed => _t(
      'सहेजी गई प्रगति लोड नहीं हो सकी। आप पढ़ना जारी रख सकते हैं।',
      'Saved progress could not be loaded. You can keep reading.');
  String get openingChapter => _t('अध्याय खुल रहा है', 'Opening chapter');
  String get chapterNotOpenedSecurely => _t(
      'यह अध्याय सुरक्षित रूप से नहीं खुल सका। कृपया फिर कोशिश करें।',
      'This chapter could not be opened securely. Please retry.');
  String get statusCompleted => _t('पूर्ण', 'Completed');
  String get statusPracticeCompleted => _t('अभ्यास पूर्ण', 'Practice completed');
  String get statusInProgress => _t('जारी', 'In progress');
  String status(String label) => _t('स्थिति: $label', 'Status: $label');
}

/// Makes the current [AppStrings] available to every route below it.
///
/// Installed by `MaterialApp.builder` in `main.dart`. Uses an inherited
/// widget (not Provider) so strings can be read inside callbacks too.
class AppStringsScope extends InheritedWidget {
  const AppStringsScope({
    super.key,
    required this.strings,
    required super.child,
  });

  final AppStrings strings;

  /// Falls back to English when no scope is present (widget tests that pump
  /// a single screen).
  static AppStrings of(BuildContext context) =>
      context.dependOnInheritedWidgetOfExactType<AppStringsScope>()?.strings ??
      AppStrings.english;

  @override
  bool updateShouldNotify(AppStringsScope oldWidget) =>
      oldWidget.strings.language != strings.language;
}

extension AppStringsContext on BuildContext {
  AppStrings get strings => AppStringsScope.of(this);
}
