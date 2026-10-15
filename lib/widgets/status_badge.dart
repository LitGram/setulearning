import 'package:flutter/material.dart';

enum BadgeType {
  completed,
  inProgress,
  notStarted,
  quizPassed,
  quizNeedsReview
}

class StatusBadge extends StatelessWidget {
  final BadgeType type;
  final String? customLabel;

  const StatusBadge({
    super.key,
    required this.type,
    this.customLabel,
  });

  @override
  Widget build(BuildContext context) {
    final theme = Theme.of(context);
    final colorScheme = theme.colorScheme;

    IconData icon;
    String label;
    Color bgColor;
    Color fgColor;
    BorderSide border;

    switch (type) {
      case BadgeType.completed:
        icon = Icons.check_circle_rounded;
        label = customLabel ?? 'Completed';
        bgColor = colorScheme.primaryContainer;
        fgColor = colorScheme.onPrimaryContainer;
        border = BorderSide(color: colorScheme.primary.withOpacity(0.3));
        break;
      case BadgeType.quizPassed:
        icon = Icons.emoji_events_rounded;
        label = customLabel ?? 'Practice completed';
        bgColor = colorScheme.secondaryContainer;
        fgColor = colorScheme.onSecondaryContainer;
        border = BorderSide(color: colorScheme.secondary.withOpacity(0.3));
        break;
      case BadgeType.quizNeedsReview:
        icon = Icons.replay_rounded;
        label = customLabel ?? 'Retry';
        bgColor = colorScheme.tertiaryContainer;
        fgColor = colorScheme.onTertiaryContainer;
        border = BorderSide(color: colorScheme.tertiary.withOpacity(0.3));
        break;
      case BadgeType.inProgress:
        icon = Icons.timelapse_rounded;
        label = customLabel ?? 'In progress';
        bgColor = colorScheme.surfaceVariant;
        fgColor = colorScheme.onSurfaceVariant;
        border = BorderSide(color: colorScheme.outlineVariant);
        break;
      case BadgeType.notStarted:
        icon = Icons.circle_outlined;
        label = customLabel ?? 'Unread';
        bgColor = colorScheme.surface;
        fgColor = colorScheme.onSurfaceVariant;
        border = BorderSide(color: colorScheme.outline.withOpacity(0.4));
        break;
    }

    return Semantics(
      label: 'Status: $label',
      excludeSemantics: true,
      child: Container(
        padding: const EdgeInsets.symmetric(horizontal: 10, vertical: 5),
        decoration: BoxDecoration(
          color: bgColor,
          borderRadius: BorderRadius.circular(20),
          border: Border.fromBorderSide(border),
        ),
        child: Row(
          mainAxisSize: MainAxisSize.min,
          children: [
            Icon(icon, size: 16, color: fgColor),
            const SizedBox(width: 6),
            Flexible(
                child: Text(
              label,
              style: theme.textTheme.labelMedium?.copyWith(
                color: fgColor,
                fontWeight: FontWeight.bold,
              ),
            )),
          ],
        ),
      ),
    );
  }
}
