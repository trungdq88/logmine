import time
from Processor import Processor


def debug_print(clusters):
    print("------------")
    clusters = sorted(clusters, lambda x, y: y[1] - x[1])
    for [fields, count] in clusters:
        print(count, ' '.join(map(str, fields)))
    print('total', len(clusters))


if __name__ == '__main__':
    max_dist = 0.5
    for i in xrange(50, 100):
        max_dist = i * 1.0 / 100
        multis = Processor({'max_dist': max_dist}).process(
            'a.log'
        )
        print('i=', i)
        singles = Processor({'max_dist': max_dist}).process_single_core(
            'a.log'
        )
        debug_print(multis)
        debug_print(singles)
