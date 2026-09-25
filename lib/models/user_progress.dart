class ChapterProgress {
  final String subjectId;
  final String bookId;
  final String chapterId;
  final bool isRead;
  final DateTime? lastReadAt;

  const ChapterProgress({
    required this.subjectId,
    required this.bookId,
    required this.chapterId,
    required this.isRead,
    this.lastReadAt,
  });

  Map<String, dynamic> toMap() {
    return {
      'subject_id': subjectId,
      'book_id': bookId,
      'chapter_id': chapterId,
      'is_read': isRead ? 1 : 0,
      'last_read_at': lastReadAt?.toIso8601String(),
    };
  }

  factory ChapterProgress.fromMap(Map<String, dynamic> map) {
    return ChapterProgress(
      subjectId: map['subject_id'] as String,
      bookId: map['book_id'] as String,
      chapterId: map['chapter_id'] as String,
      isRead: (map['is_read'] as int? ?? 0) == 1,
      lastReadAt: map['last_read_at'] != null
          ? DateTime.tryParse(map['last_read_at'] as String)
          : null,
    );
  }
}

class QuizRecord {
  final int? id;
  final String subjectId;
  final String bookId;
  final String chapterId;
  final int score;
  final int total;
  final DateTime completedAt;

  const QuizRecord({
    this.id,
    required this.subjectId,
    required this.bookId,
    required this.chapterId,
    required this.score,
    required this.total,
    required this.completedAt,
  });

  double get percentage => total > 0 ? (score / total) * 100 : 0.0;

  Map<String, dynamic> toMap() {
    return {
      if (id != null) 'id': id,
      'subject_id': subjectId,
      'book_id': bookId,
      'chapter_id': chapterId,
      'score': score,
      'total': total,
      'completed_at': completedAt.toIso8601String(),
    };
  }

  factory QuizRecord.fromMap(Map<String, dynamic> map) {
    return QuizRecord(
      id: map['id'] as int?,
      subjectId: map['subject_id'] as String,
      bookId: map['book_id'] as String,
      chapterId: map['chapter_id'] as String,
      score: map['score'] as int? ?? 0,
      total: map['total'] as int? ?? 0,
      completedAt: DateTime.tryParse(map['completed_at'] as String? ?? '') ??
          DateTime.now(),
    );
  }
}

class LastPosition {
  final String subjectId;
  final String bookId;
  final String chapterId;
  final String subjectName;
  final String bookTitle;
  final String chapterTitle;
  final DateTime updatedAt;

  const LastPosition({
    required this.subjectId,
    required this.bookId,
    required this.chapterId,
    required this.subjectName,
    required this.bookTitle,
    required this.chapterTitle,
    required this.updatedAt,
  });

  Map<String, dynamic> toMap() {
    return {
      'subject_id': subjectId,
      'book_id': bookId,
      'chapter_id': chapterId,
      'subject_name': subjectName,
      'book_title': bookTitle,
      'chapter_title': chapterTitle,
      'updated_at': updatedAt.toIso8601String(),
    };
  }

  factory LastPosition.fromMap(Map<String, dynamic> map) {
    return LastPosition(
      subjectId: map['subject_id'] as String? ?? '',
      bookId: map['book_id'] as String? ?? '',
      chapterId: map['chapter_id'] as String? ?? '',
      subjectName: map['subject_name'] as String? ?? '',
      bookTitle: map['book_title'] as String? ?? '',
      chapterTitle: map['chapter_title'] as String? ?? '',
      updatedAt: DateTime.tryParse(map['updated_at'] as String? ?? '') ??
          DateTime.now(),
    );
  }
}
