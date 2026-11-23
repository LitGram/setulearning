import 'dart:convert';
import 'package:shared_preferences/shared_preferences.dart';
import 'chapter_identity.dart';

/// Local, per-chapter reading positions and unfinished practice attempts.
class StudySessionStore {
  static String key(String kind, String subject, String book, String chapter) =>
      'study_${kind}_${jsonEncode([
            subject,
            book,
            ChapterIdentity.canonical(subject, book, chapter)
          ])}';

  static String? _legacyKey(String key) {
    final start = key.indexOf('[');
    if (start < 0) return null;
    final ids = jsonDecode(key.substring(start)) as List<dynamic>;
    final duplicate = ChapterIdentity.duplicate(
        ids[0] as String, ids[1] as String, ids[2] as String);
    return duplicate == null
        ? null
        : '${key.substring(0, start)}${jsonEncode([
                ids[0],
                ids[1],
                duplicate
              ])}';
  }

  static Future<Map<String, dynamic>?> read(String key) async {
    final prefs = await SharedPreferences.getInstance();
    final legacy = _legacyKey(key);
    final value = prefs.getString(key) ??
        (legacy == null ? null : prefs.getString(legacy));
    if (value == null) return null;
    try {
      return jsonDecode(value) as Map<String, dynamic>;
    } on FormatException {
      return null;
    }
  }

  static Future<void> write(String key, Map<String, dynamic> value) async {
    if (!await (await SharedPreferences.getInstance())
        .setString(key, jsonEncode(value))) {
      throw StateError('Could not save study session');
    }
  }

  static Future<void> remove(String key) async {
    final prefs = await SharedPreferences.getInstance();
    await prefs.remove(key);
    final legacy = _legacyKey(key);
    if (legacy != null) await prefs.remove(legacy);
  }

  static Future<void> reset() async {
    final prefs = await SharedPreferences.getInstance();
    for (final key
        in prefs.getKeys().where((key) => key.startsWith('study_'))) {
      await prefs.remove(key);
    }
  }
}
