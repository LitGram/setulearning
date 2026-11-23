import 'mcq.dart';

class ContentBlock {
  final String type; // 'text', 'image', 'callout', 'formula', 'heading'
  final String value;
  final String? caption;

  const ContentBlock({
    required this.type,
    required this.value,
    this.caption,
  });

  factory ContentBlock.fromJson(Map<String, dynamic> json) {
    return ContentBlock(
      type: json['type'] as String? ?? 'text',
      value: json['value'] as String? ?? '',
      caption: json['caption'] as String?,
    );
  }

  Map<String, dynamic> toJson() {
    return {
      'type': type,
      'value': value,
      if (caption != null) 'caption': caption,
    };
  }
}

class Chapter {
  final String id;
  final String title;
  final String? subtitle;
  final List<ContentBlock> content;
  final List<MCQ> mcqs;

  const Chapter({
    required this.id,
    required this.title,
    this.subtitle,
    required this.content,
    required this.mcqs,
  });

  factory Chapter.fromJson(Map<String, dynamic> json) {
    return Chapter(
      id: json['id'] as String? ?? '',
      title: json['title'] as String? ?? '',
      subtitle: json['subtitle'] as String?,
      content: (json['content'] as List<dynamic>?)
              ?.map(
                  (item) => ContentBlock.fromJson(item as Map<String, dynamic>))
              .toList() ??
          [],
      mcqs: (json['mcqs'] as List<dynamic>?)
              ?.map((item) => MCQ.fromJson(item as Map<String, dynamic>))
              .toList() ??
          [],
    );
  }

  Map<String, dynamic> toJson() {
    return {
      'id': id,
      'title': title,
      if (subtitle != null) 'subtitle': subtitle,
      'content': content.map((c) => c.toJson()).toList(),
      'mcqs': mcqs.map((m) => m.toJson()).toList(),
    };
  }
}
