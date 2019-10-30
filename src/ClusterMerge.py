from Clusterer import Clusterer


class ClusterMerge():
    def __init__(self, config):
        self.clusterer = Clusterer(**config)

    def merge(self, clusters1, clusters2):
        if len(clusters1) > len(clusters2):
            smaller = clusters2
            base_list = clusters1
        else:
            smaller = clusters1
            base_list = clusters2

        result = base_list[:]

        for [reprA, countA] in smaller:
            exists = False
            for i in range(len(result)):
                [reprB, countB] = result[i]
                score = self.clusterer.scorer.distance(
                    reprA, reprB, self.clusterer.max_dist)
                if score <= self.clusterer.max_dist:
                    exists = True
                    result[i][1] += countA
                    break
            if not exists:
                result.append([reprA, countA])

        return result
