/// Legacy duplicate IDs in the six bundled RAS books. Keep the first ID so
/// existing history, read flags, and quiz records still identify the lesson.
class ChapterIdentity {
  static const _legacyCounts = {
    'rassetu_b1': 40,
    'rassetu_b2': 54,
    'rassetu_b3': 44,
    'rassetu_b4': 48,
    'rassetu_b5': 50,
    'rassetu_b6': 44,
  };

  static String canonical(String subject, String book, String chapter) {
    // Old M.Sc. subsections now sit inside complete units. Resolve history
    // links to their unit without treating a read subsection as a read unit.
    if (subject == 'mscphysics') {
      const starts = {
        'mscphysics_mathematical_physics': [1, 22, 42, 65],
        'mscphysics_classical_mechanics': [1, 17, 33, 46],
        'mscphysics_quantum_mechanics_i': [1, 19, 34, 50],
        'mscphysics_statistical_physics': [1, 9, 16, 24],
      };
      final boundaries = starts[book];
      final legacy = RegExp(r'^ch(\d+)$').firstMatch(chapter);
      if (boundaries != null && legacy != null) {
        final number = int.parse(legacy[1]!);
        for (var unit = 0; unit < 3; unit++) {
          if (number >= boundaries[unit] && number < boundaries[unit + 1]) {
            return 'unit${unit + 1}';
          }
        }
      }
    }
    final count = subject == 'rassetu' ? _legacyCounts[book] : null;
    final match = RegExp(r'^ch(\d{2})$').firstMatch(chapter);
    if (count == null || match == null) return chapter;
    final number = int.parse(match[1]!);
    if (number < 1 || number > count || number.isOdd) return chapter;
    return 'ch${(number - 1).toString().padLeft(2, '0')}';
  }

  static String? duplicate(String subject, String book, String chapter) {
    final canonicalId = canonical(subject, book, chapter);
    final number = int.tryParse(canonicalId.replaceFirst('ch', ''));
    final count = subject == 'rassetu' ? _legacyCounts[book] : null;
    if (count == null ||
        number == null ||
        number < 1 ||
        number >= count ||
        number.isEven) {
      return null;
    }
    return 'ch${(number + 1).toString().padLeft(2, '0')}';
  }

  static String canonicalProgressKey(String key) {
    for (final book in _legacyCounts.keys) {
      final prefix = 'rassetu_${book}_';
      if (key.startsWith(prefix)) {
        return '$prefix${canonical('rassetu', book, key.substring(prefix.length))}';
      }
    }
    return key;
  }

  static bool isRetiredProgressKey(String key) {
    final english =
        RegExp(r'^englishsetu_englishsetu_(.+)_ch\d+$').firstMatch(key);
    if (english != null &&
        const {
          'phonetics',
          'grammar_glossary',
          'first_grade_literature_1',
          'first_grade_literature_2',
          'shakespeare_mcqs',
          'mayor_casterbridge',
          'pg_literature',
          'first_grade_mcqs',
          'vendor_of_sweets',
          'second_grade_guide',
          'second_grade_literature',
        }.contains(english[1])) {
      return true;
    }
    final match =
        RegExp(r'^mscphysics_(mscphysics_[a-z_]+)_(ch\d+)$').firstMatch(key);
    return match != null &&
        canonical('mscphysics', match[1]!, match[2]!) != match[2];
  }
}
