import 'package:flutter/material.dart';
import '../l10n/app_strings.dart';

/// Shared offline figure and accessible full-screen viewer for book chapters.
class EducationalImage extends StatelessWidget {
  const EducationalImage({super.key, required this.asset, this.caption});

  final String asset;
  final String? caption;

  @override
  Widget build(BuildContext context) {
    final colors = Theme.of(context).colorScheme;
    return Container(
      margin: const EdgeInsets.symmetric(vertical: 16),
      decoration: BoxDecoration(
        borderRadius: BorderRadius.circular(16),
        border: Border.all(color: colors.outlineVariant),
      ),
      clipBehavior: Clip.antiAlias,
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.stretch,
        children: [
          Semantics(
            button: true,
            label: context.strings.enlargeDiagram,
            child: InkWell(
              onTap: () => Navigator.of(context).push(MaterialPageRoute<void>(
                builder: (_) => _FigureViewer(asset: asset, caption: caption),
              )),
              child: Image.asset(
                asset,
                fit: BoxFit.contain,
                semanticLabel: caption ?? context.strings.educationalDiagram,
                errorBuilder: (_, error, stack) => SizedBox(
                  height: 160,
                  child: Center(child: Text(context.strings.imageUnavailable)),
                ),
              ),
            ),
          ),
          Container(
            color: colors.surfaceContainerHighest,
            padding: const EdgeInsets.all(12),
            child: Column(children: [
              if (caption != null) Text(caption!, textAlign: TextAlign.center),
              const SizedBox(height: 4),
              Row(mainAxisAlignment: MainAxisAlignment.center, children: [
                const Icon(Icons.zoom_in_rounded, size: 18),
                const SizedBox(width: 6),
                Flexible(
                  child: Text(context.strings.tapToEnlarge,
                      textAlign: TextAlign.center),
                ),
              ]),
            ]),
          ),
        ],
      ),
    );
  }
}

class _FigureViewer extends StatefulWidget {
  const _FigureViewer({required this.asset, this.caption});
  final String asset;
  final String? caption;

  @override
  State<_FigureViewer> createState() => _FigureViewerState();
}

class _FigureViewerState extends State<_FigureViewer> {
  final _transform = TransformationController();

  void _zoom(double factor) {
    final scale = _transform.value.getMaxScaleOnAxis();
    final target = (scale * factor).clamp(1.0, 5.0);
    // Explicit buttons also support keyboard users and desktop previews.
    _transform.value = Matrix4.identity()..scaleByDouble(target, target, 1, 1);
  }

  @override
  void dispose() {
    _transform.dispose();
    super.dispose();
  }

  @override
  Widget build(BuildContext context) => Scaffold(
        appBar: AppBar(
          title: Text(context.strings.diagramTitle),
          leading: IconButton(
            tooltip: context.strings.closeDiagram,
            icon: const Icon(Icons.close),
            onPressed: () => Navigator.of(context).pop(),
          ),
          actions: [
            IconButton(
                tooltip: context.strings.zoomOut,
                onPressed: () => _zoom(1 / 1.5),
                icon: const Icon(Icons.zoom_out)),
            IconButton(
                tooltip: context.strings.zoomIn,
                onPressed: () => _zoom(1.5),
                icon: const Icon(Icons.zoom_in)),
            IconButton(
                tooltip: context.strings.resetZoom,
                onPressed: () => _transform.value = Matrix4.identity(),
                icon: const Icon(Icons.fit_screen)),
          ],
        ),
        body: SafeArea(
          child: Column(children: [
            Expanded(
              child: InteractiveViewer(
                transformationController: _transform,
                minScale: 1,
                maxScale: 5,
                child: Center(
                    child: Image.asset(widget.asset,
                        fit: BoxFit.contain,
                        semanticLabel:
                            widget.caption ?? context.strings.educationalDiagram)),
              ),
            ),
            Padding(
              padding: const EdgeInsets.all(16),
              child: Text(widget.caption ?? context.strings.pinchToZoom,
                  textAlign: TextAlign.center),
            ),
          ]),
        ),
      );
}
