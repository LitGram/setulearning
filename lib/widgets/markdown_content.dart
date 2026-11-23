import 'package:flutter/material.dart';
import 'package:flutter_markdown_plus/flutter_markdown_plus.dart';
import 'package:flutter_math_fork/flutter_math.dart';
import 'package:markdown/markdown.dart' as md;

/// Native, offline Markdown and TeX rendering for lessons and practice.
class MarkdownContent extends StatelessWidget {
  final String data;
  final TextStyle? style;
  const MarkdownContent({super.key, required this.data, this.style});

  static String normalizeMath(String source) => source
      .replaceAll(r'\begin{align*}', r'\begin{aligned}')
      .replaceAll(r'\end{align*}', r'\end{aligned}')
      .replaceAll(r'\AA', 'Å');

  String _source() {
    var source = data.replaceAll('\u000crac', r'\frac');
    // Some imported answer explanations flattened headings and lists to one line.
    if (!source.contains('\n') && source.contains(' ##')) {
      source = source
          .replaceAll(' --- ', '\n\n---\n\n')
          .replaceAllMapped(RegExp(r'[ \t]+(#{1,6})[ \t]+'),
              (match) => '\n\n${match.group(1)} ')
          .replaceAll(' - **', '\n- **');
    }
    return source.replaceAll(
        RegExp(r'^\s*>\s*\[!(?:NOTE|TIP|IMPORTANT|WARNING|CAUTION)\]\s*$',
            multiLine: true),
        '>');
  }

  @override
  Widget build(BuildContext context) {
    final theme = Theme.of(context);
    final body = style ?? theme.textTheme.bodyLarge;
    return MarkdownBody(
      data: _source(),
      selectable: true,
      fitContent: false,
      extensionSet: md.ExtensionSet.gitHubFlavored,
      inlineSyntaxes: [_MathSyntax()],
      builders: {'study-math': _MathBuilder(body)},
      styleSheet: MarkdownStyleSheet.fromTheme(theme).copyWith(
          p: body,
          h1: theme.textTheme.headlineSmall,
          h2: theme.textTheme.titleLarge,
          h3: theme.textTheme.titleMedium,
          h4: theme.textTheme.titleSmall,
          h5: theme.textTheme.titleSmall,
          h6: theme.textTheme.titleSmall,
          blockquote: body,
          blockquoteDecoration: BoxDecoration(
              color: theme.colorScheme.primaryContainer.withValues(alpha: .2),
              border: Border(
                  left:
                      BorderSide(color: theme.colorScheme.primary, width: 3))),
          tableColumnWidth: const IntrinsicColumnWidth(),
          tableBody: body,
          tableCellsPadding: const EdgeInsets.all(12)),
    );
  }
}

class _MathSyntax extends md.InlineSyntax {
  _MathSyntax()
      : super(
            r'\$\$([\s\S]+?)\$\$|\$([^$\n]+?)\$|\\\(([\s\S]+?)\\\)|\\\[([\s\S]+?)\\\]');
  @override
  bool onMatch(md.InlineParser parser, Match match) {
    final expression =
        match.group(1) ?? match.group(2) ?? match.group(3) ?? match.group(4)!;
    final element = md.Element.text('study-math', expression);
    element.attributes['display'] =
        (match.group(1) != null || match.group(4) != null).toString();
    parser.addNode(element);
    return true;
  }
}

class _MathBuilder extends MarkdownElementBuilder {
  final TextStyle? style;
  _MathBuilder(this.style);
  @override
  Widget visitElementAfterWithContext(BuildContext context, md.Element element,
      TextStyle? preferredStyle, TextStyle? parentStyle) {
    final source = MarkdownContent.normalizeMath(element.textContent);
    final textStyle =
        (parentStyle ?? style ?? Theme.of(context).textTheme.bodyLarge)!
            .copyWith(color: Theme.of(context).colorScheme.onSurface);
    return Semantics(
        label: 'Equation: $source',
        child: SingleChildScrollView(
          scrollDirection: Axis.horizontal,
          child: Math.tex(source,
              mathStyle: element.attributes['display'] == 'true'
                  ? MathStyle.display
                  : MathStyle.text,
              textStyle: textStyle.copyWith(
                  fontSize: MediaQuery.textScalerOf(context)
                      .scale(textStyle.fontSize ?? 16)),
              onErrorFallback: (_) => Text(source, style: textStyle)),
        ));
  }
}
