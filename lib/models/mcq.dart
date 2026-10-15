class MCQ {
  final String question;
  final List<String> options;
  final int correctIndex;
  final String? explanation;

  const MCQ({
    required this.question,
    required this.options,
    required this.correctIndex,
    this.explanation,
  });

  factory MCQ.fromJson(Map<String, dynamic> json) {
    return MCQ(
      question: json['question'] as String? ?? '',
      options: (json['options'] as List<dynamic>?)
              ?.map((e) => e.toString())
              .toList() ??
          [],
      correctIndex: json['correctIndex'] as int? ?? 0,
      explanation: json['explanation'] as String?,
    );
  }

  Map<String, dynamic> toJson() {
    return {
      'question': question,
      'options': options,
      'correctIndex': correctIndex,
      if (explanation != null) 'explanation': explanation,
    };
  }
}
