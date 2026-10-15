import 'package:flutter/material.dart';
import 'package:flutter_test/flutter_test.dart';
import 'package:setu_learning/widgets/markdown_content.dart';
import 'package:flutter_math_fork/flutter_math.dart';
import 'package:setu_learning/models/chapter.dart';
import 'package:setu_learning/widgets/content_block_widget.dart';

Future<String> rendered(WidgetTester tester, String input) async {
  await tester.pumpWidget(MaterialApp(
      home: Scaffold(
    body: MarkdownContent(data: input),
  )));
  return tester
      .widgetList<SelectableText>(find.byType(SelectableText))
      .map((text) => text.textSpan?.toPlainText() ?? text.data ?? '')
      .join('\n');
}

void main() {
  testWidgets('Formula blocks use the same fraction renderer', (tester) async {
    await tester.pumpWidget(const MaterialApp(
        home: Scaffold(
            body: ContentBlockWidget(
      block: ContentBlock(type: 'formula', value: r'\frac{a+b}{c}'),
    ))));
    expect(find.byType(Math), findsOneWidget);
    expect(tester.widget<Math>(find.byType(Math)).parseError, isNull);
  });

  testWidgets('Flattened answer headings and currency keep their meaning',
      (tester) async {
    final text = await rendered(
        tester, r'Answer --- ## Review - **Step:** Read. Amount \$100; 2 * 3.');
    expect(text, contains('Review'));
    expect(text, contains(r'$100'));
    expect(text, contains('2 * 3'));
    expect(text, isNot(contains('##')));
    expect(text, isNot(contains('**')));
    expect(find.byType(Math), findsNothing);
  });

  testWidgets('Long equations remain scrollable on a compact phone',
      (tester) async {
    tester.view.physicalSize = const Size(360, 800);
    tester.view.devicePixelRatio = 1;
    addTearDown(tester.view.resetPhysicalSize);
    addTearDown(tester.view.resetDevicePixelRatio);
    await rendered(tester,
        r'$$\frac{a+b+c+d+e+f+g+h+i+j+k+l}{x+y+z} = \sqrt{123456789}$$');
    expect(tester.takeException(), isNull);
    expect(find.byType(Math), findsOneWidget);
  });
  testWidgets(
      'Fractions and Hindi math labels render as math, without raw commands',
      (tester) async {
    final text = await rendered(tester, r'$\frac{3}{2}$ and $\text{प्रतिशत}$');
    expect(text, isNot(contains(r'$1')));
    expect(text, isNot(contains(r'\frac')));
    expect(find.byType(Math), findsNWidgets(2));
    for (final math in tester.widgetList<Math>(find.byType(Math))) {
      expect(math.parseError, isNull);
    }
    expect(tester.takeException(), isNull);
  });

  testWidgets('Nested fraction expressions are parsed completely',
      (tester) async {
    await rendered(tester, r'$\dfrac{\text{Total} + 1}{\frac{x}{y}}$');
    expect(find.byType(Math), findsOneWidget);
    expect(tester.widget<Math>(find.byType(Math)).parseError, isNull);
    expect(tester.takeException(), isNull);
  });

  testWidgets(
      'Nested bold and italic headings and blockquotes do not leak markers',
      (tester) async {
    final text = await rendered(tester,
        '### **Heading**\n\n> **Important:** ***Read carefully***\n\n* **Step:** Continue');
    expect(text, contains('Heading'));
    expect(text, contains('Read carefully'));
    expect(text, isNot(contains('*')));
    expect(text, isNot(contains('#')));
  });

  testWidgets('Ordinary punctuation and mathematical operators remain intact',
      (tester) async {
    expect(
        await rendered(tester, 'x + y = 5; ₹100; 20%'), 'x + y = 5; ₹100; 20%');
  });
}
