import 'package:flutter/material.dart';
import 'package:shared_preferences/shared_preferences.dart';
import '../theme/app_theme.dart';

class ThemeProvider extends ChangeNotifier {
  static const _keyThemeMode = 'theme_mode';
  static const _keyFontScale = 'font_scale';

  SharedPreferences? _prefs;
  Color _currentSeedColor = AppTheme.defaultSeedColor;
  ThemeMode _themeMode = ThemeMode.system;
  double _fontScale = 1.0;

  ThemeProvider([this._prefs]) {
    _loadFromPrefs();
  }

  void _loadFromPrefs() {
    if (_prefs == null) return;
    final modeStr = _prefs!.getString(_keyThemeMode);
    if (modeStr != null) {
      if (modeStr == 'light') {
        _themeMode = ThemeMode.light;
      } else if (modeStr == 'dark') {
        _themeMode = ThemeMode.dark;
      } else {
        _themeMode = ThemeMode.system;
      }
    }
    final scale = _prefs!.getDouble(_keyFontScale);
    if (scale != null) {
      _fontScale = scale.clamp(0.85, 1.4);
    }
  }

  Future<void> initPrefs() async {
    _prefs ??= await SharedPreferences.getInstance();
    _loadFromPrefs();
    notifyListeners();
  }

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
      final modeStr = mode == ThemeMode.light
          ? 'light'
          : mode == ThemeMode.dark
              ? 'dark'
              : 'system';
      _prefs?.setString(_keyThemeMode, modeStr);
    }
  }

  void setFontScale(double scale) {
    final clamped = scale.clamp(0.85, 1.4);
    if (_fontScale != clamped) {
      _fontScale = clamped;
      notifyListeners();
      _prefs?.setDouble(_keyFontScale, clamped);
    }
  }
}
