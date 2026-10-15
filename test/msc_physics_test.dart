import 'dart:convert';
import 'dart:io';
import 'package:flutter/material.dart';
import 'package:flutter_test/flutter_test.dart';
import 'package:markdown/markdown.dart' as md;
import 'package:provider/provider.dart';
import 'package:shared_preferences/shared_preferences.dart';
import 'package:setu_learning/providers/progress_provider.dart';
import 'package:setu_learning/providers/theme_provider.dart';
import 'package:setu_learning/screens/book_screen.dart';
import 'package:setu_learning/screens/chapter_screen.dart';
import 'package:setu_learning/screens/home_screen.dart';
import 'package:setu_learning/screens/subject_screen.dart';
import 'package:setu_learning/services/content_service.dart';
import 'package:setu_learning/services/chapter_identity.dart';
import 'package:setu_learning/services/screenshot_protection.dart';
import 'package:setu_learning/widgets/markdown_content.dart';
import 'package:setu_learning/widgets/accessible_card.dart';

class _PhysicsProgress extends ProgressProvider {
  @override
  bool get isLoading => false;
  @override
  Future<void> loadProgress() async {}
  @override
  Future<void> ensureBookLoaded(String subjectId, String bookId) async {}
  @override
  Future<void> updateLastPosition({
    required String subjectId,
    required String bookId,
    required String chapterId,
    required String subjectName,
    required String bookTitle,
    required String chapterTitle,
  }) async {}
}

String _compact(String text) => text.replaceAll(RegExp(r'\s+'), '');

Widget _app(Widget home) => MultiProvider(
      providers: [
        ChangeNotifierProvider<ProgressProvider>(
            create: (_) => _PhysicsProgress()),
        ChangeNotifierProvider(create: (_) => ThemeProvider()),
      ],
      child: MaterialApp(home: home),
    );

void main() {
  TestWidgetsFlutterBinding.ensureInitialized();
  final service = ContentService.instance;
  final subject = service.getSubjectById('mscphysics')!;

  setUp(() {
    SharedPreferences.setMockInitialValues({});
    ScreenshotProtection.resetForTesting();
  });

  test('Four guides registered with counts derived from their source headings',
      () {
    final audit =
        jsonDecode(File('artifacts/mscphysics_import.json').readAsStringSync());
    expect(subject.name, 'M.Sc. Physics');
    expect(subject.books.length, 4);
    expect(service.getSubjectById('greatworks')!.books.length, 6);
    final records = audit['books'] as List;
    for (var i = 0; i < records.length; i++) {
      expect(subject.books[i].expectedChapterCount, records[i]['chapterCount']);
      expect(records[i]['retainedPayloadSha256'],
          records[i]['importedPayloadSha256']);
      expect(records[i]['publicationComparison']['headingsNotInMarkdown'],
          isEmpty);
      expect(records[i]['publicationComparison']['literalBlocksNotInMarkdown'],
          isEmpty);
    }
  });

  test('Every guide has three complete units and separate appendices', () {
    for (final book in subject.books) {
      final data = jsonDecode(File(book.jsonAssetPath).readAsStringSync());
      final chapters = data['chapters'] as List;
      for (var unit = 1; unit <= 3; unit++) {
        final chapter = chapters[unit - 1];
        expect(chapter['id'], 'unit$unit');
        expect(chapter['title'], startsWith('Unit $unit:'));
        expect((chapter['content'] as List).length, greaterThan(5));
        final text =
            (chapter['content'] as List).map((b) => b['value']).join('\n');
        expect(text.length, greaterThan(10000));
      }
      expect(chapters.skip(3).every((c) => c['title'].startsWith('Appendix ')),
          isTrue);
    }
    expect(
        ChapterIdentity.canonical(
            'mscphysics', 'mscphysics_mathematical_physics', 'ch20'),
        'unit1');
    expect(
        ChapterIdentity.canonical(
            'mscphysics', 'mscphysics_mathematical_physics', 'ch41'),
        'unit2');
    expect(
        ChapterIdentity.canonical(
            'mscphysics', 'mscphysics_mathematical_physics', 'ch64'),
        'unit3');
    expect(
        ChapterIdentity.canonical(
            'mscphysics', 'mscphysics_mathematical_physics', 'ch65'),
        'ch65');
    expect(
        ChapterIdentity.isRetiredProgressKey(
            'mscphysics_mscphysics_mathematical_physics_ch20'),
        isTrue);
    expect(
        ChapterIdentity.isRetiredProgressKey(
            'mscphysics_mscphysics_mathematical_physics_ch65'),
        isFalse);
    expect(
        ChapterIdentity.isRetiredProgressKey(
            'mscphysics_mscphysics_mathematical_physics_unit1'),
        isFalse);
  });

  for (final book in subject.books) {
    final data = jsonDecode(File(book.jsonAssetPath).readAsStringSync());
    final id = book.id.replaceFirst('mscphysics_', '');
    final expected = jsonDecode(
        File('artifacts/mscphysics_expected_text/$id.json').readAsStringSync());

    test(
        '${book.title} loads real asset content without fallback or deduplication',
        () async {
      final loaded = await service.loadBookContent(book);
      expect(loaded.title, book.title);
      expect(loaded.chapters.length, (data['chapters'] as List).length);
      expect(loaded.chapterCount, book.expectedChapterCount);
      expect(loaded.chapters.first.content.first.value,
          matches(r'^#{1,2} Unit 1:'));
      expect(loaded.chapters.last.title, startsWith('Appendix '));
      expect(loaded.chapters.every((chapter) => chapter.mcqs.isEmpty), isTrue);
      expect(loaded.chapters.map((ch) => ch.id).toSet().length,
          loaded.chapterCount);
    });

    test('${book.title}: every visible character survives Markdown parsing',
        () {
      for (final chapter in data['chapters'] as List) {
        final source =
            (chapter['content'] as List).map((b) => b['value']).join('\n');
        final nodes = md.Document(
                extensionSet: md.ExtensionSet.gitHubFlavored, encodeHtml: false)
            .parseLines(source.split('\n'));
        final actual = nodes.map((node) => node.textContent).join('\n');
        expect(_compact(actual), _compact(expected[chapter['id']] as String),
            reason: '${book.id}/${chapter['id']}');
      }
    });

    testWidgets('${book.title}: all chapters render at 320px with large text',
        (tester) async {
      tester.view.physicalSize = const Size(320, 700);
      tester.view.devicePixelRatio = 1;
      addTearDown(tester.view.resetPhysicalSize);
      addTearDown(tester.view.resetDevicePixelRatio);
      for (final chapter in data['chapters'] as List) {
        final source =
            (chapter['content'] as List).map((b) => b['value']).join('\n');
        await tester.pumpWidget(MaterialApp(
          theme: ThemeData.dark(),
          home: MediaQuery(
            data: const MediaQueryData(
                size: Size(320, 700), textScaler: TextScaler.linear(1.8)),
            child: Scaffold(
                body: SingleChildScrollView(
              child: Padding(
                  padding: const EdgeInsets.all(20),
                  child: MarkdownContent(data: source)),
            )),
          ),
        ));
        final actual = tester
            .widgetList<SelectableText>(find.byType(SelectableText))
            .map((text) => text.textSpan?.toPlainText() ?? text.data ?? '')
            .join('\n');
        expect(_compact(actual), _compact(expected[chapter['id']] as String),
            reason: '${book.id}/${chapter['id']} rendered visibility');
        expect(tester.takeException(), isNull,
            reason: '${book.id}/${chapter['id']}');
      }
    });

    testWidgets(
        '${book.title}: chapter list search, protected reader, Next and Previous',
        (tester) async {
      final flags = <bool>[];
      final messenger =
          TestDefaultBinaryMessengerBinding.instance.defaultBinaryMessenger;
      messenger.setMockMethodCallHandler(ScreenshotProtection.channel,
          (call) async {
        flags.add((call.arguments as Map)['enabled'] as bool);
        return null;
      });
      addTearDown(() => messenger.setMockMethodCallHandler(
          ScreenshotProtection.channel, null));
      final loaded = await service.loadBookContent(book);
      await tester.pumpWidget(_app(BookScreen(subject: subject, book: loaded)));
      await tester.pumpAndSettle();
      expect(flags, isEmpty, reason: 'Chapter list must allow screenshots');
      final search = find.byType(TextField);
      await tester.ensureVisible(search);
      await tester.enterText(search, loaded.chapters.first.title);
      await tester.pumpAndSettle();
      final title = find
          .descendant(
            of: find.byType(AccessibleCard),
            matching: find.text(loaded.chapters.first.title),
          )
          .first;
      await tester.ensureVisible(title);
      await tester.tap(title);
      await tester.pumpAndSettle();
      expect(find.byType(ChapterScreen), findsOneWidget);
      expect(flags.last, isTrue);
      expect(find.byTooltip('Practice'), findsNothing);
      await tester.tap(find.text('Next'));
      await tester.pumpAndSettle();
      expect(find.text('2 / ${loaded.chapterCount}'), findsOneWidget);
      await tester.tap(find.text('Previous'));
      await tester.pumpAndSettle();
      expect(find.text('1 / ${loaded.chapterCount}'), findsOneWidget);
      await tester.pageBack();
      await tester.pumpAndSettle();
      expect(flags.last, isFalse);
      expect(tester.takeException(), isNull);
    });
  }

  testWidgets(
      'M.Sc. Physics is reachable from the library and shows four guides',
      (tester) async {
    await tester.pumpWidget(_app(const HomeScreen()));
    await tester.pumpAndSettle();
    await tester.scrollUntilVisible(find.text(subject.name), 300);
    await tester.tap(find.text(subject.name));
    await tester.pumpAndSettle();
    expect(find.byType(SubjectScreen), findsOneWidget);
    for (final book in subject.books) {
      expect(find.text(book.title), findsOneWidget);
    }
    expect(tester.takeException(), isNull);
  });
}
