import 'dart:io';
import 'package:flutter_test/flutter_test.dart';
import 'package:setu_learning/services/content_service.dart';

// Roadmap #3: students should never see "first draft" labels, which make them
// doubt the content. ("प्रारूप" alone also means "format" and is fine.)
final _draftLabel = RegExp(r'प्रथम\s*(संपादकीय\s*)?प्रारूप|ਸੰਪਾਦਕੀ ਪ੍ਰਾਰੂਪ|\(प्रारूप\)');
// Book text may legitimately say e.g. "भारत का प्रथम प्रारूप संविधान" (history),
// so books are checked only for the editorial-status label itself.
final _bookDraftLabel = RegExp(r'संपादकीय\s*प्रारूप|ਸੰਪਾਦਕੀ ਪ੍ਰਾਰੂਪ');

void main() {
  test('subject catalog has no draft labels', () {
    for (final subject in ContentService.instance.getSubjects()) {
      for (final text in [subject.name, subject.hindiName, subject.tagline]) {
        expect(text, isNot(matches(_draftLabel)), reason: subject.id);
      }
      for (final book in subject.books) {
        expect(book.title, isNot(matches(_draftLabel)), reason: book.id);
      }
    }
  });

  test('bundled books have no draft labels', () {
    final files = Directory('assets/content')
        .listSync(recursive: true)
        .whereType<File>()
        .where((f) => f.path.endsWith('.json'));
    for (final file in files) {
      expect(_bookDraftLabel.hasMatch(file.readAsStringSync()), isFalse,
          reason: file.path);
    }
  });
}
