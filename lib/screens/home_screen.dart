import 'package:flutter/material.dart';
import 'package:provider/provider.dart';
import '../models/subject.dart';
import '../providers/progress_provider.dart';
import '../providers/theme_provider.dart';
import '../services/content_service.dart';
import '../services/chapter_identity.dart';
import '../widgets/accessible_card.dart';
import '../widgets/progress_state_panel.dart';
import 'search_screen.dart';
import 'chapter_screen.dart';
import 'progress_screen.dart';
import 'settings_screen.dart';
import 'subject_screen.dart';

class HomeScreen extends StatefulWidget {
  const HomeScreen({super.key});

  @override
  State<HomeScreen> createState() => _HomeScreenState();
}

class _HomeScreenState extends State<HomeScreen> {
  int _selectedDestination = 0;
  final Set<int> _visited = {0};

  @override
  Widget build(BuildContext context) {
    return LayoutBuilder(
      builder: (context, constraints) {
        final useRail = constraints.maxWidth >= 600;
        final pageStack = IndexedStack(
          index: _selectedDestination,
          children: [
            const _SubjectHomeScreen(),
            _visited.contains(1)
                ? const ProgressScreen()
                : const SizedBox.shrink(),
            _visited.contains(2)
                ? const SettingsScreen()
                : const SizedBox.shrink(),
          ],
        );

        return Scaffold(
          body: useRail
              ? Row(
                  children: [
                    NavigationRail(
                      selectedIndex: _selectedDestination,
                      onDestinationSelected: (index) => setState(() {
                        _selectedDestination = index;
                        _visited.add(index);
                      }),
                      labelType: NavigationRailLabelType.all,
                      destinations: const [
                        NavigationRailDestination(
                          icon: Icon(Icons.menu_book_outlined),
                          selectedIcon: Icon(Icons.menu_book_rounded),
                          label: Text('Subjects'),
                        ),
                        NavigationRailDestination(
                          icon: Icon(Icons.insights_outlined),
                          selectedIcon: Icon(Icons.insights_rounded),
                          label: Text('Progress'),
                        ),
                        NavigationRailDestination(
                          icon: Icon(Icons.settings_outlined),
                          selectedIcon: Icon(Icons.settings_rounded),
                          label: Text('Settings'),
                        ),
                      ],
                    ),
                    const VerticalDivider(width: 1),
                    Expanded(child: pageStack),
                  ],
                )
              : pageStack,
          bottomNavigationBar: useRail
              ? null
              : NavigationBar(
                  selectedIndex: _selectedDestination,
                  onDestinationSelected: (index) => setState(() {
                    _selectedDestination = index;
                    _visited.add(index);
                  }),
                  destinations: const [
                    NavigationDestination(
                      icon: Icon(Icons.menu_book_outlined),
                      selectedIcon: Icon(Icons.menu_book_rounded),
                      label: 'Subjects',
                    ),
                    NavigationDestination(
                      icon: Icon(Icons.insights_outlined),
                      selectedIcon: Icon(Icons.insights_rounded),
                      label: 'Progress',
                    ),
                    NavigationDestination(
                      icon: Icon(Icons.settings_outlined),
                      selectedIcon: Icon(Icons.settings_rounded),
                      label: 'Settings',
                    ),
                  ],
                ),
        );
      },
    );
  }
}

class _SubjectHomeScreen extends StatefulWidget {
  const _SubjectHomeScreen();
  @override
  State<_SubjectHomeScreen> createState() => _SubjectHomeScreenState();
}

class _SubjectHomeScreenState extends State<_SubjectHomeScreen> {
  bool _resuming = false;

  @override
  Widget build(BuildContext context) {
    final theme = Theme.of(context);
    final colorScheme = theme.colorScheme;
    final subjects = ContentService.instance.getSubjects();
    return Scaffold(
      appBar: AppBar(
        toolbarHeight: (MediaQuery.textScalerOf(context).scale(
                    Theme.of(context).textTheme.titleMedium?.fontSize ?? 18) *
                2.8)
            .clamp(56.0, 160.0),
        title: Row(
          children: [
            ClipRRect(
              borderRadius: BorderRadius.circular(10),
              child: Image.asset(
                'assets/icons/app_logo.png',
                width: 36,
                height: 36,
                fit: BoxFit.cover,
                errorBuilder: (context, error, stackTrace) => Container(
                  padding: const EdgeInsets.all(8),
                  decoration: BoxDecoration(
                    color: colorScheme.primaryContainer,
                    borderRadius: BorderRadius.circular(10),
                  ),
                  child: Icon(
                    Icons.school_rounded,
                    color: colorScheme.primary,
                    size: 22,
                  ),
                ),
              ),
            ),
            const SizedBox(width: 12),
            Expanded(
                child: Column(
              crossAxisAlignment: CrossAxisAlignment.start,
              children: [
                Text(
                  'Setu Learning',
                  style: theme.textTheme.titleMedium?.copyWith(
                    fontWeight: FontWeight.bold,
                  ),
                ),
                Text(
                  'पढ़ाई, जब चाहो',
                  style: theme.textTheme.bodySmall?.copyWith(
                    color: colorScheme.onSurfaceVariant,
                  ),
                ),
              ],
            )),
          ],
        ),
      ),
      body: Consumer<ProgressProvider>(
        builder: (context, progressProvider, child) {
          final lastPos = progressProvider.lastPosition;

          return ListView(
            padding:
                const EdgeInsets.symmetric(horizontal: 16.0, vertical: 12.0),
            children: [
              const ProgressStatePanel(),
              if (lastPos != null) ...[
                _buildResumeBanner(context, lastPos),
                const SizedBox(height: 16),
              ],
              OutlinedButton.icon(
                icon: const Icon(Icons.search_rounded),
                label: const Text('Search books and chapters'),
                onPressed: () => Navigator.push(context,
                    MaterialPageRoute(builder: (_) => const SearchScreen())),
              ),
              const SizedBox(height: 16),
              // Section Header
              Padding(
                padding:
                    const EdgeInsets.symmetric(vertical: 8.0, horizontal: 4.0),
                child: Text(
                  'Choose a subject',
                  style: theme.textTheme.titleLarge?.copyWith(
                    fontWeight: FontWeight.bold,
                  ),
                ),
              ),
              Text(
                'अपनी परीक्षा और विषय के अनुसार पुस्तकें चुनें।',
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
      onTap: _resuming
          ? null
          : () async {
              setState(() => _resuming = true);
              try {
                final subject =
                    ContentService.instance.getSubjectById(lastPos.subjectId);
                if (subject != null) {
                  final book = subject.books.firstWhere(
                    (b) => b.id == lastPos.bookId,
                    orElse: () => subject.books.first,
                  );
                  final loadedBook =
                      await ContentService.instance.loadBookContent(book);
                  final chapter = loadedBook.chapters.firstWhere(
                    (c) =>
                        c.id ==
                        ChapterIdentity.canonical(
                            subject.id, book.id, lastPos.chapterId),
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
              } catch (_) {
                if (context.mounted) {
                  ScaffoldMessenger.of(context).showSnackBar(const SnackBar(
                      content: Text(
                          'Could not open the chapter. Please try again.')));
                }
              } finally {
                if (mounted) setState(() => _resuming = false);
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
                    Flexible(
                        child: Text(
                      'Continue reading',
                      style: theme.textTheme.labelMedium?.copyWith(
                        color: colorScheme.primary,
                        fontWeight: FontWeight.bold,
                      ),
                    )),
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
    final subjectColor = ColorScheme.fromSeed(
            seedColor: subject.seedColor, brightness: theme.brightness)
        .primary;
    final readCount = progressProvider.getReadCountForSubject(subject.id);

    return AccessibleCard(
      semanticLabel:
          '${subject.name}, ${subject.hindiName}, ${subject.books.length} पुस्तकें उपलब्ध',
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
          // Distinct subject icon container.
          Container(
            width: 58,
            height: 58,
            decoration: BoxDecoration(
              color: subjectColor.withOpacity(0.14),
              borderRadius: BorderRadius.circular(14),
              border: Border.all(
                color: subjectColor.withOpacity(0.3),
                width: 1.5,
              ),
            ),
            child: Icon(
              subject.icon,
              size: 32,
              color: subjectColor,
            ),
          ),
          const SizedBox(width: 16),
          Expanded(
            child: Column(
              crossAxisAlignment: CrossAxisAlignment.start,
              children: [
                Row(
                  children: [
                    Expanded(
                      child: Text(
                        subject.name,
                        style: theme.textTheme.titleLarge?.copyWith(
                          fontWeight: FontWeight.bold,
                        ),
                      ),
                    ),
                    const SizedBox(width: 8),
                    Container(
                      padding: const EdgeInsets.symmetric(
                          horizontal: 8, vertical: 2),
                      decoration: BoxDecoration(
                        color: colorScheme.surfaceVariant,
                        borderRadius: BorderRadius.circular(6),
                      ),
                      child: Text(
                        '${subject.books.length} Books',
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
                    color: subjectColor,
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
