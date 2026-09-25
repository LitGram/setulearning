import 'package:flutter/material.dart';
import '../theme/app_theme.dart';

class ThemeProvider extends ChangeNotifier {
  Color _currentSeedColor = AppTheme.defaultSeedColor;
  ThemeMode _themeMode = ThemeMode.system;
  double _fontScale = 1.0;

  Color get currentSeedColor => _currentSeedColor;
  ThemeMode get themeMode => _themeMode;
  double get fontScale => _fontScale;

  ThemeData get lightTheme => AppTheme.createTheme(
        seedColor: _currentSeedColor,
        brightness: Brightness.light,
        fontScale: _fontScale,
      );

  ThemeData get darkTheme => AppTheme.createTheme(
        seedColor: _currentSeedColor,
        brightness: Brightness.dark,
        fontScale: _fontScale,
      );

  void setSubjectSeedColor(Color color) {
    if (_currentSeedColor != color) {
      _currentSeedColor = color;
      notifyListeners();
    }
  }

  void resetToDefaultSeedColor() {
    if (_currentSeedColor != AppTheme.defaultSeedColor) {
      _currentSeedColor = AppTheme.defaultSeedColor;
      notifyListeners();
    }
  }

  void setThemeMode(ThemeMode mode) {
    if (_themeMode != mode) {
      _themeMode = mode;
      notifyListeners();
    }
  }

  void setFontScale(double scale) {
    final clamped = scale.clamp(0.85, 1.4);
    if (_fontScale != clamped) {
      _fontScale = clamped;
      notifyListeners();
    }
  }
}
