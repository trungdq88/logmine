import os


class FileSegmentReader():
    @staticmethod
    def read(filename, start, end, size=None):
        f = open(filename, 'r')

        if size is None:
            f.seek(0, os.SEEK_END)
            size = f.tell()

        f.seek(start, os.SEEK_SET)
        if start != 0:
            while True:  # skip until next line
                c = f.read(1)
                if c == '\n':
                    break

        data = f.read(end-start).split('\n')

        incomplete_line = data[-1] != ''

        if data[-1] == '':
            data = data[:-1]  # Remove last empty line

        if end != size and incomplete_line:
            while True:  # read until next line
                c = f.read(1)
                if c == '\n':
                    break
                data[-1] = data[-1] + c

        f.close()
        return data
