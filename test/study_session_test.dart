import 'package:flutter_test/flutter_test.dart';
import 'package:shared_preferences/shared_preferences.dart';
import 'package:setu_learning/services/study_session_store.dart';

void main() {
  TestWidgetsFlutterBinding.ensureInitialized();
  setUp(() => SharedPreferences.setMockInitialValues({}));

  test('Chapter sessions remain distinct when ids contain separators',
      () async {
    final first = StudySessionStore.key('reading', 'a_b', 'c', 'd');
    final second = StudySessionStore.key('reading', 'a', 'b_c', 'd');
    await StudySessionStore.write(first, {'offset': 400, 'anchor': 2});
    await StudySessionStore.write(second, {'offset': 800, 'anchor': 5});
    expect((await StudySessionStore.read(first))!['anchor'], 2);
    expect((await StudySessionStore.read(second))!['offset'], 800);
  });

  test('Reset clears reading and quiz drafts but preserves preferences',
      () async {
    final prefs = await SharedPreferences.getInstance();
    await prefs.setString('theme_mode', 'dark');
    await StudySessionStore.write('study_reading_test', {'offset': 200});
    await StudySessionStore.write('study_quiz_test', {
      'answers': {'0': 1}
    });
    await StudySessionStore.reset();
    expect(await StudySessionStore.read('study_reading_test'), isNull);
    expect(await StudySessionStore.read('study_quiz_test'), isNull);
    expect(prefs.getString('theme_mode'), 'dark');
  });

  test('Malformed local session can be ignored and overwritten', () async {
    final prefs = await SharedPreferences.getInstance();
    await prefs.setString('study_test', '{broken');
    expect(await StudySessionStore.read('study_test'), isNull);
    await StudySessionStore.write('study_test', {'offset': 0});
    expect((await StudySessionStore.read('study_test'))!['offset'], 0);
  });
}
