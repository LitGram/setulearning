import 'package:flutter/material.dart';
import 'package:flutter_test/flutter_test.dart';
import 'package:shared_preferences/shared_preferences.dart';
import 'package:setu_learning/models/chapter.dart';
import 'package:setu_learning/models/mcq.dart';
import 'package:setu_learning/screens/quiz_screen.dart';
import 'package:setu_learning/services/screenshot_protection.dart';
import 'package:setu_learning/services/study_session_store.dart';
import 'package:setu_learning/widgets/accessible_card.dart';
import 'learning_flow_test.dart' as helpers;

const lesson =
    Chapter(id: 'lifelines', title: 'Lifeline practice', content: [], mcqs: [
  MCQ(
      question: 'Choose the correct fruit.',
      options: ['Apple', 'Stone', 'Metal', 'Plastic'],
      correctIndex: 0),
  MCQ(
      question: 'Choose the correct number.',
      options: ['Letter', 'Word', 'Two', 'Sentence'],
      correctIndex: 2),
]);

Widget practice(helpers.TestProgress progress,
        {Chapter chapter = lesson, double scale = 1}) =>
    helpers.app(
        QuizScreen(
            subject: helpers.subject, book: helpers.book, chapter: chapter),
        progress,
        scale: scale);

void main() {
  setUp(() {
    ScreenshotProtection.resetForTesting();
    SharedPreferences.setMockInitialValues({});
    TestDefaultBinaryMessengerBinding.instance.defaultBinaryMessenger
        .setMockMethodCallHandler(
            ScreenshotProtection.channel, (_) async => null);
  });

  testWidgets(
      'Skip clears an unchecked choice, can be revisited, and gives no credit',
      (tester) async {
    final progress = helpers.TestProgress();
    await tester.pumpWidget(practice(progress));
    await tester.pumpAndSettle();
    await tester.tap(find.ancestor(
        of: find.text('Apple'), matching: find.byType(AccessibleCard)));
    await tester.tap(find.text('Skip'));
    await tester.pumpAndSettle();
    expect(find.text('Question 2 of 2'), findsOneWidget);
    await tester.tap(find.text('Previous'));
    await tester.pumpAndSettle();
    final check = tester.widget<FilledButton>(
        find.widgetWithText(FilledButton, 'Check answer'));
    expect(check.onPressed, isNull);
    await tester.tap(find.text('Skip'));
    await tester.pumpAndSettle();
    await tester.tap(find.text('Skip'));
    await tester.pumpAndSettle();
    expect(progress.result?.score, 0);
    expect(progress.result?.total, 2);
    expect(find.text('2 skipped / unanswered'), findsOneWidget);
    expect(find.text('Review skipped questions'), findsOneWidget);
  });

  testWidgets(
      '50–50 preserves correct answer, hides two wrong options, and survives resume',
      (tester) async {
    tester.view.physicalSize = const Size(800, 1200);
    tester.view.devicePixelRatio = 1;
    addTearDown(tester.view.resetPhysicalSize);
    addTearDown(tester.view.resetDevicePixelRatio);
    final progress = helpers.TestProgress();
    await tester.pumpWidget(practice(progress));
    await tester.pumpAndSettle();
    await tester.tap(find.text('50–50 lifeline'));
    await tester.pumpAndSettle();
    expect(find.byType(AccessibleCard), findsNWidgets(2));
    expect(find.text('Apple'), findsOneWidget);
    final key = StudySessionStore.key(
        'quiz', helpers.subject.id, helpers.book.id, lesson.id);
    final draft = (await StudySessionStore.read(key))!;
    final hidden = (draft['hiddenOptions']['0'] as List).cast<int>();
    expect(hidden.length, 2);
    expect(hidden.contains(0), isFalse);
    await tester.tap(find.text('Skip'));
    await tester.pumpAndSettle();
    expect(find.byType(AccessibleCard), findsNWidgets(4));
    await tester.pumpWidget(const SizedBox());
    await tester.pumpAndSettle();
    await tester.pumpWidget(practice(progress));
    await tester.pumpAndSettle();
    await tester.tap(find.text('Resume'));
    await tester.pumpAndSettle();
    await tester.tap(find.text('Previous'));
    await tester.pumpAndSettle();
    expect(find.byType(AccessibleCard), findsNWidgets(2));
    expect(find.text('50–50 used'), findsOneWidget);
    await tester.tap(find.ancestor(
        of: find.text('Apple'), matching: find.byType(AccessibleCard)));
    await tester.pumpAndSettle();
    await tester.tap(find.text('Check answer'));
    await tester.pumpAndSettle();
    expect(find.text('Correct answer'), findsOneWidget);
    await tester.tap(find.text('Next question'));
    await tester.pumpAndSettle();
    await tester.tap(find.text('Skip'));
    await tester.pumpAndSettle();
    expect(progress.result?.score, 1);
    expect(find.text('1 skipped / unanswered'), findsOneWidget);
    await tester.tap(find.text('Try again'));
    await tester.pumpAndSettle();
    expect(find.byType(AccessibleCard), findsNWidgets(4));
    expect(find.text('50–50 lifeline'), findsOneWidget);
  });

  testWidgets('Small option sets omit lifeline; actions fit large text',
      (tester) async {
    tester.view.physicalSize = const Size(360, 900);
    tester.view.devicePixelRatio = 1;
    addTearDown(tester.view.resetPhysicalSize);
    addTearDown(tester.view.resetDevicePixelRatio);
    await tester.pumpWidget(
        practice(helpers.TestProgress(), chapter: helpers.chapter, scale: 2));
    await tester.pumpAndSettle();
    expect(find.text('50–50 lifeline'), findsNothing);
    expect(find.text('Skip'), findsOneWidget);
    await tester.tap(find.text('Skip'));
    await tester.pumpAndSettle();
    expect(tester.takeException(), isNull);
  });
}
