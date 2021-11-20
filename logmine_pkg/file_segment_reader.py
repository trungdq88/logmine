import os


def isStartOfLine(offset, f):
    if offset == 0:
        return True
    crt_pos = f.tell()
    f.seek(crt_pos-1, os.SEEK_SET)
    return f.read(1) == '\n'


class FileSegmentReader():

    @staticmethod
    def read(filename, start, end, size=None):
        # print('read', filename, start, end)
        with open(filename, 'r') as f:

            if size is None:
                f.seek(0, os.SEEK_END)
                size = f.tell()

            f.seek(start, os.SEEK_SET)
            if not isStartOfLine(start, f):
                while True:  # skip until next line
                    c = f.read(1)
                    if f.tell() >= end:
                        # print('returned', f.tell())
                        return []
                    if c == '\n':
                        break

            # print('end=%s, start=%s, tell=%s' % (end, start, f.tell()))
            data = f.read(end - f.tell()).split('\n')
            # print('data=%s' % data)

            incomplete_line = data[-1] != ''

            if data[-1] == '':
                data = data[:-1]  # Remove last empty line

            if end != size and incomplete_line:
                while True:  # read until next line
                    c = f.read(1)
                    if c == '\n':
                        break
                    data[-1] = data[-1] + c
            # print('data=%s' % data)
            return data
