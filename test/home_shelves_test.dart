import 'package:flutter/material.dart';
import 'package:flutter_test/flutter_test.dart';
import 'package:provider/provider.dart';
import 'package:setu_learning/models/shelf.dart';
import 'package:setu_learning/providers/progress_provider.dart';
import 'package:setu_learning/providers/theme_provider.dart';
import 'package:setu_learning/screens/home_screen.dart';
import 'package:setu_learning/services/content_service.dart';
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
      child: const MaterialApp(home: HomeScreen()),
    );

void main() {
  test('every subject belongs to exactly one shelf', () {
    final subjects = ContentService.instance.getSubjects();
    final total =
        Shelf.values.fold<int>(0, (n, s) => n + s.filter(subjects).length);
    expect(total, subjects.length);
    for (final shelf in Shelf.values) {
      expect(shelf.filter(subjects), isNotEmpty, reason: shelf.id);
    }
    expect(
        Shelf.class10
            .filter(subjects)
            .every((s) => s.id.startsWith('rbse10_')),
        isTrue);
    expect(
        Shelf.ugcNet.filter(subjects).every((s) => s.id.startsWith('ugcnet_')),
        isTrue);
  });

  testWidgets('first launch asks for a shelf and remembers it',
      (tester) async {
    SharedPreferences.setMockInitialValues({});
    await tester.pumpWidget(_app());
    await tester.pumpAndSettle();

    expect(find.text('आप किसकी तैयारी कर रहे हैं?'), findsOneWidget);

    await tester.tap(find.widgetWithText(OutlinedButton, 'UGC NET'));
    await tester.pumpAndSettle();

    expect(find.text('आप किसकी तैयारी कर रहे हैं?'), findsNothing);
    expect(find.text('UGC NET English'), findsOneWidget);
    expect(find.text('RBSE 10th Mathematics'), findsNothing);

    final prefs = await SharedPreferences.getInstance();
    expect(prefs.getString('home_shelf'), 'ugcnet');
  });

  testWidgets('saved shelf opens directly and "All" shows every shelf',
      (tester) async {
    SharedPreferences.setMockInitialValues({'home_shelf': 'class10'});
    await tester.pumpWidget(_app());
    await tester.pumpAndSettle();

    expect(find.text('आप किसकी तैयारी कर रहे हैं?'), findsNothing);
    expect(find.text('RBSE 10th Mathematics'), findsOneWidget);
    expect(find.text('MathSetu'), findsNothing);

    await tester.tap(find.widgetWithText(ChoiceChip, 'सभी'));
    await tester.pumpAndSettle();
    await tester.scrollUntilVisible(find.text('MathSetu'), 300);
    expect(find.text('MathSetu'), findsOneWidget);
  });
}
