import 'package:flutter/material.dart';
import '../l10n/app_strings.dart';
import 'package:provider/provider.dart';
import '../models/book.dart';
import '../models/subject.dart';
import '../providers/progress_provider.dart';
import '../widgets/accessible_card.dart';
import '../widgets/status_badge.dart';
import 'book_screen.dart';

class SubjectScreen extends StatelessWidget {
  final Subject subject;

  const SubjectScreen({
    super.key,
    required this.subject,
  });

  @override
  Widget build(BuildContext context) {
    final theme = Theme.of(context);
    final colorScheme = theme.colorScheme;

    return Scaffold(
      appBar: AppBar(
        toolbarHeight: (MediaQuery.textScalerOf(context).scale(
                    Theme.of(context).textTheme.titleMedium?.fontSize ?? 18) *
                2.8)
            .clamp(56.0, 160.0),
        title: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            Text(
              subject.name,
              maxLines: 2,
              overflow: TextOverflow.ellipsis,
              style: theme.textTheme.titleMedium?.copyWith(
                fontWeight: FontWeight.bold,
              ),
            ),
            Text(
              subject.hindiName,
              maxLines: 1,
              overflow: TextOverflow.ellipsis,
              style: theme.textTheme.bodySmall?.copyWith(
                color: colorScheme.onSurfaceVariant,
              ),
            ),
          ],
        ),
      ),
      body: Consumer<ProgressProvider>(
        builder: (context, progressProvider, child) {
          return ListView(
            padding:
                const EdgeInsets.symmetric(horizontal: 16.0, vertical: 12.0),
            children: [
              // Subject Header Card
              Container(
                padding: const EdgeInsets.all(16.0),
                decoration: BoxDecoration(
                  color: colorScheme.primaryContainer.withOpacity(0.4),
                  borderRadius: BorderRadius.circular(16),
                  border: Border.all(
                    color: colorScheme.primary.withOpacity(0.2),
                  ),
                ),
                child: Row(
                  children: [
                    Icon(
                      subject.icon,
                      size: 36,
                      color: colorScheme.primary,
                    ),
                    const SizedBox(width: 14),
                    Expanded(
                      child: Column(
                        crossAxisAlignment: CrossAxisAlignment.start,
                        children: [
                          Text(
                            context.strings.booksAvailable(subject.books.length),
                            style: theme.textTheme.titleSmall?.copyWith(
                              fontWeight: FontWeight.bold,
                              color: colorScheme.primary,
                            ),
                          ),
                          const SizedBox(height: 2),
                          Text(
                            subject.tagline,
                            style: theme.textTheme.bodySmall?.copyWith(
                              color: colorScheme.onSurfaceVariant,
                            ),
                          ),
                          const SizedBox(height: 4),
                          Text(
                            context.strings.subjectBlurb,
                            style: theme.textTheme.bodySmall?.copyWith(
                              color: colorScheme.onSurfaceVariant,
                            ),
                          ),
                        ],
                      ),
                    ),
                  ],
                ),
              ),
              const SizedBox(height: 16),

              Padding(
                padding:
                    const EdgeInsets.symmetric(horizontal: 4.0, vertical: 4.0),
                child: Text(
                  context.strings.chooseBook,
                  style: theme.textTheme.titleMedium?.copyWith(
                    fontWeight: FontWeight.bold,
                  ),
                ),
              ),
              const SizedBox(height: 8),

              // List every book registered for this subject.
              ...subject.books.map((book) {
                return Padding(
                  padding: const EdgeInsets.only(bottom: 12.0),
                  child: _buildBookCard(context, book, progressProvider),
                );
              }),

              const SizedBox(height: 20),
            ],
          );
        },
      ),
    );
  }

  Widget _buildBookCard(
    BuildContext context,
    Book book,
    ProgressProvider progressProvider,
  ) {
    final theme = Theme.of(context);
    final colorScheme = theme.colorScheme;
    final readCount = progressProvider.getReadCountForBook(subject.id, book.id);

    return AccessibleCard(
      semanticLabel: context.strings.bookSemantics(book.title),
      onTap: () {
        Navigator.push(
          context,
          MaterialPageRoute(
            builder: (_) => BookScreen(
              subject: subject,
              book: book,
            ),
          ),
        );
      },
      child: Row(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          // Book Number Avatar
          Container(
            width: 48,
            height: 48,
            decoration: BoxDecoration(
              color: colorScheme.primary,
              borderRadius: BorderRadius.circular(12),
            ),
            child: Center(
              child: Text(
                'B${book.bookNumber}',
                style: theme.textTheme.titleMedium?.copyWith(
                  color: colorScheme.onPrimary,
                  fontWeight: FontWeight.bold,
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
                  book.title,
                  maxLines: 2,
                  overflow: TextOverflow.ellipsis,
                  style: theme.textTheme.titleMedium?.copyWith(
                    fontWeight: FontWeight.bold,
                  ),
                ),
                const SizedBox(height: 4),
                Text(
                  book.description,
                  style: theme.textTheme.bodySmall?.copyWith(
                    color: colorScheme.onSurfaceVariant,
                  ),
                  maxLines: 2,
                  overflow: TextOverflow.ellipsis,
                ),
                if (readCount > 0) ...[
                  const SizedBox(height: 8),
                  StatusBadge(
                    type: BadgeType.inProgress,
                    customLabel: context.strings.chaptersRead(readCount),
                  ),
                ],
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
