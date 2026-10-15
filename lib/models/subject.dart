import 'package:flutter/material.dart';
import 'book.dart';

class Subject {
  final String id;
  final String name;
  final String hindiName;
  final String tagline;
  final Color seedColor;
  final IconData icon;
  final List<Book> books;

  const Subject({
    required this.id,
    required this.name,
    required this.hindiName,
    required this.tagline,
    required this.seedColor,
    required this.icon,
    required this.books,
  });
}
