import os
import multiprocessing
from Clusterer import Clusterer
from ClusterMerge import ClusterMerge
from FileSegmentReader import FileSegmentReader
from MapReduce import MapReduce

FIXED_MAP_JOB_KEY = 1  # Single key for the whole map-reduce operation


class Processor():
    def __init__(self, config):
        self.config = config

    def process(self, filename):
        f = open(filename, 'r')
        f.seek(0, os.SEEK_END)
        size = f.tell()
        mapper = MapReduce(
            map_segments_to_clusters,
            reduce_clusters,
            params=self.config
        )
        n = multiprocessing.cpu_count()
        ranges = [(i * size / n, (i + 1) * size / n) for i in xrange(n)]
        result = mapper([(filename, r[0], r[1], size) for r in ranges])
        return result[0][1]

    def process_single_core(self, filename):
        clusterer = Clusterer(**self.config)
        with open(filename, 'r') as f:
            return clusterer.find(f)

# The methods below are used by multiprocessing.Pool and need to be defined at
# top level


def map_segments_to_clusters(x):
    # print('mapper: %s working on %s' % (os.getpid(), x))
    ((filename, start, end, size), config) = x
    clusterer = Clusterer(**config)
    lines = FileSegmentReader.read(filename, start, end, size)
    clusters = clusterer.find(lines)
    return [(FIXED_MAP_JOB_KEY, clusters)]


def reduce_clusters(x):
    # print('reducer: %s working on %s items' % (os.getpid(), len(x[1])))
    ((key, clusters_groups), config) = x
    if len(clusters_groups) <= 1:
        return (key, clusters_groups)

    base_clusters = clusters_groups[0]
    merger = ClusterMerge(config)
    for clusters in clusters_groups[1:]:
        # print('merging %s-%s' % (len(base_clusters), len(clusters)))
        base_clusters = merger.merge(base_clusters, clusters)
    return (key, base_clusters)
