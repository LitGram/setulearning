import 'package:flutter/material.dart';
import 'package:provider/provider.dart';
import '../models/book.dart';
import '../models/chapter.dart';
import '../models/subject.dart';
import '../providers/progress_provider.dart';
import '../providers/theme_provider.dart';
import '../widgets/content_block_widget.dart';
import 'quiz_screen.dart';

class ChapterScreen extends StatefulWidget {
  final Subject subject;
  final Book book;
  final Chapter chapter;

  const ChapterScreen({
    super.key,
    required this.subject,
    required this.book,
    required this.chapter,
  });

  @override
  State<ChapterScreen> createState() => _ChapterScreenState();
}

class _ChapterScreenState extends State<ChapterScreen> {
  late Chapter _currentChapter;
  final ScrollController _scrollController = ScrollController();

  @override
  void initState() {
    super.initState();
    _currentChapter = widget.chapter;
    _onChapterOpened();
  }

  void _onChapterOpened() {
    WidgetsBinding.instance.addPostFrameCallback((_) {
      final progress = Provider.of<ProgressProvider>(context, listen: false);
      // Mark as read
      progress.markChapterRead(
        subjectId: widget.subject.id,
        bookId: widget.book.id,
        chapterId: _currentChapter.id,
      );
      // Save last position
      progress.updateLastPosition(
        subjectId: widget.subject.id,
        bookId: widget.book.id,
        chapterId: _currentChapter.id,
        subjectName: widget.subject.name,
        bookTitle: widget.book.title,
        chapterTitle: _currentChapter.title,
      );
    });
  }

  int get _currentIndex =>
      widget.book.chapters.indexWhere((c) => c.id == _currentChapter.id);

  bool get _hasPrevious => _currentIndex > 0;
  bool get _hasNext =>
      _currentIndex >= 0 && _currentIndex < widget.book.chapters.length - 1;

  void _goToChapter(int newIndex) {
    if (newIndex >= 0 && newIndex < widget.book.chapters.length) {
      setState(() {
        _currentChapter = widget.book.chapters[newIndex];
      });
      _onChapterOpened();
      _scrollController.animateTo(
        0,
        duration: const Duration(milliseconds: 300),
        curve: Curves.easeInOut,
      );
    }
  }

  @override
  void dispose() {
    _scrollController.dispose();
    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    final theme = Theme.of(context);
    final colorScheme = theme.colorScheme;
    final themeProvider = Provider.of<ThemeProvider>(context);

    return Scaffold(
      appBar: AppBar(
        title: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            Text(
              _currentChapter.title,
              style: theme.textTheme.titleMedium?.copyWith(
                fontWeight: FontWeight.bold,
              ),
              maxLines: 1,
              overflow: TextOverflow.ellipsis,
            ),
            Text(
              '${widget.subject.name} • ${widget.book.title}',
              style: theme.textTheme.bodySmall?.copyWith(
                color: colorScheme.onSurfaceVariant,
              ),
              maxLines: 1,
              overflow: TextOverflow.ellipsis,
            ),
          ],
        ),
        actions: [
          // Text size adjustment controls for accessibility
          IconButton(
            tooltip: 'अक्षर छोटा करें (Decrease Font)',
            icon: const Icon(Icons.text_decrease_rounded),
            onPressed: () {
              themeProvider.setFontScale(themeProvider.fontScale - 0.1);
            },
          ),
          IconButton(
            tooltip: 'अक्षर बड़ा करें (Increase Font)',
            icon: const Icon(Icons.text_increase_rounded),
            onPressed: () {
              themeProvider.setFontScale(themeProvider.fontScale + 0.1);
            },
          ),
          const SizedBox(width: 8),
        ],
      ),
      body: Column(
        children: [
          // Reading Content
          Expanded(
            child: ListView(
              controller: _scrollController,
              padding: const EdgeInsets.symmetric(horizontal: 20.0, vertical: 16.0),
              children: [
                // Chapter Header Card
                Container(
                  padding: const EdgeInsets.all(16),
                  decoration: BoxDecoration(
                    color: colorScheme.primaryContainer.withOpacity(0.3),
                    borderRadius: BorderRadius.circular(16),
                    border: Border.all(
                      color: colorScheme.primary.withOpacity(0.2),
                    ),
                  ),
                  child: Column(
                    crossAxisAlignment: CrossAxisAlignment.start,
                    children: [
                      Text(
                        _currentChapter.title,
                        style: theme.textTheme.titleLarge?.copyWith(
                          fontWeight: FontWeight.bold,
                          color: colorScheme.primary,
                        ),
                      ),
                      if (_currentChapter.subtitle != null) ...[
                        const SizedBox(height: 4),
                        Text(
                          _currentChapter.subtitle!,
                          style: theme.textTheme.bodyMedium?.copyWith(
                            color: colorScheme.onSurfaceVariant,
                            fontStyle: FontStyle.italic,
                          ),
                        ),
                      ],
                    ],
                  ),
                ),
                const SizedBox(height: 16),

                // Content Blocks
                ..._currentChapter.content.map((block) {
                  return ContentBlockWidget(block: block);
                }),

                const SizedBox(height: 24),

                // Practice Quiz Launch Section
                if (_currentChapter.mcqs.isNotEmpty) ...[
                  Container(
                    padding: const EdgeInsets.all(18),
                    decoration: BoxDecoration(
                      color: colorScheme.secondaryContainer.withOpacity(0.6),
                      borderRadius: BorderRadius.circular(16),
                      border: Border.all(
                        color: colorScheme.secondary.withOpacity(0.3),
                      ),
                    ),
                    child: Column(
                      children: [
                        Row(
                          children: [
                            Icon(
                              Icons.quiz_rounded,
                              size: 32,
                              color: colorScheme.secondary,
                            ),
                            const SizedBox(width: 12),
                            Expanded(
                              child: Column(
                                crossAxisAlignment: CrossAxisAlignment.start,
                                children: [
                                  Text(
                                    'अभ्यास प्रश्न (Self Check Quiz)',
                                    style: theme.textTheme.titleMedium?.copyWith(
                                      fontWeight: FontWeight.bold,
                                      color: colorScheme.onSecondaryContainer,
                                    ),
                                  ),
                                  Text(
                                    'कुल प्रश्न: ${_currentChapter.mcqs.length}',
                                    style: theme.textTheme.bodySmall?.copyWith(
                                      color: colorScheme.onSecondaryContainer
                                          .withOpacity(0.8),
                                    ),
                                  ),
                                ],
                              ),
                            ),
                          ],
                        ),
                        const SizedBox(height: 16),
                        SizedBox(
                          width: double.infinity,
                          child: FilledButton.icon(
                            icon: const Icon(Icons.play_circle_fill_rounded),
                            label: const Text('प्रश्नोत्तरी प्रारंभ करें (Start Quiz)'),
                            style: FilledButton.styleFrom(
                              backgroundColor: colorScheme.secondary,
                              foregroundColor: colorScheme.onSecondary,
                            ),
                            onPressed: () {
                              Navigator.push(
                                context,
                                MaterialPageRoute(
                                  builder: (_) => QuizScreen(
                                    subject: widget.subject,
                                    book: widget.book,
                                    chapter: _currentChapter,
                                  ),
                                ),
                              );
                            },
                          ),
                        ),
                      ],
                    ),
                  ),
                  const SizedBox(height: 24),
                ],
              ],
            ),
          ),

          // Bottom Chapter Stepper Bar (Explicit buttons, no gesture-only navigation)
          Container(
            padding: const EdgeInsets.symmetric(horizontal: 16, vertical: 10),
            decoration: BoxDecoration(
              color: colorScheme.surface,
              border: Border(
                top: BorderSide(
                  color: colorScheme.outlineVariant.withOpacity(0.5),
                ),
              ),
            ),
            child: SafeArea(
              child: Row(
                children: [
                  // Previous Button
                  Expanded(
                    child: OutlinedButton.icon(
                      icon: const Icon(Icons.arrow_back_rounded, size: 18),
                      label: const Text('पिछला'),
                      onPressed: _hasPrevious
                          ? () => _goToChapter(_currentIndex - 1)
                          : null,
                    ),
                  ),
                  const SizedBox(width: 12),
                  // Chapter indicator
                  Text(
                    '${_currentIndex + 1} / ${widget.book.chapters.length}',
                    style: theme.textTheme.labelMedium?.copyWith(
                      fontWeight: FontWeight.bold,
                      color: colorScheme.onSurfaceVariant,
                    ),
                  ),
                  const SizedBox(width: 12),
                  // Next Button
                  Expanded(
                    child: FilledButton.icon(
                      icon: const Icon(Icons.arrow_forward_rounded, size: 18),
                      label: const Text('अगला'),
                      onPressed:
                          _hasNext ? () => _goToChapter(_currentIndex + 1) : null,
                    ),
                  ),
                ],
              ),
            ),
          ),
        ],
      ),
    );
  }
}
