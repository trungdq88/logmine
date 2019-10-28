import multiprocessing


def mapper(x):
    print('work on', x)
    return x


class SingleFileProcessor():
    def __init__(self, filename, chunk_size=2):
        self.filename = filename
        self.pool = multiprocessing.Pool(processes=multiprocessing.cpu_count())
        self.chunk_size = chunk_size

    def process(self):

        with open(self.filename, 'r') as f:
            print self.pool.map(mapper, f, self.chunk_size)
