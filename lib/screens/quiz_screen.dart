import 'dart:convert';
import 'dart:math';
import 'package:flutter/material.dart';
import 'package:provider/provider.dart';
import '../models/book.dart';
import '../models/chapter.dart';
import '../models/mcq.dart';
import '../models/subject.dart';
import '../providers/progress_provider.dart';
import '../widgets/study_action_row.dart';
import '../widgets/accessible_card.dart';
import '../widgets/markdown_content.dart';
import '../widgets/screenshot_protected_screen.dart';
import '../services/study_session_store.dart';

class QuizScreen extends StatefulWidget {
  final Subject subject;
  final Book book;
  final Chapter chapter;

  const QuizScreen({
    super.key,
    required this.subject,
    required this.book,
    required this.chapter,
  });

  @override
  State<QuizScreen> createState() => _QuizScreenState();
}

class _QuizScreenState extends State<QuizScreen> {
  int _questionIndex = 0;
  final Map<int, int> _selectedAnswers =
      {}; // questionIndex -> selectedOptionIndex
  bool _submittedCurrent = false;
  int _score = 0;
  bool _isQuizComplete = false;

  List<MCQ> get _mcqs => widget.chapter.mcqs;

  final Set<int> _checked = {};
  final Set<int> _skipped = {};
  final Map<int, Set<int>> _hiddenOptions = {};
  bool _loadingDraft = true;
  bool _savingResult = false;
  bool _resultSaved = false;
  bool _allowExit = false;
  bool _saveFailed = false;
  Future<void> _pendingSave = Future.value();
  String get _draftKey => StudySessionStore.key(
      'quiz', widget.subject.id, widget.book.id, widget.chapter.id);
  String get _signature => jsonEncode(
      _mcqs.map((q) => [q.question, q.options, q.correctIndex]).toList());

  @override
  void initState() {
    super.initState();
    _loadDraft();
  }

  Future<void> _loadDraft() async {
    try {
      final draft = await StudySessionStore.read(_draftKey);
      if (!mounted) return;
      if (draft != null && draft['signature'] == _signature) {
        setState(() => _loadingDraft = false);
        final resume = await showDialog<bool>(
            context: context,
            barrierDismissible: false,
            builder: (context) => AlertDialog(
                    title: const Text('Resume practice?'),
                    content: const Text(
                        'Your unfinished answers are saved on this device.'),
                    actions: [
                      TextButton(
                          onPressed: () => Navigator.pop(context, false),
                          child: const Text('Start again')),
                      FilledButton(
                          onPressed: () => Navigator.pop(context, true),
                          child: const Text('Resume'))
                    ]));
        if (!mounted) return;
        if (resume == true) {
          final answers = draft['answers'] as Map<String, dynamic>;
          for (final entry in answers.entries) {
            final index = int.parse(entry.key);
            final option = entry.value as int;
            if (index >= 0 &&
                index < _mcqs.length &&
                option >= 0 &&
                option < _mcqs[index].options.length) {
              _selectedAnswers[index] = option;
            }
          }
          _checked.addAll((draft['checked'] as List)
              .cast<int>()
              .where(_selectedAnswers.containsKey));
          _skipped.addAll((draft['skipped'] as List? ?? []).cast<int>().where(
              (i) => i >= 0 && i < _mcqs.length && !_checked.contains(i)));
          final hidden = draft['hiddenOptions'] as Map<String, dynamic>? ?? {};
          for (final entry in hidden.entries) {
            final i = int.tryParse(entry.key);
            if (i == null || i < 0 || i >= _mcqs.length) continue;
            final options = (entry.value as List).cast<int>().toSet();
            if (options.length == 2 &&
                _mcqs[i].options.length >= 4 &&
                options.every((o) =>
                    o >= 0 &&
                    o < _mcqs[i].options.length &&
                    o != _mcqs[i].correctIndex)) {
              _hiddenOptions[i] = options;
              if (!_checked.contains(i) &&
                  options.contains(_selectedAnswers[i])) {
                _selectedAnswers.remove(i);
              }
            }
          }
          _questionIndex = (draft['index'] as int).clamp(0, _mcqs.length - 1);
          _score = _checked
              .where((i) => _selectedAnswers[i] == _mcqs[i].correctIndex)
              .length;
          _submittedCurrent = _checked.contains(_questionIndex);
        } else {
          await StudySessionStore.remove(_draftKey);
        }
      }
    } catch (_) {
      _saveFailed = true;
    }
    if (mounted) setState(() => _loadingDraft = false);
  }

  Future<void> _saveDraft() {
    final data = {
      'signature': _signature,
      'index': _questionIndex,
      'answers': _selectedAnswers.map((key, value) => MapEntry('$key', value)),
      'checked': _checked.toList(),
      'skipped': _skipped.toList(),
      'hiddenOptions':
          _hiddenOptions.map((key, value) => MapEntry('$key', value.toList())),
    };
    _pendingSave = _pendingSave.then((_) async {
      try {
        await StudySessionStore.write(_draftKey, data);
        if (mounted) setState(() => _saveFailed = false);
      } catch (_) {
        if (mounted) setState(() => _saveFailed = true);
      }
    });
    return _pendingSave;
  }

  Future<void> _exit() async {
    final exit = await showDialog<bool>(
        context: context,
        builder: (context) => AlertDialog(
                title: const Text('Leave practice?'),
                content: const Text('Save your answers and resume later.'),
                actions: [
                  TextButton(
                      onPressed: () => Navigator.pop(context, false),
                      child: const Text('Keep practicing')),
                  FilledButton(
                      onPressed: () => Navigator.pop(context, true),
                      child: const Text('Save & exit'))
                ]));
    if (exit != true || !mounted) return;
    await _saveDraft();
    if (!mounted || _saveFailed) return;
    setState(() => _allowExit = true);
    WidgetsBinding.instance.addPostFrameCallback((_) {
      if (mounted) Navigator.pop(context);
    });
  }

  void _selectOption(int optionIndex) {
    if (_submittedCurrent ||
        (_hiddenOptions[_questionIndex]?.contains(optionIndex) ?? false)) {
      return;
    }
    setState(() {
      _selectedAnswers[_questionIndex] = optionIndex;
    });
    _saveDraft();
  }

  void _checkCurrentAnswer() {
    if (_submittedCurrent || _selectedAnswers[_questionIndex] == null) return;

    final selected = _selectedAnswers[_questionIndex]!;
    final correct = _mcqs[_questionIndex].correctIndex;

    setState(() {
      _submittedCurrent = true;
      _checked.add(_questionIndex);
      _skipped.remove(_questionIndex);
      if (selected == correct) {
        _score++;
      }
    });
    _saveDraft();
  }

  void _nextQuestion() {
    if (_questionIndex < _mcqs.length - 1) {
      setState(() {
        _questionIndex++;
        _submittedCurrent = _checked.contains(_questionIndex);
      });
      _saveDraft();
    } else {
      _finishQuiz();
    }
  }

  void _skipQuestion() {
    if (_submittedCurrent) return;
    setState(() {
      _selectedAnswers.remove(_questionIndex);
      _skipped.add(_questionIndex);
    });
    _saveDraft();
    _nextQuestion();
  }

  void _useFiftyFifty() {
    final question = _mcqs[_questionIndex];
    if (_submittedCurrent ||
        _hiddenOptions.containsKey(_questionIndex) ||
        question.options.length < 4) {
      return;
    }
    final incorrect = List.generate(question.options.length, (i) => i)
        .where((i) => i != question.correctIndex)
        .toList()
      ..shuffle(Random());
    setState(() {
      final hidden = incorrect.take(2).toSet();
      _hiddenOptions[_questionIndex] = hidden;
      if (hidden.contains(_selectedAnswers[_questionIndex])) {
        _selectedAnswers.remove(_questionIndex);
      }
    });
    _saveDraft();
  }

  void _previousQuestion() {
    if (_questionIndex > 0) {
      setState(() {
        _questionIndex--;
        _submittedCurrent = _checked.contains(_questionIndex);
      });
      _saveDraft();
    }
  }

  Future<void> _finishQuiz() async {
    if (_savingResult || _resultSaved) return;
    setState(() {
      _isQuizComplete = true;
      _savingResult = true;
    });
    try {
      await context.read<ProgressProvider>().recordQuizScore(
          subjectId: widget.subject.id,
          bookId: widget.book.id,
          chapterId: widget.chapter.id,
          score: _score,
          total: _mcqs.length);
      _resultSaved = true;
      await _pendingSave;
      await StudySessionStore.remove(_draftKey);
    } catch (_) {
      _saveFailed = true;
    }
    if (mounted) setState(() => _savingResult = false);
  }

  void _resetQuiz() {
    setState(() {
      _questionIndex = 0;
      _selectedAnswers.clear();
      _checked.clear();
      _skipped.clear();
      _hiddenOptions.clear();
      _resultSaved = false;
      _saveFailed = false;
      _submittedCurrent = false;
      _score = 0;
      _isQuizComplete = false;
    });
    _saveDraft();
  }

  @override
  Widget build(BuildContext context) => PopScope(
        canPop: _allowExit ||
            _resultSaved ||
            (_selectedAnswers.isEmpty &&
                _skipped.isEmpty &&
                _hiddenOptions.isEmpty),
        onPopInvokedWithResult: (didPop, result) {
          if (!didPop) _exit();
        },
        child: ScreenshotProtectedScreen(child: _buildQuiz(context)),
      );

  Widget _buildQuiz(BuildContext context) {
    final theme = Theme.of(context);
    final colorScheme = theme.colorScheme;

    if (_loadingDraft) {
      return const Scaffold(body: Center(child: CircularProgressIndicator()));
    }

    if (_mcqs.isEmpty) {
      return Scaffold(
        appBar: AppBar(title: const Text('प्रश्नोत्तरी')),
        body: Center(
          child: Column(
            mainAxisAlignment: MainAxisAlignment.center,
            children: [
              const Icon(Icons.quiz_outlined, size: 60),
              const SizedBox(height: 16),
              Text(
                'इस अध्याय में कोई प्रश्न नहीं हैं।',
                style: theme.textTheme.titleMedium,
              ),
              const SizedBox(height: 16),
              FilledButton(
                onPressed: () => Navigator.pop(context),
                child: const Text('Go back'),
              ),
            ],
          ),
        ),
      );
    }

    if (_isQuizComplete) {
      return _buildResultScreen(context);
    }

    final currentMcq = _mcqs[_questionIndex];
    final selectedOption = _selectedAnswers[_questionIndex];
    final optionLetters = ['A', 'B', 'C', 'D', 'E', 'F'];

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
              'Practice',
              style: theme.textTheme.titleMedium?.copyWith(
                fontWeight: FontWeight.bold,
              ),
            ),
            Text(
              widget.chapter.title,
              style: theme.textTheme.bodySmall?.copyWith(
                color: colorScheme.onSurfaceVariant,
              ),
              maxLines: 1,
              overflow: TextOverflow.ellipsis,
            ),
          ],
        ),
      ),
      body: Column(
        children: [
          if (_saveFailed)
            MaterialBanner(
                content: const Text('Answers could not be saved.'),
                actions: [
                  TextButton(onPressed: _saveDraft, child: const Text('Retry'))
                ]),
          // Linear progress bar
          LinearProgressIndicator(
            value: (_questionIndex + 1) / _mcqs.length,
            backgroundColor: colorScheme.surfaceVariant,
          ),

          Expanded(
            child: ListView(
              padding:
                  const EdgeInsets.symmetric(horizontal: 16.0, vertical: 16.0),
              children: [
                // Question Header
                Wrap(
                  spacing: 16,
                  runSpacing: 8,
                  alignment: WrapAlignment.spaceBetween,
                  children: [
                    Container(
                      padding: const EdgeInsets.symmetric(
                          horizontal: 12, vertical: 6),
                      decoration: BoxDecoration(
                        color: colorScheme.primaryContainer,
                        borderRadius: BorderRadius.circular(10),
                      ),
                      child: Text(
                        'Question ${_questionIndex + 1} of ${_mcqs.length}',
                        style: theme.textTheme.labelMedium?.copyWith(
                          color: colorScheme.onPrimaryContainer,
                          fontWeight: FontWeight.bold,
                        ),
                      ),
                    ),
                    Text(
                      'Score: $_score',
                      style: theme.textTheme.labelMedium?.copyWith(
                        color: colorScheme.onSurfaceVariant,
                        fontWeight: FontWeight.w600,
                      ),
                    ),
                  ],
                ),
                const SizedBox(height: 16),

                // Question Box
                Container(
                  padding: const EdgeInsets.all(18),
                  decoration: BoxDecoration(
                    color: colorScheme.surfaceVariant.withOpacity(0.4),
                    borderRadius: BorderRadius.circular(16),
                    border: Border.all(
                      color: colorScheme.outlineVariant,
                    ),
                  ),
                  child: MarkdownContent(
                    data: currentMcq.question,
                    style: theme.textTheme.titleMedium?.copyWith(
                      fontWeight: FontWeight.bold,
                      height: 1.4,
                    ),
                  ),
                ),
                const SizedBox(height: 18),

                if (currentMcq.options.length >= 4) ...[
                  Align(
                    alignment: Alignment.centerLeft,
                    child: OutlinedButton.icon(
                      onPressed: _submittedCurrent ||
                              _hiddenOptions.containsKey(_questionIndex)
                          ? null
                          : _useFiftyFifty,
                      icon: const Icon(Icons.auto_awesome_rounded),
                      label: Text(_hiddenOptions.containsKey(_questionIndex)
                          ? '50–50 used'
                          : '50–50 lifeline'),
                    ),
                  ),
                  if (_hiddenOptions.containsKey(_questionIndex))
                    Semantics(
                        liveRegion: true,
                        child: const Text('Two incorrect options removed.')),
                  const SizedBox(height: 12),
                ],

                // Options List
                ...currentMcq.options
                    .asMap()
                    .entries
                    .where((entry) =>
                        !(_hiddenOptions[_questionIndex]?.contains(entry.key) ??
                            false))
                    .map((entry) {
                  final optIdx = entry.key;
                  final optText = entry.value;
                  final isSelected = selectedOption == optIdx;
                  final isCorrect = optIdx == currentMcq.correctIndex;

                  Color? cardBg;
                  BorderSide? border;
                  Widget? statusIcon;

                  if (_submittedCurrent) {
                    if (isCorrect) {
                      cardBg = colorScheme.primaryContainer.withOpacity(0.5);
                      border = BorderSide(color: colorScheme.primary, width: 2);
                      statusIcon = Icon(
                        Icons.check_circle_rounded,
                        color: colorScheme.primary,
                        size: 22,
                      );
                    } else if (isSelected) {
                      cardBg = colorScheme.errorContainer.withOpacity(0.5);
                      border = BorderSide(color: colorScheme.error, width: 2);
                      statusIcon = Icon(
                        Icons.cancel_rounded,
                        color: colorScheme.error,
                        size: 22,
                      );
                    }
                  } else if (isSelected) {
                    cardBg = colorScheme.primaryContainer.withOpacity(0.3);
                    border = BorderSide(color: colorScheme.primary, width: 1.5);
                  }

                  return Padding(
                    padding: const EdgeInsets.only(bottom: 12.0),
                    child: AccessibleCard(
                      selected: isSelected,
                      color: cardBg,
                      border: border,
                      semanticLabel:
                          'Option ${optionLetters[optIdx]}: $optText ${isSelected ? "Selected" : ""} ${_submittedCurrent ? (isCorrect ? "Correct answer" : isSelected ? "Incorrect answer" : "") : ""}',
                      onTap: _submittedCurrent
                          ? null
                          : () => _selectOption(optIdx),
                      child: Row(
                        children: [
                          Container(
                            width: 38,
                            height: 38,
                            decoration: BoxDecoration(
                              color: isSelected
                                  ? colorScheme.primary
                                  : colorScheme.surfaceVariant,
                              borderRadius: BorderRadius.circular(8),
                            ),
                            child: Center(
                              child: Text(
                                optionLetters[optIdx],
                                style: theme.textTheme.titleSmall?.copyWith(
                                  color: isSelected
                                      ? colorScheme.onPrimary
                                      : colorScheme.onSurfaceVariant,
                                  fontWeight: FontWeight.bold,
                                ),
                              ),
                            ),
                          ),
                          const SizedBox(width: 14),
                          Expanded(
                            child: IgnorePointer(
                                child: MarkdownContent(
                              data: optText,
                              style: theme.textTheme.bodyLarge?.copyWith(
                                fontWeight: isSelected
                                    ? FontWeight.bold
                                    : FontWeight.normal,
                              ),
                            )),
                          ),
                          if (statusIcon != null) ...[
                            const SizedBox(width: 8),
                            statusIcon,
                          ],
                        ],
                      ),
                    ),
                  );
                }),

                if (_submittedCurrent)
                  Semantics(
                      liveRegion: true,
                      child: Padding(
                          padding: const EdgeInsets.symmetric(vertical: 12),
                          child: Text(
                              selectedOption == currentMcq.correctIndex
                                  ? 'Correct answer'
                                  : 'Not quite. The correct answer is ${optionLetters[currentMcq.correctIndex]}.',
                              style: theme.textTheme.titleSmall))),
                // Explanation Box (if submitted)
                if (_submittedCurrent && currentMcq.explanation != null) ...[
                  const SizedBox(height: 12),
                  Container(
                    padding: const EdgeInsets.all(16),
                    decoration: BoxDecoration(
                      color: colorScheme.secondaryContainer.withOpacity(0.4),
                      borderRadius: BorderRadius.circular(12),
                      border: Border.all(
                        color: colorScheme.secondary.withOpacity(0.3),
                      ),
                    ),
                    child: Row(
                      crossAxisAlignment: CrossAxisAlignment.start,
                      children: [
                        Icon(
                          Icons.info_outline_rounded,
                          color: colorScheme.secondary,
                          size: 22,
                        ),
                        const SizedBox(width: 10),
                        Expanded(
                          child: Column(
                            crossAxisAlignment: CrossAxisAlignment.start,
                            children: [
                              Text(
                                'Explanation',
                                style: theme.textTheme.labelMedium?.copyWith(
                                  fontWeight: FontWeight.bold,
                                  color: colorScheme.secondary,
                                ),
                              ),
                              const SizedBox(height: 4),
                              MarkdownContent(
                                data: currentMcq.explanation!,
                                style: theme.textTheme.bodyMedium?.copyWith(
                                  color: colorScheme.onSecondaryContainer,
                                ),
                              ),
                            ],
                          ),
                        ),
                      ],
                    ),
                  ),
                ],

                const SizedBox(height: 20),
              ],
            ),
          ),

          // Bottom Action Bar
          Container(
            padding: const EdgeInsets.symmetric(horizontal: 16, vertical: 12),
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
                  if (_questionIndex > 0)
                    OutlinedButton(
                      onPressed: _previousQuestion,
                      child: const Text('Previous'),
                    ),
                  if (_questionIndex > 0) const SizedBox(width: 10),
                  if (!_submittedCurrent)
                    TextButton(
                        onPressed: _skipQuestion, child: const Text('Skip')),
                  Expanded(
                    child: !_submittedCurrent
                        ? FilledButton(
                            onPressed: selectedOption != null
                                ? _checkCurrentAnswer
                                : null,
                            child: const Text('Check answer'),
                          )
                        : FilledButton(
                            onPressed: _nextQuestion,
                            child: Text(
                              _questionIndex < _mcqs.length - 1
                                  ? 'Next question'
                                  : 'View results',
                            ),
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

  Widget _buildResultScreen(BuildContext context) {
    final theme = Theme.of(context);
    final colorScheme = theme.colorScheme;
    final percentage = (_score / _mcqs.length) * 100;
    final isPassed = percentage >= 60;

    return Scaffold(
      appBar: AppBar(
        toolbarHeight: (MediaQuery.textScalerOf(context).scale(
                    Theme.of(context).textTheme.titleMedium?.fontSize ?? 18) *
                2.8)
            .clamp(56.0, 160.0),
        title: const Text('Practice results'),
        automaticallyImplyLeading: false,
      ),
      body: Center(
        child: SingleChildScrollView(
          padding: const EdgeInsets.all(24.0),
          child: Column(
            mainAxisAlignment: MainAxisAlignment.center,
            children: [
              Container(
                width: 90,
                height: 90,
                decoration: BoxDecoration(
                  color: isPassed
                      ? colorScheme.primaryContainer
                      : colorScheme.errorContainer,
                  shape: BoxShape.circle,
                ),
                child: Icon(
                  isPassed ? Icons.emoji_events_rounded : Icons.replay_rounded,
                  size: 50,
                  color: isPassed ? colorScheme.primary : colorScheme.error,
                ),
              ),
              const SizedBox(height: 20),
              Text(
                isPassed ? 'शानदार प्रदर्शन!' : 'अभ्यास जारी रखें!',
                style: theme.textTheme.headlineSmall?.copyWith(
                  fontWeight: FontWeight.bold,
                ),
              ),
              const SizedBox(height: 8),
              Text(
                '${widget.chapter.title} अभ्यास पूर्ण',
                style: theme.textTheme.bodyMedium?.copyWith(
                  color: colorScheme.onSurfaceVariant,
                ),
                textAlign: TextAlign.center,
              ),
              const SizedBox(height: 24),

              // Score Card
              Container(
                padding: const EdgeInsets.all(20),
                decoration: BoxDecoration(
                  color: colorScheme.surfaceVariant.withOpacity(0.5),
                  borderRadius: BorderRadius.circular(16),
                  border: Border.all(
                    color: colorScheme.outlineVariant,
                  ),
                ),
                child: Wrap(
                  spacing: 24,
                  runSpacing: 16,
                  alignment: WrapAlignment.center,
                  children: [
                    Column(
                      children: [
                        Text(
                          'Questions',
                          style: theme.textTheme.bodySmall?.copyWith(
                            color: colorScheme.onSurfaceVariant,
                          ),
                        ),
                        const SizedBox(height: 4),
                        Text(
                          '${_mcqs.length}',
                          style: theme.textTheme.titleLarge?.copyWith(
                            fontWeight: FontWeight.bold,
                          ),
                        ),
                      ],
                    ),
                    Container(
                      width: 1,
                      height: 40,
                      color: colorScheme.outlineVariant,
                    ),
                    Column(
                      children: [
                        Text(
                          'Correct answers',
                          style: theme.textTheme.bodySmall?.copyWith(
                            color: colorScheme.onSurfaceVariant,
                          ),
                        ),
                        const SizedBox(height: 4),
                        Text(
                          '$_score',
                          style: theme.textTheme.titleLarge?.copyWith(
                            fontWeight: FontWeight.bold,
                            color: colorScheme.primary,
                          ),
                        ),
                      ],
                    ),
                    Container(
                      width: 1,
                      height: 40,
                      color: colorScheme.outlineVariant,
                    ),
                    Column(
                      children: [
                        Text(
                          'Score',
                          style: theme.textTheme.bodySmall?.copyWith(
                            color: colorScheme.onSurfaceVariant,
                          ),
                        ),
                        const SizedBox(height: 4),
                        Text(
                          '${percentage.toStringAsFixed(0)}%',
                          style: theme.textTheme.titleLarge?.copyWith(
                            fontWeight: FontWeight.bold,
                            color: isPassed
                                ? colorScheme.primary
                                : colorScheme.error,
                          ),
                        ),
                      ],
                    ),
                  ],
                ),
              ),
              const SizedBox(height: 32),

              Text('${_mcqs.length - _checked.length} skipped / unanswered'),
              if (_checked.length < _mcqs.length)
                ExpansionTile(
                  title: const Text('Review skipped questions'),
                  children: [
                    for (var i = 0; i < _mcqs.length; i++)
                      if (!_checked.contains(i))
                        Padding(
                            padding: const EdgeInsets.all(16),
                            child: Column(
                                crossAxisAlignment: CrossAxisAlignment.start,
                                children: [
                                  MarkdownContent(data: _mcqs[i].question),
                                  MarkdownContent(
                                      data:
                                          'Correct answer: ${_mcqs[i].options[_mcqs[i].correctIndex]}'),
                                  if (_mcqs[i].explanation != null)
                                    MarkdownContent(
                                        data: _mcqs[i].explanation!),
                                ])),
                  ],
                ),

              Text(_savingResult
                  ? 'Saving progress…'
                  : _resultSaved
                      ? 'Progress saved'
                      : 'Progress not saved'),
              if (!_resultSaved && !_savingResult)
                TextButton(
                    onPressed: _finishQuiz, child: const Text('Retry saving')),
              if (_checked
                  .any((i) => _selectedAnswers[i] != _mcqs[i].correctIndex))
                ExpansionTile(
                    title: const Text('Review incorrect answers'),
                    children: [
                      ..._checked
                          .where((i) =>
                              _selectedAnswers[i] != _mcqs[i].correctIndex)
                          .map((i) => Padding(
                              padding: const EdgeInsets.all(16),
                              child: Column(
                                  crossAxisAlignment: CrossAxisAlignment.start,
                                  children: [
                                    MarkdownContent(data: _mcqs[i].question),
                                    const SizedBox(height: 8),
                                    MarkdownContent(
                                        data:
                                            'Correct answer: ${_mcqs[i].options[_mcqs[i].correctIndex]}'),
                                    if (_mcqs[i].explanation != null)
                                      MarkdownContent(
                                          data: _mcqs[i].explanation!),
                                  ]))),
                    ]),
              // Actions
              SizedBox(
                width: double.infinity,
                child: FilledButton.icon(
                  icon: const Icon(Icons.arrow_back_rounded),
                  label: const Text('Back to chapter'),
                  onPressed: () => Navigator.pop(context),
                ),
              ),
              const SizedBox(height: 12),
              SizedBox(
                width: double.infinity,
                child: OutlinedButton.icon(
                  icon: const Icon(Icons.refresh_rounded),
                  label: const Text('Try again'),
                  onPressed: _savingResult || !_resultSaved ? null : _resetQuiz,
                ),
              ),
            ],
          ),
        ),
      ),
    );
  }
}
