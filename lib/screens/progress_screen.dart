import 'package:flutter/material.dart';
import 'package:provider/provider.dart';
import '../providers/progress_provider.dart';
import '../services/content_service.dart';
import '../widgets/accessible_card.dart';

class ProgressScreen extends StatelessWidget {
  const ProgressScreen({super.key});

  @override
  Widget build(BuildContext context) {
    final theme = Theme.of(context);
    final colorScheme = theme.colorScheme;
    final subjects = ContentService.instance.getSubjects();

    return Scaffold(
      appBar: AppBar(
        title: const Text('अध्ययन प्रगति (My Progress)'),
      ),
      body: Consumer<ProgressProvider>(
        builder: (context, progressProvider, child) {
          int totalReadAcrossAll = 0;
          for (final s in subjects) {
            totalReadAcrossAll += progressProvider.getReadCountForSubject(s.id);
          }

          return ListView(
            padding: const EdgeInsets.symmetric(horizontal: 16.0, vertical: 16.0),
            children: [
              // Hero Progress Card
              Container(
                padding: const EdgeInsets.all(20),
                decoration: BoxDecoration(
                  gradient: LinearGradient(
                    colors: [
                      colorScheme.primary,
                      colorScheme.primary.withOpacity(0.8),
                    ],
                    begin: Alignment.topLeft,
                    end: Alignment.bottomRight,
                  ),
                  borderRadius: BorderRadius.circular(20),
                ),
                child: Row(
                  children: [
                    Container(
                      padding: const EdgeInsets.all(14),
                      decoration: BoxDecoration(
                        color: colorScheme.onPrimary.withOpacity(0.2),
                        shape: BoxShape.circle,
                      ),
                      child: Icon(
                        Icons.auto_stories_rounded,
                        color: colorScheme.onPrimary,
                        size: 36,
                      ),
                    ),
                    const SizedBox(width: 16),
                    Expanded(
                      child: Column(
                        crossAxisAlignment: CrossAxisAlignment.start,
                        children: [
                          Text(
                            'कुल पूर्ण अध्याय',
                            style: theme.textTheme.bodyMedium?.copyWith(
                              color: colorScheme.onPrimary.withOpacity(0.9),
                            ),
                          ),
                          const SizedBox(height: 4),
                          Text(
                            '$totalReadAcrossAll अध्याय',
                            style: theme.textTheme.headlineMedium?.copyWith(
                              color: colorScheme.onPrimary,
                              fontWeight: FontWeight.bold,
                            ),
                          ),
                        ],
                      ),
                    ),
                  ],
                ),
              ),
              const SizedBox(height: 24),

              Text(
                'विषयवार स्थिति (Subject Breakdown)',
                style: theme.textTheme.titleMedium?.copyWith(
                  fontWeight: FontWeight.bold,
                ),
              ),
              const SizedBox(height: 12),

              // Subject Wise Progress
              ...subjects.map((subject) {
                final readCount = progressProvider.getReadCountForSubject(subject.id);
                // Approximate 4 chapters per book x 8 books = 32 chapters
                const totalTargetChapters = 32;
                final progressFraction = (readCount / totalTargetChapters).clamp(0.0, 1.0);

                return Padding(
                  padding: const EdgeInsets.only(bottom: 12.0),
                  child: AccessibleCard(
                    semanticLabel: '${subject.name}: $readCount अध्याय पूर्ण',
                    child: Column(
                      crossAxisAlignment: CrossAxisAlignment.start,
                      children: [
                        Row(
                          children: [
                            Icon(subject.icon, color: subject.seedColor, size: 24),
                            const SizedBox(width: 10),
                            Expanded(
                              child: Text(
                                '${subject.name} (${subject.hindiName})',
                                style: theme.textTheme.titleSmall?.copyWith(
                                  fontWeight: FontWeight.bold,
                                ),
                              ),
                            ),
                            Text(
                              '$readCount / $totalTargetChapters',
                              style: theme.textTheme.labelMedium?.copyWith(
                                fontWeight: FontWeight.bold,
                                color: subject.seedColor,
                              ),
                            ),
                          ],
                        ),
                        const SizedBox(height: 10),
                        ClipRRect(
                          borderRadius: BorderRadius.circular(6),
                          child: LinearProgressIndicator(
                            value: progressFraction,
                            minHeight: 8,
                            backgroundColor: colorScheme.surfaceVariant,
                            valueColor: AlwaysStoppedAnimation<Color>(subject.seedColor),
                          ),
                        ),
                      ],
                    ),
                  ),
                );
              }),

              const SizedBox(height: 32),

              // Reset Progress Section with Confirmation Dialog (Section 6.5)
              Center(
                child: TextButton.icon(
                  icon: Icon(Icons.delete_outline_rounded, color: colorScheme.error),
                  label: Text(
                    'प्रगति रीसेट करें (Reset All Progress)',
                    style: TextStyle(color: colorScheme.error),
                  ),
                  onPressed: () => _confirmReset(context, progressProvider),
                ),
              ),
              const SizedBox(height: 20),
            ],
          );
        },
      ),
    );
  }

  void _confirmReset(BuildContext context, ProgressProvider provider) {
    showDialog(
      context: context,
      builder: (dialogCtx) {
        return AlertDialog(
          icon: const Icon(Icons.warning_amber_rounded, size: 36),
          title: const Text('प्रगति रीसेट की पुष्टि'),
          content: const Text(
            'क्या आप वास्तव में अपने सभी पठित अध्याय और क्विज स्कोर रीसेट करना चाहते हैं? यह क्रिया पूर्ववत नहीं की जा सकती।',
          ),
          actions: [
            TextButton(
              onPressed: () => Navigator.pop(dialogCtx),
              child: const Text('रद्द करें'),
            ),
            FilledButton(
              style: FilledButton.styleFrom(
                backgroundColor: Theme.of(context).colorScheme.error,
              ),
              onPressed: () async {
                Navigator.pop(dialogCtx);
                await provider.resetAllProgress();
                if (context.mounted) {
                  ScaffoldMessenger.of(context).showSnackBar(
                    const SnackBar(content: Text('समस्त प्रगति रीसेट कर दी गई है।')),
                  );
                }
              },
              child: const Text('हाँ, रीसेट करें'),
            ),
          ],
        );
      },
    );
  }
}
