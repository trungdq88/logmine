from Clusterer import Clusterer
from alignment import create_pattern


class ClusterMerge():
    def __init__(self, config):
        self.clusterer = Clusterer(**config)

    def merge(self, base_list, other_list):
        for [reprA, countA, patternA] in other_list:
            exists = False
            for i in xrange(len(base_list)):
                [reprB, countB, patternB] = base_list[i]
                score = self.clusterer.scorer.distance(
                    reprA, reprB, self.clusterer.max_dist)
                if score <= self.clusterer.max_dist:
                    exists = True
                    base_list[i][1] += countA
                    merged_pattern = create_pattern(patternA, patternB)
                    # if len(merged_pattern) > 4 and patternA[2] == "sentry.tasks.process_buffer:":
                    #     print('merged_pattern (ClusterMerge)')
                    #     print(patternA, reprA)
                    #     print(patternB, reprB)
                    #     print('*')
                    #     print(merged_pattern)
                    #     print('---')
                    base_list[i][2] = merged_pattern
                    break
            if not exists:
                base_list.append([reprA, countA, reprA])
