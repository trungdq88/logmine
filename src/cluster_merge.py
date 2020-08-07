from .clusterer import Clusterer


class ClusterMerge():
    def __init__(self, config):
        self.clusterer = Clusterer(**config)
        self.pattern_generator = self.clusterer.pattern_generator

    def merge(self, base_list, other_list):
        for [reprA, countA, patternA] in other_list:
            exists = False
            for i in range(len(base_list)):
                [reprB, countB, patternB] = base_list[i]
                score = self.clusterer.scorer.distance(
                    reprA, reprB, self.clusterer.max_dist)
                if score <= self.clusterer.max_dist:
                    exists = True
                    base_list[i][1] += countA
                    merged_pattern = self.pattern_generator.create_pattern(
                            patternA, patternB)
                    base_list[i][2] = merged_pattern
                    break
            if not exists:
                base_list.append([reprA, countA, patternA])
