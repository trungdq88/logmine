import unittest
from Preprocessor import Preprocessor
from Variable import Variable


class TestPreprocessor(unittest.TestCase):
    def test(self):
        processor = Preprocessor([
            'name:/abc/'
        ])
        self.assertEqual(
            processor.process(['123', 'abc', '456']),
            ['123', Variable('name'), '456']
        )
        processor = Preprocessor([
            'ip:/\\d\\d\\d\\.\\d\\d\\d\\.\\d\\d\\d/'
        ])
        self.assertEqual(
            processor.process(['127.123.321.888', 'abc', '456']),
            [Variable('ip'), 'abc', '456']
        )

    def test_multiple_variable(self):
        processor = Preprocessor([
            'ip:/\\d\\d\\d\\.\\d\\d\\d\\.\\d\\d\\d/',
            'name:/abc/'
        ])
        self.assertEqual(
            processor.process(['127.123.321.888', 'abc', '456']),
            [Variable('ip'), Variable('name'), '456']
        )


if __name__ == '__main__':
    unittest.main()
