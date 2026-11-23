import 'package:flutter/material.dart';

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
            label: 'Enlarge diagram / चित्र बड़ा करें',
            child: InkWell(
              onTap: () => Navigator.of(context).push(MaterialPageRoute<void>(
                builder: (_) => _FigureViewer(asset: asset, caption: caption),
              )),
              child: Image.asset(
                asset,
                fit: BoxFit.contain,
                semanticLabel: caption ?? 'Educational diagram',
                errorBuilder: (_, error, stack) => const SizedBox(
                  height: 160,
                  child: Center(child: Text('चित्र उपलब्ध नहीं है')),
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
              const Row(mainAxisAlignment: MainAxisAlignment.center, children: [
                Icon(Icons.zoom_in_rounded, size: 18),
                SizedBox(width: 6),
                Flexible(
                  child: Text('चित्र पर टैप करें • Tap to enlarge',
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
          title: const Text('चित्र देखें / Diagram'),
          leading: IconButton(
            tooltip: 'Close diagram',
            icon: const Icon(Icons.close),
            onPressed: () => Navigator.of(context).pop(),
          ),
          actions: [
            IconButton(
                tooltip: 'Zoom out',
                onPressed: () => _zoom(1 / 1.5),
                icon: const Icon(Icons.zoom_out)),
            IconButton(
                tooltip: 'Zoom in',
                onPressed: () => _zoom(1.5),
                icon: const Icon(Icons.zoom_in)),
            IconButton(
                tooltip: 'Reset zoom',
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
                            widget.caption ?? 'Educational diagram')),
              ),
            ),
            Padding(
              padding: const EdgeInsets.all(16),
              child: Text(widget.caption ?? 'Pinch to zoom • Drag to explore',
                  textAlign: TextAlign.center),
            ),
          ]),
        ),
      );
}
