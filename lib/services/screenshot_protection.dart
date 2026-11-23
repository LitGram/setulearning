import 'package:flutter/foundation.dart';
import 'package:flutter/services.dart';

/// Android's secure-window flag, shared by all currently open chapter routes.
class ScreenshotProtection {
  static const channel =
      MethodChannel('com.setulearning.app/screenshot_protection');
  static ScreenshotProtection _instance = ScreenshotProtection();
  static ScreenshotProtection get instance => _instance;

  @visibleForTesting
  static void resetForTesting() {
    // Fake-async widget tests must not inherit another test's pending messages.
    _instance = ScreenshotProtection();
  }

  final Set<Object> _owners = {};
  Future<void>? _pending;

  /// A new Dart session starts on the public library screen.
  Future<void> initialize() => _synchronize();

  Future<void> acquire(Object owner) {
    _owners.add(owner);
    return _synchronize();
  }

  Future<void> release(Object owner) {
    _owners.remove(owner);
    return _synchronize();
  }

  Future<void> _synchronize() {
    if (kIsWeb || defaultTargetPlatform != TargetPlatform.android) {
      return Future.value();
    }
    final enabled = _owners.isNotEmpty;
    // Serialize rapid navigation so an old request cannot override a new one.
    Future<void> send() =>
        channel.invokeMethod<void>('setSecure', {'enabled': enabled});
    final operation = _pending?.then((_) => send()) ?? send();
    // Keep subsequent requests usable after an error; the caller still gets it.
    _pending =
        operation.then<void>((_) {}, onError: (Object _, StackTrace __) {});
    return operation;
  }
}
