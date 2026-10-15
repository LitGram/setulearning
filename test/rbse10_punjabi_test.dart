import 'dart:convert';
import 'dart:io';
import 'package:flutter/material.dart';
import 'package:flutter/services.dart';
import 'package:flutter_test/flutter_test.dart';
import 'package:setu_learning/services/content_service.dart';
import 'package:setu_learning/widgets/content_block_widget.dart';

void main() {
  TestWidgetsFlutterBinding.ensureInitialized();

  test('punjabi catalog loads all actual bundled chapters and quizzes',
      () async {
    final subject = ContentService.instance.getSubjectById('rbse10_punjabi')!;
    final catalog = subject.books.single;
    expect(catalog.bookNumber, 7);
    expect(catalog.expectedChapterCount, 23);
    final book = await ContentService.instance.loadBookContent(catalog);
    final expectedIds = [
      ...List.generate(
          7, (i) => 'pun_kav_ch${(i + 1).toString().padLeft(2, '0')}'),
      ...List.generate(
          6, (i) => 'pun_nib_ch${(i + 8).toString().padLeft(2, '0')}'),
      ...List.generate(
          5, (i) => 'pun_kah_ch${(i + 14).toString().padLeft(2, '0')}'),
      'pun_vya_ch19',
      'pun_vya_ch20',
      'pun_rac_ch21',
      'pun_rac_ch22',
      'pun_ch23',
    ];
    expect(book.chapters.map((c) => c.id), expectedIds);
    expect(book.chapters.fold<int>(0, (n, c) => n + c.mcqs.length), 348);
    final original = jsonDecode(File(catalog.jsonAssetPath).readAsStringSync())
        as Map<String, dynamic>;
    for (var i = 0; i < 23; i++) {
      expect(book.chapters[i].toJson(), original['chapters'][i]);
      expect(book.chapters[i].content.last.value, contains('ਅੱਗੇ ਦੀ ਕੜੀ'));
      for (final image
          in book.chapters[i].content.where((b) => b.type == 'image')) {
        expect(
            (await rootBundle.load('assets/images/${image.value}'))
                .lengthInBytes,
            greaterThan(5000));
      }
    }
  });

  test('punjabi last chapter retains every solved exam reference and solution',
      () async {
    final subject = ContentService.instance.getSubjectById('rbse10_punjabi')!;
    final book =
        await ContentService.instance.loadBookContent(subject.books.single);
    final chapter = book.chapters.last;
    expect(chapter.id, 'pun_ch23');
    final provenance = jsonDecode(
        File('10th rbse/07_punjabi/pyq_provenance.json').readAsStringSync());
    expect(provenance['solved_occurrences'], 221);
    expect(provenance['papers'], 17);
    final lesson = chapter.content.map((b) => b.value).join('\n');
    for (final question in provenance['questions']) {
      expect(lesson, contains(question['answer']));
      expect(lesson, contains('${question['url']}#page=${question['page']}'));
    }
    expect(chapter.mcqs, hasLength(18));
  });

  testWidgets('punjabi gurmukhi grammar diagram displays and opens zoom viewer',
      (tester) async {
    tester.view.physicalSize = const Size(360, 800);
    tester.view.devicePixelRatio = 1;
    addTearDown(tester.view.resetPhysicalSize);
    addTearDown(tester.view.resetDevicePixelRatio);
    final subject = ContentService.instance.getSubjectById('rbse10_punjabi')!;
    final book =
        await ContentService.instance.loadBookContent(subject.books.single);
    final image =
        book.chapters[18].content.singleWhere((b) => b.type == 'image');
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
