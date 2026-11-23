import 'package:flutter/material.dart';
import 'package:flutter/services.dart';
import 'package:provider/provider.dart';
import 'package:shared_preferences/shared_preferences.dart';
import 'providers/progress_provider.dart';
import 'providers/theme_provider.dart';
import 'screens/home_screen.dart';
import 'services/screenshot_protection.dart';

void main() async {
  WidgetsFlutterBinding.ensureInitialized();
  try {
    await ScreenshotProtection.instance.initialize();
  } catch (error) {
    // The library is public. Individual chapters still wait for protection.
    debugPrint('Could not initialize screen capture: $error');
  }

  // Prefer portrait orientation for textbook/quiz readability
  await SystemChrome.setPreferredOrientations([
    DeviceOrientation.portraitUp,
    DeviceOrientation.portraitDown,
    DeviceOrientation.landscapeLeft,
    DeviceOrientation.landscapeRight,
  ]);

  final prefs = await SharedPreferences.getInstance();

  runApp(
    MultiProvider(
      providers: [
        ChangeNotifierProvider(create: (_) => ThemeProvider(prefs)),
        ChangeNotifierProvider(create: (_) => ProgressProvider()),
      ],
      child: const SetuLearningApp(),
    ),
  );
}

class SetuLearningApp extends StatelessWidget {
  const SetuLearningApp({super.key});

  @override
  Widget build(BuildContext context) {
    return Consumer<ThemeProvider>(
      builder: (context, themeProvider, child) {
        return MaterialApp(
          title: 'Setu Learning',
          debugShowCheckedModeBanner: false,
          theme: themeProvider.lightTheme,
          darkTheme: themeProvider.darkTheme,
          themeMode: themeProvider.themeMode,
          home: const HomeScreen(),
        );
      },
    );
  }
}
