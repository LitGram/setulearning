import 'package:flutter/foundation.dart';
import 'package:shared_preferences/shared_preferences.dart';
import '../l10n/app_strings.dart';

/// Holds the interface language chosen in Settings. Hindi is the default
/// because most learners use Hindi-medium books.
class LanguageProvider extends ChangeNotifier {
  static const prefKey = 'ui_language';
  static const defaultLanguage = AppLanguage.hi;

  LanguageProvider([this._prefs]) {
    _language =
        AppLanguage.fromCode(_prefs?.getString(prefKey)) ?? defaultLanguage;
  }

  final SharedPreferences? _prefs;
  late AppLanguage _language;

  AppLanguage get language => _language;
  AppStrings get strings => AppStrings.of(_language);

  void setLanguage(AppLanguage language) {
    if (_language == language) return;
    _language = language;
    notifyListeners();
    _prefs?.setString(prefKey, language.code);
  }
}
