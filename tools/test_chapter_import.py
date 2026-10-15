import unittest
from audit_chapter_completeness import reading_blocks
from recompile_ras_books import extract_reading_content


class ChapterImportTest(unittest.TestCase):
    def test_ras_lesson_keeps_all_teaching_and_revision(self):
        paragraphs = [f'Teaching paragraph {i}: MCQs use this concept.' for i in range(60)]
        source = '# Geography\n\n## भाग 1: अवधारणा\n\n' + '\n\n'.join(paragraphs)
        source += '\n\n## भाग 5: परीक्षा अभ्यास: बहुविकल्पीय प्रश्नोत्तरी\n\n'
        source += '#### प्रश्न 1\nQuiz stem\n(A) Wrong\n(B) Correct\n\n'
        source += '## भाग 6: क्विक रिवीजन\n\nRevision facts at the end.'
        actual = '\n'.join(b['value'] for b in extract_reading_content(source))
        for paragraph in paragraphs:
            self.assertIn(paragraph, actual)
        self.assertIn('Revision facts at the end.', actual)
        self.assertNotIn('Quiz stem', actual)

    def test_vigyan_part_five_and_worked_examples_are_teaching(self):
        source = '''# Science

## भाग 5: यह क्यों होता है?

The lesson explains scientific causes before MCQs.

## भाग 9: हल किए हुए उदाहरण

### प्रश्न 1
Worked example with a complete solution.

## भाग 11: अभ्यास प्रश्न बैंक

Practice-only question.

## भाग 12: विस्तृत उत्तर एवं वैज्ञानिक व्याख्या

Practice-only explanation.
'''
        actual = '\n'.join(b['value'] for b in reading_blocks(source))
        self.assertIn('scientific causes', actual)
        self.assertIn('Worked example with a complete solution.', actual)
        self.assertNotIn('Practice-only', actual)


if __name__ == '__main__':
    unittest.main()
