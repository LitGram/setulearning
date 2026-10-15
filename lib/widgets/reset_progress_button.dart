import 'package:flutter/material.dart';
import 'package:provider/provider.dart';
import '../providers/progress_provider.dart';

class ResetProgressButton extends StatelessWidget {
  const ResetProgressButton({super.key});
  @override
  Widget build(BuildContext context) => ListTile(
        leading: Icon(Icons.delete_outline,
            color: Theme.of(context).colorScheme.error),
        title: const Text('Reset all progress'),
        subtitle: const Text(
            'Clear reading history, quiz scores, and unfinished attempts'),
        onTap: () async {
          final confirmed = await showDialog<bool>(
              context: context,
              builder: (context) => AlertDialog(
                    title: const Text('Reset all progress?'),
                    content: const Text(
                        'This removes your saved reading progress and practice scores. This cannot be undone.'),
                    actions: [
                      TextButton(
                          onPressed: () => Navigator.pop(context, false),
                          child: const Text('Cancel')),
                      FilledButton(
                          onPressed: () => Navigator.pop(context, true),
                          child: const Text('Reset'))
                    ],
                  ));
          if (confirmed != true || !context.mounted) return;
          try {
            await context.read<ProgressProvider>().resetAllProgress();
            if (context.mounted) {
              ScaffoldMessenger.of(context).showSnackBar(
                  const SnackBar(content: Text('Progress reset')));
            }
          } catch (_) {
            if (context.mounted) {
              ScaffoldMessenger.of(context).showSnackBar(const SnackBar(
                  content: Text('Could not reset progress. Try again.')));
            }
          }
        },
      );
}
