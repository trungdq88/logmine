import unittest

class SomeOtherClass:
    pass


class TestLegacyImport(unittest.TestCase):
    def test(self):
        from src import log_mine
        from src.log_mine import LogMine
        assert log_mine.LogMine == LogMine
        assert LogMine != SomeOtherClass