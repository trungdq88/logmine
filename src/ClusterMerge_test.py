import unittest
from ClusterMerge import ClusterMerge


class TestClusterMerge(unittest.TestCase):
    def test(self):
        config = {'k1': 1, 'k2': 1, 'max_dist': 0.01}
        merger = ClusterMerge(config)
        result = [
            [['a', 'b', 'c'], 1, []],
            [['x', 'y', 'z'], 3, []],
        ]
        merger.merge(
            result,
            [
                [['a', 'b', 'c'], 5, []],
                [['m', 'n', 'p'], 2, []],
            ],
        )
        self.assertEqual(result, [
            [['a', 'b', 'c'], 6, []],
            [['x', 'y', 'z'], 3, []],
            [['m', 'n', 'p'], 2, []]
        ])

    def test_merge_with_pattern(self):
        config = {'k1': 1, 'k2': 1, 'max_dist': 0.01}
        merger = ClusterMerge(config)
        result = [
            [['a', 'b', 'c'], 1, ['a', 'b', 'XXX']],
            [['x', 'y', 'z'], 3, ['x', 'y', 'XXX']],
        ]
        merger.merge(
            result,
            [
                [['a', 'b', 'c'], 5, ['a', 'b', 'XXX']],
                [['m', 'n', 'p'], 2, ['m', 'n', 'XXX']],
            ],
        )
        self.assertEqual(result, [
            [['a', 'b', 'c'], 6, ['a', 'b', 'XXX']],
            [['x', 'y', 'z'], 3, ['x', 'y', 'XXX']],
            [['m', 'n', 'p'], 2, ['m', 'n', 'XXX']]
        ])


if __name__ == '__main__':
    unittest.main()
