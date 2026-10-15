import 'dart:convert';
import 'dart:io';
import 'package:flutter_test/flutter_test.dart';

void main() {
  test('RAS geography retains teaching and revision beyond the old block cap',
      () {
    final data = jsonDecode(
        File('assets/content/rassetu/rassetu_book2.json').readAsStringSync());
    final chapter = data['chapters'][0];
    final text = (chapter['content'] as List).map((b) => b['value']).join('\n');
    expect(text, contains('3.7 अरावली के प्रमुख दर्रे'));
    expect(text, contains('## भाग 4:'));
    expect(text, contains('## भाग 6:'));
    expect(text, contains('6.2 अन्य पुस्तकों से जुड़ाव'));
    expect(text, isNot(contains('#### प्रश्न 45')));
    expect((chapter['mcqs'] as List).length, greaterThan(20));
  });

  for (final number in [7, 8]) {
    test('Vigyan book $number retains applications, examples, and revision',
        () {
      final data = jsonDecode(
          File('assets/content/vigyansetu/vigyansetu_book$number.json')
              .readAsStringSync());
      for (final chapter in data['chapters']) {
        final text =
            (chapter['content'] as List).map((b) => b['value']).join('\n');
        for (final section in [8, 9, 10]) {
          expect(text, contains('भाग $section:'), reason: chapter['title']);
        }
      }
    });
  }
}
