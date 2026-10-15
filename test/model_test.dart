import 'dart:convert';
import 'dart:io';
import 'package:flutter_test/flutter_test.dart';
import 'package:setu_learning/models/book.dart';
import 'package:setu_learning/models/user_progress.dart';

void main() {
  group('JSON Content & Model Validation Tests', () {
    test('MathSetu Book 1 JSON parses properly into models', () {
      final file = File('assets/content/mathsetu/mathsetu_book1.json');
      expect(file.existsSync(), isTrue,
          reason: 'mathsetu_book1.json must exist');

      final content = file.readAsStringSync();
      final Map<String, dynamic> json = jsonDecode(content);

      expect(json['subject'], equals('MathSetu'));
      final book = Book.fromBookJson(
        json,
        id: 'mathsetu_b1',
        subjectId: 'mathsetu',
        bookNumber: 1,
        description: 'Test Book',
        jsonAssetPath: 'assets/content/mathsetu/mathsetu_book1.json',
      );

      expect(book.chapters.length, greaterThanOrEqualTo(4));
      for (final ch in book.chapters) {
        expect(ch.id.isNotEmpty, isTrue);
        expect(ch.title.isNotEmpty, isTrue);
        expect(ch.content.isNotEmpty, isTrue);
        for (final mcq in ch.mcqs) {
          expect(mcq.question.isNotEmpty, isTrue);
          expect(mcq.options.length, greaterThanOrEqualTo(2));
          expect(mcq.correctIndex, inInclusiveRange(0, mcq.options.length - 1));
        }
      }
    });

    test('EnglishSetu literature MCQ book parses properly into models', () {
      final file =
          File('assets/content/englishsetu/first_grade_literature_mcqs.json');
      expect(file.existsSync(), isTrue,
          reason: 'first_grade_literature_mcqs.json must exist');

      final content = file.readAsStringSync();
      final Map<String, dynamic> json = jsonDecode(content);

      expect(json['subject'], equals('EnglishSetu'));
      final book = Book.fromBookJson(
        json,
        id: 'englishsetu_first_grade_mcqs',
        subjectId: 'englishsetu',
        bookNumber: 1,
        description: 'Test English Book',
        jsonAssetPath:
            'assets/content/englishsetu/first_grade_literature_mcqs.json',
      );

      expect(book.chapters.isNotEmpty, isTrue);
      for (final ch in book.chapters) {
        expect(ch.id.isNotEmpty, isTrue);
        expect(ch.title.isNotEmpty, isTrue);
        for (final mcq in ch.mcqs) {
          expect(mcq.correctIndex, inInclusiveRange(0, mcq.options.length - 1));
        }
      }
    });

    test('UserProgress serialization and deserialization', () {
      final progress = ChapterProgress(
        subjectId: 'mathsetu',
        bookId: 'mathsetu_b1',
        chapterId: 'ch1',
        isRead: true,
        lastReadAt: DateTime(2026, 9, 25, 12, 0),
      );

      final map = progress.toMap();
      expect(map['is_read'], equals(1));

      final restored = ChapterProgress.fromMap(map);
      expect(restored.subjectId, equals('mathsetu'));
      expect(restored.isRead, isTrue);
    });

    test('QuizRecord scoring calculation', () {
      final quiz = QuizRecord(
        subjectId: 'mathsetu',
        bookId: 'mathsetu_b1',
        chapterId: 'ch1',
        score: 4,
        total: 5,
        completedAt: DateTime.now(),
      );

      expect(quiz.percentage, equals(80.0));
    });
  });
}
