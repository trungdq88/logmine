import os


class FileSegmentReader():
    @staticmethod
    def read(filename, start, end, size=None):
        # print('read', filename, start, end)
        f = open(filename, 'r')

        if size is None:
            f.seek(0, os.SEEK_END)
            size = f.tell()

        f.seek(start, os.SEEK_SET)
        if start != 0:
            while True:  # skip until next line
                c = f.read(1)
                if f.tell() >= end:
                    f.close()
                    # print('returned')
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

        f.close()
        return data
