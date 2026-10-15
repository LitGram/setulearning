import 'package:flutter/material.dart';
import '../models/user_progress.dart';
import '../services/database_helper.dart';
import '../services/study_session_store.dart';
import '../services/chapter_identity.dart';

class ProgressProvider extends ChangeNotifier {
  final DatabaseHelper _dbHelper = DatabaseHelper.instance;

  final Set<String> _readChapterKeys = {};
  final Map<String, QuizRecord> _bestScores = {};
  LastPosition? _lastPosition;
  bool _isLoading = true;
  String? loadError;

  bool get isLoading => _isLoading;
  LastPosition? get lastPosition => _lastPosition;

  ProgressProvider() {
    loadProgress();
  }

  Future<void> loadProgress() async {
    _isLoading = true;
    loadError = null;
    notifyListeners();

    try {
      _lastPosition = await _dbHelper.getLastPosition();
      final readKeys = await _dbHelper.getAllReadChapterKeys();
      _readChapterKeys.clear();
      _readChapterKeys.addAll(readKeys
          .where((key) => !ChapterIdentity.isRetiredProgressKey(key))
          .map(ChapterIdentity.canonicalProgressKey));

      final scores = await _dbHelper.getAllBestScores();
      _bestScores.clear();
      for (final entry in scores.entries) {
        final key = ChapterIdentity.canonicalProgressKey(entry.key);
        if (!_bestScores.containsKey(key) ||
            entry.value.score > _bestScores[key]!.score) {
          _bestScores[key] = entry.value;
        }
      }
    } catch (e) {
      loadError = e.toString();
      debugPrint('Error loading progress from database: $e');
    } finally {
      _isLoading = false;
      notifyListeners();
    }
  }

  String _key(String subjectId, String bookId, String chapterId) =>
      '${subjectId}_${bookId}_${ChapterIdentity.canonical(subjectId, bookId, chapterId)}';

  Future<void> ensureBookLoaded(String subjectId, String bookId) async {
    try {
      final readIds = await _dbHelper.getReadChapterIds(
        subjectId: subjectId,
        bookId: bookId,
      );
      for (final chId in readIds) {
        if (ChapterIdentity.isRetiredProgressKey(
            '${subjectId}_${bookId}_$chId')) {
          continue;
        }
        _readChapterKeys.add(_key(subjectId, bookId, chId));
      }

      final scores = await _dbHelper.getBestScoresForBook(
        subjectId: subjectId,
        bookId: bookId,
      );
      for (final entry in scores.entries) {
        final key = _key(subjectId, bookId, entry.key);
        if (!_bestScores.containsKey(key) ||
            entry.value.score > _bestScores[key]!.score) {
          _bestScores[key] = entry.value;
        }
      }
    } catch (error) {
      loadError = error.toString();
    }
    notifyListeners();
  }

  bool isChapterRead(String subjectId, String bookId, String chapterId) {
    return _readChapterKeys.contains(_key(subjectId, bookId, chapterId));
  }

  QuizRecord? getBestQuizScore(
      String subjectId, String bookId, String chapterId) {
    return _bestScores[_key(subjectId, bookId, chapterId)];
  }

  Future<void> markChapterRead({
    required String subjectId,
    required String bookId,
    required String chapterId,
  }) async {
    final key = _key(subjectId, bookId, chapterId);
    if (!_readChapterKeys.contains(key)) {
      await _dbHelper.markChapterRead(
        subjectId: subjectId,
        bookId: bookId,
        chapterId: chapterId,
      );
      _readChapterKeys.add(key);
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
    await StudySessionStore.reset();
    _readChapterKeys.clear();
    _bestScores.clear();
    _lastPosition = null;
    notifyListeners();
  }
}
