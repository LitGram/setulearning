import 'package:flutter/material.dart';
import 'package:flutter_test/flutter_test.dart';
import 'package:provider/provider.dart';
import 'package:setu_learning/l10n/app_strings.dart';
import 'package:setu_learning/models/subject_group.dart';
import 'package:setu_learning/providers/progress_provider.dart';
import 'package:setu_learning/providers/theme_provider.dart';
import 'package:setu_learning/screens/home_screen.dart';
import 'package:shared_preferences/shared_preferences.dart';

class _TestProgress extends ProgressProvider {
  @override
  bool get isLoading => false;
  @override
  Future<void> loadProgress() async {}
}

Widget _app() => MultiProvider(
      providers: [
        ChangeNotifierProvider(create: (_) => ThemeProvider()),
        ChangeNotifierProvider<ProgressProvider>(
            create: (_) => _TestProgress()),
      ],
      child: MaterialApp(
        builder: (context, child) =>
            AppStringsScope(strings: AppStrings.hindi, child: child!),
        home: const HomeScreen(),
      ),
    );

void main() {
  test('group ids round-trip for the saved preference', () {
    for (final group in SubjectGroup.values) {
      expect(SubjectGroup.fromId(group.id), group);
    }
    expect(SubjectGroup.fromId('all'), isNull);
    expect(SubjectGroup.fromId(null), isNull);
  });

  testWidgets('first launch asks for a group and remembers it',
      (tester) async {
    SharedPreferences.setMockInitialValues({});
    await tester.pumpWidget(_app());
    await tester.pumpAndSettle();

    expect(find.text('आप किसकी तैयारी कर रहे हैं?'), findsOneWidget);

    await tester.tap(find.widgetWithText(OutlinedButton, SubjectGroup.ugcNet.hindiLabel));
    await tester.pumpAndSettle();

    expect(find.text('आप किसकी तैयारी कर रहे हैं?'), findsNothing);
    expect(find.text('UGC NET English'), findsOneWidget);
    expect(find.text('RBSE 10th Mathematics'), findsNothing);

    final prefs = await SharedPreferences.getInstance();
    expect(prefs.getString('home_shelf'), 'ugcnet');
  });

  testWidgets('saved group opens directly and "All" shows every shelf',
      (tester) async {
    SharedPreferences.setMockInitialValues({'home_shelf': 'class10'});
    await tester.pumpWidget(_app());
    await tester.pumpAndSettle();

    expect(find.text('आप किसकी तैयारी कर रहे हैं?'), findsNothing);
    expect(find.text('RBSE 10th Mathematics'), findsOneWidget);
    expect(find.text('MathSetu'), findsNothing);

    await tester.tap(find.textContaining('सभी ('));
    await tester.pumpAndSettle();
    await tester.scrollUntilVisible(find.text('MathSetu'), 300);
    expect(find.text('MathSetu'), findsOneWidget);
  });
}
