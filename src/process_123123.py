import os
import multiprocessing
from Clusterer import Clusterer
from LineScorer import LineScorer
from FileSegmentReader import FileSegmentReader
from MapReduce import MapReduce


max_dist = 0.9
scorer = LineScorer(1, 1)
clusterer = Clusterer(max_dist=max_dist)


def map_segments_to_clusters(x):
    print('mapper: %s working on %s' % (os.getpid(), x))
    (filename, start, end, size) = x
    lines = FileSegmentReader.read(filename, start, end, size)
    clusters = clusterer.find(lines)
    return [(1, clusters)]


# TODO: 1 big key
def reduce_clusters(x):
    print('reducer: %s working on %s items' % (os.getpid(), len(x[1])))
    (key, clusters) = x
    if len(clusters) <= 1:
        return (key, clusters)

    tmp = clusters[0]
    for cluster in clusters[1:]:
        tmp = merge_clusters(tmp, cluster)
    return (key, tmp)


def merge_clusters(cluster1, cluster2):
    # print('merging %s-%s' % ((cluster1), (cluster2)))
    if len(cluster1) > len(cluster2):
        smaller = cluster2
        base_list = cluster1
    else:
        smaller = cluster1
        base_list = cluster2

    result = base_list[:]

    for [reprA, countA] in smaller:
        exists = False
        for i in range(len(result)):
            [reprB, countB] = result[i]
            score = scorer.distance(reprA, reprB)
            if score <= max_dist:
                exists = True
                result[i][1] += countA
                break
        if not exists:
            result.append([reprA, countA])

    return result


if __name__ == '__main__':
    # filename = 'a.log'
    filename = '/Users/tdinh/Desktop/sentry_logs/home/sentry/logs/sentry-worker.log.4'
    f = open(filename, 'r')
    f.seek(0, os.SEEK_END)
    size = f.tell()
    mapper = MapReduce(map_segments_to_clusters, reduce_clusters)
    n = multiprocessing.cpu_count()
    ranges = [(i * size / n, (i + 1) * size / n) for i in xrange(n)]
    result = mapper([(filename, r[0], r[1], size) for r in ranges])
    clusters = result[0][1]
    clusters = sorted(clusters, lambda x, y: y[1] - x[1])
    print('total', len(clusters))
    for [fields, count] in clusters:
        print(count, ' '.join(fields))
