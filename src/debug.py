import os


def log(*args):
    if 'VERBOSE' in os.environ:
        print(args)
