import 'package:flutter/material.dart';
import '../l10n/app_strings.dart';
import 'package:provider/provider.dart';
import 'package:shared_preferences/shared_preferences.dart';
import '../models/shelf.dart';
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
                      destinations: [
                        NavigationRailDestination(
                          icon: const Icon(Icons.menu_book_outlined),
                          selectedIcon: const Icon(Icons.menu_book_rounded),
                          label: Text(context.strings.navSubjects),
                        ),
                        NavigationRailDestination(
                          icon: const Icon(Icons.insights_outlined),
                          selectedIcon: const Icon(Icons.insights_rounded),
                          label: Text(context.strings.navProgress),
                        ),
                        NavigationRailDestination(
                          icon: const Icon(Icons.settings_outlined),
                          selectedIcon: const Icon(Icons.settings_rounded),
                          label: Text(context.strings.navSettings),
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
                  destinations: [
                    NavigationDestination(
                      icon: const Icon(Icons.menu_book_outlined),
                      selectedIcon: const Icon(Icons.menu_book_rounded),
                      label: context.strings.navSubjects,
                    ),
                    NavigationDestination(
                      icon: const Icon(Icons.insights_outlined),
                      selectedIcon: const Icon(Icons.insights_rounded),
                      label: context.strings.navProgress,
                    ),
                    NavigationDestination(
                      icon: const Icon(Icons.settings_outlined),
                      selectedIcon: const Icon(Icons.settings_rounded),
                      label: context.strings.navSettings,
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
  static const _shelfPrefKey = 'home_shelf';
  static const _allShelvesId = 'all';

  bool _resuming = false;

  /// The shelf being shown; null means every shelf ("सभी").
  Shelf? _shelf;

  /// True once the learner has answered (or skipped) the first-run question.
  /// Starts true so nothing flashes before preferences load.
  bool _shelfChosen = true;

  @override
  void initState() {
    super.initState();
    _loadShelf();
  }

  Future<void> _loadShelf() async {
    try {
      final prefs = await SharedPreferences.getInstance();
      final saved = prefs.getString(_shelfPrefKey);
      if (!mounted) return;
      setState(() {
        _shelfChosen = saved != null;
        _shelf = Shelf.fromId(saved);
      });
    } catch (error) {
      debugPrint('Could not load the saved shelf: $error');
    }
  }

  Future<void> _chooseShelf(Shelf? shelf) async {
    setState(() {
      _shelf = shelf;
      _shelfChosen = true;
    });
    try {
      final prefs = await SharedPreferences.getInstance();
      await prefs.setString(_shelfPrefKey, shelf?.id ?? _allShelvesId);
    } catch (error) {
      debugPrint('Could not save the shelf: $error');
    }
  }

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
                  context.strings.appTagline,
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
                label: Text(context.strings.searchBooksAndChapters),
                onPressed: () => Navigator.push(context,
                    MaterialPageRoute(builder: (_) => const SearchScreen())),
              ),
              const SizedBox(height: 16),
              if (!_shelfChosen) ...[
                _buildShelfQuestion(context),
                const SizedBox(height: 16),
              ] else ...[
                _buildShelfChips(context),
                const SizedBox(height: 8),
              ],

              // Subject cards, grouped by shelf.
              for (final shelf in Shelf.values)
                if ((_shelf == null || _shelf == shelf) &&
                    shelf.filter(subjects).isNotEmpty) ...[
                  _buildShelfHeader(context, shelf),
                  ...shelf.filter(subjects).map((subject) => Padding(
                        padding: const EdgeInsets.only(bottom: 14.0),
                        child: _buildSubjectCard(
                            context, subject, progressProvider),
                      )),
                ],

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
                            context.strings.offlineTitle,
                            style: theme.textTheme.labelLarge?.copyWith(
                              fontWeight: FontWeight.bold,
                            ),
                          ),
                          const SizedBox(height: 2),
                          Text(
                            context.strings.offlineBody,
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

  /// First-run question: which shelf should the home screen open on?
  Widget _buildShelfQuestion(BuildContext context) {
    final theme = Theme.of(context);
    final colorScheme = theme.colorScheme;
    return AccessibleCard(
      color: colorScheme.secondaryContainer.withOpacity(0.5),
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.stretch,
        children: [
          Text(
            context.strings.shelfQuestion,
            style: theme.textTheme.titleLarge?.copyWith(
              fontWeight: FontWeight.bold,
            ),
          ),
          const SizedBox(height: 4),
          Text(
            context.strings.shelfQuestionHint,
            style: theme.textTheme.bodyMedium?.copyWith(
              color: colorScheme.onSurfaceVariant,
            ),
          ),
          const SizedBox(height: 12),
          for (final shelf in Shelf.values)
            Padding(
              padding: const EdgeInsets.only(bottom: 8),
              child: OutlinedButton(
                style: OutlinedButton.styleFrom(
                  minimumSize: const Size.fromHeight(56),
                  alignment: Alignment.centerLeft,
                  padding:
                      const EdgeInsets.symmetric(horizontal: 14, vertical: 8),
                ),
                onPressed: () => _chooseShelf(shelf),
                child: Row(
                  children: [
                    Icon(shelf.icon, color: colorScheme.primary),
                    const SizedBox(width: 12),
                    Expanded(
                      child: Column(
                        crossAxisAlignment: CrossAxisAlignment.start,
                        children: [
                          Text(
                            shelf.labelIn(context.strings.language),
                            style: theme.textTheme.titleSmall?.copyWith(
                              fontWeight: FontWeight.bold,
                              color: colorScheme.onSurface,
                            ),
                          ),
                          Text(
                            shelf.descriptionIn(context.strings.language),
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
            ),
          TextButton(
            onPressed: () => _chooseShelf(null),
            child: Text(context.strings.showAllSubjects),
          ),
        ],
      ),
    );
  }

  /// Chips for switching shelf after the first-run question is answered.
  Widget _buildShelfChips(BuildContext context) {
    Widget chip(String label, Shelf? shelf, IconData? icon) => ChoiceChip(
          avatar: icon == null ? null : Icon(icon, size: 18),
          label: Text(label),
          selected: _shelf == shelf,
          showCheckmark: false,
          onSelected: (_) => _chooseShelf(shelf),
        );
    return Semantics(
      label: context.strings.chooseShelf,
      container: true,
      child: Wrap(
        spacing: 8,
        runSpacing: 8,
        children: [
          chip(context.strings.allShelves, null, Icons.apps_rounded),
          for (final shelf in Shelf.values)
            chip(shelf.labelIn(context.strings.language), shelf, shelf.icon),
        ],
      ),
    );
  }

  Widget _buildShelfHeader(BuildContext context, Shelf shelf) {
    final theme = Theme.of(context);
    return Padding(
      padding: const EdgeInsets.fromLTRB(4, 12, 4, 10),
      child: Semantics(
        header: true,
        child: Row(
          children: [
            Icon(shelf.icon, color: theme.colorScheme.primary),
            const SizedBox(width: 8),
            Expanded(
              child: Text(
                shelf.labelIn(context.strings.language),
                style: theme.textTheme.titleLarge?.copyWith(
                  fontWeight: FontWeight.bold,
                ),
              ),
            ),
          ],
        ),
      ),
    );
  }

  Widget _buildResumeBanner(BuildContext context, dynamic lastPos) {
    final theme = Theme.of(context);
    final colorScheme = theme.colorScheme;

    return AccessibleCard(
      color: colorScheme.primaryContainer.withOpacity(0.7),
      semanticLabel: context.strings.continueChapterSemantics(lastPos.chapterTitle),
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
                  ScaffoldMessenger.of(context).showSnackBar(
                      SnackBar(content: Text(context.strings.couldNotOpenChapter)));
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
                      context.strings.continueReading,
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
          context.strings.subjectCardSemantics(
              subject.name, subject.hindiName, subject.books.length),
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
                        context.strings.booksCount(subject.books.length),
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
                        context.strings.chaptersDone(readCount),
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
