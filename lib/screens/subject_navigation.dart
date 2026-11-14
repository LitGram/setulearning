import 'package:flutter/material.dart';
import 'package:provider/provider.dart';
import '../models/subject.dart';
import '../providers/theme_provider.dart';
import 'book_screen.dart';
import 'subject_screen.dart';

/// Opens a subject with its color theme.
///
/// Subjects that hold a single book open that book directly, which saves a
/// tap on a "Choose a book" screen with only one choice. The default app
/// color comes back when the student returns.
Future<void> openSubject(BuildContext context, Subject subject) {
  return openWithSubjectTheme(
    context,
    subject,
    (_) => subject.books.length == 1
        ? BookScreen(subject: subject, book: subject.books.first)
        : SubjectScreen(subject: subject),
  );
}

/// Pushes [builder] with the subject's color theme and restores the default
/// theme once that route is popped.
Future<void> openWithSubjectTheme(
  BuildContext context,
  Subject subject,
  WidgetBuilder builder,
) async {
  final theme = Provider.of<ThemeProvider>(context, listen: false);
  theme.setSubjectSeedColor(subject.seedColor);
  await Navigator.push(context, MaterialPageRoute(builder: builder));
  theme.resetToDefaultSeedColor();
}
