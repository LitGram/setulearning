import 'dart:convert';
import 'dart:io';
import 'dart:ui' as ui;
import 'package:flutter/material.dart';
import 'package:flutter_test/flutter_test.dart';
import 'package:setu_learning/models/chapter.dart';
import 'package:setu_learning/widgets/content_block_widget.dart';
import 'package:setu_learning/widgets/educational_image.dart';

void main() {
  final books = Directory('assets/content/mscphysics').listSync()
      .whereType<File>().where((f) => f.path.endsWith('.json'))
      .map((f) => jsonDecode(f.readAsStringSync()) as Map<String, dynamic>).toList();
  final figures = books.expand((b) => b['chapters'] as List)
      .expand((c) => c['content'] as List)
      .where((b) => b['type'] == 'image').toList();

  test('Revised guides retain prerequisites, explained questions and author', () {
    expect(books.length, 4);
    for (final book in books) {
      expect(book['author'], 'Shiwali Sharma');
      final chapters = book['chapters'] as List;
      expect(chapters.first['id'], 'preface');
      final preface = (chapters.first['content'] as List).map((b) => b['value']).join('\n');
      expect(preface, contains('Shiwali Sharma'));
      if (book['book'] == 'Mathematical Physics') continue;
      expect(preface.toLowerCase(), contains('before unit 1'));
      for (var unit = 1; unit <= 3; unit++) {
        final ch = chapters.firstWhere((c) => c['id'] == 'unit$unit');
        final text = (ch['content'] as List).where((b) => b['type'] == 'text')
            .map((b) => b['value']).join('\n');
        expect(RegExp(r'^#### Question U\d-\d+', multiLine: true).allMatches(text).length, 45);
        expect(RegExp(r'\*\*Answer: [ABCD]\.\*\*').allMatches(text).length, 45);
        expect(text, contains('Sixty Revision Points'));
      }
    }
    expect(figures.length, 12);
    for (final figure in figures) {
      expect(File('assets/images/${figure['value']}').existsSync(), isTrue);
      expect(figure['caption'], isNotEmpty);
    }
  });

  testWidgets('Every revised diagram decodes offline and opens in the phone viewer', (tester) async {
    tester.view.physicalSize = const Size(360, 800);
    tester.view.devicePixelRatio = 1;
    addTearDown(tester.view.resetPhysicalSize);
    addTearDown(tester.view.resetDevicePixelRatio);
    for (final figure in figures) {
      await tester.runAsync(() async {
        final bytes = File('assets/images/${figure['value']}').readAsBytesSync();
        final codec = await ui.instantiateImageCodec(bytes);
        final frame = await codec.getNextFrame();
        expect(frame.image.width, greaterThanOrEqualTo(1000));
        frame.image.dispose();
        codec.dispose();
      });
      await tester.pumpWidget(MaterialApp(home: Scaffold(body: SingleChildScrollView(
          child: ContentBlockWidget(block: ContentBlock.fromJson(Map<String, dynamic>.from(figure)))))));
      await tester.pumpAndSettle();
      await tester.runAsync(() => precacheImage(AssetImage('assets/images/${figure['value']}'),
          tester.element(find.byType(EducationalImage))));
      await tester.pumpAndSettle();
      expect(tester.takeException(), isNull);
      await tester.tap(find.byType(InkWell).first);
      await tester.pumpAndSettle();
      expect(find.byType(InteractiveViewer), findsOneWidget);
      expect(find.text(figure['caption'] as String), findsWidgets);
      await tester.tap(find.byTooltip('Close diagram'));
      await tester.pumpAndSettle();
      expect(find.byType(InteractiveViewer), findsNothing);
      expect(tester.takeException(), isNull);
    }
  });
}
