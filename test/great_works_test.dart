import 'dart:convert';
import 'dart:io';
import 'package:flutter/material.dart';
import 'package:flutter_test/flutter_test.dart';
import 'package:provider/provider.dart';
import 'package:setu_learning/providers/progress_provider.dart';
import 'package:setu_learning/providers/theme_provider.dart';
import 'package:setu_learning/screens/home_screen.dart';
import 'package:setu_learning/screens/subject_screen.dart';
import 'package:setu_learning/services/content_service.dart';
import 'package:setu_learning/widgets/markdown_content.dart';

class _TestProgress extends ProgressProvider {
  @override
  bool get isLoading => false;
  @override
  Future<void> loadProgress() async {}
}

void main() {
  TestWidgetsFlutterBinding.ensureInitialized();
  final service = ContentService.instance;
  final subject = service.getSubjectById('greatworks')!;

  test('The six guides have their own section and 600 lessons', () {
    expect(subject.name, '100 Great Works of All Time');
    expect(subject.books.length, 6);
    expect(service.getTotalChaptersForSubject(subject.id), 600);
    expect(service.getSubjectById('englishsetu')!.books.length, 13);
    expect(subject.books.map((book) => book.id).toSet().length, 6);
  });

  testWidgets('The separate section opens from the home library',
      (tester) async {
    await tester.pumpWidget(MultiProvider(
      providers: [
        ChangeNotifierProvider<ProgressProvider>(
            create: (_) => _TestProgress()),
        ChangeNotifierProvider(create: (_) => ThemeProvider()),
      ],
      child: const MaterialApp(home: HomeScreen()),
    ));
    await tester.pumpAndSettle();
    await tester.scrollUntilVisible(find.text(subject.name), 300);
    await tester.tap(find.text(subject.name));
    await tester.pumpAndSettle();
    expect(find.byType(SubjectScreen), findsOneWidget);
    expect(find.text('100 Great Novels of All Time'), findsOneWidget);
    expect(tester.takeException(), isNull);
  });

  testWidgets('The new section supports large text on a compact phone',
      (tester) async {
    tester.view.physicalSize = const Size(360, 800);
    tester.view.devicePixelRatio = 1;
    addTearDown(tester.view.resetPhysicalSize);
    addTearDown(tester.view.resetDevicePixelRatio);
    await tester.pumpWidget(ChangeNotifierProvider<ProgressProvider>(
      create: (_) => _TestProgress(),
      child: MaterialApp(
        builder: (context, child) => MediaQuery(
          data: MediaQuery.of(context)
              .copyWith(textScaler: const TextScaler.linear(2)),
          child: child!,
        ),
        home: SubjectScreen(subject: subject),
      ),
    ));
    await tester.pumpAndSettle();
    expect(tester.takeException(), isNull);
  });

  for (final book in subject.books) {
    test('${book.title} loads all 100 real chapters from bundled assets',
        () async {
      final loaded = await service.loadBookContent(book);
      expect(loaded.title, book.title);
      expect(loaded.chapters.length, 100);
      expect(loaded.chapters.first.id, 'ch1');
      expect(loaded.chapters.last.id, 'ch100');
      expect(loaded.chapters.every((chapter) => chapter.mcqs.isEmpty), isTrue);
      // Contents and other publication pages must never become reading chapters.
      for (final chapter in loaded.chapters) {
        expect(chapter.title,
            startsWith('${loaded.chapters.indexOf(chapter) + 1}. '));
        expect(chapter.title.toLowerCase(), isNot(contains('mukesh')));
        expect(chapter.content.any((block) => block.value.startsWith('# ')),
            isFalse);
      }
    });
  }

  testWidgets('Imported verse keeps line breaks and emphasis on a small phone',
      (tester) async {
    tester.view.physicalSize = const Size(360, 800);
    tester.view.devicePixelRatio = 1;
    addTearDown(tester.view.resetPhysicalSize);
    addTearDown(tester.view.resetDevicePixelRatio);
    final data = jsonDecode(
        File('assets/content/greatworks/poems.json').readAsStringSync());
    final milton = (data['chapters'] as List).firstWhere(
        (chapter) => (chapter['title'] as String).contains('Paradise Lost'));
    final verse = (milton['content'] as List).firstWhere(
            (block) => (block['value'] as String).startsWith('> '))['value']
        as String;
    await tester.pumpWidget(MaterialApp(
      theme: ThemeData.dark(),
      home: Scaffold(
          body: SingleChildScrollView(child: MarkdownContent(data: verse))),
    ));
    final rendered = tester
        .widgetList<SelectableText>(find.byType(SelectableText))
        .map((text) => text.textSpan?.toPlainText() ?? text.data ?? '')
        .join('\n');
    expect(rendered, contains("Of Man's first disobedience, and the fruit\n"));
    expect(rendered, contains('Of that forbidden tree whose mortal taste'));
    expect(rendered, contains('Paradise Lost'));
    expect(rendered, isNot(contains('*')));
    expect(rendered, isNot(contains('>')));
    expect(tester.takeException(), isNull);
  });
}
