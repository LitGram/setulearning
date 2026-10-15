import json
import tempfile
import unittest
import zipfile
from pathlib import Path
from xml.etree import ElementTree as ET
from recover_english_docx import W, recover
from format_mcq_books import clean_book


class WordRecoveryTest(unittest.TestCase):
    def test_teaching_and_in_place_table_survive_cover_removal(self):
        document = ET.Element(W + 'document')
        body = ET.SubElement(document, W + 'body')

        def paragraph(parent, text):
            p = ET.SubElement(parent, W + 'p')
            ET.SubElement(ET.SubElement(p, W + 'r'), W + 't').text = text

        paragraph(body, 'Copyright and cover information')
        paragraph(body, 'Chapter 1 - Literary Devices')
        paragraph(body, 'Author: William Shakespeare. This is teaching metadata.')
        for i in range(60):
            paragraph(body, f'Complete explanation paragraph {i}.')
        table = ET.SubElement(body, W + 'tbl')
        for cells in [('Device', 'Example'), ('Simile', 'As bright as the sun')]:
            row = ET.SubElement(table, W + 'tr')
            for value in cells:
                paragraph(ET.SubElement(row, W + 'tc'), value)
        paragraph(body, 'Teaching immediately after the table.')
        paragraph(body, 'Chapter 2 - Poetic Forms')
        paragraph(body, 'A full explanation of the sonnet follows.')
        with tempfile.TemporaryDirectory(dir=Path(__file__).resolve().parents[1]) as directory:
            folder = Path(directory)
            source = folder / 'sample.docx'
            with zipfile.ZipFile(source, 'w') as archive:
                archive.writestr('word/document.xml', ET.tostring(document))
            asset = folder / 'sample.json'
            asset.write_text(json.dumps({'subject': 'EnglishSetu', 'book': 'Test', 'chapters': []}))
            # Report paths normally live inside the app workspace.
            data, report, _ = recover(asset, source)
            self.assertEqual(report['retainedTables'], 1)
            self.assertEqual(report['sourcePayloadSha256'], report['recoveredPayloadSha256'])
            self.assertEqual(len(data['chapters']), 2)
            values = [b['value'] for b in data['chapters'][0]['content']]
            self.assertIn('Author: William Shakespeare. This is teaching metadata.', values)
            self.assertIn('Complete explanation paragraph 59.', values)
            index = next(i for i, value in enumerate(values) if value.startswith('| Device'))
            self.assertEqual(values[index + 1], 'Teaching immediately after the table.')
            self.assertEqual(clean_book(data), data)


if __name__ == '__main__':
    unittest.main()
