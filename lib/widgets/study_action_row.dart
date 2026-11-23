import 'package:flutter/material.dart';

/// Keeps chapter and practice actions reachable with large accessibility text.
class StudyActionRow extends StatelessWidget {
  final List<Widget> children;
  const StudyActionRow({super.key, required this.children});

  @override
  Widget build(BuildContext context) =>
      LayoutBuilder(builder: (context, constraints) {
        final scale = MediaQuery.textScalerOf(context).scale(16) / 16;
        if (scale < 1.6 || constraints.maxWidth >= 600) {
          return Row(children: children);
        }
        final actions = children.where((child) => child is! SizedBox).toList();
        return Column(mainAxisSize: MainAxisSize.min, children: [
          for (var index = 0; index < actions.length; index++) ...[
            if (index > 0) const SizedBox(height: 8),
            if (actions[index] is Expanded)
              SizedBox(
                  width: double.infinity,
                  child: (actions[index] as Expanded).child)
            else
              actions[index],
          ],
        ]);
      });
}
