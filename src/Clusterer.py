import re
from Preprocessor import Preprocessor
from LineScorer import LineScorer


# VARIABLES = [
#     ('version', 'v\\d+\\.\\d+\\.\\d+')
# ]

class Clusterer():
    def __init__(self, k1=1, k2=0, max_dist=0.9, variables=[]):
        self.preprocessor = Preprocessor(variables)
        self.scorer = LineScorer(k1, k2)
        self.max_dist = max_dist

    def find(self, iterable_logs):
        clusters = []
        c = 0
        for line in iterable_logs:
            c += 1
            # print('read', c)
            tokens = re.split('\\s+', line)
            processed_tokens = self.preprocessor.process(tokens)

            found = False
            for i in range(len(clusters)):
                [representative, count] = clusters[i]
                score = self.scorer.distance(
                    representative, processed_tokens, self.max_dist
                )
                if score < self.max_dist:
                    found = True
                    clusters[i][1] += 1
                    break
            if not found:
                clusters.append([processed_tokens, 1])
        return clusters
