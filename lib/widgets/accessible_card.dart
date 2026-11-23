import 'package:flutter/material.dart';
import '../theme/app_theme.dart';

class AccessibleCard extends StatelessWidget {
  final Widget child;
  final VoidCallback? onTap;
  final String? semanticLabel;
  final String? semanticHint;
  final bool? selected;
  final EdgeInsetsGeometry padding;
  final Color? color;
  final BorderSide? border;

  const AccessibleCard({
    super.key,
    required this.child,
    this.onTap,
    this.semanticLabel,
    this.semanticHint,
    this.selected,
    this.padding = const EdgeInsets.all(AppSpacing.medium),
    this.color,
    this.border,
  });

  @override
  Widget build(BuildContext context) {
    final theme = Theme.of(context);
    final cardContent = ConstrainedBox(
      constraints: const BoxConstraints(
        minWidth: 48,
        minHeight: 48, // Section 6.4: >= 48x48 tap target
      ),
      child: Padding(
        padding: padding,
        child: child,
      ),
    );

    return Semantics(
      label: semanticLabel,
      selected: selected,
      hint: semanticHint,
      button: onTap != null,
      enabled: onTap != null,
      child: Card(
        color: color ?? theme.cardTheme.color,
        shape: RoundedRectangleBorder(
          borderRadius: BorderRadius.circular(16),
          side: border ??
              BorderSide(
                color: theme.colorScheme.outlineVariant.withOpacity(0.5),
                width: 1,
              ),
        ),
        child: onTap != null
            ? InkWell(
                onTap: onTap,
                borderRadius: BorderRadius.circular(16),
                splashColor: theme.colorScheme.primary.withOpacity(0.12),
                highlightColor: theme.colorScheme.primary.withOpacity(0.06),
                child: cardContent,
              )
            : cardContent,
      ),
    );
  }
}
