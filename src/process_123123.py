import os
from Clusterer import Clusterer
from LineScorer import LineScorer
from FileSegmentReader import FileSegmentReader
from MapReduce import MapReduce


max_dist = 0.8
scorer = LineScorer(1, 1)
clusterer = Clusterer(max_dist=max_dist)


def map_segments_to_clusters(x):
    (filename, start, end, size) = x
    lines = FileSegmentReader.read(filename, start, end, size)
    print('mapper: %s working on %s' % (os.getpid(), x), lines)
    clusters = clusterer.find(lines)
    return [(1, clusters)]


# TODO: 1 big key
def reduce_clusters(x):
    print('reducer: %s working on %s' % (os.getpid(), x))
    (key, clusters) = x
    if len(clusters) <= 1:
        return (key, clusters)

    tmp = clusters[0]
    for cluster in clusters[1:]:
        tmp = merge_clusters(tmp, cluster)
    return (key, tmp)


def merge_clusters(cluster1, cluster2):
    print('merge', cluster1, cluster2)
    if len(cluster1) > len(cluster2):
        smaller = cluster2
        base_list = cluster1
    else:
        smaller = cluster1
        base_list = cluster2

    result = base_list[:]

    for [reprA, count] in smaller:
        exists = False
        for i in range(len(result)):
            [reprB, _] = result[i]
            if scorer.distance(reprA, reprB) <= max_dist:
                exists = True
                result[i][1] += 1
                # Increase count
                break
        if not exists:
            print('adding', reprA)
            result.append([reprA, count])

    return result


if __name__ == '__main__':
    filename = 'a.log'
    f = open(filename, 'r')
    f.seek(0, os.SEEK_END)
    size = f.tell()

    # pool = Pool(processes=4)              # start 4 worker processes
    # f.close()
    # result = pool.map(
    #     process,
    #     [
    #         (filename, 0, size / 2, size),
    #         (filename, size / 2, size, size)
    #     ]
    # )
    #
    # print(result)
    #
    # with open('a.log', 'r') as f:
    #     print pool.map(process, f, 4)

    mapper = MapReduce(map_segments_to_clusters, reduce_clusters)
    result = mapper([
        (filename, 0, size / 4, size),
        (filename, size / 4, size / 2, size),
        (filename, size / 2, 3 * size / 4, size),
        (filename, 3 * size / 4, size, size)
    ])
    print(result)
