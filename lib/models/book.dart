import 'chapter.dart';

class Book {
  final String id;
  final String subjectId;
  final int bookNumber;
  final String title;
  final String level;
  final String description;
  final String jsonAssetPath;
  List<Chapter> chapters;

  Book({
    required this.id,
    required this.subjectId,
    required this.bookNumber,
    required this.title,
    required this.level,
    required this.description,
    required this.jsonAssetPath,
    this.chapters = const [],
  });

  factory Book.fromBookJson(Map<String, dynamic> json, {
    required String id,
    required String subjectId,
    required int bookNumber,
    required String level,
    required String description,
    required String jsonAssetPath,
  }) {
    final chaptersList = (json['chapters'] as List<dynamic>?)
            ?.map((c) => Chapter.fromJson(c as Map<String, dynamic>))
            .toList() ??
        [];

    return Book(
      id: id,
      subjectId: subjectId,
      bookNumber: bookNumber,
      title: json['book'] as String? ?? 'Book $bookNumber',
      level: level,
      description: description,
      jsonAssetPath: jsonAssetPath,
      chapters: chaptersList,
    );
  }

  int get chapterCount => chapters.length;
}
