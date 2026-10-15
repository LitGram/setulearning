import 'dart:async';
import 'package:flutter/material.dart';
import '../services/screenshot_protection.dart';

/// Keep chapter content off screen until Android confirms capture is blocked.
class ScreenshotProtectedScreen extends StatefulWidget {
  final Widget child;
  final VoidCallback? onProtected;
  const ScreenshotProtectedScreen({
    super.key,
    required this.child,
    this.onProtected,
  });

  @override
  State<ScreenshotProtectedScreen> createState() =>
      _ScreenshotProtectedScreenState();
}

class _ScreenshotProtectedScreenState extends State<ScreenshotProtectedScreen> {
  final _owner = Object();
  final _service = ScreenshotProtection.instance;
  late Future<void> _protection;
  bool _notified = false;

  @override
  void initState() {
    super.initState();
    _protection = _service.acquire(_owner);
  }

  @override
  void dispose() {
    // Flutter disposes a popped route after its exit animation, protecting the
    // outgoing reader until it has disappeared from the screen.
    unawaited(_service.release(_owner).catchError((Object error) =>
        debugPrint('Could not restore screen capture: $error')));
    super.dispose();
  }

  @override
  Widget build(BuildContext context) => FutureBuilder<void>(
        future: _protection,
        builder: (context, snapshot) {
          if (snapshot.connectionState == ConnectionState.done &&
              !snapshot.hasError) {
            if (!_notified) {
              _notified = true;
              widget.onProtected?.call();
            }
            return widget.child;
          }
          return Scaffold(
            appBar: AppBar(title: const Text('Opening chapter')),
            body: Center(
              child: snapshot.hasError
                  ? Padding(
                      padding: const EdgeInsets.all(24),
                      child: Column(mainAxisSize: MainAxisSize.min, children: [
                        const Text(
                            'This chapter could not be opened securely. Please retry.'),
                        const SizedBox(height: 12),
                        FilledButton(
                          onPressed: () => setState(() {
                            _protection = _service.acquire(_owner);
                          }),
                          child: const Text('Retry'),
                        ),
                      ]),
                    )
                  : const CircularProgressIndicator(),
            ),
          );
        },
      );
}
