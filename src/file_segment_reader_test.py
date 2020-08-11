import unittest
from .file_segment_reader import FileSegmentReader


class TestFileSegmentReader(unittest.TestCase):
    FILE_A = 'src/tests/a.log.test'
    FILE_B = 'src/tests/b.log.test'

    def test_read_until_next_line(self):
        lines = FileSegmentReader.read(self.FILE_A, 0, 1)
        self.assertEqual(lines, ['111'])

        lines = FileSegmentReader.read(self.FILE_A, 0, 2)
        self.assertEqual(lines, ['111'])

        lines = FileSegmentReader.read(self.FILE_A, 0, 3)
        self.assertEqual(lines, ['111'])

        lines = FileSegmentReader.read(self.FILE_A, 0, 4)
        self.assertEqual(lines, ['111'])

        lines = FileSegmentReader.read(self.FILE_A, 0, 5)
        self.assertEqual(lines, ['111', '222'])

    def test_skip_until_next_line(self):
        lines = FileSegmentReader.read(self.FILE_A, 1, 1)
        self.assertEqual(lines, [])

        lines = FileSegmentReader.read(self.FILE_A, 1, 2)
        self.assertEqual(lines, [])

        lines = FileSegmentReader.read(self.FILE_A, 1, 3)
        self.assertEqual(lines, [])

        lines = FileSegmentReader.read(self.FILE_A, 1, 4)
        self.assertEqual(lines, [])

        lines = FileSegmentReader.read(self.FILE_A, 1, 5)
        self.assertEqual(lines, ['222'])

    def test(self):
        lines = FileSegmentReader.read(self.FILE_B, 0, 12)
        self.assertEqual(lines, ['11', '22', '33', '44aaaxa'])

        lines = FileSegmentReader.read(self.FILE_B, 12, 25)
        self.assertEqual(lines, ['55', '66', '77'])

        lines = FileSegmentReader.read(self.FILE_B, 25, 37)
        self.assertEqual(lines, ['88', '99', '10', '11'])

        lines = FileSegmentReader.read(self.FILE_B, 37, 50)
        self.assertEqual(lines, ['12', '13', '14', '15'])

    def test_start_of_line(self):
        lines = FileSegmentReader.read(self.FILE_B, 9, 14)
        self.assertEqual(lines, ['44aaaxa'])
