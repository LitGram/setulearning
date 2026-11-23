import 'dart:convert';
import 'dart:io';
import 'dart:ui' as ui;
import 'package:flutter/material.dart';
import 'package:flutter_test/flutter_test.dart';
import 'package:markdown/markdown.dart' as md;
import 'package:setu_learning/widgets/markdown_content.dart';

String compact(String value) => value.replaceAll(RegExp(r'\s+'), '');

void main() {
  final report = jsonDecode(
      File('artifacts/english_docx_recovery.json').readAsStringSync());
  test('All original Word illustrations are retained and decodable', () async {
    final images = [for (final book in report['books']) ...book['images']];
    expect(images.length, 23);
    for (final image in images) {
      final bytes = File('assets/images/${image['file']}').readAsBytesSync();
      final codec = await ui.instantiateImageCodec(bytes);
      final frame = await codec.getNextFrame();
      expect(frame.image.width, greaterThan(0));
      expect(frame.image.height, greaterThan(0));
      frame.image.dispose();
      codec.dispose();
    }
  });
  for (final book in report['books']) {
    test('${book['asset']}: every retained Word character survives Markdown',
        () {
      final data = jsonDecode(File(book['asset']).readAsStringSync());
      final filename = (book['asset'] as String).split('/').last;
      final oracle = jsonDecode(
          File('artifacts/english_docx_expected_text/$filename')
              .readAsStringSync());
      expect(book['sourcePayloadSha256'], book['recoveredPayloadSha256']);
      for (final chapter in data['chapters']) {
        final markdown = (chapter['content'] as List)
            .where((b) => b['type'] != 'image')
            .map((b) => b['value'])
            .join('\n\n');
        final nodes = md.Document(
                extensionSet: md.ExtensionSet.gitHubFlavored, encodeHtml: false)
            .parseLines(markdown.split('\n'));
        expect(compact(nodes.map((n) => n.textContent).join('\n')),
            compact(oracle[chapter['id']]),
            reason: chapter['title']);
      }
      expect(
          (data['chapters'] as List)
              .any((c) => RegExp(r'^Table \d+$').hasMatch(c['title'])),
          isFalse);
    });
  }

  testWidgets('Restored literary teaching and tables render on a compact phone',
      (tester) async {
    final data = jsonDecode(
        File('assets/content/englishsetu/second_grade_guide.json')
            .readAsStringSync());
    final chapter = data['chapters'][0];
    final blocks = chapter['content'] as List;
    final texts = [
      blocks.take(12).map((b) => b['value']).join('\n\n'),
      for (final c in data['chapters'])
        for (final b in c['content'])
          if ((b['value'] as String).startsWith('| ')) b['value'] as String
    ];
    expect(texts.length, 37);
    tester.view.physicalSize = const Size(320, 700);
    tester.view.devicePixelRatio = 1;
    addTearDown(tester.view.resetPhysicalSize);
    addTearDown(tester.view.resetDevicePixelRatio);
    for (final text in texts) {
      await tester.pumpWidget(MaterialApp(
          home: MediaQuery(
              data: const MediaQueryData(
                  size: Size(320, 700), textScaler: TextScaler.linear(1.8)),
              child: Scaffold(
                  body: SingleChildScrollView(
                      child: Padding(
                          padding: const EdgeInsets.all(20),
                          child: MarkdownContent(data: text)))))));
      await tester.pumpAndSettle();
      expect(tester.takeException(), isNull);
    }
  });
}
