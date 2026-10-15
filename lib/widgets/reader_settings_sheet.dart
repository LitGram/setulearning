import 'package:flutter/material.dart';
import 'package:provider/provider.dart';
import '../providers/theme_provider.dart';

void showReaderSettings(BuildContext context) {
  showModalBottomSheet<void>(
      context: context,
      isScrollControlled: true,
      showDragHandle: true,
      builder: (context) => const _ReaderSettings());
}

class _ReaderSettings extends StatelessWidget {
  const _ReaderSettings();
  @override
  Widget build(BuildContext context) {
    final settings = context.watch<ThemeProvider>();
    return SafeArea(
        child: SingleChildScrollView(
      padding: const EdgeInsets.fromLTRB(24, 0, 24, 24),
      child: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          mainAxisSize: MainAxisSize.min,
          children: [
            Text('Reading settings',
                style: Theme.of(context).textTheme.titleLarge),
            const SizedBox(height: 16),
            Text('Text size: ${(settings.fontScale * 100).round()}%'),
            Slider(
                value: settings.fontScale,
                min: .85,
                max: 1.4,
                divisions: 11,
                label: '${(settings.fontScale * 100).round()}%',
                onChanged: settings.setFontScale),
            Text('पढ़ने का आरामदायक अनुभव। A comfortable reading experience.',
                style: Theme.of(context).textTheme.bodyLarge),
            const SizedBox(height: 16),
            DropdownButtonFormField<ThemeMode>(
                initialValue: settings.themeMode,
                decoration: const InputDecoration(
                    labelText: 'Theme', border: OutlineInputBorder()),
                items: const [
                  DropdownMenuItem(
                      value: ThemeMode.system, child: Text('System')),
                  DropdownMenuItem(
                      value: ThemeMode.light, child: Text('Light')),
                  DropdownMenuItem(value: ThemeMode.dark, child: Text('Dark')),
                ],
                onChanged: (value) {
                  if (value != null) settings.setThemeMode(value);
                }),
            TextButton(
                onPressed: () => settings.setFontScale(1),
                child: const Text('Reset text size')),
          ]),
    ));
  }
}
