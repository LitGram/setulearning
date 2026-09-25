import 'package:flutter/material.dart';
import 'package:provider/provider.dart';
import '../providers/theme_provider.dart';
import '../widgets/accessible_card.dart';

class SettingsScreen extends StatelessWidget {
  const SettingsScreen({super.key});

  @override
  Widget build(BuildContext context) {
    final theme = Theme.of(context);
    final colorScheme = theme.colorScheme;
    final themeProvider = Provider.of<ThemeProvider>(context);

    return Scaffold(
      appBar: AppBar(
        title: const Text('सेटिंग्स एवं परिचय (Settings)'),
      ),
      body: ListView(
        padding: const EdgeInsets.symmetric(horizontal: 16.0, vertical: 16.0),
        children: [
          // Accessibility & Text Sizing Section (Section 6.4)
          Padding(
            padding: const EdgeInsets.symmetric(horizontal: 4.0, vertical: 4.0),
            child: Text(
              'पठन सुगमता (Accessibility & Text)',
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
                    Text(
                      'अक्षर आकार (Font Scale)',
                      style: theme.textTheme.titleSmall?.copyWith(
                        fontWeight: FontWeight.bold,
                      ),
                    ),
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
                  max: 1.35,
                  divisions: 5,
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
              'थीम (Appearance)',
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
                  title: const Text('सिस्टम डिफ़ॉल्ट (System Default)'),
                  value: ThemeMode.system,
                  groupValue: themeProvider.themeMode,
                  onChanged: (val) {
                    if (val != null) themeProvider.setThemeMode(val);
                  },
                ),
                RadioListTile<ThemeMode>(
                  title: const Text('लाइट मोड (Light Mode)'),
                  value: ThemeMode.light,
                  groupValue: themeProvider.themeMode,
                  onChanged: (val) {
                    if (val != null) themeProvider.setThemeMode(val);
                  },
                ),
                RadioListTile<ThemeMode>(
                  title: const Text('डार्क मोड (Dark Mode)'),
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
              'ऐप परिचय (About Setu Learning)',
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
                    Icon(Icons.verified_user_rounded, color: colorScheme.primary, size: 28),
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
                  'सेतु शिक्षण श्रृंखला (Setu Series) स्कूली एवं प्रतियोगी परीक्षा विद्यार्थियों के लिए पूर्णतः ऑफ़लाइन, संकल्पना-केंद्रित एवं व्यवस्थित अध्ययन सामग्री प्रदान करता है। इसमें MathSetu, EnglishSetu और VigyanSetu जैसे प्रमुख विषयों की संपूर्ण 8-8 पुस्तकें सम्मिलित हैं।',
                  style: theme.textTheme.bodyMedium?.copyWith(height: 1.5),
                ),
                const SizedBox(height: 14),
                Row(
                  children: [
                    Icon(Icons.wifi_off_rounded, size: 18, color: colorScheme.secondary),
                    const SizedBox(width: 8),
                    Text(
                      '100% Offline-First (इंटरनेट की आवश्यकता नहीं)',
                      style: theme.textTheme.labelSmall?.copyWith(
                        fontWeight: FontWeight.bold,
                        color: colorScheme.secondary,
                      ),
                    ),
                  ],
                ),
              ],
            ),
          ),
          const SizedBox(height: 24),
        ],
      ),
    );
  }
}
