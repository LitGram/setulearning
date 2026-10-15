import 'dart:async';
import 'package:flutter/material.dart';
import 'package:provider/provider.dart';
import '../models/book.dart';
import '../models/chapter.dart';
import '../models/subject.dart';
import '../providers/progress_provider.dart';
import '../widgets/study_action_row.dart';
import '../widgets/content_block_widget.dart';
import 'quiz_screen.dart';
import '../services/study_session_store.dart';
import '../widgets/reader_settings_sheet.dart';
import '../widgets/screenshot_protected_screen.dart';
import '../theme/app_theme.dart';

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

class _ChapterScreenState extends State<ChapterScreen>
    with WidgetsBindingObserver {
  late Chapter _currentChapter;
  final ScrollController _scrollController = ScrollController();

  Timer? _saveTimer;
  late ProgressProvider _progress;
  bool _restoring = true;
  final Map<int, GlobalKey> _blockKeys = {};
  String get _positionKey => StudySessionStore.key(
      'reading', widget.subject.id, widget.book.id, _currentChapter.id);

  @override
  void initState() {
    super.initState();
    WidgetsBinding.instance.addObserver(this);
    _currentChapter = widget.chapter;
    _progress = context.read<ProgressProvider>();
    _scrollController.addListener(_scheduleSave);
  }

  void _scheduleSave() {
    if (_restoring) return;
    _saveTimer?.cancel();
    _saveTimer = Timer(const Duration(milliseconds: 500), _savePosition);
  }

  Future<void> _savePosition() async {
    if (!_scrollController.hasClients || _restoring) return;
    final offset = _scrollController.offset;
    int? anchor;
    double? delta;
    for (final entry in _blockKeys.entries) {
      final box = entry.value.currentContext?.findRenderObject();
      if (box is RenderBox && box.attached) {
        final y = box.localToGlobal(Offset.zero).dy;
        if (y <= 180 && (delta == null || y > delta)) {
          anchor = entry.key;
          delta = y;
        }
      }
    }
    try {
      await StudySessionStore.write(_positionKey, {
        'offset': offset,
        'anchor': anchor,
        'y': delta,
      });
    } catch (_) {
      if (mounted) {
        ScaffoldMessenger.of(context).showSnackBar(const SnackBar(
            content: Text('Reading position could not be saved.')));
      }
    }
  }

  void _onChapterOpened() {
    _restoring = true;
    final chapter = _currentChapter;
    WidgetsBinding.instance.addPostFrameCallback((_) async {
      if (!mounted) return;
      try {
        final saved = await StudySessionStore.read(_positionKey);
        if (!mounted || chapter.id != _currentChapter.id) return;
        if (_scrollController.hasClients) {
          final offset = (saved?['offset'] as num?)?.toDouble() ?? 0;
          // Lazy lists discover their extent while scrolling. Advance over
          // several frames rather than clamping against the initial estimate.
          for (var i = 0; i < 8 && mounted; i++) {
            _scrollController.jumpTo(
                offset.clamp(0, _scrollController.position.maxScrollExtent));
            await WidgetsBinding.instance.endOfFrame;
            if (!mounted || chapter.id != _currentChapter.id) return;
            if (_scrollController.offset >= offset) break;
          }
          final anchor = saved?['anchor'] as int?;
          final box = _blockKeys[anchor]?.currentContext?.findRenderObject();
          if (box is RenderBox && box.attached && saved?['y'] is num) {
            final adjustment = box.localToGlobal(Offset.zero).dy -
                (saved!['y'] as num).toDouble();
            _scrollController.jumpTo((_scrollController.offset + adjustment)
                .clamp(0, _scrollController.position.maxScrollExtent));
          }
        }
        await _progress.updateLastPosition(
            subjectId: widget.subject.id,
            bookId: widget.book.id,
            chapterId: chapter.id,
            subjectName: widget.subject.name,
            bookTitle: widget.book.title,
            chapterTitle: chapter.title);
      } catch (_) {
        if (mounted) {
          ScaffoldMessenger.of(context).showSnackBar(const SnackBar(
              content: Text('Reading history could not be saved.')));
        }
      } finally {
        if (mounted && chapter.id == _currentChapter.id) _restoring = false;
      }
    });
  }

  int get _currentIndex =>
      widget.book.chapters.indexWhere((c) => c.id == _currentChapter.id);

  bool get _hasPrevious => _currentIndex > 0;
  bool get _hasNext =>
      _currentIndex >= 0 && _currentIndex < widget.book.chapters.length - 1;

  void _goToChapter(int newIndex) {
    if (newIndex >= 0 && newIndex < widget.book.chapters.length) {
      _saveTimer?.cancel();
      _savePosition();
      _blockKeys.clear();
      setState(() {
        _currentChapter = widget.book.chapters[newIndex];
      });
      _onChapterOpened();
      _scrollController.jumpTo(0);
    }
  }

  @override
  void didChangeAppLifecycleState(AppLifecycleState state) {
    if (state != AppLifecycleState.resumed) {
      _saveTimer?.cancel();
      _savePosition();
    }
  }

  @override
  void dispose() {
    WidgetsBinding.instance.removeObserver(this);
    _saveTimer?.cancel();
    _savePosition();
    _scrollController.dispose();
    super.dispose();
  }

  @override
  Widget build(BuildContext context) => ScreenshotProtectedScreen(
        onProtected: _onChapterOpened,
        child: _buildChapter(context),
      );

  Widget _buildChapter(BuildContext context) {
    final theme = Theme.of(context);
    final colorScheme = theme.colorScheme;

    final chapterHeader = Container(
      padding: const EdgeInsets.all(16),
      decoration: BoxDecoration(
        color: colorScheme.primaryContainer.withOpacity(0.3),
        borderRadius: BorderRadius.circular(16),
        border: Border.all(color: colorScheme.primary.withOpacity(0.2)),
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
    );
    final quizLauncher = _currentChapter.mcqs.isEmpty
        ? null
        : Container(
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
                    Icon(Icons.quiz_rounded,
                        size: 32, color: colorScheme.secondary),
                    const SizedBox(width: 12),
                    Expanded(
                      child: Column(
                        crossAxisAlignment: CrossAxisAlignment.start,
                        children: [
                          Text(
                            'अध्याय-अंत अभ्यास (वैकल्पिक)',
                            style: theme.textTheme.titleMedium?.copyWith(
                              fontWeight: FontWeight.bold,
                              color: colorScheme.onSecondaryContainer,
                            ),
                          ),
                          Text(
                            'कुल प्रश्न: ${_currentChapter.mcqs.length} • अध्याय पढ़ने के बाद कभी भी हल करें',
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
                    label: const Text('वैकल्पिक अभ्यास शुरू करें'),
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
          );

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
          IconButton(
              tooltip: 'Reading settings',
              icon: const Icon(Icons.text_fields_rounded),
              onPressed: () => showReaderSettings(context)),
          if (_currentChapter.mcqs.isNotEmpty)
            IconButton(
                tooltip: 'Practice',
                icon: const Icon(Icons.quiz_outlined),
                onPressed: () => Navigator.push(
                    context,
                    MaterialPageRoute(
                        builder: (_) => QuizScreen(
                            subject: widget.subject,
                            book: widget.book,
                            chapter: _currentChapter)))),
          const SizedBox(width: 8),
        ],
      ),
      body: Column(
        children: [
          // Reading Content
          Expanded(
            child: LayoutBuilder(
              builder: (context, constraints) {
                // Keep the reading column centered on tablets while letting it
                // occupy the full available width on phones. The gutters scale
                // with the viewport so they cannot make the chapter look
                // shifted to the right on compact screens.
                final horizontalPadding =
                    (constraints.maxWidth * 0.05).clamp(12.0, 24.0);
                return Center(
                  child: ConstrainedBox(
                    constraints:
                        const BoxConstraints(maxWidth: AppSpacing.contentWidth),
                    child: SizedBox(
                      width: double.infinity,
                      child: ListView.builder(
                        controller: _scrollController,
                        padding: EdgeInsets.symmetric(
                            horizontal: horizontalPadding, vertical: 16.0),
                        itemCount: 3 +
                            _currentChapter.content.length +
                            (quizLauncher == null ? 0 : 2),
                        itemBuilder: (context, index) {
                          if (index == 0) return chapterHeader;
                          if (index == 1) return const SizedBox(height: 16);

                          final contentIndex = index - 2;
                          if (contentIndex < _currentChapter.content.length) {
                            return KeyedSubtree(
                                key: _blockKeys.putIfAbsent(
                                    contentIndex, GlobalKey.new),
                                child: ContentBlockWidget(
                                    block:
                                        _currentChapter.content[contentIndex]));
                          }
                          if (contentIndex == _currentChapter.content.length) {
                            final completed = context
                                .watch<ProgressProvider>()
                                .isChapterRead(widget.subject.id,
                                    widget.book.id, _currentChapter.id);
                            return Padding(
                                padding:
                                    const EdgeInsets.symmetric(vertical: 24),
                                child: FilledButton.icon(
                                    icon: Icon(completed
                                        ? Icons.check_circle
                                        : Icons.check),
                                    label: Text(completed
                                        ? 'Reading completed'
                                        : 'Mark as read'),
                                    onPressed: completed
                                        ? null
                                        : () async {
                                            try {
                                              await _progress.markChapterRead(
                                                  subjectId: widget.subject.id,
                                                  bookId: widget.book.id,
                                                  chapterId:
                                                      _currentChapter.id);
                                              if (context.mounted) {
                                                ScaffoldMessenger.of(context)
                                                    .showSnackBar(const SnackBar(
                                                        content: Text(
                                                            'Progress saved')));
                                              }
                                            } catch (_) {
                                              if (context.mounted) {
                                                ScaffoldMessenger.of(context)
                                                    .showSnackBar(const SnackBar(
                                                        content: Text(
                                                            'Could not save progress. Try again.')));
                                              }
                                            }
                                          }));
                          }
                          if (quizLauncher != null &&
                              contentIndex ==
                                  _currentChapter.content.length + 1) {
                            return quizLauncher;
                          }
                          return const SizedBox(height: 24);
                        },
                      ),
                    ),
                  ),
                );
              },
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
              child: StudyActionRow(
                children: [
                  // Previous Button
                  Expanded(
                    child: OutlinedButton.icon(
                      icon: const Icon(Icons.arrow_back_rounded, size: 18),
                      label: const Text('Previous'),
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
                      label: const Text('Next'),
                      onPressed: _hasNext
                          ? () => _goToChapter(_currentIndex + 1)
                          : null,
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
