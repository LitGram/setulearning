import 'package:flutter/material.dart';
import '../l10n/app_strings.dart';
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
            Text(context.strings.readingSettings,
                style: Theme.of(context).textTheme.titleLarge),
            const SizedBox(height: 16),
            Text(context.strings.textSizePercent((settings.fontScale * 100).round())),
            Slider(
                value: settings.fontScale,
                min: .85,
                max: 1.4,
                divisions: 11,
                label: '${(settings.fontScale * 100).round()}%',
                onChanged: settings.setFontScale),
            Text(context.strings.comfortableReading,
                style: Theme.of(context).textTheme.bodyLarge),
            const SizedBox(height: 16),
            DropdownButtonFormField<ThemeMode>(
                initialValue: settings.themeMode,
                decoration: InputDecoration(
                    labelText: context.strings.theme, border: const OutlineInputBorder()),
                items: [
                  DropdownMenuItem(
                      value: ThemeMode.system, child: Text(context.strings.system)),
                  DropdownMenuItem(
                      value: ThemeMode.light, child: Text(context.strings.light)),
                  DropdownMenuItem(value: ThemeMode.dark, child: Text(context.strings.dark)),
                ],
                onChanged: (value) {
                  if (value != null) settings.setThemeMode(value);
                }),
            TextButton(
                onPressed: () => settings.setFontScale(1),
                child: Text(context.strings.resetTextSize)),
          ]),
    ));
  }
}
