import 'package:flutter/material.dart';
import 'package:provider/provider.dart';
import '../providers/progress_provider.dart';
import '../services/content_service.dart';
import '../widgets/accessible_card.dart';
import '../widgets/progress_state_panel.dart';
import 'subject_screen.dart';

class ProgressScreen extends StatelessWidget {
  const ProgressScreen({super.key});

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
        title: const Text('My progress'),
      ),
      body: Consumer<ProgressProvider>(
        builder: (context, progressProvider, child) {
          int totalReadAcrossAll = 0;
          for (final s in subjects) {
            totalReadAcrossAll += progressProvider.getReadCountForSubject(s.id);
          }

          return ListView(
            padding:
                const EdgeInsets.symmetric(horizontal: 16.0, vertical: 16.0),
            children: [
              const ProgressStatePanel(),
              if (totalReadAcrossAll == 0)
                const Padding(
                    padding: EdgeInsets.all(16),
                    child: Text(
                        'अपना पहला अध्याय पढ़ें और अंत में “पढ़ लिया” चुनें। अभ्यास स्कोर अलग सहेजे जाते हैं।')),
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
                'By subject',
                style: theme.textTheme.titleMedium?.copyWith(
                  fontWeight: FontWeight.bold,
                ),
              ),
              const SizedBox(height: 12),

              // Subject Wise Progress
              ...subjects.map((subject) {
                final subjectColor = ColorScheme.fromSeed(
                        seedColor: subject.seedColor,
                        brightness: theme.brightness)
                    .primary;
                final readCount =
                    progressProvider.getReadCountForSubject(subject.id);
                final totalTargetChapters = ContentService.instance
                    .getTotalChaptersForSubject(subject.id);
                final progressFraction = totalTargetChapters > 0
                    ? (readCount / totalTargetChapters).clamp(0.0, 1.0)
                    : 0.0;

                return Padding(
                  padding: const EdgeInsets.only(bottom: 12.0),
                  child: AccessibleCard(
                    semanticLabel: '${subject.name}: $readCount अध्याय पूर्ण',
                    onTap: () => Navigator.push(
                        context,
                        MaterialPageRoute(
                            builder: (_) => SubjectScreen(subject: subject))),
                    child: Column(
                      crossAxisAlignment: CrossAxisAlignment.start,
                      children: [
                        Row(
                          children: [
                            Icon(subject.icon, color: subjectColor, size: 24),
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
                                color: subjectColor,
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
                            valueColor: AlwaysStoppedAnimation<Color>(
                                subject.seedColor),
                          ),
                        ),
                      ],
                    ),
                  ),
                );
              }),

              const SizedBox(height: 32),

              const SizedBox(height: 20),
            ],
          );
        },
      ),
    );
  }
}
