import 'package:flutter_test/flutter_test.dart';
import 'package:setu_learning/services/content_service.dart';

void main() {
  testWidgets(
      'Completed UGC NET books load their packaged lessons and MCQs',
      (tester) async {
    final service = ContentService.instance;
    for (final entry in {
      'ugcnet_english': 60,
      'ugcnet_political_science': 51,
      'ugcnet_history': 86,
      'ugcnet_commerce': 65,
      'ugcnet_hindi': 58,
    }.entries) {
      final subject = service.getSubjectById(entry.key);
      expect(subject, isNotNull);
      expect(subject!.books.length, 1);
      final book = await tester
          .runAsync(() => service.loadBookContent(subject.books.single));
      expect(book, isNotNull);
      expect(book!.chapterCount, entry.value);
      expect(book.chapters.first.content.length, greaterThan(10),
          reason: 'The source asset must load rather than fallback lessons.');
      expect(book.chapters.first.mcqs.length, greaterThan(10));
      expect(book.chapters.last.content, isNotEmpty);
    }
  });
}
