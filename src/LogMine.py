from Clusterer import Clusterer
from SingleFileProcessor import SingleFileProcessor


class LogMine():
    def __init__(self):
        self.clusterer = Clusterer(max_dist=0.8)
        self.processor = SingleFileProcessor('a.log')

    def run(self):
        self.processor.process()

    # def parse(self, f):
    #     clusters = self.clusterer.find(f)
    #     clusters = sorted(clusters, lambda x, y: y[1] - x[1])
    #     for [fields, count] in clusters:
    #         print(count, ' '.join(fields))


if __name__ == '__main__':
    LogMine().run()
