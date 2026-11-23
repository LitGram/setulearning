import 'dart:convert';
import 'dart:io';
import 'package:flutter/material.dart';
import 'package:flutter_test/flutter_test.dart';
import 'package:provider/provider.dart';
import 'package:shared_preferences/shared_preferences.dart';
import 'package:setu_learning/models/book.dart';
import 'package:setu_learning/models/chapter.dart';
import 'package:setu_learning/models/mcq.dart';
import 'package:setu_learning/models/subject.dart';
import 'package:setu_learning/models/user_progress.dart';
import 'package:setu_learning/providers/progress_provider.dart';
import 'package:setu_learning/providers/theme_provider.dart';
import 'package:setu_learning/screens/chapter_screen.dart';
import 'package:setu_learning/screens/quiz_screen.dart';
import 'package:setu_learning/screens/settings_screen.dart';
import 'package:setu_learning/screens/home_screen.dart';
import 'package:setu_learning/screens/subject_screen.dart';
import 'package:setu_learning/screens/progress_screen.dart';
import 'package:setu_learning/services/study_session_store.dart';
import 'package:setu_learning/theme/app_theme.dart';
import 'package:setu_learning/services/screenshot_protection.dart';

const chapter = Chapter(id: 'test_chapter', title: 'Test chapter', content: [
  ContentBlock(type: 'text', value: 'Read this short lesson.'),
], mcqs: [
  MCQ(
      question: 'One plus one?',
      options: ['Two', 'Three'],
      correctIndex: 0,
      explanation: 'One plus one is two.'),
  MCQ(question: 'Two plus one?', options: ['Three', 'Four'], correctIndex: 0),
]);
final book = Book(
    id: 'test_book',
    subjectId: 'test_subject',
    bookNumber: 1,
    title: 'Test book',
    description: '',
    jsonAssetPath: '',
    chapters: [chapter]);
final subject = Subject(
    id: 'test_subject',
    name: 'Test',
    hindiName: 'परीक्षण',
    tagline: '',
    seedColor: Colors.indigo,
    icon: Icons.school,
    books: [book]);

class TestProgress extends ProgressProvider {
  @override
  bool get isLoading => false;
  bool read = false;
  QuizRecord? result;
  @override
  Future<void> loadProgress() async {}
  @override
  Future<void> resetAllProgress() async {
    read = false;
    result = null;
  }

  @override
  bool isChapterRead(String subjectId, String bookId, String chapterId) => read;
  @override
  Future<void> markChapterRead(
      {required String subjectId,
      required String bookId,
      required String chapterId}) async {
    read = true;
    notifyListeners();
  }

  @override
  Future<void> updateLastPosition(
      {required String subjectId,
      required String bookId,
      required String chapterId,
      required String subjectName,
      required String bookTitle,
      required String chapterTitle}) async {}
  @override
  Future<void> recordQuizScore(
      {required String subjectId,
      required String bookId,
      required String chapterId,
      required int score,
      required int total}) async {
    result = QuizRecord(
        subjectId: subjectId,
        bookId: bookId,
        chapterId: chapterId,
        score: score,
        total: total,
        completedAt: DateTime.now());
  }

  @override
  QuizRecord? getBestQuizScore(
          String subjectId, String bookId, String chapterId) =>
      result;
}

Widget app(Widget screen, ProgressProvider progress, {double scale = 1}) =>
    MultiProvider(
      providers: [
        ChangeNotifierProvider.value(value: progress),
        ChangeNotifierProvider(create: (_) => ThemeProvider())
      ],
      child: MaterialApp(
          theme: AppTheme.createTheme(fontScale: scale > 1 ? 1.4 : 1),
          home: screen,
          builder: (context, child) => MediaQuery(
              data: MediaQuery.of(context)
                  .copyWith(textScaler: TextScaler.linear(scale)),
              child: child!)),
    );

void main() {
  for (var number = 1; number <= 8; number++) {
    testWidgets('MathSetu book $number advances to a distinct next chapter',
        (tester) async {
      final loaded = Book.fromBookJson(
          jsonDecode(File('assets/content/mathsetu/mathsetu_book$number.json')
              .readAsStringSync()),
          id: 'mathsetu_b$number',
          subjectId: 'mathsetu',
          bookNumber: number,
          description: '',
          jsonAssetPath: '');
      await tester.pumpWidget(app(
          ChapterScreen(
              subject: subject, book: loaded, chapter: loaded.chapters.first),
          TestProgress()));
      await tester.pumpAndSettle();
      expect(find.text('1 / ${loaded.chapterCount}'), findsOneWidget);
      await tester.tap(find.text('Next'));
      await tester.pumpAndSettle();
      expect(find.text('2 / ${loaded.chapterCount}'), findsOneWidget);
      expect(find.text(loaded.chapters[1].title), findsWidgets);
      expect(find.text(loaded.chapters.first.title), findsNothing);
      await tester.tap(find.text('Previous'));
      await tester.pumpAndSettle();
      expect(find.text('1 / ${loaded.chapterCount}'), findsOneWidget);
    });
  }
  testWidgets('Next skips duplicate chapters and counter uses unique lessons',
      (tester) async {
    SharedPreferences.setMockInitialValues({});
    final loaded = Book.fromBookJson({
      'chapters': [
        {...chapter.toJson(), 'id': 'ch01'},
        {...chapter.toJson(), 'id': 'ch02'},
        {...chapter.toJson(), 'id': 'ch03', 'title': 'Actual next chapter'},
        {...chapter.toJson(), 'id': 'ch04', 'title': 'Actual next chapter'},
      ]
    },
        id: 'test_book',
        subjectId: 'test_subject',
        bookNumber: 1,
        description: '',
        jsonAssetPath: '');
    await tester.pumpWidget(app(
        ChapterScreen(
            subject: subject, book: loaded, chapter: loaded.chapters.first),
        TestProgress()));
    await tester.pumpAndSettle();
    expect(find.text('1 / 2'), findsOneWidget);
    await tester.tap(find.text('Next'));
    await tester.pumpAndSettle();
    expect(find.text('2 / 2'), findsOneWidget);
    expect(find.text('Actual next chapter'), findsWidgets);
    await tester.tap(find.text('Previous'));
    await tester.pumpAndSettle();
    expect(find.text('1 / 2'), findsOneWidget);
  });
  setUp(() {
    ScreenshotProtection.resetForTesting();
    SharedPreferences.setMockInitialValues({});
    TestDefaultBinaryMessengerBinding.instance.defaultBinaryMessenger
        .setMockMethodCallHandler(
            ScreenshotProtection.channel, (_) async => null);
  });

  testWidgets('Opening a chapter does not mark it read; completion is explicit',
      (tester) async {
    final progress = TestProgress();
    await progress.resetAllProgress();
    await tester.pumpWidget(app(
        ChapterScreen(subject: subject, book: book, chapter: chapter),
        progress));
    await tester.pumpAndSettle();
    expect(progress.isChapterRead(subject.id, book.id, chapter.id), isFalse);
    await tester.tap(find.text('Mark as read'));
    await tester.pumpAndSettle();
    expect(progress.isChapterRead(subject.id, book.id, chapter.id), isTrue);
    expect(find.text('Progress saved'), findsOneWidget);
  });

  testWidgets(
      'chapter reader uses balanced centered gutters on phone and tablet',
      (tester) async {
    final progress = TestProgress();
    for (final width in [360.0, 1000.0]) {
      tester.view.physicalSize = Size(width, 800);
      tester.view.devicePixelRatio = 1;
      await tester.pumpWidget(app(
          ChapterScreen(subject: subject, book: book, chapter: chapter),
          progress));
      await tester.pumpAndSettle();
      final header = tester.getRect(find.byType(Container).first);
      final viewport = tester.getRect(find.byType(ListView).first);
      expect(
          (header.center.dx - viewport.center.dx).abs(), lessThanOrEqualTo(1));
      expect(tester.takeException(), isNull);
    }
    tester.view.resetPhysicalSize();
    tester.view.resetDevicePixelRatio();
  });

  testWidgets('Selected but unchecked answers remain editable after Previous',
      (tester) async {
    final progress = TestProgress();
    await progress.resetAllProgress();
    await tester.pumpWidget(app(
        QuizScreen(subject: subject, book: book, chapter: chapter), progress));
    await tester.pumpAndSettle();
    await tester.tap(find.text('Two'), warnIfMissed: false);
    await tester.pump();
    await tester.tap(find.text('Check answer'));
    await tester.pumpAndSettle();
    await tester.tap(find.text('Next question'));
    await tester.pumpAndSettle();
    await tester.tap(find.text('Four'), warnIfMissed: false);
    await tester.tap(find.text('Previous'));
    await tester.pumpAndSettle();
    await tester.tap(find.text('Next question'));
    await tester.pumpAndSettle();
    expect(find.text('Check answer'), findsOneWidget);
    await tester.tap(find.text('Three'), warnIfMissed: false);
    await tester.pump();
    await tester.tap(find.text('Check answer'));
    await tester.pumpAndSettle();
    await tester.tap(find.text('View results'));
    await tester.pumpAndSettle();
    expect(
        progress.getBestQuizScore(subject.id, book.id, chapter.id)?.score, 2);
    expect(progress.isChapterRead(subject.id, book.id, chapter.id), isFalse);
    expect(
        await StudySessionStore.read(
            StudySessionStore.key('quiz', subject.id, book.id, chapter.id)),
        isNull);
  });

  testWidgets('Unfinished practice resumes checked answers without rescoring',
      (tester) async {
    final key = StudySessionStore.key('quiz', subject.id, book.id, chapter.id);
    SharedPreferences.setMockInitialValues({
      key: jsonEncode({
        'signature': jsonEncode(chapter.mcqs
            .map((q) => [q.question, q.options, q.correctIndex])
            .toList()),
        'index': 1,
        'answers': {'0': 0, '1': 1},
        'checked': [0],
      })
    });
    final progress = TestProgress();
    await tester.pumpWidget(app(
        QuizScreen(subject: subject, book: book, chapter: chapter), progress));
    await tester.pumpAndSettle();
    expect(find.text('Resume practice?'), findsOneWidget);
    await tester.tap(find.text('Resume'));
    await tester.pumpAndSettle();
    expect(find.text('Question 2 of 2'), findsOneWidget);
    expect(find.text('Check answer'), findsOneWidget);
    await tester.tap(find.text('Three'), warnIfMissed: false);
    await tester.pump();
    await tester.tap(find.text('Check answer'));
    await tester.pumpAndSettle();
    await tester.tap(find.text('View results'));
    await tester.pumpAndSettle();
    expect(progress.result?.score, 2);
  });

  testWidgets('Reader restores a saved position within a long chapter',
      (tester) async {
    final longChapter = Chapter(
        id: 'long',
        title: 'Long chapter',
        mcqs: const [],
        content: List.generate(
            30, (i) => ContentBlock(type: 'text', value: 'Lesson $i. ' * 20)));
    final longBook = Book(
        id: book.id,
        subjectId: subject.id,
        bookNumber: 1,
        title: book.title,
        description: '',
        jsonAssetPath: '',
        chapters: [longChapter]);
    SharedPreferences.setMockInitialValues({
      StudySessionStore.key('reading', subject.id, book.id, longChapter.id):
          jsonEncode({'offset': 500.0})
    });
    await tester.pumpWidget(app(
        ChapterScreen(subject: subject, book: longBook, chapter: longChapter),
        TestProgress()));
    await tester.pumpAndSettle();
    final list = tester.widget<ListView>(find.byType(ListView));
    expect(list.controller!.offset, closeTo(500, 1));
    expect(find.text('Mark as read'), findsNothing);
  });

  testWidgets('Settings supports 200% text on a compact phone', (tester) async {
    tester.view.physicalSize = const Size(360, 800);
    tester.view.devicePixelRatio = 1;
    addTearDown(tester.view.resetPhysicalSize);
    addTearDown(tester.view.resetDevicePixelRatio);
    await tester
        .pumpWidget(app(const SettingsScreen(), TestProgress(), scale: 2));
    await tester.pumpAndSettle();
    expect(tester.takeException(), isNull);
  });
  for (final entry in <String, Widget>{
    'Home': const HomeScreen(),
    'Subjects': SubjectScreen(subject: subject),
    'Progress': const ProgressScreen(),
    'Reader': ChapterScreen(subject: subject, book: book, chapter: chapter),
    'Practice': QuizScreen(subject: subject, book: book, chapter: chapter),
  }.entries) {
    testWidgets('${entry.key} supports compact phone large text',
        (tester) async {
      tester.view.physicalSize = const Size(360, 800);
      tester.view.devicePixelRatio = 1;
      addTearDown(tester.view.resetPhysicalSize);
      addTearDown(tester.view.resetDevicePixelRatio);
      await tester.pumpWidget(app(entry.value, TestProgress(), scale: 2));
      await tester.pumpAndSettle();
      expect(tester.takeException(), isNull);
    });
  }
}
