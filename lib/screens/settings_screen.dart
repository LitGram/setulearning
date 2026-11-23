import 'package:flutter/material.dart';
import 'package:provider/provider.dart';
import '../providers/theme_provider.dart';
import '../widgets/accessible_card.dart';
import '../widgets/reset_progress_button.dart';

class SettingsScreen extends StatelessWidget {
  const SettingsScreen({super.key});

  @override
  Widget build(BuildContext context) {
    final theme = Theme.of(context);
    final colorScheme = theme.colorScheme;
    final themeProvider = Provider.of<ThemeProvider>(context);

    return Scaffold(
      appBar: AppBar(
        toolbarHeight: (MediaQuery.textScalerOf(context).scale(
                    Theme.of(context).textTheme.titleMedium?.fontSize ?? 18) *
                2.8)
            .clamp(56.0, 160.0),
        title: const Text('Settings'),
      ),
      body: ListView(
        padding: const EdgeInsets.symmetric(horizontal: 16.0, vertical: 16.0),
        children: [
          // Accessibility & Text Sizing Section (Section 6.4)
          Padding(
            padding: const EdgeInsets.symmetric(horizontal: 4.0, vertical: 4.0),
            child: Text(
              'Reading',
              style: theme.textTheme.titleMedium?.copyWith(
                fontWeight: FontWeight.bold,
              ),
            ),
          ),
          const SizedBox(height: 8),

          AccessibleCard(
            child: Column(
              crossAxisAlignment: CrossAxisAlignment.start,
              children: [
                Row(
                  mainAxisAlignment: MainAxisAlignment.spaceBetween,
                  children: [
                    Expanded(
                        child: Text(
                      'Text size',
                      style: theme.textTheme.titleSmall?.copyWith(
                        fontWeight: FontWeight.bold,
                      ),
                    )),
                    Text(
                      '${(themeProvider.fontScale * 100).toInt()}%',
                      style: theme.textTheme.labelMedium?.copyWith(
                        color: colorScheme.primary,
                        fontWeight: FontWeight.bold,
                      ),
                    ),
                  ],
                ),
                const SizedBox(height: 8),
                Slider(
                  value: themeProvider.fontScale,
                  min: 0.85,
                  max: 1.4,
                  divisions: 11,
                  label: '${(themeProvider.fontScale * 100).toInt()}%',
                  onChanged: (newScale) {
                    themeProvider.setFontScale(newScale);
                  },
                ),
                const SizedBox(height: 8),
                // Text Preview Box
                Container(
                  padding: const EdgeInsets.all(12),
                  decoration: BoxDecoration(
                    color: colorScheme.surfaceVariant.withOpacity(0.5),
                    borderRadius: BorderRadius.circular(8),
                  ),
                  child: Text(
                    'पूर्वावलोकन: सेतु श्रृंखला से अपनी परीक्षा तैयारी को सहज और प्रभावी बनाएं।',
                    style: theme.textTheme.bodyMedium,
                  ),
                ),
              ],
            ),
          ),
          const SizedBox(height: 20),

          // Theme Settings
          Padding(
            padding: const EdgeInsets.symmetric(horizontal: 4.0, vertical: 4.0),
            child: Text(
              'Appearance',
              style: theme.textTheme.titleMedium?.copyWith(
                fontWeight: FontWeight.bold,
              ),
            ),
          ),
          const SizedBox(height: 8),

          AccessibleCard(
            child: Column(
              children: [
                RadioListTile<ThemeMode>(
                  title: const Text('System default'),
                  value: ThemeMode.system,
                  groupValue: themeProvider.themeMode,
                  onChanged: (val) {
                    if (val != null) themeProvider.setThemeMode(val);
                  },
                ),
                RadioListTile<ThemeMode>(
                  title: const Text('Light mode'),
                  value: ThemeMode.light,
                  groupValue: themeProvider.themeMode,
                  onChanged: (val) {
                    if (val != null) themeProvider.setThemeMode(val);
                  },
                ),
                RadioListTile<ThemeMode>(
                  title: const Text('Dark mode'),
                  value: ThemeMode.dark,
                  groupValue: themeProvider.themeMode,
                  onChanged: (val) {
                    if (val != null) themeProvider.setThemeMode(val);
                  },
                ),
              ],
            ),
          ),
          const SizedBox(height: 20),

          // About App Section
          Padding(
            padding: const EdgeInsets.symmetric(horizontal: 4.0, vertical: 4.0),
            child: Text(
              'About Setu Learning',
              style: theme.textTheme.titleMedium?.copyWith(
                fontWeight: FontWeight.bold,
              ),
            ),
          ),
          const SizedBox(height: 8),

          AccessibleCard(
            child: Column(
              crossAxisAlignment: CrossAxisAlignment.start,
              children: [
                Row(
                  children: [
                    ClipRRect(
                      borderRadius: BorderRadius.circular(8),
                      child: Image.asset(
                        'assets/icons/app_logo.png',
                        width: 36,
                        height: 36,
                        fit: BoxFit.cover,
                        errorBuilder: (context, error, stackTrace) => Icon(
                          Icons.verified_user_rounded,
                          color: colorScheme.primary,
                          size: 28,
                        ),
                      ),
                    ),
                    const SizedBox(width: 12),
                    Expanded(
                      child: Column(
                        crossAxisAlignment: CrossAxisAlignment.start,
                        children: [
                          Text(
                            'Setu Learning App',
                            style: theme.textTheme.titleSmall?.copyWith(
                              fontWeight: FontWeight.bold,
                            ),
                          ),
                          Text(
                            'संस्करण 1.0.0 (Release Build)',
                            style: theme.textTheme.bodySmall?.copyWith(
                              color: colorScheme.onSurfaceVariant,
                            ),
                          ),
                        ],
                      ),
                    ),
                  ],
                ),
                const Divider(height: 24),
                Text(
                  'सेतु लर्निंग स्कूली, कॉलेज और प्रतियोगी परीक्षा के विद्यार्थियों के लिए विषयवार अध्ययन सामग्री उपलब्ध कराता है। MathSetu, VigyanSetu, EnglishSetu, RASSetu और अन्य विषयों की पुस्तकें ऑफ़लाइन पढ़ी जा सकती हैं।',
                  style: theme.textTheme.bodyMedium?.copyWith(height: 1.5),
                ),
                const SizedBox(height: 14),
                Row(
                  children: [
                    Icon(Icons.wifi_off_rounded,
                        size: 18, color: colorScheme.secondary),
                    const SizedBox(width: 8),
                    Flexible(
                        child: Text(
                      'Works offline',
                      style: theme.textTheme.labelSmall?.copyWith(
                        fontWeight: FontWeight.bold,
                        color: colorScheme.secondary,
                      ),
                    )),
                  ],
                ),
              ],
            ),
          ),
          const SizedBox(height: 24),
          const ResetProgressButton(),
        ],
      ),
    );
  }
}
