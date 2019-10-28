import os
from Clusterer import Clusterer
from multiprocessing import Pool
from FileSegmentReader import FileSegmentReader


clusterer = Clusterer(max_dist=0.8)


def process(x):
    (filename, start, end, size) = x
    lines = FileSegmentReader.read(filename, start, end, size)
    clusters = clusterer.find(lines)
    clusters = sorted(clusters, lambda x, y: y[1] - x[1])  # TODO
    return clusters


if __name__ == '__main__':
    pool = Pool(processes=4)              # start 4 worker processes

    filename = 'a.log'
    f = open(filename, 'r')
    f.seek(0, os.SEEK_END)
    size = f.tell()
    f.close()
    result = pool.map(
        process,
        [
            (filename, 0, size / 2, size),
            (filename, size / 2, size, size)
        ]
    )

    print(result)

    # with open('a.log', 'r') as f:
    #     print pool.map(process, f, 4)
