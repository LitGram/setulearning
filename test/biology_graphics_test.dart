import 'dart:convert';
import 'dart:io';
import 'dart:ui' as ui;
import 'package:flutter/material.dart';
import 'package:flutter_test/flutter_test.dart';
import 'package:setu_learning/widgets/educational_image.dart';

void main() {
  test('Every planned figure exists within its complete lesson and budget', () {
    final manifest = jsonDecode(
        File('assets/biology_graphics_manifest.json').readAsStringSync());
    int book1Images = 0;
    int book1Bytes = 0;
    int book1Chapters = 0;
    int book2Images = 0;
    int book2Bytes = 0;
    int book2Chapters = 0;
    for (final entry in manifest['chapters']) {
      final isBook1 =
          (entry['asset'] as String).endsWith('vigyansetu_book5.json');
      if (isBook1) book1Chapters++;
      final isBook2 =
          (entry['asset'] as String).endsWith('vigyansetu_book6.json');
      if (isBook2) book2Chapters++;
      final book = jsonDecode(File(entry['asset']).readAsStringSync());
      final chapter = (book['chapters'] as List)
          .firstWhere((c) => c['id'] == entry['chapter']);
      for (final block in entry['blocks']) {
        expect(
            (chapter['content'] as List)
                .where((b) => jsonEncode(b) == jsonEncode(block)),
            hasLength(1));
        if (block['type'] == 'image') {
          expect(File('assets/images/${block['value']}').existsSync(), isTrue);
          if (isBook1) {
            book1Images++;
            book1Bytes += File('assets/images/${block['value']}').lengthSync();
          }
          if (isBook2) {
            book2Images++;
            book2Bytes += File('assets/images/${block['value']}').lengthSync();
          }
        }
      }
      expect(chapter['mcqs'], isNotEmpty);
    }
    expect(book1Chapters, 16);
    expect(book1Images, 46);
    expect(book1Bytes, lessThanOrEqualTo(7 * 1024 * 1024));
    expect(book2Chapters, 24);
    expect(book2Images, 64);
    expect(book2Bytes, lessThanOrEqualTo(10 * 1024 * 1024));
    final briefs = jsonDecode(
        File('artifacts/biology_book2_figure_briefs.json').readAsStringSync()) as List;
    expect(briefs.where((f) => f['kind'] == 'raster'), hasLength(19));
    expect(briefs.where((f) => f['kind'] == 'existing'), hasLength(1));
  });

  testWidgets('All 110 compressed biology graphics decode at readable resolution',
      (tester) async {
    final manifest = jsonDecode(
        File('assets/biology_graphics_manifest.json').readAsStringSync());
    await tester.runAsync(() async {
      for (final entry in manifest['chapters']) {
        for (final block in entry['blocks']) {
          if (block['type'] != 'image') continue;
          final bytes =
              await File('assets/images/${block['value']}').readAsBytes();
          final codec = await ui.instantiateImageCodec(bytes);
          final frame = await codec.getNextFrame();
          expect(frame.image.width, greaterThanOrEqualTo(960),
              reason: block['value']);
          expect(frame.image.height, greaterThanOrEqualTo(640),
              reason: block['value']);
          frame.image.dispose();
          codec.dispose();
        }
      }
    });
  });

  testWidgets('Book 2 figure opens, zooms, resets and closes at phone width',
      (tester) async {
    tester.view.physicalSize = const Size(360, 800);
    tester.view.devicePixelRatio = 1;
    addTearDown(tester.view.resetPhysicalSize);
    addTearDown(tester.view.resetDevicePixelRatio);
    await tester.pumpWidget(const MaterialApp(
        home: Scaffold(
      body: SingleChildScrollView(
          child: EducationalImage(
        asset: 'assets/images/bio2_heart.webp',
        caption: 'मानव हृदय',
      )),
    )));
    await tester.pumpAndSettle();
    await tester.runAsync(() => precacheImage(
          const AssetImage('assets/images/bio2_heart.webp'),
          tester.element(find.byType(EducationalImage)),
        ));
    await tester.pumpAndSettle();
    expect(tester.takeException(), isNull);
    await tester.tap(find.byType(InkWell).first);
    await tester.pumpAndSettle();
    final viewer =
        tester.widget<InteractiveViewer>(find.byType(InteractiveViewer));
    expect(viewer.transformationController!.value.getMaxScaleOnAxis(), 1);
    await tester.tap(find.byTooltip('Zoom in'));
    await tester.pump();
    expect(viewer.transformationController!.value.getMaxScaleOnAxis(), 1.5);
    await tester.tap(find.byTooltip('Reset zoom'));
    await tester.pump();
    expect(viewer.transformationController!.value.getMaxScaleOnAxis(), 1);
    await tester.tap(find.byTooltip('Close diagram'));
    await tester.pumpAndSettle();
    expect(find.byType(InteractiveViewer), findsNothing);
    expect(tester.takeException(), isNull);
  });
}
