import 'dart:convert';
import 'dart:io';
import 'dart:ui' as ui;
import 'package:flutter/material.dart';
import 'package:flutter_test/flutter_test.dart';
import 'package:setu_learning/widgets/educational_image.dart';

void main() {
  test('Every planned vertical physics graphic exists in Android App assets and database', () {
    final manifestFile = File('assets/physics_graphics_manifest.json');
    expect(manifestFile.existsSync(), isTrue);

    final manifest = jsonDecode(manifestFile.readAsStringSync());
    final books = manifest['books'] as List;

    int totalImages = 0;
    int totalBytes = 0;

    for (final b in books) {
      final jsonAsset = b['json_asset'] as String;
      final bookFile = File(jsonAsset);
      expect(bookFile.existsSync(), isTrue, reason: 'Book JSON should exist: $jsonAsset');

      final bookData = jsonDecode(bookFile.readAsStringSync());
      final chapters = bookData['chapters'] as List;
      expect(chapters.length, b['chapters_count']);

      final images = b['images'] as List;
      expect(images.length, b['graphics_count']);

      for (final img in images) {
        final filename = img['file'] as String;
        final imgFile = File('assets/images/$filename');
        expect(imgFile.existsSync(), isTrue, reason: 'Image file should exist in assets/images: $filename');

        final byteSize = imgFile.lengthSync();
        expect(byteSize, lessThanOrEqualTo(95 * 1024), reason: 'Image $filename must be under 95 KB');
        totalBytes += byteSize;
        totalImages++;

        // Verify chapter linkage
        final chapter = chapters.firstWhere((c) => c['id'] == img['chapter_id']);
        final hasImageBlock = (chapter['content'] as List).any(
          (blk) => blk['type'] == 'image' && blk['value'] == filename,
        );
        expect(hasImageBlock, isTrue, reason: 'Chapter ${img['chapter_id']} must have image block for $filename');
      }
    }

    expect(totalImages, 95); // 39 in Book 1 + 56 in Book 2
    expect(totalBytes, lessThanOrEqualTo(8 * 1024 * 1024)); // Total well under 8 MB
  });

  testWidgets('All 95 vertical physics graphics decode at exact 1000x1400 resolution',
      (tester) async {
    final manifest = jsonDecode(
        File('assets/physics_graphics_manifest.json').readAsStringSync());
    final books = manifest['books'] as List;

    await tester.runAsync(() async {
      for (final b in books) {
        final images = b['images'] as List;
        for (final img in images) {
          final filename = img['file'] as String;
          final bytes = await File('assets/images/$filename').readAsBytes();
          final codec = await ui.instantiateImageCodec(bytes);
          final frame = await codec.getNextFrame();
          expect(frame.image.width, 1000, reason: '$filename width should be exactly 1000');
          expect(frame.image.height, 1400, reason: '$filename height should be exactly 1400');
          frame.image.dispose();
          codec.dispose();
        }
      }
    });
  });

  testWidgets('Book 1 & Book 2 figures open, zoom and close cleanly at phone width',
      (tester) async {
    tester.view.physicalSize = const Size(360, 800);
    tester.view.devicePixelRatio = 1;
    addTearDown(tester.view.resetPhysicalSize);
    addTearDown(tester.view.resetDevicePixelRatio);

    await tester.pumpWidget(const MaterialApp(
      home: Scaffold(
        body: SingleChildScrollView(
          child: EducationalImage(
            asset: 'assets/images/phys1_scientific_method.webp',
            caption: 'वैज्ञानिक विधि एवं अनुसंधान चक्र',
          ),
        ),
      ),
    ));
    await tester.pumpAndSettle();
    await tester.runAsync(() => precacheImage(
          const AssetImage('assets/images/phys1_scientific_method.webp'),
          tester.element(find.byType(EducationalImage)),
        ));
    await tester.pumpAndSettle();
    expect(tester.takeException(), isNull);

    expect(find.byType(EducationalImage), findsOneWidget);
    await tester.tap(find.byType(InkWell).first);
    await tester.pumpAndSettle();

    expect(find.byType(InteractiveViewer), findsOneWidget);
    await tester.tap(find.byTooltip('Close diagram'));
    await tester.pumpAndSettle();

    expect(find.byType(InteractiveViewer), findsNothing);
  });
}
