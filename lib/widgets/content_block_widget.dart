import 'package:flutter/material.dart';
import '../models/chapter.dart';
import 'markdown_content.dart';
import 'educational_image.dart';

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
          child: MarkdownContent(
            data: block.value,
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
                child: MarkdownContent(
                  data: block.value,
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
              MarkdownContent(
                data: RegExp(r'\\[a-zA-Z]').hasMatch(block.value) &&
                        !block.value.contains(r'$')
                    ? r'$' + block.value + r'$'
                    : block.value,
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
        return EducationalImage(
          asset: 'assets/images/${block.value}',
          caption: block.caption,
        );

      case 'text':
      default:
        return MarkdownContent(data: block.value);
    }
  }
}
