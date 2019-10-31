import unittest
import random
from Processor import Processor



class TestSameResultProcessor(unittest.TestCase):
    def setUp(self):
        sample_max_dist = random.randrange(70, 99) * 1.0 / 100
        print('sample == ', sample_max_dist)
        self.processor = Processor({'max_dist': sample_max_dist})

    def find_sorted_clusters(self, filename, process_func):
        clusters = process_func(filename)
        return sorted(clusters, lambda x, y: y[1] - x[1])

    def print_debug(self, clusters):
        print('===== PRINT DEBUG =====')
        for [fields, count] in clusters:
            print(count, ' '.join(map(str, fields)))

    def test_same_result(self):
        files = [
            'src/tests/HDFS_2k.log',
            'src/tests/Linux_2k.log',
        ]

        single_core_func = self.processor.process_single_core
        multi_core_func = self.processor.process

        for filename in files:
            a = self.find_sorted_clusters(filename, single_core_func)
            b = self.find_sorted_clusters(filename, multi_core_func)
            self.print_debug(a)
            self.print_debug(b)
            self.assertEqual(a, b)


if __name__ == '__main__':
    unittest.main()
