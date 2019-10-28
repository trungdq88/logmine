import re
from Preprocessor import Preprocessor
from LineScorer import LineScorer


VARIABLES = [
    ('<ip>', '\\d{3}\\.\\d{3}\\.\\d{3}\\.\\d{3}'),
    ('<date>', '\\d{4}-\\d{2}-\\d{2}'),
    ('<time>', '\\d{2}:\\d{2}(:\\d{2})?'),
    ('<number>', '\\d+'),
]


class Clusterer():
    def __init__(self, k1=1, k2=1, max_dist=0.01, variables=[]):
        self.preprocessor = Preprocessor(variables)
        self.scorer = LineScorer(k1, k2)
        self.max_dist = max_dist
        self.clusters = []

    def reset(self):
        self.clusters = []

    def process_line(self, line):
        tokens = re.split('\\s+', line)
        processed_tokens = self.preprocessor.process(tokens)

        found = False
        for i in range(len(self.clusters)):
            [representative, count] = self.clusters[i]
            score = self.scorer.distance(
                representative, processed_tokens, self.max_dist
            )
            if score < self.max_dist:
                found = True
                self.clusters[i][1] += 1
                break
        if not found:
            self.clusters.append([processed_tokens, 1])

    def find(self, iterable_logs):
        self.reset()
        for line in iterable_logs:
            self.process_line(line)
        return self.clusters
