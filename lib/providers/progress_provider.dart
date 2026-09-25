import 'package:flutter/material.dart';
import '../models/user_progress.dart';
import '../services/database_helper.dart';

class ProgressProvider extends ChangeNotifier {
  final DatabaseHelper _dbHelper = DatabaseHelper.instance;

  final Set<String> _readChapterKeys = {};
  final Map<String, QuizRecord> _bestScores = {};
  LastPosition? _lastPosition;
  bool _isLoading = true;

  bool get isLoading => _isLoading;
  LastPosition? get lastPosition => _lastPosition;

  ProgressProvider() {
    loadProgress();
  }

  Future<void> loadProgress() async {
    _isLoading = true;
    notifyListeners();

    try {
      _lastPosition = await _dbHelper.getLastPosition();
      // Additional cached progress can be populated as subjects/books are opened
    } catch (e) {
      debugPrint('Error loading progress from database: $e');
    } finally {
      _isLoading = false;
      notifyListeners();
    }
  }

  String _key(String subjectId, String bookId, String chapterId) =>
      '${subjectId}_${bookId}_$chapterId';

  Future<void> ensureBookLoaded(String subjectId, String bookId) async {
    final readIds = await _dbHelper.getReadChapterIds(
      subjectId: subjectId,
      bookId: bookId,
    );
    for (final chId in readIds) {
      _readChapterKeys.add(_key(subjectId, bookId, chId));
    }

    final scores = await _dbHelper.getBestScoresForBook(
      subjectId: subjectId,
      bookId: bookId,
    );
    for (final entry in scores.entries) {
      _bestScores[_key(subjectId, bookId, entry.key)] = entry.value;
    }
    notifyListeners();
  }

  bool isChapterRead(String subjectId, String bookId, String chapterId) {
    return _readChapterKeys.contains(_key(subjectId, bookId, chapterId));
  }

  QuizRecord? getBestQuizScore(String subjectId, String bookId, String chapterId) {
    return _bestScores[_key(subjectId, bookId, chapterId)];
  }

  Future<void> markChapterRead({
    required String subjectId,
    required String bookId,
    required String chapterId,
  }) async {
    final key = _key(subjectId, bookId, chapterId);
    if (!_readChapterKeys.contains(key)) {
      _readChapterKeys.add(key);
      await _dbHelper.markChapterRead(
        subjectId: subjectId,
        bookId: bookId,
        chapterId: chapterId,
      );
      notifyListeners();
    }
  }

  Future<void> recordQuizScore({
    required String subjectId,
    required String bookId,
    required String chapterId,
    required int score,
    required int total,
  }) async {
    final record = QuizRecord(
      subjectId: subjectId,
      bookId: bookId,
      chapterId: chapterId,
      score: score,
      total: total,
      completedAt: DateTime.now(),
    );

    await _dbHelper.saveQuizScore(record);

    final key = _key(subjectId, bookId, chapterId);
    final existing = _bestScores[key];
    if (existing == null || score > existing.score) {
      _bestScores[key] = record;
    }
    // Also mark chapter as read if attempted quiz
    markChapterRead(subjectId: subjectId, bookId: bookId, chapterId: chapterId);
    notifyListeners();
  }

  Future<void> updateLastPosition({
    required String subjectId,
    required String bookId,
    required String chapterId,
    required String subjectName,
    required String bookTitle,
    required String chapterTitle,
  }) async {
    final position = LastPosition(
      subjectId: subjectId,
      bookId: bookId,
      chapterId: chapterId,
      subjectName: subjectName,
      bookTitle: bookTitle,
      chapterTitle: chapterTitle,
      updatedAt: DateTime.now(),
    );
    _lastPosition = position;
    await _dbHelper.saveLastPosition(position);
    notifyListeners();
  }

  int getReadCountForBook(String subjectId, String bookId) {
    final prefix = '${subjectId}_${bookId}_';
    return _readChapterKeys.where((k) => k.startsWith(prefix)).length;
  }

  int getReadCountForSubject(String subjectId) {
    final prefix = '${subjectId}_';
    return _readChapterKeys.where((k) => k.startsWith(prefix)).length;
  }

  Future<void> resetAllProgress() async {
    await _dbHelper.resetAllProgress();
    _readChapterKeys.clear();
    _bestScores.clear();
    _lastPosition = null;
    notifyListeners();
  }
}
