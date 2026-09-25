import 'package:flutter/material.dart';
import '../models/chapter.dart';

class ContentBlockWidget extends StatelessWidget {
  final ContentBlock block;

  const ContentBlockWidget({
    super.key,
    required this.block,
  });

  @override
  Widget build(BuildContext context) {
    final theme = Theme.of(context);
    final colorScheme = theme.colorScheme;

    switch (block.type) {
      case 'heading':
        return Padding(
          padding: const EdgeInsets.only(top: 16.0, bottom: 8.0),
          child: Text(
            block.value,
            style: theme.textTheme.titleMedium?.copyWith(
              fontWeight: FontWeight.bold,
              color: colorScheme.primary,
            ),
          ),
        );

      case 'callout':
        return Container(
          margin: const EdgeInsets.symmetric(vertical: 12.0),
          padding: const EdgeInsets.all(16.0),
          decoration: BoxDecoration(
            color: colorScheme.secondaryContainer.withOpacity(0.7),
            borderRadius: BorderRadius.circular(12),
            border: Border.all(
              color: colorScheme.secondary.withOpacity(0.3),
              width: 1.5,
            ),
          ),
          child: Row(
            crossAxisAlignment: CrossAxisAlignment.start,
            children: [
              Icon(
                Icons.lightbulb_outline_rounded,
                color: colorScheme.secondary,
                size: 24,
              ),
              const SizedBox(width: 12),
              Expanded(
                child: SelectableText(
                  block.value,
                  style: theme.textTheme.bodyMedium?.copyWith(
                    color: colorScheme.onSecondaryContainer,
                    fontWeight: FontWeight.w500,
                    height: 1.5,
                  ),
                ),
              ),
            ],
          ),
        );

      case 'formula':
        return Container(
          margin: const EdgeInsets.symmetric(vertical: 12.0),
          padding: const EdgeInsets.all(14.0),
          decoration: BoxDecoration(
            color: colorScheme.surfaceVariant.withOpacity(0.5),
            borderRadius: BorderRadius.circular(12),
            border: Border.all(
              color: colorScheme.outlineVariant,
              width: 1,
            ),
          ),
          child: Column(
            crossAxisAlignment: CrossAxisAlignment.stretch,
            children: [
              SelectableText(
                block.value,
                textAlign: TextAlign.center,
                style: theme.textTheme.titleMedium?.copyWith(
                  fontWeight: FontWeight.bold,
                  letterSpacing: 0.5,
                  color: colorScheme.onSurfaceVariant,
                ),
              ),
              if (block.caption != null) ...[
                const SizedBox(height: 6),
                Text(
                  block.caption!,
                  textAlign: TextAlign.center,
                  style: theme.textTheme.bodySmall?.copyWith(
                    color: colorScheme.onSurfaceVariant.withOpacity(0.8),
                  ),
                ),
              ],
            ],
          ),
        );

      case 'image':
        return Container(
          margin: const EdgeInsets.symmetric(vertical: 16.0),
          decoration: BoxDecoration(
            borderRadius: BorderRadius.circular(16),
            border: Border.all(
              color: colorScheme.outlineVariant,
              width: 1,
            ),
          ),
          clipBehavior: Clip.antiAlias,
          child: Column(
            crossAxisAlignment: CrossAxisAlignment.stretch,
            children: [
              Image.asset(
                'assets/images/${block.value}',
                fit: BoxFit.contain,
                semanticLabel: block.caption ?? 'Educational diagram ${block.value}',
                errorBuilder: (context, error, stackTrace) {
                  return Container(
                    height: 160,
                    color: colorScheme.surfaceVariant,
                    child: Center(
                      child: Column(
                        mainAxisAlignment: MainAxisAlignment.center,
                        children: [
                          Icon(
                            Icons.image_rounded,
                            size: 44,
                            color: colorScheme.onSurfaceVariant.withOpacity(0.6),
                          ),
                          const SizedBox(height: 8),
                          Text(
                            block.caption ?? 'चित्र: ${block.value}',
                            style: theme.textTheme.bodySmall?.copyWith(
                              color: colorScheme.onSurfaceVariant,
                              fontStyle: FontStyle.italic,
                            ),
                          ),
                        ],
                      ),
                    ),
                  );
                },
              ),
              if (block.caption != null)
                Container(
                  color: colorScheme.surfaceVariant.withOpacity(0.6),
                  padding: const EdgeInsets.symmetric(horizontal: 12, vertical: 8),
                  child: Text(
                    block.caption!,
                    textAlign: TextAlign.center,
                    style: theme.textTheme.bodySmall?.copyWith(
                      color: colorScheme.onSurfaceVariant,
                      fontWeight: FontWeight.w500,
                    ),
                  ),
                ),
            ],
          ),
        );

      case 'text':
      default:
        return Padding(
          padding: const EdgeInsets.symmetric(vertical: 8.0),
          child: SelectableText(
            block.value,
            style: theme.textTheme.bodyLarge?.copyWith(
              color: colorScheme.onSurface,
              height: 1.6,
            ),
          ),
        );
    }
  }
}
