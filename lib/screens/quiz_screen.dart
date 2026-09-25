import 'package:flutter/material.dart';
import 'package:provider/provider.dart';
import '../models/book.dart';
import '../models/chapter.dart';
import '../models/mcq.dart';
import '../models/subject.dart';
import '../providers/progress_provider.dart';
import '../widgets/accessible_card.dart';

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
  final Map<int, int> _selectedAnswers = {}; // questionIndex -> selectedOptionIndex
  bool _submittedCurrent = false;
  int _score = 0;
  bool _isQuizComplete = false;

  List<MCQ> get _mcqs => widget.chapter.mcqs;

  void _selectOption(int optionIndex) {
    if (_submittedCurrent) return;
    setState(() {
      _selectedAnswers[_questionIndex] = optionIndex;
    });
  }

  void _checkCurrentAnswer() {
    if (_selectedAnswers[_questionIndex] == null) return;

    final selected = _selectedAnswers[_questionIndex]!;
    final correct = _mcqs[_questionIndex].correctIndex;

    setState(() {
      _submittedCurrent = true;
      if (selected == correct) {
        _score++;
      }
    });
  }

  void _nextQuestion() {
    if (_questionIndex < _mcqs.length - 1) {
      setState(() {
        _questionIndex++;
        _submittedCurrent = _selectedAnswers.containsKey(_questionIndex);
      });
    } else {
      _finishQuiz();
    }
  }

  void _previousQuestion() {
    if (_questionIndex > 0) {
      setState(() {
        _questionIndex--;
        _submittedCurrent = _selectedAnswers.containsKey(_questionIndex);
      });
    }
  }

  Future<void> _finishQuiz() async {
    setState(() {
      _isQuizComplete = true;
    });

    final progress = Provider.of<ProgressProvider>(context, listen: false);
    await progress.recordQuizScore(
      subjectId: widget.subject.id,
      bookId: widget.book.id,
      chapterId: widget.chapter.id,
      score: _score,
      total: _mcqs.length,
    );
  }

  void _resetQuiz() {
    setState(() {
      _questionIndex = 0;
      _selectedAnswers.clear();
      _submittedCurrent = false;
      _score = 0;
      _isQuizComplete = false;
    });
  }

  @override
  Widget build(BuildContext context) {
    final theme = Theme.of(context);
    final colorScheme = theme.colorScheme;

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
                child: const Text('वापस जाएं'),
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
        title: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            Text(
              'अभ्यास प्रश्नोत्तरी',
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
          // Linear progress bar
          LinearProgressIndicator(
            value: (_questionIndex + 1) / _mcqs.length,
            backgroundColor: colorScheme.surfaceVariant,
          ),

          Expanded(
            child: ListView(
              padding: const EdgeInsets.symmetric(horizontal: 16.0, vertical: 16.0),
              children: [
                // Question Header
                Row(
                  mainAxisAlignment: MainAxisAlignment.spaceBetween,
                  children: [
                    Container(
                      padding: const EdgeInsets.symmetric(horizontal: 12, vertical: 6),
                      decoration: BoxDecoration(
                        color: colorScheme.primaryContainer,
                        borderRadius: BorderRadius.circular(10),
                      ),
                      child: Text(
                        'प्रश्न ${_questionIndex + 1} / ${_mcqs.length}',
                        style: theme.textTheme.labelMedium?.copyWith(
                          color: colorScheme.onPrimaryContainer,
                          fontWeight: FontWeight.bold,
                        ),
                      ),
                    ),
                    Text(
                      'वर्तमान स्कोर: $_score',
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
                  child: Text(
                    currentMcq.question,
                    style: theme.textTheme.titleMedium?.copyWith(
                      fontWeight: FontWeight.bold,
                      height: 1.4,
                    ),
                  ),
                ),
                const SizedBox(height: 18),

                // Options List
                ...currentMcq.options.asMap().entries.map((entry) {
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
                      color: cardBg,
                      border: border,
                      semanticLabel:
                          'विकल्प ${optionLetters[optIdx]}: $optText ${isSelected ? "चयनित" : ""}',
                      onTap: () => _selectOption(optIdx),
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
                            child: Text(
                              optText,
                              style: theme.textTheme.bodyLarge?.copyWith(
                                fontWeight: isSelected
                                    ? FontWeight.bold
                                    : FontWeight.normal,
                              ),
                            ),
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
                                'स्पष्टीकरण (Explanation):',
                                style: theme.textTheme.labelMedium?.copyWith(
                                  fontWeight: FontWeight.bold,
                                  color: colorScheme.secondary,
                                ),
                              ),
                              const SizedBox(height: 4),
                              Text(
                                currentMcq.explanation!,
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
              child: Row(
                children: [
                  if (_questionIndex > 0)
                    OutlinedButton(
                      onPressed: _previousQuestion,
                      child: const Text('पिछला'),
                    ),
                  if (_questionIndex > 0) const SizedBox(width: 10),
                  Expanded(
                    child: !_submittedCurrent
                        ? FilledButton(
                            onPressed: selectedOption != null
                                ? _checkCurrentAnswer
                                : null,
                            child: const Text('जांचें (Check Answer)'),
                          )
                        : FilledButton(
                            onPressed: _nextQuestion,
                            child: Text(
                              _questionIndex < _mcqs.length - 1
                                  ? 'अगला प्रश्न'
                                  : 'परिणाम देखें (View Results)',
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
        title: const Text('प्रश्नोत्तरी परिणाम'),
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
                child: Row(
                  mainAxisAlignment: MainAxisAlignment.spaceAround,
                  children: [
                    Column(
                      children: [
                        Text(
                          'कुल प्रश्न',
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
                          'सही उत्तर',
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
                          'प्रतिशत',
                          style: theme.textTheme.bodySmall?.copyWith(
                            color: colorScheme.onSurfaceVariant,
                          ),
                        ),
                        const SizedBox(height: 4),
                        Text(
                          '${percentage.toStringAsFixed(0)}%',
                          style: theme.textTheme.titleLarge?.copyWith(
                            fontWeight: FontWeight.bold,
                            color: isPassed ? colorScheme.primary : colorScheme.error,
                          ),
                        ),
                      ],
                    ),
                  ],
                ),
              ),
              const SizedBox(height: 32),

              // Actions
              SizedBox(
                width: double.infinity,
                child: FilledButton.icon(
                  icon: const Icon(Icons.arrow_back_rounded),
                  label: const Text('अध्याय पर वापस जाएं'),
                  onPressed: () => Navigator.pop(context),
                ),
              ),
              const SizedBox(height: 12),
              SizedBox(
                width: double.infinity,
                child: OutlinedButton.icon(
                  icon: const Icon(Icons.refresh_rounded),
                  label: const Text('क्विज पुनः दें (Retake)'),
                  onPressed: _resetQuiz,
                ),
              ),
            ],
          ),
        ),
      ),
    );
  }
}
