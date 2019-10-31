import unittest
from ClusterMerge import ClusterMerge


class TestClusterMerge(unittest.TestCase):
    def test(self):
        config = {'k1': 1, 'k2': 1, 'max_dist': 0.01}
        merger = ClusterMerge(config)
        result = merger.merge(
            [
                [['a', 'b', 'c'], 1, []],
                [['x', 'y', 'z'], 3, []],
            ],
            [
                [['a', 'b', 'c'], 5, []],
                [['m', 'n', 'p'], 2, []],
            ],
        )
        self.assertEqual(result, [
            [['a', 'b', 'c'], 6, []],
            [['m', 'n', 'p'], 2, []],
            [['x', 'y', 'z'], 3, []]
        ])


if __name__ == '__main__':
    unittest.main()
