from Clusterer import Clusterer


class LogMine():
    def __init__(self):
        self.clusterer = Clusterer(max_dist=0.8)

    def parse(self, f):
        clusters = self.clusterer.find(f)
        clusters = sorted(clusters, lambda x, y: y[1] - x[1])
        for [fields, count] in clusters:
            print(count, ' '.join(fields))


if __name__ == '__main__':
    text = ''
    with open('sentry-worker.log', 'r') as f:
        LogMine().parse(f)
