import os


def size_of(filename):
    return os.stat(filename).st_size


class Segmentator():
    """
    Try to break a list of filenames into multiple segment that can be
    scheduled optimally by multiprocessing pool.

    Currently, this uses a very simple strategy: break all files into
    "prefer_size" number of segments. This guarantee the number of segments
    can fit equally into all processes in a pool, but some cases will create
    unnecessary overhead as there are many small size files.

    TODO: Improve this.
    """
    def __init__(self, prefer_size=1):
        self.prefer_size = prefer_size

    def _split_file(self, file_with_size):
        (filename, size) = file_with_size
        n = self.prefer_size
        ranges = [(i * size // n, (i + 1) * size // n) for i in range(n)]
        return [(filename, r[0], r[1], size) for r in ranges]

    def create_segments(self, filenames):
        filename_with_sizes = [(f, size_of(f)) for f in filenames]
        result = []
        for f in filename_with_sizes:
            result.extend(self._split_file(f))
        return result
