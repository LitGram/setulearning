import 'package:flutter/material.dart';
import 'package:provider/provider.dart';
import '../providers/progress_provider.dart';

class ProgressStatePanel extends StatelessWidget {
  const ProgressStatePanel({super.key});

  @override
  Widget build(BuildContext context) {
    final progress = context.watch<ProgressProvider>();
    if (progress.isLoading) {
      return const Padding(
        padding: EdgeInsets.all(16),
        child: LinearProgressIndicator(semanticsLabel: 'Loading progress'),
      );
    }
    if (progress.loadError == null) return const SizedBox.shrink();
    return Card(
      child: Padding(
        padding: const EdgeInsets.all(16),
        child: Column(crossAxisAlignment: CrossAxisAlignment.start, children: [
          const Text(
              'Saved progress could not be loaded. You can keep reading.'),
          TextButton(
              onPressed: progress.loadProgress, child: const Text('Retry')),
        ]),
      ),
    );
  }
}
