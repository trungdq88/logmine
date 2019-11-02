import unittest
from PatternGenerator import PatternGenerator


class TestPatternGenerator(unittest.TestCase):
    def test(self):
        generator = PatternGenerator('XXX')
        pattern = generator.create_pattern(['a', 'b'], ['a', 'c'])
        self.assertEqual(pattern, ['a', 'XXX'])

    def test_with_gaps(self):
        generator = PatternGenerator('XXX')
        pattern = generator.create_pattern(['a', 'c', 'b'], ['a', 'b'])
        self.assertEqual(pattern, ['a', 'XXX', 'b'])
        pattern = generator.create_pattern(['a', 'c', 'b'], ['a', 'b', 'd'])
        self.assertEqual(pattern, ['a', 'XXX', 'b', 'XXX'])


if __name__ == '__main__':
    unittest.main()
