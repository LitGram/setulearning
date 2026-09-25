import 'package:flutter/material.dart';
import 'package:provider/provider.dart';
import '../models/book.dart';
import '../models/chapter.dart';
import '../models/subject.dart';
import '../providers/progress_provider.dart';
import '../services/content_service.dart';
import '../widgets/accessible_card.dart';
import '../widgets/status_badge.dart';
import 'chapter_screen.dart';

class BookScreen extends StatefulWidget {
  final Subject subject;
  final Book book;

  const BookScreen({
    super.key,
    required this.subject,
    required this.book,
  });

  @override
  State<BookScreen> createState() => _BookScreenState();
}

class _BookScreenState extends State<BookScreen> {
  late Future<Book> _loadBookFuture;

  @override
  void initState() {
    super.initState();
    _loadBookFuture = ContentService.instance.loadBookContent(widget.book);

    WidgetsBinding.instance.addPostFrameCallback((_) {
      Provider.of<ProgressProvider>(context, listen: false)
          .ensureBookLoaded(widget.subject.id, widget.book.id);
    });
  }

  @override
  Widget build(BuildContext context) {
    final theme = Theme.of(context);
    final colorScheme = theme.colorScheme;

    return Scaffold(
      appBar: AppBar(
        title: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            Text(
              widget.book.title,
              style: theme.textTheme.titleMedium?.copyWith(
                fontWeight: FontWeight.bold,
              ),
              maxLines: 1,
              overflow: TextOverflow.ellipsis,
            ),
            Text(
              '${widget.subject.name} • ${widget.book.level}',
              style: theme.textTheme.bodySmall?.copyWith(
                color: colorScheme.onSurfaceVariant,
              ),
            ),
          ],
        ),
      ),
      body: FutureBuilder<Book>(
        future: _loadBookFuture,
        builder: (context, snapshot) {
          if (snapshot.connectionState == ConnectionState.waiting) {
            return Center(
              child: Column(
                mainAxisAlignment: MainAxisAlignment.center,
                children: [
                  const CircularProgressIndicator(),
                  const SizedBox(height: 16),
                  Text(
                    'विषय सूची लोड हो रही है...',
                    style: theme.textTheme.bodyMedium?.copyWith(
                      color: colorScheme.onSurfaceVariant,
                    ),
                  ),
                ],
              ),
            );
          }

          if (snapshot.hasError) {
            return Center(
              child: Padding(
                padding: const EdgeInsets.all(24.0),
                child: Column(
                  mainAxisAlignment: MainAxisAlignment.center,
                  children: [
                    Icon(Icons.error_outline_rounded, size: 48, color: colorScheme.error),
                    const SizedBox(height: 12),
                    Text(
                      'पुस्तक लोड करने में समस्या आई',
                      style: theme.textTheme.titleMedium?.copyWith(
                        color: colorScheme.error,
                      ),
                    ),
                    const SizedBox(height: 8),
                    FilledButton(
                      onPressed: () {
                        setState(() {
                          _loadBookFuture =
                              ContentService.instance.loadBookContent(widget.book);
                        });
                      },
                      child: const Text('पुनः प्रयास करें'),
                    ),
                  ],
                ),
              ),
            );
          }

          final book = snapshot.data ?? widget.book;
          final chapters = book.chapters;

          return Consumer<ProgressProvider>(
            builder: (context, progressProvider, child) {
              return ListView(
                padding: const EdgeInsets.symmetric(horizontal: 16.0, vertical: 12.0),
                children: [
                  // Book Overview Header
                  Container(
                    padding: const EdgeInsets.all(16.0),
                    decoration: BoxDecoration(
                      color: colorScheme.surfaceVariant.withOpacity(0.5),
                      borderRadius: BorderRadius.circular(16),
                      border: Border.all(
                        color: colorScheme.outlineVariant,
                      ),
                    ),
                    child: Column(
                      crossAxisAlignment: CrossAxisAlignment.start,
                      children: [
                        Row(
                          children: [
                            Container(
                              padding: const EdgeInsets.symmetric(horizontal: 10, vertical: 4),
                              decoration: BoxDecoration(
                                color: colorScheme.primary,
                                borderRadius: BorderRadius.circular(8),
                              ),
                              child: Text(
                                widget.book.level,
                                style: theme.textTheme.labelSmall?.copyWith(
                                  color: colorScheme.onPrimary,
                                  fontWeight: FontWeight.bold,
                                ),
                              ),
                            ),
                            const Spacer(),
                            Text(
                              'कुल अध्याय: ${chapters.length}',
                              style: theme.textTheme.labelMedium?.copyWith(
                                color: colorScheme.primary,
                                fontWeight: FontWeight.bold,
                              ),
                            ),
                          ],
                        ),
                        const SizedBox(height: 10),
                        Text(
                          widget.book.title,
                          style: theme.textTheme.titleMedium?.copyWith(
                            fontWeight: FontWeight.bold,
                          ),
                        ),
                        const SizedBox(height: 4),
                        Text(
                          widget.book.description,
                          style: theme.textTheme.bodySmall?.copyWith(
                            color: colorScheme.onSurfaceVariant,
                          ),
                        ),
                      ],
                    ),
                  ),
                  const SizedBox(height: 18),

                  Padding(
                    padding: const EdgeInsets.symmetric(horizontal: 4.0, vertical: 4.0),
                    child: Text(
                      'अध्याय सूची (Table of Contents)',
                      style: theme.textTheme.titleMedium?.copyWith(
                        fontWeight: FontWeight.bold,
                      ),
                    ),
                  ),
                  const SizedBox(height: 8),

                  // Chapters List
                  ...chapters.asMap().entries.map((entry) {
                    final index = entry.key;
                    final chapter = entry.value;
                    return Padding(
                      padding: const EdgeInsets.only(bottom: 12.0),
                      child: _buildChapterTile(
                        context,
                        index + 1,
                        chapter,
                        book,
                        progressProvider,
                      ),
                    );
                  }),

                  const SizedBox(height: 24),
                ],
              );
            },
          );
        },
      ),
    );
  }

  Widget _buildChapterTile(
    BuildContext context,
    int index,
    Chapter chapter,
    Book book,
    ProgressProvider progressProvider,
  ) {
    final theme = Theme.of(context);
    final colorScheme = theme.colorScheme;
    final isRead = progressProvider.isChapterRead(widget.subject.id, book.id, chapter.id);
    final quizRecord = progressProvider.getBestQuizScore(widget.subject.id, book.id, chapter.id);

    return AccessibleCard(
      semanticLabel: 'अध्याय $index: ${chapter.title}, ${isRead ? "पठित" : "अपठित"}',
      onTap: () {
        Navigator.push(
          context,
          MaterialPageRoute(
            builder: (_) => ChapterScreen(
              subject: widget.subject,
              book: book,
              chapter: chapter,
            ),
          ),
        );
      },
      child: Row(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          // Chapter Number Badge
          Container(
            width: 40,
            height: 40,
            decoration: BoxDecoration(
              color: isRead
                  ? colorScheme.primaryContainer
                  : colorScheme.surfaceVariant,
              borderRadius: BorderRadius.circular(10),
              border: Border.all(
                color: isRead ? colorScheme.primary : colorScheme.outlineVariant,
              ),
            ),
            child: Center(
              child: isRead
                  ? Icon(Icons.check_rounded, color: colorScheme.primary, size: 22)
                  : Text(
                      '$index',
                      style: theme.textTheme.titleSmall?.copyWith(
                        fontWeight: FontWeight.bold,
                        color: colorScheme.onSurfaceVariant,
                      ),
                    ),
            ),
          ),
          const SizedBox(width: 14),
          Expanded(
            child: Column(
              crossAxisAlignment: CrossAxisAlignment.start,
              children: [
                Text(
                  chapter.title,
                  style: theme.textTheme.titleSmall?.copyWith(
                    fontWeight: FontWeight.bold,
                  ),
                ),
                if (chapter.subtitle != null) ...[
                  const SizedBox(height: 2),
                  Text(
                    chapter.subtitle!,
                    style: theme.textTheme.bodySmall?.copyWith(
                      color: colorScheme.onSurfaceVariant,
                    ),
                  ),
                ],
                const SizedBox(height: 8),
                Wrap(
                  spacing: 8,
                  runSpacing: 4,
                  children: [
                    if (isRead)
                      const StatusBadge(type: BadgeType.completed, customLabel: 'पठित')
                    else
                      const StatusBadge(type: BadgeType.notStarted, customLabel: 'अपठित'),
                    if (quizRecord != null)
                      StatusBadge(
                        type: quizRecord.percentage >= 60
                            ? BadgeType.quizPassed
                            : BadgeType.quizNeedsReview,
                        customLabel:
                            'स्कोर: ${quizRecord.score}/${quizRecord.total} (${quizRecord.percentage.toStringAsFixed(0)}%)',
                      )
                    else if (chapter.mcqs.isNotEmpty)
                      StatusBadge(
                        type: BadgeType.inProgress,
                        customLabel: '${chapter.mcqs.length} अभ्यास प्रश्न',
                      ),
                  ],
                ),
              ],
            ),
          ),
          const SizedBox(width: 8),
          const Icon(Icons.chevron_right_rounded),
        ],
      ),
    );
  }
}
