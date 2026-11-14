import 'package:flutter/material.dart';
import 'subject.dart';

/// Groups the library so students can jump to their own exam or class
/// instead of scrolling through every subject.
enum SubjectGroup {
  school('School', 'RBSE कक्षा 10', Icons.school_rounded),
  competitive(
      'Competitive exams', 'प्रतियोगी परीक्षाएँ', Icons.emoji_events_rounded),
  ugcNet('UGC NET', 'यूजीसी नेट', Icons.workspace_premium_rounded),
  higher(
      'Higher studies', 'उच्च अध्ययन एवं साहित्य', Icons.auto_stories_rounded);

  final String label;
  final String hindiLabel;
  final IconData icon;

  const SubjectGroup(this.label, this.hindiLabel, this.icon);

  static SubjectGroup of(Subject subject) {
    final id = subject.id;
    if (id.startsWith('rbse10_')) return SubjectGroup.school;
    if (id.startsWith('ugcnet_')) return SubjectGroup.ugcNet;
    if (id == 'mscphysics' || id == 'greatworks') return SubjectGroup.higher;
    return SubjectGroup.competitive;
  }
}
