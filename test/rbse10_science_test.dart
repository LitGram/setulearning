import 'dart:convert';
import 'dart:io';
import 'package:flutter/material.dart';
import 'package:flutter/services.dart';
import 'package:flutter_test/flutter_test.dart';
import 'package:setu_learning/services/content_service.dart';
import 'package:setu_learning/widgets/content_block_widget.dart';

void main() {
  TestWidgetsFlutterBinding.ensureInitialized();

  test('science catalog loads all actual bundled chapters and quizzes',
      () async {
    final subject = ContentService.instance.getSubjectById('rbse10_science')!;
    final catalog = subject.books.single;
    expect(catalog.bookNumber, 2);
    expect(catalog.expectedChapterCount, 14);
    final book = await ContentService.instance.loadBookContent(catalog);
    expect(
        book.chapters.map((c) => c.id),
        List.generate(
            14, (i) => 'sci_ch${(i + 1).toString().padLeft(2, '0')}'));
    expect(book.chapters.fold<int>(0, (n, c) => n + c.mcqs.length), 213);
    final original = jsonDecode(File(catalog.jsonAssetPath).readAsStringSync())
        as Map<String, dynamic>;
    for (var i = 0; i < 14; i++) {
      // Model and loader must retain the entire manuscript, especially the
      // answer/revision/self-test sections after the quiz.
      expect(book.chapters[i].toJson(), original['chapters'][i]);
      expect(book.chapters[i].content.last.value, contains('आगे की कड़ी'));
      for (final image
          in book.chapters[i].content.where((b) => b.type == 'image')) {
        expect(
            (await rootBundle.load('assets/images/${image.value}'))
                .lengthInBytes,
            greaterThan(5000));
      }
    }
  });

  test('science last chapter retains every solved exam reference and solution',
      () async {
    final subject = ContentService.instance.getSubjectById('rbse10_science')!;
    final book =
        await ContentService.instance.loadBookContent(subject.books.single);
    final chapter = book.chapters.last;
    expect(chapter.id, 'sci_ch14');
    final provenance = jsonDecode(
        File('10th rbse/02_science/pyq_provenance.json').readAsStringSync());
    expect(provenance['solved_occurrences'], 361);
    expect(provenance['papers'], 18);
    final lesson = chapter.content.map((b) => b.value).join('\n');
    for (final question in provenance['questions']) {
      expect(lesson, contains(question['answer']));
      expect(lesson, contains('${question['url']}#page=${question['page']}'));
    }
    expect(chapter.mcqs, hasLength(18));
  });

  testWidgets('science ray diagram displays and opens the existing zoom viewer',
      (tester) async {
    tester.view.physicalSize = const Size(360, 800);
    tester.view.devicePixelRatio = 1;
    addTearDown(tester.view.resetPhysicalSize);
    addTearDown(tester.view.resetDevicePixelRatio);
    final subject = ContentService.instance.getSubjectById('rbse10_science')!;
    final book =
        await ContentService.instance.loadBookContent(subject.books.single);
    final image =
        book.chapters[8].content.singleWhere((b) => b.type == 'image');
    await tester.pumpWidget(MaterialApp(
      home: Scaffold(
          body: SingleChildScrollView(child: ContentBlockWidget(block: image))),
    ));
    await tester.runAsync(() => precacheImage(
          AssetImage('assets/images/${image.value}'),
          tester.element(find.byType(ContentBlockWidget)),
        ));
    await tester.pumpAndSettle();
    expect(find.text('चित्र उपलब्ध नहीं है'), findsNothing);
    expect(find.byType(Image), findsOneWidget);
    await tester.tap(find.byType(Image));
    await tester.pumpAndSettle();
    expect(find.text('चित्र देखें / Diagram'), findsOneWidget);
    expect(find.byType(InteractiveViewer), findsOneWidget);
    expect(tester.takeException(), isNull);
  });
}
