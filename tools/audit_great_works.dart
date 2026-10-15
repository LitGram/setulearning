// Dump Markdown's rendered text for comparison with the original EPUB lessons.
// dart run tools/audit_great_works.dart > artifacts/great_works_rendered_text.json
// python tools/import_great_works.py --verify-render artifacts/great_works_rendered_text.json
import 'dart:convert';
import 'dart:io';
import 'package:markdown/markdown.dart' as md;

void main() {
  final result = <String, Map<String, String>>{};
  final files = Directory('assets/content/greatworks')
      .listSync()
      .whereType<File>()
      .where((file) => file.path.endsWith('.json'));
  for (final file in files) {
    final data = jsonDecode(file.readAsStringSync()) as Map<String, dynamic>;
    final chapters = <String, String>{};
    for (final chapter in data['chapters'] as List<dynamic>) {
      final text = StringBuffer();
      for (final block in chapter['content'] as List<dynamic>) {
        final document =
            md.Document(extensionSet: md.ExtensionSet.gitHubFlavored);
        for (final node
            in document.parseLines((block['value'] as String).split('\n'))) {
          text.write(node.textContent);
        }
      }
      chapters[chapter['id'] as String] = text.toString();
    }
    final name = file.uri.pathSegments.last.replaceFirst('.json', '');
    result[name] = chapters;
  }
  stdout.write(jsonEncode(result));
}
