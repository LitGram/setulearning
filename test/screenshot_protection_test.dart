import 'dart:async';
import 'package:flutter/foundation.dart';
import 'package:flutter/material.dart';
import 'package:flutter/services.dart';
import 'package:flutter_test/flutter_test.dart';
import 'package:setu_learning/services/screenshot_protection.dart';
import 'package:setu_learning/widgets/screenshot_protected_screen.dart';

void main() {
  TestWidgetsFlutterBinding.ensureInitialized();
  final flags = <bool>[];
  final messenger =
      TestDefaultBinaryMessengerBinding.instance.defaultBinaryMessenger;

  setUp(() {
    ScreenshotProtection.resetForTesting();
    flags.clear();
    messenger.setMockMethodCallHandler(ScreenshotProtection.channel,
        (call) async {
      expect(call.method, 'setSecure');
      flags.add((call.arguments as Map)['enabled'] as bool);
      return null;
    });
  });

  tearDown(() {
    debugDefaultTargetPlatformOverride = null;
    messenger.setMockMethodCallHandler(ScreenshotProtection.channel, null);
  });

  test('Startup permits screenshots on the public library', () async {
    await ScreenshotProtection().initialize();
    expect(flags, [false]);
  });

  test('Popping a quiz keeps its underlying reader protected', () async {
    final protection = ScreenshotProtection();
    final reader = Object(), quiz = Object();
    await protection.acquire(reader);
    await protection.acquire(quiz);
    await protection.release(quiz);
    expect(flags, [true, true, true]);
    await protection.release(reader);
    expect(flags.last, false);
  });

  test('Rapid requests reach Android in navigation order', () async {
    final protection = ScreenshotProtection();
    final started = Completer<void>(), acknowledge = Completer<void>();
    messenger.setMockMethodCallHandler(ScreenshotProtection.channel,
        (call) async {
      flags.add((call.arguments as Map)['enabled'] as bool);
      if (flags.length == 1) {
        started.complete();
        await acknowledge.future;
      }
      return null;
    });
    final first = Object(), second = Object();
    final openFirst = protection.acquire(first);
    await started.future;
    final closeFirst = protection.release(first);
    final openSecond = protection.acquire(second);
    expect(flags, [true]);
    acknowledge.complete();
    await Future.wait([openFirst, closeFirst, openSecond]);
    expect(flags, [true, false, true]);
    await protection.release(second);
    expect(flags.last, false);
  });

  testWidgets(
      'Content waits for native protection; pop waits for the exit animation',
      (tester) async {
    final acknowledge = Completer<void>();
    messenger.setMockMethodCallHandler(ScreenshotProtection.channel,
        (call) async {
      final secure = (call.arguments as Map)['enabled'] as bool;
      flags.add(secure);
      if (secure) await acknowledge.future;
      return null;
    });
    await tester.pumpWidget(MaterialApp(
      home: Builder(
          builder: (context) => Scaffold(
                body: TextButton(
                  onPressed: () =>
                      Navigator.of(context).push(MaterialPageRoute<void>(
                    builder: (_) => ScreenshotProtectedScreen(
                        child: Scaffold(
                      appBar: AppBar(title: const Text('Protected reader')),
                      body: const Text('Private chapter content'),
                    )),
                  )),
                  child: const Text('Open chapter'),
                ),
              )),
    ));
    expect(flags, isEmpty);
    await tester.tap(find.text('Open chapter'));
    await tester.pump();
    expect(find.text('Private chapter content'), findsNothing);
    acknowledge.complete();
    await tester.pumpAndSettle();
    expect(find.text('Private chapter content'), findsOneWidget);
    expect(flags.last, true);
    await tester.pageBack();
    await tester.pump(const Duration(milliseconds: 100));
    expect(flags.last, true);
    await tester.pumpAndSettle();
    expect(flags.last, false);
  });

  testWidgets('A native error keeps content hidden and permits retry',
      (tester) async {
    var fail = true;
    messenger.setMockMethodCallHandler(ScreenshotProtection.channel,
        (call) async {
      if (fail) throw PlatformException(code: 'TEST_ERROR');
      flags.add((call.arguments as Map)['enabled'] as bool);
      return null;
    });
    await tester.pumpWidget(const MaterialApp(
      home: ScreenshotProtectedScreen(
          child: Scaffold(body: Text('Private content'))),
    ));
    await tester.pumpAndSettle();
    expect(find.text('Private content'), findsNothing);
    expect(find.text('Retry'), findsOneWidget);
    fail = false;
    await tester.tap(find.text('Retry'));
    await tester.pumpAndSettle();
    expect(find.text('Private content'), findsOneWidget);
    expect(flags.last, true);
    await tester.pumpWidget(const SizedBox.shrink());
    await tester.pumpAndSettle();
    expect(flags.last, false);
  });

  test('Other platforms do not call the Android channel', () async {
    debugDefaultTargetPlatformOverride = TargetPlatform.windows;
    final protection = ScreenshotProtection();
    final owner = Object();
    await protection.acquire(owner);
    await protection.release(owner);
    expect(flags, isEmpty);
  });
}
