import unittest
from tempfile import mkstemp
from .segmentator import Segmentator


class TestSegmentator(unittest.TestCase):
    def _create_temp(self, content):
        _fd, path = mkstemp()
        with open(path, 'w') as f:
            f.write(content)
        return path

    def setUp(self):
        self.file1 = self._create_temp('hello')
        self.file2 = self._create_temp('abc')
        self.file3 = self._create_temp('123123123')
        self.files = [self.file1, self.file2, self.file3]

    def test_size_1(self):
        segmentator = Segmentator(1)
        segments = segmentator.create_segments(self.files)
        self.assertEqual(segments, [
            (self.file1, 0, 5, 5),
            (self.file2, 0, 3, 3),
            (self.file3, 0, 9, 9),
        ])

    def test_size_2(self):
        segmentator = Segmentator(2)
        segments = segmentator.create_segments(self.files)
        self.assertEqual(segments, [
            (self.file1, 0, 2, 5),
            (self.file1, 2, 5, 5),
            (self.file2, 0, 1, 3),
            (self.file2, 1, 3, 3),
            (self.file3, 0, 4, 9),
            (self.file3, 4, 9, 9),
        ])
