import unittest
from Clusterer import Clusterer


class TestClusterer(unittest.TestCase):
    def test(self):
        clusterer = Clusterer(k1=1, k2=1, max_dist=0.5, variables=[])
        clusters = clusterer.find([
            'hello 1 y 3',
            'hello 1 x 3',
            'abc m n q',
        ])
        self.assertEqual(
            clusters,
            [
                [['hello', '1', 'y', '3'], 2, ['hello', '1', '---', '3']],
                [['abc', 'm', 'n', 'q'], 1, ['abc', 'm', 'n', 'q']]
            ]
        )

    def test_min_members(self):
        clusterer = Clusterer(
            k1=1, k2=1, max_dist=0.5, variables=[], min_members=2)
        clusters = clusterer.find([
            'hello 1 y 3',
            'hello 1 x 3',
            'abc m n q',
        ])
        self.assertEqual(
            clusters,
            [
                [['hello', '1', 'y', '3'], 2, ['hello', '1', '---', '3']],
            ]
        )

    def test_small_max_dist(self):
        clusterer = Clusterer(k1=1, k2=1, max_dist=0.01, variables=[])
        clusters = clusterer.find([
            'hello 1 y 3 ',
            'hello 1 x 3 ',
            'abc m n q ',
        ])
        self.assertEqual(
            clusters,
            [
                [['hello', '1', 'y', '3'], 1, ['hello', '1', 'y', '3']],
                [['hello', '1', 'x', '3'], 1, ['hello', '1', 'x', '3']],
                [['abc', 'm', 'n', 'q'], 1, ['abc', 'm', 'n', 'q']]
            ]
        )


if __name__ == '__main__':
    unittest.main()
