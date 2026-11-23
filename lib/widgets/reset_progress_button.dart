import 'package:flutter/material.dart';
import '../l10n/app_strings.dart';
import 'package:provider/provider.dart';
import '../providers/progress_provider.dart';

class ResetProgressButton extends StatelessWidget {
  const ResetProgressButton({super.key});
  @override
  Widget build(BuildContext context) => ListTile(
        leading: Icon(Icons.delete_outline,
            color: Theme.of(context).colorScheme.error),
        title: Text(context.strings.resetAllProgress),
        subtitle: Text(
            context.strings.resetAllProgressSubtitle),
        onTap: () async {
          final confirmed = await showDialog<bool>(
              context: context,
              builder: (context) => AlertDialog(
                    title: Text(context.strings.resetConfirmTitle),
                    content: Text(
                        context.strings.resetConfirmBody),
                    actions: [
                      TextButton(
                          onPressed: () => Navigator.pop(context, false),
                          child: Text(context.strings.cancel)),
                      FilledButton(
                          onPressed: () => Navigator.pop(context, true),
                          child: Text(context.strings.reset))
                    ],
                  ));
          if (confirmed != true || !context.mounted) return;
          try {
            await context.read<ProgressProvider>().resetAllProgress();
            if (context.mounted) {
              ScaffoldMessenger.of(context).showSnackBar(
                  SnackBar(content: Text(context.strings.progressReset)));
            }
          } catch (_) {
            if (context.mounted) {
              ScaffoldMessenger.of(context).showSnackBar(SnackBar(
                  content: Text(context.strings.couldNotReset)));
            }
          }
        },
      );
}
