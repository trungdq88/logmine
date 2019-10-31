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
        """
        Process the file in parallel with multiple processes.

        This is a little bit different than the approach described in the
        LogMine paper. Each "map job" is a chunk of multiple lines (instead of
        a single line), this helps utilizing multiprocessing better.

        Do note that this method may return different result in each run, and
        different with the other version "process_single_core". This is
        expected, as the result depends on the processing order - which is
        not guaranteed when tasks are performed in parallel.
        """

        # Check file length and split into multiple chunks
        with open(filename, 'r') as f:
            f.seek(0, os.SEEK_END)
            size = f.tell()
        n = multiprocessing.cpu_count()
        ranges = [(i * size / n, (i + 1) * size / n) for i in xrange(n)]

        # Perform clustering all chunks in parallel
        mapper = MapReduce(
            map_segments_to_clusters,
            reduce_clusters,
            params=self.config
        )
        result = mapper([(filename, r[0], r[1], size) for r in ranges])
        (key, clusters) = result[0]  # Should only contains one result
        return clusters

    def process_single_core(self, filename):
        """
        Process the file sequencially using 1 a single processor
        """
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
    """
    Because all map job have the same key, this reduce operation will be
    executed in one single processor. Most of the time, the number of clusters
    in this step is small so it is kind of acceptable.
    """
    # print('reducer: %s working on %s items' % (os.getpid(), len(x[0][1])))
    ((key, clusters_groups), config) = x
    if len(clusters_groups) <= 1:
        return (key, clusters_groups)  # Nothing to merge

    base_clusters = clusters_groups[0]
    merger = ClusterMerge(config)
    for clusters in clusters_groups[1:]:
        # print('merging %s-%s' % (len(base_clusters), len(clusters)))
        base_clusters = merger.merge(base_clusters, clusters)
    return (key, base_clusters)
