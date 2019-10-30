from Processor import Processor


if __name__ == '__main__':
    clusters = Processor(
        '/Users/tdinh/Desktop/sentry_logs/home/sentry/logs/sentry-worker.log'
    ).process()
    clusters = sorted(clusters, lambda x, y: y[1] - x[1])
    for [fields, count] in clusters:
        print(count, ' '.join(fields))
    print('total', len(clusters))
