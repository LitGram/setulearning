import 'package:flutter/material.dart';
import '../l10n/app_strings.dart';
import 'subject.dart';

/// A group of subjects aimed at one kind of learner, used to shorten the
/// home screen. Order here is the order shown on the home screen.
enum Shelf {
  class10(
    id: 'class10',
    label: 'कक्षा 10 (RBSE)',
    description: 'बोर्ड परीक्षा की अध्यायवार गाइड',
    labelEn: 'Class 10 (RBSE)',
    descriptionEn: 'Chapter-wise board exam guides',
    icon: Icons.school_rounded,
  ),
  competitive(
    id: 'competitive',
    label: 'प्रतियोगी परीक्षाएँ',
    description: 'RAS, गणित, अंग्रेज़ी और विज्ञान की तैयारी',
    labelEn: 'Competitive exams',
    descriptionEn: 'RAS, maths, English and science preparation',
    icon: Icons.emoji_events_rounded,
  ),
  ugcNet(
    id: 'ugcnet',
    label: 'UGC NET',
    description: 'विषयवार संपूर्ण ग्रंथ',
    labelEn: 'UGC NET',
    descriptionEn: 'Complete subject-wise texts',
    icon: Icons.workspace_premium_rounded,
  ),
  higher(
    id: 'higher',
    label: 'कॉलेज व साहित्य',
    description: 'M.Sc. Physics और विश्व साहित्य',
    labelEn: 'College & literature',
    descriptionEn: 'M.Sc. Physics and world literature',
    icon: Icons.auto_stories_rounded,
  );

  const Shelf({
    required this.id,
    required this.label,
    required this.description,
    required this.labelEn,
    required this.descriptionEn,
    required this.icon,
  });

  final String id;
  final String label;
  final String description;
  final String labelEn;
  final String descriptionEn;
  final IconData icon;

  String labelIn(AppLanguage language) =>
      language == AppLanguage.hi ? label : labelEn;
  String descriptionIn(AppLanguage language) =>
      language == AppLanguage.hi ? description : descriptionEn;

  static Shelf? fromId(String? id) {
    for (final shelf in Shelf.values) {
      if (shelf.id == id) return shelf;
    }
    return null;
  }

  /// Which shelf a subject belongs to. New subjects default to [higher]
  /// unless their id says otherwise, so nothing is ever hidden from "All".
  static Shelf of(Subject subject) {
    final id = subject.id;
    if (id.startsWith('rbse10_')) return Shelf.class10;
    if (id.startsWith('ugcnet_')) return Shelf.ugcNet;
    const competitive = {'mathsetu', 'englishsetu', 'vigyansetu', 'rassetu'};
    if (competitive.contains(id)) return Shelf.competitive;
    return Shelf.higher;
  }

  List<Subject> filter(List<Subject> subjects) =>
      subjects.where((s) => Shelf.of(s) == this).toList();
}
