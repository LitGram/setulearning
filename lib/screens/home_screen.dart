import 'package:flutter/material.dart';
import '../l10n/app_strings.dart';
import 'package:provider/provider.dart';
import 'package:shared_preferences/shared_preferences.dart';
import '../models/subject.dart';
import '../models/subject_group.dart';
import '../providers/progress_provider.dart';
import '../services/content_service.dart';
import '../services/chapter_identity.dart';
import '../widgets/accessible_card.dart';
import '../widgets/progress_state_panel.dart';
import 'search_screen.dart';
import 'chapter_screen.dart';
import 'progress_screen.dart';
import 'settings_screen.dart';
import 'subject_navigation.dart';

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
  static const _groupPrefKey = 'home_shelf';
  static const _allGroupsId = 'all';

  bool _resuming = false;

  /// `null` shows every group.
  SubjectGroup? _group;

  /// True once the student has answered the first-launch question (or picked
  /// a chip). Starts true so nothing flashes before preferences load.
  bool _groupChosen = true;

  @override
  void initState() {
    super.initState();
    _loadGroup();
  }

  Future<void> _loadGroup() async {
    try {
      final prefs = await SharedPreferences.getInstance();
      final saved = prefs.getString(_groupPrefKey);
      if (!mounted) return;
      setState(() {
        _groupChosen = saved != null;
        _group = SubjectGroup.fromId(saved);
      });
    } catch (error) {
      debugPrint('Could not load the saved subject group: $error');
    }
  }

  /// Shows [group] (null = every group) and remembers it for next time.
  Future<void> _chooseGroup(SubjectGroup? group) async {
    setState(() {
      _group = group;
      _groupChosen = true;
    });
    try {
      final prefs = await SharedPreferences.getInstance();
      await prefs.setString(_groupPrefKey, group?.id ?? _allGroupsId);
    } catch (error) {
      debugPrint('Could not save the subject group: $error');
    }
  }

  @override
  Widget build(BuildContext context) {
    final theme = Theme.of(context);
    final colorScheme = theme.colorScheme;
    final subjects = ContentService.instance.getSubjects();
    final groups = SubjectGroup.values
        .where((group) => subjects.any((s) => SubjectGroup.of(s) == group))
        .toList();
    final visibleGroups = _group == null ? groups : [_group!];

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
                excludeFromSemantics: true,
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
        actions: [
          IconButton(
            tooltip: context.strings.search,
            icon: const Icon(Icons.search_rounded),
            onPressed: _openSearch,
          ),
          const SizedBox(width: 4),
        ],
      ),
      body: Consumer<ProgressProvider>(
        builder: (context, progressProvider, child) {
          final lastPos = progressProvider.lastPosition;

          return LayoutBuilder(builder: (context, constraints) {
            // Two columns of subject cards once there is room for them.
            final twoColumns = constraints.maxWidth >= 720;
            return Align(
              alignment: Alignment.topCenter,
              child: ConstrainedBox(
                constraints: const BoxConstraints(maxWidth: 1040),
                child: ListView(
                  padding: const EdgeInsets.symmetric(
                      horizontal: 16.0, vertical: 12.0),
                  children: [
                    const ProgressStatePanel(),
                    if (lastPos != null) ...[
                      _buildResumeBanner(context, lastPos),
                      const SizedBox(height: 12),
                    ],
                    _buildSearchField(context),
                    const SizedBox(height: 20),
                    Padding(
                      padding: const EdgeInsets.symmetric(horizontal: 4.0),
                      child: Text(
                        context.strings.chooseSubject,
                        style: theme.textTheme.titleLarge?.copyWith(
                          fontWeight: FontWeight.bold,
                        ),
                      ),
                    ),
                    Padding(
                      padding: const EdgeInsets.fromLTRB(4, 2, 4, 0),
                      child: Text(
                        context.strings.chooseSubjectHint,
                        style: theme.textTheme.bodyMedium?.copyWith(
                          color: colorScheme.onSurfaceVariant,
                        ),
                      ),
                    ),
                    const SizedBox(height: 12),
                    if (!_groupChosen) ...[
                      _buildGroupQuestion(context, groups),
                      const SizedBox(height: 12),
                    ],
                    _buildGroupFilter(context, subjects, groups),
                    const SizedBox(height: 8),
                    for (final group in visibleGroups) ...[
                      _buildGroupHeader(context, group, subjects),
                      _buildSubjectGrid(
                        context,
                        subjects
                            .where((s) => SubjectGroup.of(s) == group)
                            .toList(),
                        progressProvider,
                        twoColumns,
                      ),
                      const SizedBox(height: 8),
                    ],
                    const SizedBox(height: 8),
                    _buildOfflineNote(context),
                    const SizedBox(height: 24),
                  ],
                ),
              ),
            );
          });
        },
      ),
    );
  }

  void _openSearch() {
    Navigator.push(
        context, MaterialPageRoute(builder: (_) => const SearchScreen()));
  }

  /// Looks like a search box so it is easy to spot. Tapping opens the
  /// search screen with the keyboard ready.
  Widget _buildSearchField(BuildContext context) {
    final theme = Theme.of(context);
    final colorScheme = theme.colorScheme;
    return Semantics(
      button: true,
      label: context.strings.searchBooksAndChapters,
      excludeSemantics: true,
      child: Material(
        color: colorScheme.surfaceContainerHigh,
        borderRadius: BorderRadius.circular(28),
        child: InkWell(
          borderRadius: BorderRadius.circular(28),
          onTap: _openSearch,
          child: ConstrainedBox(
            constraints: const BoxConstraints(minHeight: 56),
            child: Padding(
              padding: const EdgeInsets.symmetric(horizontal: 20, vertical: 12),
              child: Row(
                children: [
                  Icon(Icons.search_rounded,
                      color: colorScheme.onSurfaceVariant),
                  const SizedBox(width: 12),
                  Expanded(
                    child: Text(
                      context.strings.searchBooksAndChapters,
                      style: theme.textTheme.bodyLarge?.copyWith(
                        color: colorScheme.onSurfaceVariant,
                      ),
                    ),
                  ),
                ],
              ),
            ),
          ),
        ),
      ),
    );
  }

  Widget _buildGroupFilter(
      BuildContext context, List<Subject> subjects, List<SubjectGroup> groups) {
    Widget chip(SubjectGroup? group, String label, int count) {
      final selected = _group == group;
      return ChoiceChip(
        label: Text('$label ($count)'),
        selected: selected,
        onSelected: (_) => _chooseGroup(group),
      );
    }

    final language = context.strings.language;
    return Semantics(
      label: context.strings.chooseShelf,
      container: true,
      child: Wrap(
        spacing: 8,
        runSpacing: 8,
        children: [
          chip(null, context.strings.all, subjects.length),
          for (final group in groups)
            chip(group, group.labelIn(language),
                subjects.where((s) => SubjectGroup.of(s) == group).length),
        ],
      ),
    );
  }

  /// First-launch question: which group should home open on next time?
  /// Picking a chip below answers it too.
  Widget _buildGroupQuestion(BuildContext context, List<SubjectGroup> groups) {
    final theme = Theme.of(context);
    final colorScheme = theme.colorScheme;
    final strings = context.strings;
    return AccessibleCard(
      color: colorScheme.secondaryContainer.withOpacity(0.5),
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.stretch,
        children: [
          Text(
            strings.shelfQuestion,
            style: theme.textTheme.titleLarge?.copyWith(
              fontWeight: FontWeight.bold,
            ),
          ),
          const SizedBox(height: 4),
          Text(
            strings.shelfQuestionHint,
            style: theme.textTheme.bodyMedium?.copyWith(
              color: colorScheme.onSurfaceVariant,
            ),
          ),
          const SizedBox(height: 12),
          for (final group in groups)
            Padding(
              padding: const EdgeInsets.only(bottom: 8),
              child: OutlinedButton(
                style: OutlinedButton.styleFrom(
                  minimumSize: const Size.fromHeight(56),
                  alignment: Alignment.centerLeft,
                  padding:
                      const EdgeInsets.symmetric(horizontal: 14, vertical: 8),
                ),
                onPressed: () => _chooseGroup(group),
                child: Row(
                  children: [
                    Icon(group.icon, color: colorScheme.primary),
                    const SizedBox(width: 12),
                    Expanded(
                      child: Column(
                        crossAxisAlignment: CrossAxisAlignment.start,
                        children: [
                          Text(
                            group.labelIn(strings.language),
                            style: theme.textTheme.titleSmall?.copyWith(
                              fontWeight: FontWeight.bold,
                              color: colorScheme.onSurface,
                            ),
                          ),
                          Text(
                            group.descriptionIn(strings.language),
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
            onPressed: () => _chooseGroup(null),
            child: Text(strings.showAllSubjects),
          ),
        ],
      ),
    );
  }

  Widget _buildGroupHeader(
      BuildContext context, SubjectGroup group, List<Subject> subjects) {
    final theme = Theme.of(context);
    final colorScheme = theme.colorScheme;
    return Semantics(
      header: true,
      child: Padding(
        padding: const EdgeInsets.fromLTRB(4, 16, 4, 8),
        child: Row(
          children: [
            Icon(group.icon, size: 20, color: colorScheme.primary),
            const SizedBox(width: 8),
            Flexible(
              child: Text(
                group.labelIn(context.strings.language),
                style: theme.textTheme.titleMedium?.copyWith(
                  fontWeight: FontWeight.bold,
                ),
              ),
            ),
          ],
        ),
      ),
    );
  }

  Widget _buildSubjectGrid(
    BuildContext context,
    List<Subject> subjects,
    ProgressProvider progressProvider,
    bool twoColumns,
  ) {
    final cards = [
      for (final subject in subjects)
        _buildSubjectCard(context, subject, progressProvider),
    ];
    if (!twoColumns) {
      return Column(
        children: [
          for (final card in cards)
            Padding(padding: const EdgeInsets.only(bottom: 10), child: card),
        ],
      );
    }
    return Column(
      children: [
        for (var i = 0; i < cards.length; i += 2)
          Padding(
            padding: const EdgeInsets.only(bottom: 10),
            child: IntrinsicHeight(
              child: Row(
                crossAxisAlignment: CrossAxisAlignment.stretch,
                children: [
                  Expanded(child: cards[i]),
                  const SizedBox(width: 12),
                  Expanded(
                    child: i + 1 < cards.length
                        ? cards[i + 1]
                        : const SizedBox.shrink(),
                  ),
                ],
              ),
            ),
          ),
      ],
    );
  }

  Widget _buildOfflineNote(BuildContext context) {
    final theme = Theme.of(context);
    final colorScheme = theme.colorScheme;
    return Padding(
      padding: const EdgeInsets.symmetric(horizontal: 4),
      child: Row(
        children: [
          Icon(Icons.offline_pin_rounded, color: colorScheme.primary, size: 22),
          const SizedBox(width: 10),
          Expanded(
            child: Text(
              context.strings.offlineNote,
              style: theme.textTheme.bodySmall?.copyWith(
                color: colorScheme.onSurfaceVariant,
              ),
            ),
          ),
        ],
      ),
    );
  }

  Widget _buildResumeBanner(BuildContext context, dynamic lastPos) {
    final theme = Theme.of(context);
    final colorScheme = theme.colorScheme;

    return AccessibleCard(
      color: colorScheme.primaryContainer,
      semanticLabel: context.strings
          .continueReadingSemantics(lastPos.chapterTitle, lastPos.bookTitle),
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
                    setState(() => _resuming = false);
                    await openWithSubjectTheme(
                      context,
                      subject,
                      (_) => ChapterScreen(
                        subject: subject,
                        book: loadedBook,
                        chapter: chapter,
                      ),
                    );
                  }
                }
              } catch (_) {
                if (context.mounted) {
                  ScaffoldMessenger.of(context).showSnackBar(SnackBar(
                      content: Text(context.strings.couldNotOpenChapter)));
                }
              } finally {
                if (mounted && _resuming) setState(() => _resuming = false);
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
            child: _resuming
                ? SizedBox(
                    width: 28,
                    height: 28,
                    child: Padding(
                      padding: const EdgeInsets.all(4),
                      child: CircularProgressIndicator(
                        strokeWidth: 3,
                        color: colorScheme.onPrimary,
                      ),
                    ),
                  )
                : Icon(
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
                Text(
                  context.strings.continueReading,
                  style: theme.textTheme.labelLarge?.copyWith(
                    color: colorScheme.onPrimaryContainer,
                    fontWeight: FontWeight.bold,
                  ),
                ),
                const SizedBox(height: 4),
                Text(
                  lastPos.chapterTitle,
                  style: theme.textTheme.titleMedium?.copyWith(
                    fontWeight: FontWeight.bold,
                    color: colorScheme.onPrimaryContainer,
                  ),
                  maxLines: 2,
                  overflow: TextOverflow.ellipsis,
                ),
                Text(
                  '${lastPos.subjectName} • ${lastPos.bookTitle}',
                  style: theme.textTheme.bodySmall?.copyWith(
                    color: colorScheme.onPrimaryContainer,
                  ),
                  maxLines: 1,
                  overflow: TextOverflow.ellipsis,
                ),
              ],
            ),
          ),
          const SizedBox(width: 8),
          Icon(Icons.chevron_right_rounded,
              size: 28, color: colorScheme.onPrimaryContainer),
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
    final bookCount = subject.books.length;
    final bookLabel = context.strings.booksLower(bookCount);

    return AccessibleCard(
      semanticLabel: '${subject.name}, ${subject.hindiName}, $bookLabel'
          '${readCount > 0 ? ', ${context.strings.chaptersRead(readCount)}' : ''}',
      onTap: () => openSubject(context, subject),
      child: Row(
        children: [
          // Distinct subject icon container.
          Container(
            width: 52,
            height: 52,
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
              size: 28,
              color: subjectColor,
            ),
          ),
          const SizedBox(width: 14),
          Expanded(
            child: Column(
              crossAxisAlignment: CrossAxisAlignment.start,
              children: [
                Text(
                  subject.name,
                  style: theme.textTheme.titleMedium?.copyWith(
                    fontWeight: FontWeight.bold,
                  ),
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
                const SizedBox(height: 8),
                Wrap(
                  spacing: 12,
                  runSpacing: 4,
                  children: [
                    _meta(context, Icons.menu_book_outlined, bookLabel,
                        colorScheme.onSurfaceVariant),
                    if (readCount > 0)
                      _meta(
                          context,
                          Icons.check_circle_outline_rounded,
                          context.strings.chaptersDone(readCount),
                          colorScheme.primary),
                  ],
                ),
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

  Widget _meta(BuildContext context, IconData icon, String text, Color color) {
    return Row(
      mainAxisSize: MainAxisSize.min,
      children: [
        Icon(icon, size: 16, color: color),
        const SizedBox(width: 4),
        Flexible(
          child: Text(
            text,
            style: Theme.of(context).textTheme.labelMedium?.copyWith(
                  color: color,
                  fontWeight: FontWeight.bold,
                ),
          ),
        ),
      ],
    );
  }
}
