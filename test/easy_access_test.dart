import 'dart:convert';
import 'dart:io';
import 'package:flutter/material.dart';
import 'package:flutter_test/flutter_test.dart';
import 'package:provider/provider.dart';
import 'package:shared_preferences/shared_preferences.dart';
import 'package:setu_learning/models/book.dart';
import 'package:setu_learning/models/chapter.dart';
import 'package:setu_learning/models/subject.dart';
import 'package:setu_learning/models/subject_group.dart';
import 'package:setu_learning/providers/progress_provider.dart';
import 'package:setu_learning/providers/theme_provider.dart';
import 'package:setu_learning/screens/book_screen.dart';
import 'package:setu_learning/screens/chapter_screen.dart';
import 'package:setu_learning/screens/home_screen.dart';
import 'package:setu_learning/screens/subject_screen.dart';
import 'package:setu_learning/services/content_service.dart';
import 'package:setu_learning/services/screenshot_protection.dart';
import 'package:setu_learning/theme/app_theme.dart';
import 'package:setu_learning/widgets/accessible_card.dart';

class _Progress extends ProgressProvider {
  final Set<String> read;
  _Progress([Set<String>? read]) : read = read ?? {};
  @override
  bool get isLoading => false;
  @override
  Future<void> loadProgress() async {}
  @override
  bool isChapterRead(String subjectId, String bookId, String chapterId) =>
      read.contains(chapterId);
  @override
  Future<void> updateLastPosition(
      {required String subjectId,
      required String bookId,
      required String chapterId,
      required String subjectName,
      required String bookTitle,
      required String chapterTitle}) async {}
}

Chapter _chapter(int n) => Chapter(
    id: 'c$n',
    title: 'Lesson $n',
    content: [ContentBlock(type: 'text', value: 'Body of lesson $n.')],
    mcqs: const []);

final _book = Book(
    id: 'b',
    subjectId: 's',
    bookNumber: 1,
    title: 'Sample book',
    description: 'A short sample.',
    jsonAssetPath: '',
    chapters: [for (var i = 1; i <= 4; i++) _chapter(i)]);

final _subject = Subject(
    id: 's',
    name: 'Sample',
    hindiName: 'नमूना',
    tagline: '',
    seedColor: Colors.indigo,
    icon: Icons.school,
    books: [_book]);

/// A real bundled book, so BookScreen loads the same chapters from assets.
Book _mathBook() {
  const path = 'assets/content/mathsetu/mathsetu_book1.json';
  return Book.fromBookJson(jsonDecode(File(path).readAsStringSync()),
      id: 'mathsetu_b1',
      subjectId: 'mathsetu_test',
      bookNumber: 1,
      description: 'A short sample.',
      jsonAssetPath: path);
}

Widget _app(Widget home, ProgressProvider progress) => MultiProvider(
      providers: [
        ChangeNotifierProvider<ProgressProvider>.value(value: progress),
        ChangeNotifierProvider(create: (_) => ThemeProvider()),
      ],
      child: MaterialApp(theme: AppTheme.createTheme(), home: home),
    );

void main() {
  setUp(() {
    ScreenshotProtection.resetForTesting();
    SharedPreferences.setMockInitialValues({});
    TestDefaultBinaryMessengerBinding.instance.defaultBinaryMessenger
        .setMockMethodCallHandler(
            ScreenshotProtection.channel, (_) async => null);
  });

  test('every subject belongs to a home group', () {
    final subjects = ContentService.instance.getSubjects();
    final groups = subjects.map(SubjectGroup.of).toSet();
    expect(groups, containsAll(SubjectGroup.values));
    expect(
        SubjectGroup.of(
            ContentService.instance.getSubjectById('ugcnet_history')!),
        SubjectGroup.ugcNet);
    expect(
        SubjectGroup.of(
            ContentService.instance.getSubjectById('rbse10_maths')!),
        SubjectGroup.school);
  });

  testWidgets('home group filter narrows the subject list', (tester) async {
    await tester.pumpWidget(_app(const HomeScreen(), _Progress()));
    await tester.pumpAndSettle();
    await tester.tap(find.textContaining('UGC NET ('));
    await tester.pumpAndSettle();
    expect(find.text('UGC NET History'), findsOneWidget);
    expect(find.text('MathSetu'), findsNothing);
    expect(find.text('RBSE 10th Mathematics'), findsNothing);
    await tester.tap(find.textContaining('All ('));
    await tester.pumpAndSettle();
    expect(find.text('RBSE 10th Mathematics'), findsOneWidget);
  });

  testWidgets('a subject with one book opens that book directly',
      (tester) async {
    final subject = ContentService.instance.getSubjectById('ugcnet_history')!;
    expect(subject.books, hasLength(1));
    await tester.runAsync(
        () => ContentService.instance.loadBookContent(subject.books.first));
    await tester.pumpWidget(_app(const HomeScreen(), _Progress()));
    await tester.pumpAndSettle();
    await tester.tap(find.textContaining('UGC NET ('));
    await tester.pumpAndSettle();
    await tester.ensureVisible(find.text(subject.name));
    await tester.pumpAndSettle();
    await tester.tap(find.text(subject.name));
    await tester.pumpAndSettle();
    expect(find.byType(BookScreen), findsOneWidget);
    expect(find.byType(SubjectScreen), findsNothing);
  });

  testWidgets('book screen offers to continue with the next unread chapter',
      (tester) async {
    final book = (await tester
        .runAsync(() => ContentService.instance.loadBookContent(_mathBook())))!;
    final chapters = book.chapters;
    await tester.pumpWidget(_app(BookScreen(subject: _subject, book: book),
        _Progress({chapters[0].id, chapters[1].id})));
    await tester.pumpAndSettle();
    expect(find.text('2 of ${chapters.length} chapters read'), findsOneWidget);
    await tester.tap(find.text('Continue with chapter 3'));
    await tester.pumpAndSettle();
    expect(find.byType(ChapterScreen), findsOneWidget);
    expect(find.text('3 / ${chapters.length}'), findsOneWidget);
  });

  testWidgets('book screen Read filter shows only finished chapters',
      (tester) async {
    final book = (await tester
        .runAsync(() => ContentService.instance.loadBookContent(_mathBook())))!;
    final chapters = book.chapters;
    await tester.pumpWidget(_app(BookScreen(subject: _subject, book: book),
        _Progress({chapters[1].id})));
    await tester.pumpAndSettle();
    expect(find.text('Start reading'), findsNothing);
    expect(find.text('Continue with chapter 1'), findsOneWidget);
    await tester.tap(find.widgetWithText(ChoiceChip, 'Read'));
    await tester.pumpAndSettle();
    expect(
        find.descendant(
            of: find.byType(AccessibleCard),
            matching: find.text(chapters[1].title)),
        findsOneWidget);
    expect(find.byType(AccessibleCard), findsOneWidget);
  });

  testWidgets('reader chapter list jumps to any chapter', (tester) async {
    await tester.pumpWidget(_app(
        ChapterScreen(
            subject: _subject, book: _book, chapter: _book.chapters.first),
        _Progress()));
    await tester.pumpAndSettle();
    expect(find.text('1 / 4'), findsOneWidget);
    await tester.tap(find.byTooltip('All chapters'));
    await tester.pumpAndSettle();
    await tester.tap(find.widgetWithText(ListTile, 'Lesson 4'));
    await tester.pumpAndSettle();
    expect(find.text('4 / 4'), findsOneWidget);

    // The counter also opens the list.
    await tester.tap(find.text('4 / 4'));
    await tester.pumpAndSettle();
    expect(find.text('Reading now'), findsOneWidget);
  });
}
