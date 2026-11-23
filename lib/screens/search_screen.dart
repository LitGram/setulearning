import 'package:flutter/material.dart';
import '../l10n/app_strings.dart';
import '../models/book.dart';
import '../models/chapter.dart';
import '../models/subject.dart';
import '../services/content_service.dart';
import '../services/study_session_store.dart';
import 'book_screen.dart';
import 'chapter_screen.dart';

class SearchScreen extends StatefulWidget {
  const SearchScreen({super.key});
  @override
  State<SearchScreen> createState() => _SearchScreenState();
}

class _SearchScreenState extends State<SearchScreen> {
  final _controller = TextEditingController();
  final _entries = <({Subject subject, Book book, Chapter? chapter})>[];
  bool _loading = true;
  bool _failed = false;
  List<String> _recent = [];

  @override
  void initState() {
    super.initState();
    _index();
  }

  Future<void> _index() async {
    setState(() {
      _loading = true;
      _failed = false;
    });
    _entries.clear();
    for (final subject in ContentService.instance.getSubjects()) {
      for (final book in subject.books) {
        _entries.add((subject: subject, book: book, chapter: null));
      }
    }
    try {
      final recent = await StudySessionStore.read('study_search_recent');
      _recent = (recent?['queries'] as List?)?.cast<String>() ?? [];
      // Load each asset once, outside the keystroke/filter path.
      for (final entry in List.of(_entries)) {
        try {
          final book =
              await ContentService.instance.loadBookContent(entry.book);
          if (!mounted) return;
          for (final chapter in book.chapters) {
            _entries
                .add((subject: entry.subject, book: book, chapter: chapter));
          }
        } catch (_) {
          _failed = true;
        }
      }
    } catch (_) {
      _failed = true;
    }
    if (mounted) setState(() => _loading = false);
  }

  @override
  void dispose() {
    _controller.dispose();
    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    final query = _controller.text.trim().toLowerCase();
    final results = _entries
        .where((entry) =>
            '${entry.book.title} ${entry.chapter?.title ?? ''} ${entry.chapter?.subtitle ?? ''} ${entry.subject.hindiName}'
                .toLowerCase()
                .contains(query))
        .toList();
    return Scaffold(
      appBar: AppBar(title: Text(context.strings.searchBooksAndChapters)),
      body: Column(children: [
        Padding(
            padding: const EdgeInsets.all(16),
            child: TextField(
              controller: _controller,
              onChanged: (_) => setState(() {}),
              decoration: InputDecoration(
                labelText: context.strings.searchFieldLabel,
                prefixIcon: const Icon(Icons.search),
                suffixIcon: IconButton(
                    tooltip: context.strings.clearSearch,
                    icon: const Icon(Icons.clear),
                    onPressed: () => setState(_controller.clear)),
                border: const OutlineInputBorder(),
              ),
            )),
        if (_loading)
          LinearProgressIndicator(
              semanticsLabel: context.strings.preparingSearch),
        if (_failed)
          Padding(
              padding: const EdgeInsets.symmetric(horizontal: 16),
              child: Wrap(
                  crossAxisAlignment: WrapCrossAlignment.center,
                  children: [
                    Text(
                        context.strings.someChaptersNotLoaded),
                    TextButton(
                        onPressed: _loading ? null : _index,
                        child: Text(context.strings.retry)),
                  ])),
        Expanded(
            child: query.isEmpty
                ? ListView(padding: const EdgeInsets.all(16), children: [
                    Text(
                        context.strings.searchHint),
                    const SizedBox(height: 16),
                    if (_recent.isNotEmpty) Text(context.strings.recentSearches),
                    ..._recent.map((value) => ListTile(
                        leading: const Icon(Icons.history),
                        title: Text(value),
                        onTap: () => setState(() => _controller.text = value))),
                  ])
                : results.isEmpty
                    ? Center(
                        child: Padding(
                            padding: const EdgeInsets.all(24),
                            child: Text(
                                context.strings.noResults)))
                    : ListView.builder(
                        itemCount: results.length,
                        itemBuilder: (context, index) {
                          final entry = results[index];
                          return ListTile(
                            leading: Icon(entry.chapter == null
                                ? Icons.menu_book
                                : Icons.article_outlined),
                            title:
                                Text(entry.chapter?.title ?? entry.book.title),
                            subtitle: Text(
                                '${entry.subject.name} • ${entry.chapter == null ? context.strings.book : entry.book.title}'),
                            trailing: const Icon(Icons.chevron_right),
                            onTap: () async {
                              _recent = [
                                query,
                                ..._recent.where((value) => value != query)
                              ].take(5).toList();
                              try {
                                await StudySessionStore.write(
                                    'study_search_recent',
                                    {'queries': _recent});
                              } catch (_) {/* Search remains usable. */}
                              if (!context.mounted) return;
                              Navigator.push(
                                  context,
                                  MaterialPageRoute(
                                      builder: (_) => entry.chapter == null
                                          ? BookScreen(
                                              subject: entry.subject,
                                              book: entry.book)
                                          : ChapterScreen(
                                              subject: entry.subject,
                                              book: entry.book,
                                              chapter: entry.chapter!)));
                            },
                          );
                        })),
      ]),
    );
  }
}
