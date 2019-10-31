from Processor import Processor


if __name__ == '__main__':
    clusters = Processor({'max_dist': 0.9}).process(
        '/Users/tdinh/Desktop/sentry_logs/home/sentry/logs/sentry-worker.log'
    )
    clusters = sorted(clusters, lambda x, y: y[1] - x[1])
    for [fields, count] in clusters:
        print(count, ' '.join(map(str, fields)))
    print('total', len(clusters))
