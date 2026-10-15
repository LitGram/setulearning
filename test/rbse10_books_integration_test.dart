import 'package:flutter_test/flutter_test.dart';
import 'package:setu_learning/services/content_service.dart';

void main() {
  TestWidgetsFlutterBinding.ensureInitialized();

  test('all seven RBSE Class 10 subjects resolve their bundled books',
      () async {
    final service = ContentService.instance;
    const expected = <String, int>{
      'rbse10_maths': 15,
      'rbse10_science': 14,
      'rbse10_social': 24,
      'rbse10_hindi': 31,
      'rbse10_english': 40,
      'rbse10_sanskrit': 22,
      'rbse10_punjabi': 23,
    };

    for (final entry in expected.entries) {
      final subject = service.getSubjectById(entry.key);
      expect(subject, isNotNull,
          reason: 'Missing catalog subject ${entry.key}');
      final book = subject!.books.single;
      final loaded = await service.loadBookContent(book);
      expect(loaded.chapters, hasLength(entry.value), reason: entry.key);
      expect(
        loaded.chapters.every((chapter) => chapter.content.isNotEmpty),
        isTrue,
        reason: '${entry.key} contains an empty chapter',
      );
    }
  });

  test('fact-checked corrections are present in app reader content', () async {
    final service = ContentService.instance;

    Future<String> content(String subjectId, String chapterId) async {
      final subject = service.getSubjectById(subjectId)!;
      final book = await service.loadBookContent(subject.books.single);
      return book.chapters
          .singleWhere((chapter) => chapter.id == chapterId)
          .content
          .map((block) => block.value)
          .join('\n');
    }

    final hindi = await content('rbse10_hindi', 'gad_ch09_netaji_ka_chashma');
    expect(hindi, contains('कहानी यह नहीं बताती कि चश्मा किस बच्चे ने लगाया'));
    expect(hindi, contains('कथावाचक यह नहीं कहता कि मोतीलाल सचमुच भूल गया था'));

    final science = await content('rbse10_science', 'sci_ch01');
    expect(science, contains('2H₂O₂ → 2H₂O + O₂ ऊष्माक्षेपी वियोजन है'));

    final social = await content('rbse10_social', 'eco_ch05_upbhokta_adhikar');
    expect(social, contains('उपभोक्ता अधिकार'));

    final hindiWriting =
        await content('rbse10_hindi', 'rac_ch30_sankshepan_pallavan');
    expect(hindiWriting, contains('संक्षिप्तीकरण एवं पल्लवन'));

    final english = await content('rbse10_english', 'gr_ch06_determiners');
    expect(english, contains('Determiners'));
  });
}
