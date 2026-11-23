import 'dart:convert';
import 'dart:io';
import 'package:flutter_test/flutter_test.dart';
import 'package:flutter_math_fork/flutter_math.dart';
import 'package:setu_learning/widgets/markdown_content.dart';

void main() {
  test('Audit unique bundled math expressions', () {
    final expressions = <String, String>{};
    final pattern = RegExp(
        r'(?<!\\)\$\$([\s\S]+?)\$\$|(?<![\\$])\$(?!\$)([^$\n]+?)(?<!\\)\$(?!\$)');
    void collect(dynamic value, String file) {
      if (value is Map) {
        if (value['type'] == 'formula' && value['value'] is String) {
          final source = value['value'] as String;
          if (source.contains(r'\') && !source.contains(r'$')) {
            expressions[source] = file;
          }
        }
        for (final child in value.values) {
          collect(child, file);
        }
      } else if (value is List) {
        for (final child in value) {
          collect(child, file);
        }
      } else if (value is String) {
        expect(value.contains('\u000crac'), isFalse, reason: file);
        for (final match in pattern.allMatches(value)) {
          expressions[match.group(1) ?? match.group(2)!] = file;
        }
      }
    }

    for (final file in Directory('assets/content')
        .listSync(recursive: true)
        .whereType<File>()) {
      if (file.path.endsWith('.json')) {
        collect(jsonDecode(file.readAsStringSync()), file.path);
      }
    }
    final failures = <Map<String, String>>[];
    for (final entry in expressions.entries) {
      final math = Math.tex(MarkdownContent.normalizeMath(entry.key));
      if (math.parseError != null) {
        failures.add({
          'file': entry.value,
          'expression': entry.key,
          'error': math.parseError.toString()
        });
      }
    }
    Directory('artifacts').createSync();
    File('artifacts/math-rendering-audit.json').writeAsStringSync(
        const JsonEncoder.withIndent('  ').convert(
            {'uniqueExpressions': expressions.length, 'failures': failures}));
    expect(expressions, isNotEmpty);
    expect(failures, isEmpty, reason: 'See artifacts/math-rendering-audit.json');
  });
}
