import 'package:flutter/material.dart';
import 'package:provider/provider.dart';
import '../models/subject.dart';
import '../providers/progress_provider.dart';
import '../providers/theme_provider.dart';
import '../services/content_service.dart';
import '../widgets/accessible_card.dart';
import 'chapter_screen.dart';
import 'progress_screen.dart';
import 'settings_screen.dart';
import 'subject_screen.dart';

class HomeScreen extends StatelessWidget {
  const HomeScreen({super.key});

  @override
  Widget build(BuildContext context) {
    final theme = Theme.of(context);
    final colorScheme = theme.colorScheme;
    final subjects = ContentService.instance.getSubjects();

    return Scaffold(
      appBar: AppBar(
        title: Row(
          children: [
            Container(
              padding: const EdgeInsets.all(8),
              decoration: BoxDecoration(
                color: colorScheme.primaryContainer,
                borderRadius: BorderRadius.circular(10),
              ),
              child: Icon(
                Icons.school_rounded,
                color: colorScheme.primary,
                size: 24,
              ),
            ),
            const SizedBox(width: 12),
            Column(
              crossAxisAlignment: CrossAxisAlignment.start,
              children: [
                Text(
                  'Setu Learning',
                  style: theme.textTheme.titleMedium?.copyWith(
                    fontWeight: FontWeight.bold,
                  ),
                ),
                Text(
                  'सेतु शिक्षण श्रृंखला',
                  style: theme.textTheme.bodySmall?.copyWith(
                    color: colorScheme.onSurfaceVariant,
                  ),
                ),
              ],
            ),
          ],
        ),
        actions: [
          IconButton(
            tooltip: 'प्रगति (Learning Progress)',
            icon: const Icon(Icons.insights_rounded),
            onPressed: () {
              Navigator.push(
                context,
                MaterialPageRoute(builder: (_) => const ProgressScreen()),
              );
            },
          ),
          IconButton(
            tooltip: 'सेटिंग्स (Settings & About)',
            icon: const Icon(Icons.settings_rounded),
            onPressed: () {
              Navigator.push(
                context,
                MaterialPageRoute(builder: (_) => const SettingsScreen()),
              );
            },
          ),
          const SizedBox(width: 8),
        ],
      ),
      body: Consumer<ProgressProvider>(
        builder: (context, progressProvider, child) {
          final lastPos = progressProvider.lastPosition;

          return ListView(
            padding: const EdgeInsets.symmetric(horizontal: 16.0, vertical: 12.0),
            children: [
              // Resume Banner (if student previously read a chapter)
              if (lastPos != null) ...[
                _buildResumeBanner(context, lastPos),
                const SizedBox(height: 16),
              ],

              // Section Header
              Padding(
                padding: const EdgeInsets.symmetric(vertical: 8.0, horizontal: 4.0),
                child: Text(
                  'विषय चुनें (Select Subject)',
                  style: theme.textTheme.titleLarge?.copyWith(
                    fontWeight: FontWeight.bold,
                  ),
                ),
              ),
              Text(
                'प्रत्येक विषय में 8 पुस्तकें (Book 1 से Book 8) उपलब्ध हैं।',
                style: theme.textTheme.bodyMedium?.copyWith(
                  color: colorScheme.onSurfaceVariant,
                ),
              ),
              const SizedBox(height: 16),

              // Subject Cards
              ...subjects.map((subject) {
                return Padding(
                  padding: const EdgeInsets.only(bottom: 14.0),
                  child: _buildSubjectCard(context, subject, progressProvider),
                );
              }),

              const SizedBox(height: 16),

              // Quick Offline Info Card
              AccessibleCard(
                color: colorScheme.surfaceVariant.withOpacity(0.4),
                child: Row(
                  children: [
                    Icon(
                      Icons.offline_pin_rounded,
                      color: colorScheme.primary,
                      size: 28,
                    ),
                    const SizedBox(width: 14),
                    Expanded(
                      child: Column(
                        crossAxisAlignment: CrossAxisAlignment.start,
                        children: [
                          Text(
                            'पूर्णतः ऑफलाइन अध्ययन',
                            style: theme.textTheme.labelLarge?.copyWith(
                              fontWeight: FontWeight.bold,
                            ),
                          ),
                          const SizedBox(height: 2),
                          Text(
                            'सभी पुस्तकें एवं अभ्यास प्रश्न बिना इंटरनेट के उपलब्ध हैं।',
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
              const SizedBox(height: 24),
            ],
          );
        },
      ),
    );
  }

  Widget _buildResumeBanner(BuildContext context, dynamic lastPos) {
    final theme = Theme.of(context);
    final colorScheme = theme.colorScheme;

    return AccessibleCard(
      color: colorScheme.primaryContainer.withOpacity(0.7),
      semanticLabel: 'अंतिम पठित अध्याय जारी रखें: ${lastPos.chapterTitle}',
      onTap: () async {
        final subject = ContentService.instance.getSubjectById(lastPos.subjectId);
        if (subject != null) {
          final book = subject.books.firstWhere(
            (b) => b.id == lastPos.bookId,
            orElse: () => subject.books.first,
          );
          final loadedBook = await ContentService.instance.loadBookContent(book);
          final chapter = loadedBook.chapters.firstWhere(
            (c) => c.id == lastPos.chapterId,
            orElse: () => loadedBook.chapters.first,
          );

          if (context.mounted) {
            Provider.of<ThemeProvider>(context, listen: false)
                .setSubjectSeedColor(subject.seedColor);
            Navigator.push(
              context,
              MaterialPageRoute(
                builder: (_) => ChapterScreen(
                  subject: subject,
                  book: loadedBook,
                  chapter: chapter,
                ),
              ),
            );
          }
        }
      },
      child: Row(
        children: [
          Container(
            padding: const EdgeInsets.all(12),
            decoration: BoxDecoration(
              color: colorScheme.primary,
              shape: BoxShape.circle,
            ),
            child: Icon(
              Icons.play_arrow_rounded,
              color: colorScheme.onPrimary,
              size: 28,
            ),
          ),
          const SizedBox(width: 14),
          Expanded(
            child: Column(
              crossAxisAlignment: CrossAxisAlignment.start,
              children: [
                Row(
                  children: [
                    Text(
                      'जारी रखें (Continue)',
                      style: theme.textTheme.labelMedium?.copyWith(
                        color: colorScheme.primary,
                        fontWeight: FontWeight.bold,
                      ),
                    ),
                    const SizedBox(width: 6),
                    Icon(
                      Icons.arrow_forward_rounded,
                      size: 14,
                      color: colorScheme.primary,
                    ),
                  ],
                ),
                const SizedBox(height: 4),
                Text(
                  lastPos.chapterTitle,
                  style: theme.textTheme.titleMedium?.copyWith(
                    fontWeight: FontWeight.bold,
                  ),
                  maxLines: 1,
                  overflow: TextOverflow.ellipsis,
                ),
                Text(
                  '${lastPos.subjectName} • ${lastPos.bookTitle}',
                  style: theme.textTheme.bodySmall?.copyWith(
                    color: colorScheme.onSurfaceVariant,
                  ),
                  maxLines: 1,
                  overflow: TextOverflow.ellipsis,
                ),
              ],
            ),
          ),
        ],
      ),
    );
  }

  Widget _buildSubjectCard(
    BuildContext context,
    Subject subject,
    ProgressProvider progressProvider,
  ) {
    final theme = Theme.of(context);
    final colorScheme = theme.colorScheme;
    final readCount = progressProvider.getReadCountForSubject(subject.id);

    return AccessibleCard(
      semanticLabel: '${subject.name}, ${subject.hindiName}, 8 पुस्तकें उपलब्ध',
      onTap: () {
        // Set dynamic theme matching this subject per Section 6.2
        Provider.of<ThemeProvider>(context, listen: false)
            .setSubjectSeedColor(subject.seedColor);

        Navigator.push(
          context,
          MaterialPageRoute(
            builder: (_) => SubjectScreen(subject: subject),
          ),
        );
      },
      child: Row(
        children: [
          // Distinct Subject Icon Container
          Container(
            width: 58,
            height: 58,
            decoration: BoxDecoration(
              color: subject.seedColor.withOpacity(0.14),
              borderRadius: BorderRadius.circular(14),
              border: Border.all(
                color: subject.seedColor.withOpacity(0.3),
                width: 1.5,
              ),
            ),
            child: Icon(
              subject.icon,
              size: 32,
              color: subject.seedColor,
            ),
          ),
          const SizedBox(width: 16),
          Expanded(
            child: Column(
              crossAxisAlignment: CrossAxisAlignment.start,
              children: [
                Row(
                  children: [
                    Text(
                      subject.name,
                      style: theme.textTheme.titleLarge?.copyWith(
                        fontWeight: FontWeight.bold,
                      ),
                    ),
                    const SizedBox(width: 8),
                    Container(
                      padding: const EdgeInsets.symmetric(horizontal: 8, vertical: 2),
                      decoration: BoxDecoration(
                        color: colorScheme.surfaceVariant,
                        borderRadius: BorderRadius.circular(6),
                      ),
                      child: Text(
                        '8 Books',
                        style: theme.textTheme.labelSmall?.copyWith(
                          fontWeight: FontWeight.bold,
                        ),
                      ),
                    ),
                  ],
                ),
                const SizedBox(height: 2),
                Text(
                  subject.hindiName,
                  style: theme.textTheme.titleSmall?.copyWith(
                    color: subject.seedColor,
                    fontWeight: FontWeight.w600,
                  ),
                ),
                const SizedBox(height: 4),
                Text(
                  subject.tagline,
                  style: theme.textTheme.bodySmall?.copyWith(
                    color: colorScheme.onSurfaceVariant,
                  ),
                  maxLines: 2,
                  overflow: TextOverflow.ellipsis,
                ),
                if (readCount > 0) ...[
                  const SizedBox(height: 8),
                  Row(
                    children: [
                      Icon(
                        Icons.check_circle_outline_rounded,
                        size: 14,
                        color: colorScheme.primary,
                      ),
                      const SizedBox(width: 4),
                      Text(
                        '$readCount अध्याय पूर्ण',
                        style: theme.textTheme.labelSmall?.copyWith(
                          color: colorScheme.primary,
                          fontWeight: FontWeight.bold,
                        ),
                      ),
                    ],
                  ),
                ],
              ],
            ),
          ),
          const SizedBox(width: 8),
          Icon(
            Icons.chevron_right_rounded,
            size: 28,
            color: colorScheme.onSurfaceVariant,
          ),
        ],
      ),
    );
  }
}
