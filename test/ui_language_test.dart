import 'package:flutter/material.dart';
import 'package:flutter_test/flutter_test.dart';
import 'package:provider/provider.dart';
import 'package:setu_learning/l10n/app_strings.dart';
import 'package:setu_learning/main.dart';
import 'package:setu_learning/models/shelf.dart';
import 'package:setu_learning/providers/language_provider.dart';
import 'package:setu_learning/providers/progress_provider.dart';
import 'package:setu_learning/providers/theme_provider.dart';
import 'package:shared_preferences/shared_preferences.dart';

class _TestProgress extends ProgressProvider {
  @override
  bool get isLoading => false;
  @override
  Future<void> loadProgress() async {}
}

Future<void> _pumpApp(WidgetTester tester) async {
  final prefs = await SharedPreferences.getInstance();
  await tester.pumpWidget(MultiProvider(
    providers: [
      ChangeNotifierProvider(create: (_) => ThemeProvider(prefs)),
      ChangeNotifierProvider<ProgressProvider>(create: (_) => _TestProgress()),
      ChangeNotifierProvider(create: (_) => LanguageProvider(prefs)),
    ],
    child: const SetuLearningApp(),
  ));
  await tester.pumpAndSettle();
}

void main() {
  test('Hindi and English strings are both filled in and differ', () {
    // Spot-check the buttons the roadmap called out.
    const hi = AppStrings.hindi;
    const en = AppStrings.english;
    expect(en.previous, 'Previous');
    expect(en.next, 'Next');
    expect(en.markAsRead, 'Mark as read');
    expect(hi.previous, isNot(en.previous));
    expect(hi.next, isNot(en.next));
    expect(hi.markAsRead, isNot(en.markAsRead));
    for (final shelf in Shelf.values) {
      expect(shelf.labelIn(AppLanguage.en), isNotEmpty);
      expect(shelf.descriptionIn(AppLanguage.en), isNotEmpty);
    }
  });

  testWidgets('app opens in Hindi by default', (tester) async {
    SharedPreferences.setMockInitialValues({'home_shelf': 'class10'});
    await _pumpApp(tester);
    expect(find.text(AppStrings.hindi.navSubjects), findsWidgets);
    expect(find.text(AppStrings.hindi.searchBooksAndChapters), findsOneWidget);
    expect(find.text('Search books and chapters'), findsNothing);
  });

  testWidgets('switching to English in Settings changes the UI and is saved',
      (tester) async {
    SharedPreferences.setMockInitialValues({'home_shelf': 'class10'});
    await _pumpApp(tester);

    await tester.tap(find.text(AppStrings.hindi.navSettings).last);
    await tester.pumpAndSettle();
    await tester.tap(find.text('English'));
    await tester.pumpAndSettle();

    expect(find.text('Settings'), findsWidgets);
    expect(find.text('Subjects'), findsOneWidget);
    expect(find.text(AppStrings.hindi.navSubjects), findsNothing);

    final prefs = await SharedPreferences.getInstance();
    expect(prefs.getString(LanguageProvider.prefKey), 'en');

    // The saved choice is used on the next launch.
    await tester.pumpWidget(const SizedBox.shrink());
    await _pumpApp(tester);
    expect(find.text('Search books and chapters'), findsOneWidget);
  });
}
