import 'dart:convert';
import 'package:flutter/material.dart';
import 'package:flutter/services.dart';
import '../models/book.dart';
import '../models/chapter.dart';
import '../models/mcq.dart';
import '../models/subject.dart';

class ContentService {
  static final ContentService instance = ContentService._init();
  final Map<String, Book> _bookCache = {};

  ContentService._init();

  List<Subject> getSubjects() {
    return [
      Subject(
        id: 'mathsetu',
        name: 'MathSetu',
        hindiName: 'गणित सेतु',
        tagline: 'गणना कौशल, अंकगणित से उन्नत गणित तक',
        seedColor: const Color(0xFF1E40AF), // Deep Royal Blue
        icon: Icons.calculate_rounded,
        books: _generateBookList('mathsetu', 'MathSetu', [
          'गणना कौशल, संख्या पद्धति एवं सरलीकरण',
          'प्रतिशतता, लाभ-हानि एवं बट्टा',
          'साधारण एवं चक्रवृद्धि ब्याज',
          'अनुपात, समानुपात एवं साझेदारी',
          'समय, कार्य, नल एवं हौज',
          'चाल, समय एवं दूरी',
          'बीजगणित एवं त्रिकोणमिति',
          'क्षेत्रमिति एवं ज्यामिति',
        ]),
      ),
      Subject(
        id: 'englishsetu',
        name: 'EnglishSetu',
        hindiName: 'अंग्रेजी सेतु',
        tagline: 'English Grammar, Vocabulary & Comprehension',
        seedColor: const Color(0xFF0F766E), // Emerald Teal
        icon: Icons.menu_book_rounded,
        books: _generateBookList('englishsetu', 'EnglishSetu', [
          'Foundations of Grammar & Parts of Speech',
          'Tenses, Voice & Narration Masterclass',
          'Sentence Structure, Clauses & Conditionals',
          'Vocabulary Builder: Roots, Synonyms & Antonyms',
          'Idioms, Phrasal Verbs & One-Word Substitutions',
          'Common Errors & Spotting the Errors Drill',
          'Reading Comprehension & Para Jumbles',
          'Cloze Test, Fillers & Advanced Writing Skills',
        ]),
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
        ]),
      ),
    ];
  }

  static List<Book> _generateBookList(
    String subjectId,
    String subjectName,
    List<String> bookTitles,
  ) {
    return List.generate(8, (index) {
      final bookNum = index + 1;
      final title = index < bookTitles.length ? bookTitles[index] : 'Book $bookNum';
      return Book(
        id: '${subjectId}_b$bookNum',
        subjectId: subjectId,
        bookNumber: bookNum,
        title: 'पुस्तक $bookNum: $title',
        level: 'Class / Level $bookNum',
        description: 'Setu Series Level $bookNum comprehensive study guide & practice questions.',
        jsonAssetPath: 'assets/content/$subjectId/${subjectId}_book$bookNum.json',
      );
    });
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
    if (_bookCache.containsKey(cacheKey) && _bookCache[cacheKey]!.chapters.isNotEmpty) {
      return _bookCache[cacheKey]!;
    }

    try {
      final jsonString = await rootBundle.loadString(book.jsonAssetPath);
      final dynamic decoded = jsonDecode(jsonString);

      if (decoded is Map<String, dynamic>) {
        final loadedBook = Book.fromBookJson(
          decoded,
          id: book.id,
          subjectId: book.subjectId,
          bookNumber: book.bookNumber,
          level: book.level,
          description: book.description,
          jsonAssetPath: book.jsonAssetPath,
        );
        _bookCache[cacheKey] = loadedBook;
        return loadedBook;
      }
    } catch (e) {
      debugPrint('Could not load asset at ${book.jsonAssetPath}: $e. Using fallback chapters.');
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
        subtitle: 'Level ${book.bookNumber} Core Concepts',
        content: [
          ContentBlock(
            type: 'text',
            value:
                'यह अध्याय ${book.title} का मुख्य भाग है। इसमें मूलभूत संकल्पनाएँ, परीक्षा के दृष्टिकोण से उपयोगी उदाहरण और अभ्यास प्रश्न सम्मिलित हैं।',
          ),
          const ContentBlock(
            type: 'callout',
            value: 'महत्वपूर्ण नियम: नियमित अभ्यास और सूत्रों की समझ से प्रश्नों को कम समय में हल किया जा सकता है।',
          ),
          const ContentBlock(
            type: 'text',
            value: 'प्रत्येक खंड को ध्यान से पढ़ें और अंत में दिए गए बहुविकल्पीय प्रश्नों (MCQs) का अभ्यास करें।',
          ),
        ],
        mcqs: [
          MCQ(
            question: 'इस अध्याय की मुख्य संकल्पना किस पर आधारित है?',
            options: [
              'केवल सैद्धांतिक रटन',
              'अवधारणात्मक स्पष्टता एवं अभ्यास',
              'बिना समझे याद करना',
              'उपरोक्त में से कोई नहीं'
            ],
            correctIndex: 1,
            explanation: 'सेतु श्रृंखला का उद्देश्य अवधारणात्मक स्पष्टता और नियमित अभ्यास सुनिश्चित करना है।',
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
            explanation: 'सतत अभ्यास और नियमित स्व-मूल्यांकन ही स्थायी परिणाम देते हैं।',
          ),
        ],
      );
    });
  }
}
