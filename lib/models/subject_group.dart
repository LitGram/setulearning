import 'package:flutter/material.dart';
import '../l10n/app_strings.dart';
import 'subject.dart';

/// Groups the library so students can jump to their own exam or class
/// instead of scrolling through every subject. The home screen remembers
/// the chosen group (see [id]).
enum SubjectGroup {
  school(
    id: 'class10',
    label: 'School',
    hindiLabel: 'RBSE कक्षा 10',
    description: 'Chapter-wise board exam guides',
    hindiDescription: 'बोर्ड परीक्षा की अध्यायवार गाइड',
    icon: Icons.school_rounded,
  ),
  competitive(
    id: 'competitive',
    label: 'Competitive exams',
    hindiLabel: 'प्रतियोगी परीक्षाएँ',
    description: 'RAS, maths, English and science preparation',
    hindiDescription: 'RAS, गणित, अंग्रेज़ी और विज्ञान की तैयारी',
    icon: Icons.emoji_events_rounded,
  ),
  ugcNet(
    id: 'ugcnet',
    label: 'UGC NET',
    hindiLabel: 'यूजीसी नेट',
    description: 'Complete subject-wise texts',
    hindiDescription: 'विषयवार संपूर्ण ग्रंथ',
    icon: Icons.workspace_premium_rounded,
  ),
  higher(
    id: 'higher',
    label: 'Higher studies',
    hindiLabel: 'उच्च अध्ययन एवं साहित्य',
    description: 'M.Sc. Physics and world literature',
    hindiDescription: 'M.Sc. Physics और विश्व साहित्य',
    icon: Icons.auto_stories_rounded,
  );

  const SubjectGroup({
    required this.id,
    required this.label,
    required this.hindiLabel,
    required this.description,
    required this.hindiDescription,
    required this.icon,
  });

  /// Stable key saved in preferences. Do not change once released.
  final String id;
  final String label;
  final String hindiLabel;
  final String description;
  final String hindiDescription;
  final IconData icon;

  String labelIn(AppLanguage language) =>
      language == AppLanguage.hi ? hindiLabel : label;

  String descriptionIn(AppLanguage language) =>
      language == AppLanguage.hi ? hindiDescription : description;

  static SubjectGroup? fromId(String? id) {
    for (final group in SubjectGroup.values) {
      if (group.id == id) return group;
    }
    return null;
  }

  static SubjectGroup of(Subject subject) {
    final id = subject.id;
    if (id.startsWith('rbse10_')) return SubjectGroup.school;
    if (id.startsWith('ugcnet_')) return SubjectGroup.ugcNet;
    if (id == 'mscphysics' || id == 'greatworks') return SubjectGroup.higher;
    return SubjectGroup.competitive;
  }
}
