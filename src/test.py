from Processor import Processor
# from Variable import Variable
# from alignment import create_pattern

# print(create_pattern(['a',Variable('x'), 'b', 'c'], ['a','c','b']))


def debug_print(clusters):
    print("------------")
    clusters = sorted(clusters, lambda x, y: y[1] - x[1])
    for [fields, count, pattern] in clusters:
        print(
            count,
            ' '.join(map(str, pattern)),
            ' '.join(map(str, fields))
        )
    print('total', len(clusters))


if __name__ == '__main__':
    max_dist = 0.7
    # f = 'big.log'
    # f = 'Linux_2k.log'
    f = 'a.log'
    # f = '/Users/tdinh/desktop-archives/2019-11-02/sentry_logs/home/sentry/logs/sentry-worker.log'
    singles = Processor({'max_dist': max_dist}).process(f)
    debug_print(singles)
