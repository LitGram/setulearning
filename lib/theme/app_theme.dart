import 'package:flutter/material.dart';

class AppSpacing {
  static const double small = 8;
  static const double medium = 16;
  static const double large = 24;
  static const double contentWidth = 720;
}

class AppTheme {
  // Default app seed color (Deep Blue)
  static const Color defaultSeedColor = Color(0xFF1E40AF);

  static ThemeData createTheme({
    Color seedColor = defaultSeedColor,
    Brightness brightness = Brightness.light,
    double fontScale = 1.0,
  }) {
    final colorScheme = ColorScheme.fromSeed(
      seedColor: seedColor,
      brightness: brightness,
    );

    final baseTextTheme = Typography.material2021()
        .englishLike
        .merge(ThemeData(brightness: brightness).textTheme)
        .apply(fontSizeFactor: fontScale);
    return ThemeData(
      useMaterial3: true,
      colorScheme: colorScheme,
      brightness: brightness,
      scaffoldBackgroundColor: colorScheme.surface,
      appBarTheme: AppBarTheme(
        centerTitle: false,
        elevation: 0,
        scrolledUnderElevation: 2,
        backgroundColor: colorScheme.surface,
        foregroundColor: colorScheme.onSurface,
        titleTextStyle: TextStyle(
          fontSize: 20 * fontScale,
          fontWeight: FontWeight.bold,
          color: colorScheme.onSurface,
          letterSpacing: -0.2,
        ),
      ),
      cardTheme: CardThemeData(
        elevation: 1,
        shape: RoundedRectangleBorder(
          borderRadius: BorderRadius.circular(16),
          side: BorderSide(
            color: colorScheme.outlineVariant.withOpacity(0.5),
            width: 1,
          ),
        ),
        clipBehavior: Clip.antiAlias,
        margin: const EdgeInsets.symmetric(vertical: 6, horizontal: 0),
      ),
      filledButtonTheme: FilledButtonThemeData(
        style: FilledButton.styleFrom(
          minimumSize: const Size(48, 48), // Section 6.4: >= 48x48 tap target
          padding: const EdgeInsets.symmetric(horizontal: 20, vertical: 12),
          shape: RoundedRectangleBorder(
            borderRadius: BorderRadius.circular(12),
          ),
        ),
      ),
      outlinedButtonTheme: OutlinedButtonThemeData(
        style: OutlinedButton.styleFrom(
          minimumSize: const Size(48, 48), // Section 6.4: >= 48x48 tap target
          padding: const EdgeInsets.symmetric(horizontal: 20, vertical: 12),
          shape: RoundedRectangleBorder(
            borderRadius: BorderRadius.circular(12),
          ),
        ),
      ),
      textButtonTheme: TextButtonThemeData(
        style: TextButton.styleFrom(
          minimumSize: const Size(48, 48), // Section 6.4: >= 48x48 tap target
          padding: const EdgeInsets.symmetric(horizontal: 16, vertical: 12),
          shape: RoundedRectangleBorder(
            borderRadius: BorderRadius.circular(8),
          ),
        ),
      ),
      iconButtonTheme: IconButtonThemeData(
        style: IconButton.styleFrom(
          minimumSize: const Size(48, 48), // Section 6.4: >= 48x48 tap target
        ),
      ),
      textTheme: baseTextTheme.copyWith(
        displayLarge: TextStyle(
          fontSize: 32 * fontScale,
          fontWeight: FontWeight.bold,
          color: colorScheme.onSurface,
          height: 1.2,
        ),
        titleLarge: TextStyle(
          fontSize: 22 * fontScale,
          fontWeight: FontWeight.bold,
          color: colorScheme.onSurface,
          height: 1.3,
        ),
        titleMedium: TextStyle(
          fontSize: 18 * fontScale,
          fontWeight: FontWeight.w600,
          color: colorScheme.onSurface,
          height: 1.3,
        ),
        bodyLarge: TextStyle(
          fontSize: 16 * fontScale,
          fontWeight: FontWeight.normal,
          color: colorScheme.onSurface,
          height: 1.6,
        ),
        bodyMedium: TextStyle(
          fontSize: 14 * fontScale,
          fontWeight: FontWeight.normal,
          color: colorScheme.onSurfaceVariant,
          height: 1.5,
        ),
        labelLarge: TextStyle(
          fontSize: 14 * fontScale,
          fontWeight: FontWeight.w600,
          letterSpacing: 0.2,
        ),
      ),
      dialogTheme: DialogThemeData(
        shape: RoundedRectangleBorder(
          borderRadius: BorderRadius.circular(20),
        ),
        elevation: 3,
      ),
      snackBarTheme: SnackBarThemeData(
        behavior: SnackBarBehavior.floating,
        shape: RoundedRectangleBorder(
          borderRadius: BorderRadius.circular(12),
        ),
      ),
    );
  }
}
