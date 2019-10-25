import re
from Clusterer import Clusterer


class LogMine():
    def __init__(self):
        self.clusterer = Clusterer()

    def parse(self, text):
        clusters = self.clusterer.find(text.split('\n'))
        print('\n'.join(map(lambda cluster: ' '.join(map(lambda x: str(x), cluster)), clusters)))


if __name__ == '__main__':
    text = ''
    with open('src/sentry-worker.log', 'r') as f:
        text = f.read()
    LogMine().parse(text)
