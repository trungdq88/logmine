import unittest
import random
from .line_scorer import LineScorer
from .variable import Variable


class TestLineScorer(unittest.TestCase):
    def test_score(self):
        k1 = random.random()
        k2 = random.random()
        scorer = LineScorer(k1, k2)
        self.assertEqual(scorer.score('a', 'a'), k1)
        self.assertEqual(scorer.score('a', 'b'), 0)
        self.assertEqual(scorer.score(Variable('a'), 'b'), 0)
        self.assertEqual(scorer.score(Variable('a'), Variable('b')), 0)
        self.assertEqual(scorer.score(Variable('b'), Variable('b')), k2)

    def test_distance(self):
        scorer = LineScorer(k1=1, k2=0.5)
        self.assertEqual(
            scorer.distance(['a'], ['a']),
            0
        )

        self.assertEqual(
            scorer.distance(['a'], ['b']),
            1
        )

        self.assertEqual(
            scorer.distance(['a'], ['a', 'b']),
            0.5
        )

        self.assertEqual(
            scorer.distance(['a', 'c', 'c'], ['a', 'b', 'c']),
            1 - (1.0 / 3 + 1.0 / 3)
        )

        self.assertEqual(
            scorer.distance(
                ['a', 'c', Variable('c')],
                ['a', 'b', Variable('c')]
            ),
            1 - (1.0 / 3 + 0.5 / 3)
        )

        self.assertEqual(
            scorer.distance(
                ['a', 'c', Variable('c')],
                ['a', 'b', Variable('c')],
                1
            ),
            1 - (
                    1.0 / 3  # + 0.5 / 3
                )
        )

        self.assertTrue(scorer.early_returned)
