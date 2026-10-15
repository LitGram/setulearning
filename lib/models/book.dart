import 'dart:convert';
import 'chapter.dart';

class Book {
  final String id;
  final String subjectId;
  final int bookNumber;
  final String title;
  final String description;
  final String jsonAssetPath;
  final int expectedChapterCount;
  List<Chapter> chapters;

  Book({
    required this.id,
    required this.subjectId,
    required this.bookNumber,
    required this.title,
    required this.description,
    required this.jsonAssetPath,
    this.expectedChapterCount = 0,
    this.chapters = const [],
  });

  factory Book.fromBookJson(
    Map<String, dynamic> json, {
    required String id,
    required String subjectId,
    required int bookNumber,
    required String description,
    required String jsonAssetPath,
  }) {
    // Imported books can contain the same lesson under two different IDs.
    // Compare the entire lesson and practice, never just its display title.
    final chaptersList = <Chapter>[];
    final seen = <String>{};
    for (final raw in json['chapters'] as List<dynamic>? ?? []) {
      final chapter = Chapter.fromJson(raw as Map<String, dynamic>);
      final payload = chapter.toJson()..remove('id');
      if (seen.add(jsonEncode(payload))) chaptersList.add(chapter);
    }

    return Book(
      id: id,
      subjectId: subjectId,
      bookNumber: bookNumber,
      title: json['book'] as String? ?? 'Book $bookNumber',
      description: description,
      jsonAssetPath: jsonAssetPath,
      expectedChapterCount: chaptersList.length,
      chapters: chaptersList,
    );
  }

  int get chapterCount =>
      chapters.isNotEmpty ? chapters.length : expectedChapterCount;
}
