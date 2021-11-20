import re
from .preprocessor import Preprocessor
from .line_scorer import LineScorer
from .pattern_generator import PatternGenerator


class Clusterer():
    def __init__(
            self,
            k1=1,
            k2=1,
            max_dist=0.01,
            variables=[],
            delimeters='\\s',
            min_members=1):
        self.pattern_generator = PatternGenerator()
        self.delimeters = delimeters
        self.preprocessor = Preprocessor(variables)
        self.scorer = LineScorer(k1, k2)
        self.max_dist = max_dist
        self.min_members = min_members
        # Each cluster is an array of
        # [representative line as list of fields, count, pattern]
        self.clusters = []

    def reset(self):
        self.clusters = []

    def process_line(self, line):
        tokens = re.split(self.delimeters, line.strip())
        processed_tokens = self.preprocessor.process(tokens)

        found = False
        for i in range(len(self.clusters)):
            [representative, count, pattern] = self.clusters[i]
            score = self.scorer.distance(
                # representative, processed_tokens, self.max_dist
                representative, processed_tokens, self.max_dist
            )
            if score <= self.max_dist:
                found = True
                self.clusters[i][1] += 1
                merged_pattern = self.pattern_generator.create_pattern(
                    pattern, processed_tokens)
                self.clusters[i][2] = merged_pattern
                break
        if not found:
            self.clusters.append([processed_tokens, 1, processed_tokens])

    def result(self):
        if self.min_members > 1:
            return [c for c in self.clusters if c[1] >= self.min_members]
        else:
            return self.clusters

    def find(self, iterable_logs):
        self.reset()
        for line in iterable_logs:
            self.process_line(line)
        return self.result()
