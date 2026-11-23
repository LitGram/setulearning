import 'package:flutter/foundation.dart';
import 'package:path/path.dart';
import 'package:path_provider/path_provider.dart';
import 'package:sqflite/sqflite.dart';
import '../models/user_progress.dart';

class DatabaseHelper {
  static final DatabaseHelper instance = DatabaseHelper._init();
  static Database? _database;

  // In-memory fallback for platforms or tests where sqflite native driver is unavailable
  final Map<String, ChapterProgress> _memChapterProgress = {};
  final List<QuizRecord> _memQuizRecords = [];
  LastPosition? _memLastPosition;

  DatabaseHelper._init();

  Future<Database?> get database async {
    if (_database != null) return _database;
    try {
      _database = await _initDB('setu_learning.db');
      return _database;
    } catch (e) {
      if (!kIsWeb && defaultTargetPlatform == TargetPlatform.android) rethrow;
      debugPrint('Database initialization fallback to memory: $e');
      return null;
    }
  }

  Future<Database> _initDB(String filePath) async {
    String dbPath;
    if (kIsWeb) {
      dbPath = filePath;
    } else {
      final docsDir = await getApplicationDocumentsDirectory();
      dbPath = join(docsDir.path, filePath);
    }

    return await openDatabase(
      dbPath,
      version: 1,
      onCreate: _createDB,
    );
  }

  Future<void> _createDB(Database db, int version) async {
    await db.execute('''
      CREATE TABLE chapter_progress (
        subject_id TEXT NOT NULL,
        book_id TEXT NOT NULL,
        chapter_id TEXT NOT NULL,
        is_read INTEGER NOT NULL DEFAULT 0,
        last_read_at TEXT,
        PRIMARY KEY (subject_id, book_id, chapter_id)
      )
    ''');

    await db.execute('''
      CREATE TABLE quiz_scores (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        subject_id TEXT NOT NULL,
        book_id TEXT NOT NULL,
        chapter_id TEXT NOT NULL,
        score INTEGER NOT NULL,
        total INTEGER NOT NULL,
        completed_at TEXT NOT NULL
      )
    ''');

    await db.execute('''
      CREATE TABLE last_position (
        id INTEGER PRIMARY KEY CHECK (id = 1),
        subject_id TEXT NOT NULL,
        book_id TEXT NOT NULL,
        chapter_id TEXT NOT NULL,
        subject_name TEXT NOT NULL,
        book_title TEXT NOT NULL,
        chapter_title TEXT NOT NULL,
        updated_at TEXT NOT NULL
      )
    ''');
  }

  // --- Chapter Progress ---

  Future<void> markChapterRead({
    required String subjectId,
    required String bookId,
    required String chapterId,
  }) async {
    final now = DateTime.now();
    final db = await database;
    if (db != null) {
      await db.insert(
        'chapter_progress',
        {
          'subject_id': subjectId,
          'book_id': bookId,
          'chapter_id': chapterId,
          'is_read': 1,
          'last_read_at': now.toIso8601String(),
        },
        conflictAlgorithm: ConflictAlgorithm.replace,
      );
    } else {
      final key = '${subjectId}_${bookId}_$chapterId';
      _memChapterProgress[key] = ChapterProgress(
        subjectId: subjectId,
        bookId: bookId,
        chapterId: chapterId,
        isRead: true,
        lastReadAt: now,
      );
    }
  }

  Future<bool> isChapterRead({
    required String subjectId,
    required String bookId,
    required String chapterId,
  }) async {
    final db = await database;
    if (db != null) {
      final maps = await db.query(
        'chapter_progress',
        where: 'subject_id = ? AND book_id = ? AND chapter_id = ?',
        whereArgs: [subjectId, bookId, chapterId],
      );
      if (maps.isNotEmpty) {
        return (maps.first['is_read'] as int? ?? 0) == 1;
      }
      return false;
    } else {
      final key = '${subjectId}_${bookId}_$chapterId';
      return _memChapterProgress[key]?.isRead ?? false;
    }
  }

  Future<Set<String>> getReadChapterIds({
    required String subjectId,
    required String bookId,
  }) async {
    final db = await database;
    if (db != null) {
      final maps = await db.query(
        'chapter_progress',
        columns: ['chapter_id'],
        where: 'subject_id = ? AND book_id = ? AND is_read = 1',
        whereArgs: [subjectId, bookId],
      );
      return maps.map((m) => m['chapter_id'] as String).toSet();
    } else {
      final prefix = '${subjectId}_${bookId}_';
      return _memChapterProgress.entries
          .where((e) => e.key.startsWith(prefix) && e.value.isRead)
          .map((e) => e.value.chapterId)
          .toSet();
    }
  }

  Future<int> getReadChaptersCount(
      {required String subjectId, String? bookId}) async {
    final db = await database;
    if (db != null) {
      String where = 'subject_id = ? AND is_read = 1';
      List<dynamic> whereArgs = [subjectId];
      if (bookId != null) {
        where += ' AND book_id = ?';
        whereArgs.add(bookId);
      }
      final result = await db.rawQuery(
        'SELECT COUNT(*) as count FROM chapter_progress WHERE $where',
        whereArgs,
      );
      return Sqflite.firstIntValue(result) ?? 0;
    } else {
      return _memChapterProgress.values
          .where((p) =>
              p.subjectId == subjectId &&
              (bookId == null || p.bookId == bookId) &&
              p.isRead)
          .length;
    }
  }

  Future<Set<String>> getAllReadChapterKeys() async {
    final db = await database;
    if (db != null) {
      final maps = await db.query(
        'chapter_progress',
        columns: ['subject_id', 'book_id', 'chapter_id'],
        where: 'is_read = 1',
      );
      return maps
          .map((m) => '${m['subject_id']}_${m['book_id']}_${m['chapter_id']}')
          .toSet();
    } else {
      return _memChapterProgress.entries
          .where((e) => e.value.isRead)
          .map((e) => e.key)
          .toSet();
    }
  }

  // --- Quiz Records ---

  Future<void> saveQuizScore(QuizRecord record) async {
    final db = await database;
    if (db != null) {
      await db.insert('quiz_scores', record.toMap());
    } else {
      _memQuizRecords.add(record);
    }
  }

  Future<QuizRecord?> getBestQuizScore({
    required String subjectId,
    required String bookId,
    required String chapterId,
  }) async {
    final db = await database;
    if (db != null) {
      final maps = await db.query(
        'quiz_scores',
        where: 'subject_id = ? AND book_id = ? AND chapter_id = ?',
        whereArgs: [subjectId, bookId, chapterId],
        orderBy: 'score DESC, completed_at DESC',
        limit: 1,
      );
      if (maps.isNotEmpty) {
        return QuizRecord.fromMap(maps.first);
      }
      return null;
    } else {
      final matches = _memQuizRecords
          .where((q) =>
              q.subjectId == subjectId &&
              q.bookId == bookId &&
              q.chapterId == chapterId)
          .toList();
      if (matches.isEmpty) return null;
      matches.sort((a, b) => b.score.compareTo(a.score));
      return matches.first;
    }
  }

  Future<Map<String, QuizRecord>> getBestScoresForBook({
    required String subjectId,
    required String bookId,
  }) async {
    final db = await database;
    final Map<String, QuizRecord> resultMap = {};

    if (db != null) {
      final maps = await db.query(
        'quiz_scores',
        where: 'subject_id = ? AND book_id = ?',
        whereArgs: [subjectId, bookId],
        orderBy: 'score DESC',
      );
      for (final map in maps) {
        final record = QuizRecord.fromMap(map);
        if (!resultMap.containsKey(record.chapterId)) {
          resultMap[record.chapterId] = record;
        }
      }
    } else {
      for (final record in _memQuizRecords) {
        if (record.subjectId == subjectId && record.bookId == bookId) {
          if (!resultMap.containsKey(record.chapterId) ||
              record.score > resultMap[record.chapterId]!.score) {
            resultMap[record.chapterId] = record;
          }
        }
      }
    }
    return resultMap;
  }

  Future<Map<String, QuizRecord>> getAllBestScores() async {
    final db = await database;
    final Map<String, QuizRecord> resultMap = {};

    if (db != null) {
      final maps = await db.query(
        'quiz_scores',
        orderBy: 'score DESC, completed_at DESC',
      );
      for (final map in maps) {
        final record = QuizRecord.fromMap(map);
        final key = '${record.subjectId}_${record.bookId}_${record.chapterId}';
        if (!resultMap.containsKey(key)) {
          resultMap[key] = record;
        }
      }
    } else {
      for (final record in _memQuizRecords) {
        final key = '${record.subjectId}_${record.bookId}_${record.chapterId}';
        if (!resultMap.containsKey(key) ||
            record.score > resultMap[key]!.score) {
          resultMap[key] = record;
        }
      }
    }
    return resultMap;
  }

  // --- Resume Last Position ---

  Future<void> saveLastPosition(LastPosition position) async {
    final db = await database;
    if (db != null) {
      await db.insert(
        'last_position',
        {
          'id': 1,
          'subject_id': position.subjectId,
          'book_id': position.bookId,
          'chapter_id': position.chapterId,
          'subject_name': position.subjectName,
          'book_title': position.bookTitle,
          'chapter_title': position.chapterTitle,
          'updated_at': position.updatedAt.toIso8601String(),
        },
        conflictAlgorithm: ConflictAlgorithm.replace,
      );
    } else {
      _memLastPosition = position;
    }
  }

  Future<LastPosition?> getLastPosition() async {
    final db = await database;
    if (db != null) {
      final maps = await db.query('last_position', where: 'id = 1');
      if (maps.isNotEmpty) {
        return LastPosition.fromMap(maps.first);
      }
      return null;
    } else {
      return _memLastPosition;
    }
  }

  // --- Reset All Progress ---

  Future<void> resetAllProgress() async {
    final db = await database;
    if (db != null) {
      await db.delete('chapter_progress');
      await db.delete('quiz_scores');
      await db.delete('last_position');
    }
    _memChapterProgress.clear();
    _memQuizRecords.clear();
    _memLastPosition = null;
  }
}
