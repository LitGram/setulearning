import 'package:flutter/material.dart';
import '../l10n/app_strings.dart';
import 'package:provider/provider.dart';
import '../providers/progress_provider.dart';

class ProgressStatePanel extends StatelessWidget {
  const ProgressStatePanel({super.key});

  @override
  Widget build(BuildContext context) {
    final progress = context.watch<ProgressProvider>();
    if (progress.isLoading) {
      return Padding(
        padding: const EdgeInsets.all(16),
        child: LinearProgressIndicator(semanticsLabel: context.strings.loadingProgress),
      );
    }
    if (progress.loadError == null) return const SizedBox.shrink();
    return Card(
      child: Padding(
        padding: const EdgeInsets.all(16),
        child: Column(crossAxisAlignment: CrossAxisAlignment.start, children: [
          Text(
              context.strings.progressLoadFailed),
          TextButton(
              onPressed: progress.loadProgress, child: Text(context.strings.retry)),
        ]),
      ),
    );
  }
}
