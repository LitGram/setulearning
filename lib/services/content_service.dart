import 'dart:convert';
import 'package:flutter/foundation.dart';
import 'package:flutter/material.dart';
import 'package:flutter/services.dart';
import '../models/book.dart';
import '../models/chapter.dart';
import '../models/mcq.dart';
import '../models/subject.dart';
import 'msc_physics_catalog.dart';

Map<String, dynamic> _decodeJsonMap(String source) {
  return jsonDecode(source) as Map<String, dynamic>;
}

class ContentService {
  static final ContentService instance = ContentService._init();
  final Map<String, Book> _bookCache = {};

  ContentService._init();

  List<Subject> getSubjects() {
    return [
      Subject(
        id: 'rbse10_maths',
        name: 'RBSE 10th Mathematics',
        hindiName: 'कक्षा 10 गणित',
        tagline: 'आरबीएसई गणित · अवधारणाएँ, हल और अभ्यास',
        seedColor: const Color(0xFF4338CA),
        icon: Icons.functions_rounded,
        books: [
          _catalogBook(
            'rbse10_maths',
            'guide',
            1,
            'कक्षा 10 गणित: अध्ययन एवं अभ्यास',
            'rbse10_maths_book1.json',
            15,
          ),
        ],
      ),
      Subject(
        id: 'rbse10_social',
        name: 'RBSE 10th Social Science',
        hindiName: 'कक्षा 10 सामाजिक विज्ञान',
        tagline: 'इतिहास, भूगोल, राजनीति विज्ञान और अर्थशास्त्र',
        seedColor: const Color(0xFF166534),
        icon: Icons.public_rounded,
        books: [
          _catalogBook(
            'rbse10_social',
            'guide',
            3,
            'कक्षा 10 सामाजिक विज्ञान: अध्ययन एवं अभ्यास',
            'rbse10_social_book1.json',
            24,
          ),
        ],
      ),
      Subject(
        id: 'rbse10_hindi',
        name: 'RBSE 10th Hindi',
        hindiName: 'कक्षा 10 हिन्दी',
        tagline: 'क्षितिज, कृतिका, व्याकरण और रचनात्मक लेखन',
        seedColor: const Color(0xFFBE123C),
        icon: Icons.auto_stories_rounded,
        books: [
          _catalogBook(
            'rbse10_hindi',
            'guide',
            4,
            'कक्षा 10 हिन्दी: अध्ययन एवं अभ्यास',
            'rbse10_hindi_book1.json',
            31,
          ),
        ],
      ),
      Subject(
        id: 'rbse10_english',
        name: 'RBSE 10th English',
        hindiName: 'कक्षा 10 अंग्रेज़ी',
        tagline: 'First Flight, Footprints Without Feet, grammar and writing',
        seedColor: const Color(0xFF0F766E),
        icon: Icons.menu_book_rounded,
        books: [
          _catalogBook(
            'rbse10_english',
            'guide',
            5,
            'Class 10 English: Study and Practice',
            'rbse10_english_book1.json',
            40,
          ),
        ],
      ),
      Subject(
        id: 'rbse10_science',
        name: 'RBSE 10th Science',
        hindiName: 'कक्षा 10 विज्ञान',
        tagline: 'आरबीएसई अध्यायवार गाइड · प्रथम प्रारूप',
        seedColor: const Color(0xFF0D766E),
        icon: Icons.biotech_rounded,
        books: [
          _catalogBook(
            'rbse10_science',
            'guide',
            2,
            'कक्षा 10 विज्ञान: अध्यायवार गाइड (प्रारूप)',
            'science_book1.json',
            14,
          ),
        ],
      ),
      Subject(
        id: 'rbse10_sanskrit',
        name: 'RBSE 10th Sanskrit',
        hindiName: 'कक्षा 10 संस्कृत',
        tagline: 'आरबीएसई शेमुषी एवं व्याकरण गाइड · प्रथम प्रारूप',
        seedColor: const Color(0xFFB45309),
        icon: Icons.auto_stories_rounded,
        books: [
          _catalogBook(
            'rbse10_sanskrit',
            'guide',
            6,
            'कक्षा 10 संस्कृत: शेमुषी एवं व्याकरण गाइड (प्रारूप)',
            'sanskrit_book1.json',
            22,
          ),
        ],
      ),
      Subject(
        id: 'rbse10_punjabi',
        name: 'RBSE 10th Punjabi',
        hindiName: 'कक्षा 10 पंजाबी (ਪੰਜਾਬੀ)',
        tagline: 'ਆਰ.ਬੀ.ਐੱਸ.ਈ. ਸਾਹਿਤ ਸੁਗੰਧੀਆਂ ਅਤੇ ਵਿਆਕਰਣ ਗਾਈਡ · प्रथम प्रारूप',
        seedColor: const Color(0xFF0369A1),
        icon: Icons.translate_rounded,
        books: [
          _catalogBook(
            'rbse10_punjabi',
            'guide',
            7,
            'ਜਮਾਤ 10 ਪੰਜਾਬੀ: ਸਾਹਿਤ ਸੁਗੰਧੀਆਂ ਅਤੇ ਵਿਆਕਰਣ ਗਾਈਡ (प्रारूप)',
            'punjabi_book1.json',
            23,
          ),
        ],
      ),
      Subject(
        id: 'mathsetu',
        name: 'MathSetu',
        hindiName: 'गणित सेतु',
        tagline: 'गणना कौशल, अंकगणित से उन्नत गणित तक',
        seedColor: const Color(0xFF1E40AF), // Deep Royal Blue
        icon: Icons.calculate_rounded,
        books: _generateBookList('mathsetu', 'MathSetu', [
          'गणना कौशल, संख्या पद्धति एवं सरलीकरण',
          'अनुपात, समानुपात, प्रतिशत एवं औसत',
          'व्यावसायिक अंकगणित — लाभ-हानि, छूट, ब्याज, साझेदारी एवं मिश्रण',
          'समय, कार्य, पाइप, गति, दूरी, रेलगाड़ी एवं नाव',
          'प्रतियोगी बीजगणित एवं निर्देशांक ज्यामिति',
          'प्रतियोगी ज्यामिति',
          'क्षेत्रमिति, ठोस आकृतियाँ एवं त्रिकोणमिति',
          'आँकड़ा विश्लेषण, सांख्यिकी एवं प्रायिकता',
        ], chapterCounts: const [
          16,
          18,
          19,
          20,
          22,
          23,
          28,
          26,
        ]),
      ),
      Subject(
        id: 'englishsetu',
        name: 'EnglishSetu',
        hindiName: 'अंग्रेजी सेतु',
        tagline: 'English Grammar, Vocabulary & Comprehension',
        seedColor: const Color(0xFF0F766E), // Emerald Teal
        icon: Icons.menu_book_rounded,
        books: [
          _catalogBook(
              'englishsetu',
              'phonetics',
              1,
              'An Introduction to English Phonetics: Objective Guide',
              'phonetics_objective_guide.json',
              1),
          _catalogBook(
              'englishsetu',
              'grammar_glossary',
              2,
              'A Glossary of English Grammar: Objective Guide',
              'geoffrey_leech_grammar.json',
              1),
          _catalogBook(
              'englishsetu',
              'first_grade_literature_1',
              3,
              'RPSC First Grade English Literature: Part 1',
              'first_grade_literature_1.json',
              22),
          _catalogBook(
              'englishsetu',
              'first_grade_literature_2',
              4,
              'RPSC First Grade English Literature: Part 2',
              'first_grade_literature_2.json',
              58),
          _catalogBook(
              'englishsetu',
              'shakespeare_mcqs',
              5,
              'Mastering Shakespeare: RPSC Exam MCQs',
              'shakespeare_mcqs.json',
              28),
          _catalogBook(
              'englishsetu',
              'mayor_casterbridge',
              6,
              'The Mayor of Casterbridge: Objective Guide',
              'mayor_casterbridge_mcqs.json',
              49),
          _catalogBook(
              'englishsetu',
              'pg_literature',
              7,
              'RPSC Postgraduate Topics: Literature MCQs',
              'pg_topics_mcqs.json',
              9),
          _catalogBook(
              'englishsetu',
              'first_grade_mcqs',
              8,
              'RPSC First Grade: Literature MCQs',
              'first_grade_literature_mcqs.json',
              70),
          _catalogBook(
              'englishsetu',
              'vendor_of_sweets',
              9,
              'The Vendor of Sweets: Objective Guide',
              'vendor_of_sweets_mcqs.json',
              14),
          _catalogBook(
              'englishsetu',
              'second_grade_guide',
              10,
              'RPSC Second Grade English: Complete Guide',
              'second_grade_guide.json',
              75),
          _catalogBook(
              'englishsetu',
              'second_grade_literature',
              11,
              'RPSC Second Grade English: Literature MCQs',
              'second_grade_literature.json',
              22),
          _catalogBook('englishsetu', 'book59', 12,
              'High-Frequency English Vocabulary', 'book59.json', 4),
          _catalogBook('englishsetu', 'book60', 13,
              'Literary Terms and Poetic Devices', 'book60.json', 4),
        ],
      ),
      Subject(
        id: 'vigyansetu',
        name: 'VigyanSetu',
        hindiName: 'विज्ञान सेतु',
        tagline: 'भौतिकी, रसायन, जीव विज्ञान एवं पर्यावरण',
        seedColor: const Color(0xFFC2410C), // Deep Rust Orange
        icon: Icons.science_rounded,
        books: _generateBookList('vigyansetu', 'VigyanSetu', [
          'भौतिकी भाग-1: गति, बल एवं कार्य',
          'भौतिकी भाग-2: प्रकाश, ध्वनि एवं विद्युत',
          'रसायन विज्ञान भाग-1: पदार्थ की प्रकृति एवं परमाणु',
          'रसायन विज्ञान भाग-2: रासायनिक अभिक्रियाएं एवं धातु',
          'जीव विज्ञान भाग-1: कोशिका एवं मानव शरीर तंत्र',
          'जीव विज्ञान भाग-2: पादप कार्यिकी एवं आनुवंशिकी',
          'पर्यावरण विज्ञान एवं पारिस्थितिकी',
          'दैनिक जीवन में विज्ञान एवं प्रौद्योगिकी',
        ], chapterCounts: const [
          18,
          25,
          23,
          19,
          16,
          24,
          27,
          28
        ]),
      ),
      Subject(
        id: 'rassetu',
        name: 'RASSetu',
        hindiName: 'आरएएस सेतु',
        tagline: 'राजस्थान और अन्य प्रतियोगी परीक्षाओं की तैयारी',
        seedColor: const Color(0xFF7C2D12),
        icon: Icons.account_balance_rounded,
        books: [
          ..._generateBookList('rassetu', 'RASSetu', [
            'राजस्थान का इतिहास, कला, संस्कृति एवं विरासत',
            'राजस्थान, भारत एवं विश्व का भूगोल',
            'भारतीय इतिहास: प्राचीन, मध्यकालीन एवं आधुनिक',
            'भारतीय संविधान, शासन एवं राजस्थान प्रशासन',
            'अर्थव्यवस्था, विज्ञान एवं प्रौद्योगिकी',
            'तार्किक योग्यता, गणित एवं करेंट अफेयर्स',
          ], chapterCounts: const [
            20,
            27,
            22,
            24,
            25,
            22
          ]),
          _catalogBook('rassetu', 'mains_answer_writing', 7,
              'RAS Mains: Answer Writing', 'mains_answer_writing.json', 18,
              assetFolder: 'rassetu_supplementary'),
          _catalogBook(
              'rassetu',
              'paper4_language_essay',
              8,
              'RAS Paper IV: Language and Essay',
              'paper4_language_essay.json',
              16,
              assetFolder: 'rassetu_supplementary'),
          _catalogBook(
              'rassetu',
              'general_science',
              9,
              'General Science for Competitive Exams',
              'general_science.json',
              49,
              assetFolder: 'rassetu_supplementary'),
          _catalogBook('rassetu', 'book52', 10, 'Rajasthan Flagship Schemes',
              'book52.json', 4,
              assetFolder: 'rassetu_supplementary'),
          _catalogBook('rassetu', 'book53', 11, 'Rajasthan Economy and Budget',
              'book53.json', 4,
              assetFolder: 'rassetu_supplementary'),
          _catalogBook('rassetu', 'book55', 12,
              'Administrative and General Hindi', 'book55.json', 4,
              assetFolder: 'rassetu_supplementary'),
        ],
      ),
      Subject(
        id: 'greatworks',
        name: '100 Great Works of All Time',
        hindiName: 'विश्व साहित्य की 100 महान कृतियाँ',
        tagline:
            'Novels, Plays, Poems, Short Stories, Essays & Literary Criticism',
        seedColor: const Color(0xFF6D28D9),
        icon: Icons.auto_stories_rounded,
        books: [
          _catalogBook('greatworks', 'novels', 1,
              '100 Great Novels of All Time', 'novels.json', 100),
          _catalogBook('greatworks', 'plays', 2, '100 Great Plays of All Time',
              'plays.json', 100),
          _catalogBook('greatworks', 'poems', 3, '100 Great Poems of All Time',
              'poems.json', 100),
          _catalogBook('greatworks', 'short_stories', 4,
              '100 Great Short Stories of All Time', 'short_stories.json', 100),
          _catalogBook('greatworks', 'essays', 5,
              '100 Great Essays of All Time', 'essays.json', 100),
          _catalogBook(
              'greatworks',
              'critical_works',
              6,
              '100 Great Critical Works of All Time',
              'critical_works.json',
              100),
        ],
      ),
      createMscPhysicsSubject(),
      Subject(
        id: 'ugcnet_english',
        name: 'UGC NET English',
        hindiName: 'यूजीसी नेट अंग्रेजी',
        tagline: 'Literature, language, criticism, theory and research methods',
        seedColor: const Color(0xFF1D4ED8),
        icon: Icons.library_books_rounded,
        books: [
          _catalogBook(
            'ugcnet_english',
            'master',
            1,
            'UGC NET English: Complete Master Compendium (Units I, II, III, IV, V & Beyond)',
            'ugcnet_english_master.json',
            60,
          ),
        ],
      ),
      Subject(
        id: 'ugcnet_political_science',
        name: 'UGC NET Political Science',
        hindiName: 'राजनीति विज्ञान सेतु',
        tagline:
            'राजनीतिक सिद्धांत, विचारक, तुलनात्मक राजनीति, IR एवं भारतीय राजव्यवस्था',
        seedColor: const Color(0xFF991B1B), // Deep Academic Crimson
        icon: Icons.account_balance_rounded,
        books: [
          _catalogBook(
            'ugcnet_political_science',
            'master',
            1,
            'राजनीति विज्ञान: संपूर्ण ग्रंथ (इकाई I से X)',
            'ugcnet_political_science_master.json',
            51,
          ),
        ],
      ),
      Subject(
        id: 'ugcnet_history',
        name: 'UGC NET History',
        hindiName: 'इतिहास सेतु',
        tagline:
            'प्राचीन, मध्यकालीन, आधुनिक भारत, राष्ट्रीय आंदोलन एवं ऐतिहासिक शोध पद्धति',
        seedColor:
            const Color(0xFFB45309), // Warm Academic Amber / Antique Bronze
        icon: Icons.history_edu_rounded,
        books: [
          _catalogBook(
            'ugcnet_history',
            'master',
            1,
            'इतिहास: संपूर्ण ग्रंथ (इकाई I से X)',
            'ugcnet_history_master.json',
            86,
          ),
        ],
      ),
      Subject(
        id: 'ugcnet_commerce',
        name: 'UGC NET Commerce',
        hindiName: 'वाणिज्य सेतु',
        tagline:
            'लेखांकन, व्यावसायिक वित्त, अर्थशास्त्र, सांख्यिकी, आयकर एवं कॉर्पोरेट विधि',
        seedColor: const Color(0xFF047857), // Deep Emerald / Mercantile Green
        icon: Icons.business_center_rounded,
        books: [
          _catalogBook(
            'ugcnet_commerce',
            'master',
            1,
            'वाणिज्य: संपूर्ण ग्रंथ (इकाई I से X)',
            'ugcnet_commerce_master.json',
            65,
          ),
        ],
      ),
      Subject(
        id: 'ugcnet_hindi',
        name: 'UGC NET Hindi',
        hindiName: 'हिन्दी सेतु',
        tagline:
            'भाषा, साहित्य का इतिहास, काव्यशास्त्र, वैचारिक पृष्ठभूमि, कविता, उपन्यास, नाटक एवं गद्य विधाएँ',
        seedColor: const Color(0xFFBE123C), // Crimson / Rich Rose Maroon
        icon: Icons.auto_stories_rounded,
        books: [
          _catalogBook(
            'ugcnet_hindi',
            'master',
            1,
            'हिन्दी: संपूर्ण ग्रंथ (इकाई I से X)',
            'ugcnet_hindi_master.json',
            58,
          ),
        ],
      ),
    ];
  }

  static List<Book> _generateBookList(
    String subjectId,
    String subjectName,
    List<String> bookTitles, {
    required List<int> chapterCounts,
  }) {
    return List.generate(bookTitles.length, (index) {
      final bookNum = index + 1;
      final rawTitle =
          index < bookTitles.length ? bookTitles[index] : 'Book $bookNum';
      final prefix =
          subjectId == 'englishsetu' ? 'Book $bookNum' : 'पुस्तक $bookNum';
      final formattedTitle =
          rawTitle.startsWith('Book ') || rawTitle.startsWith('पुस्तक ')
              ? rawTitle
              : '$prefix: $rawTitle';
      return Book(
        id: '${subjectId}_b$bookNum',
        subjectId: subjectId,
        bookNumber: bookNum,
        title: formattedTitle,
        description:
            'Topic-focused lessons, worked examples, and practice questions.',
        jsonAssetPath:
            'assets/content/$subjectId/${subjectId}_book$bookNum.json',
        expectedChapterCount: chapterCounts[index],
      );
    });
  }

  static Book _catalogBook(
    String subjectId,
    String idSuffix,
    int bookNumber,
    String title,
    String assetName,
    int chapterCount, {
    String? assetFolder,
  }) {
    return Book(
      id: '${subjectId}_$idSuffix',
      subjectId: subjectId,
      bookNumber: bookNumber,
      title: title,
      description: subjectId == 'greatworks'
          ? 'Critical readings of 100 landmark works, with literary analysis.'
          : 'Offline lessons and practice for this topic.',
      jsonAssetPath: 'assets/content/${assetFolder ?? subjectId}/$assetName',
      expectedChapterCount: chapterCount,
    );
  }

  int getTotalChaptersForSubject(String subjectId) {
    final subject = getSubjectById(subjectId);
    return subject?.books.fold<int>(
          0,
          (total, book) => total + book.chapterCount,
        ) ??
        0;
  }

  Subject? getSubjectById(String subjectId) {
    final list = getSubjects();
    try {
      return list.firstWhere((s) => s.id == subjectId);
    } catch (_) {
      return null;
    }
  }

  Future<Book> loadBookContent(Book book) async {
    final cacheKey = '${book.subjectId}_${book.id}';
    if (_bookCache.containsKey(cacheKey) &&
        _bookCache[cacheKey]!.chapters.isNotEmpty) {
      return _bookCache[cacheKey]!;
    }

    try {
      final jsonString = await rootBundle.loadString(book.jsonAssetPath);
      final decoded = await compute(_decodeJsonMap, jsonString);

      final loadedBook = Book.fromBookJson(
        decoded,
        id: book.id,
        subjectId: book.subjectId,
        bookNumber: book.bookNumber,
        description: book.description,
        jsonAssetPath: book.jsonAssetPath,
      );
      _bookCache[cacheKey] = loadedBook;
      return loadedBook;
    } catch (e) {
      debugPrint(
          'Could not load asset at ${book.jsonAssetPath}: $e. Using fallback chapters.');
    }

    // Fallback: Provide structured default chapters matching schema
    final fallbackChapters = _generateFallbackChapters(book);
    book.chapters = fallbackChapters;
    _bookCache[cacheKey] = book;
    return book;
  }

  List<Chapter> _generateFallbackChapters(Book book) {
    return List.generate(4, (i) {
      final chNum = i + 1;
      return Chapter(
        id: 'ch$chNum',
        title: 'अध्याय $chNum: ${book.title.split(': ').last} - भाग $chNum',
        subtitle:
            'मुख्य अवधारणाएँ एवं अनुप्रयोग (Core Concepts & Applications)',
        content: [
          ContentBlock(
            type: 'text',
            value:
                'यह अध्याय ${book.title} का मुख्य भाग है। इसमें मूलभूत संकल्पनाएँ, परीक्षा के दृष्टिकोण से उपयोगी उदाहरण और अभ्यास प्रश्न सम्मिलित हैं।',
          ),
          const ContentBlock(
            type: 'callout',
            value:
                'महत्वपूर्ण नियम: नियमित अभ्यास और सूत्रों की समझ से प्रश्नों को कम समय में हल किया जा सकता है।',
          ),
          const ContentBlock(
            type: 'text',
            value:
                'प्रत्येक खंड को ध्यान से पढ़ें और अंत में दिए गए बहुविकल्पीय प्रश्नों (MCQs) का अभ्यास करें।',
          ),
        ],
        mcqs: const [
          MCQ(
            question: 'इस अध्याय की मुख्य संकल्पना किस पर आधारित है?',
            options: [
              'केवल सैद्धांतिक रटन',
              'अवधारणात्मक स्पष्टता एवं अभ्यास',
              'बिना समझे याद करना',
              'उपरोक्त में से कोई नहीं'
            ],
            correctIndex: 1,
            explanation:
                'सेतु श्रृंखला का उद्देश्य अवधारणात्मक स्पष्टता और नियमित अभ्यास सुनिश्चित करना है।',
          ),
          MCQ(
            question: 'प्रतियोगी परीक्षा में सफलता के लिए क्या सबसे आवश्यक है?',
            options: [
              'केवल अंतिम दिन पढ़ना',
              'सतत अभ्यास एवं आत्म-मूल्यांकन',
              'अनुमान पर निर्भरता',
              'शॉर्टकट बिना आधार के'
            ],
            correctIndex: 1,
            explanation:
                'सतत अभ्यास और नियमित स्व-मूल्यांकन ही स्थायी परिणाम देते हैं।',
          ),
        ],
      );
    });
  }
}
