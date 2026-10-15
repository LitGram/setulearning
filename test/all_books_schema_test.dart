import 'dart:convert';
import 'dart:io';
import 'package:flutter_test/flutter_test.dart';
import 'package:setu_learning/models/book.dart';
import 'package:setu_learning/models/chapter.dart';
import 'package:setu_learning/services/content_service.dart';
import 'package:setu_learning/services/chapter_identity.dart';

void main() {
  group('Catalog book schema and integrity', () {
    final subjects = ContentService.instance.getSubjects();

    test('Every catalog book JSON file exists on disk', () {
      for (final subject in subjects) {
        for (final book in subject.books) {
          final file = File(book.jsonAssetPath);
          expect(file.existsSync(), isTrue,
              reason: 'File ${book.jsonAssetPath} must exist');
        }
      }
    });

    for (final subject in subjects) {
      for (final catalogBook in subject.books) {
        test('Validating ${catalogBook.title} schema and content', () {
          final file = File(catalogBook.jsonAssetPath);
          expect(file.existsSync(), isTrue);

          final raw = file.readAsStringSync();
          final Map<String, dynamic> data = jsonDecode(raw);

          final subjectName = data['subject'] as String?;
          expect(subjectName, equals(subject.name));

          final bookTitle = data['book'] as String?;
          expect(bookTitle, isNotNull);
          expect(bookTitle!.isNotEmpty, isTrue);

          final book = Book.fromBookJson(
            data,
            id: catalogBook.id,
            subjectId: catalogBook.subjectId,
            bookNumber: catalogBook.bookNumber,
            description: catalogBook.description,
            jsonAssetPath: catalogBook.jsonAssetPath,
          );

          expect(book.chapters, isNotEmpty,
              reason:
                  '${catalogBook.title} must contain complete source sections');
          expect(book.chapterCount, catalogBook.expectedChapterCount);
          final retained = {for (final ch in book.chapters) ch.id: ch};
          expect(retained.length, book.chapters.length,
              reason: 'Duplicate IDs can make Next revisit the same chapter');
          final lessonPayloads = <String>{};
          for (final chapter in book.chapters) {
            final payload = jsonEncode({
              'content':
                  chapter.content.map((block) => block.toJson()).toList(),
              'mcqs': chapter.mcqs.map((mcq) => mcq.toJson()).toList(),
            });
            expect(lessonPayloads.add(payload), isTrue,
                reason:
                    '${catalogBook.id}/${chapter.id} repeats a lesson and quiz');
          }
          for (final rawChapter in data['chapters'] as List<dynamic>) {
            final rawId = rawChapter['id'] as String;
            final canonicalId =
                ChapterIdentity.canonical(subject.id, catalogBook.id, rawId);
            expect(retained.containsKey(canonicalId), isTrue);
            if (canonicalId != rawId) {
              final original =
                  Chapter.fromJson(Map<String, dynamic>.from(rawChapter))
                      .toJson()
                    ..remove('id');
              final canonical = retained[canonicalId]!.toJson()..remove('id');
              expect(canonical, original,
                  reason: 'Legacy alias must match the entire lesson and quiz');
            }
          }

          for (final ch in book.chapters) {
            expect(ch.id.isNotEmpty, isTrue);
            expect(ch.title.isNotEmpty, isTrue);
            expect(ch.content.isNotEmpty, isTrue,
                reason:
                    '${ch.title} in ${catalogBook.title} must have reading content');

            for (final mcq in ch.mcqs) {
              expect(mcq.question.isNotEmpty, isTrue);
              expect(mcq.options.length, greaterThanOrEqualTo(2));
              expect(
                  mcq.correctIndex, inInclusiveRange(0, mcq.options.length - 1),
                  reason:
                      'correctIndex out of bounds for question: "${mcq.question}"');
            }
          }
        });
      }
    }
  });
}
