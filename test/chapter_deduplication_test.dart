import 'dart:convert';
import 'package:flutter_test/flutter_test.dart';
import 'package:shared_preferences/shared_preferences.dart';
import 'package:setu_learning/models/book.dart';
import 'package:setu_learning/services/chapter_identity.dart';
import 'package:setu_learning/services/study_session_store.dart';

void main() {
  TestWidgetsFlutterBinding.ensureInitialized();
  test('Only full duplicate lessons are removed, preserving order and IDs', () {
    Map<String, dynamic> chapter(String id, String text) => {
          'id': id,
          'title': 'Same title',
          'content': [
            {'type': 'text', 'value': text}
          ],
          'mcqs': []
        };
    final book = Book.fromBookJson({
      'chapters': [
        chapter('ch1', 'First lesson'),
        chapter('ch2', 'First lesson'),
        chapter('ch3', 'Second lesson'),
        {
          ...chapter('ch4', 'Second lesson'),
          'mcqs': [
            {
              'question': 'Different practice',
              'options': ['A', 'B'],
              'correctIndex': 0
            }
          ]
        },
      ]
    },
        id: 'test',
        subjectId: 'test',
        bookNumber: 1,
        description: '',
        jsonAssetPath: '');
    expect(book.chapters.map((ch) => ch.id), ['ch1', 'ch3', 'ch4']);
    expect(book.chapterCount, 3);
  });

  test('Legacy duplicate progress keys collapse to one chapter', () {
    expect(ChapterIdentity.canonicalProgressKey('rassetu_rassetu_b5_ch02'),
        'rassetu_rassetu_b5_ch01');
    expect(
        ChapterIdentity.canonical('mathsetu', 'mathsetu_b5', 'ch02'), 'ch02');
    expect(ChapterIdentity.canonical('rassetu', 'rassetu_b5', 'ch50'), 'ch49');
  });

  test('Saved position and quiz draft from the duplicate remain accessible',
      () async {
    final legacy =
        'study_quiz_${jsonEncode(['rassetu', 'rassetu_b5', 'ch02'])}';
    SharedPreferences.setMockInitialValues({
      legacy: jsonEncode({
        'answers': {'0': 1}
      })
    });
    final key = StudySessionStore.key('quiz', 'rassetu', 'rassetu_b5', 'ch01');
    expect((await StudySessionStore.read(key))!['answers'], {'0': 1});
    expect(StudySessionStore.key('quiz', 'rassetu', 'rassetu_b5', 'ch02'), key);
    await StudySessionStore.remove(key);
    expect(await StudySessionStore.read(key), isNull);
  });
}
