import sys  
import re
import datetime
import getopt
from splunklib.searchcommands import dispatch, EventingCommand, Configuration  

@Configuration()  

class testpython(EventingCommand):  
    def __init__( self ):
        self.delimiters = "\\s"
        self.clusters = []
        self.k1 = 1
        self.k2 = 0.5
        self.contents = [] 
        self.m = 0.15
        self.match_award = 10
        self.mismatch_penalty = 1
        self.gap_penalty = 0
        self.placeholder = '---'
        self.listout = [{'frequency': 1, 'pattern': 2}]
        EventingCommand.__init__(self)

    def create_pattern(self, a, b):
        if len(a) == 0 and len(b) == 0:
            return []
        (a, b) = self.water(a, b)
        new = []
        for i in range(len(a)):
            if a[i] == b[i]:
                new.append(a[i])
            else:
                new.append(self.placeholder)
        return new

    def zeros(self, shape):
        retval = []
        for x in range(shape[0]):
            retval.append([])
            for y in range(shape[1]):
                retval[-1].append(0)
        return retval

    def match_score(self, alpha, beta):
        if alpha == beta:
            return self.match_award
        elif alpha is None or beta is None:
            return self.gap_penalty
        else:
            return self.mismatch_penalty
        return 0

    def finalize(self, align1, align2):
        align1.reverse()  # reverse sequence 1
        align2.reverse()  # reverse sequence 2

        i, j = 0, 0

        # calcuate identity, score and aligned sequeces
        symbol = ''
        found = 0
        score = 0
        identity = 0
        for i in range(0, len(align1)):
            # if two AAs are the same, then output the letter
            if align1[i] == align2[i]:
                symbol = symbol + align1[i]
                identity = identity + 1
                score += self.match_score(align1[i], align2[i])

            # if they are not identical and none of them is gap
            elif align1[i] != align2[i] and align1[i] is not None and align2[i] is not None:
                score += self.match_score(align1[i], align2[i])
                symbol += ' '
                found = 0

            # if one of them is a gap, output a space
            elif align1[i] is None or align2[i] is None:
                symbol += ' '
                score += self.gap_penalty

        identity = float(identity) / len(align1) * 100

        return align1, align2

    def water(self, seq1, seq2):
        m, n = len(seq1), len(seq2)  # length of two sequences

        # Generate DP table and traceback path pointer matrix
        score = self.zeros((m + 1, n + 1))  # the DP table
        pointer = self.zeros((m + 1, n + 1))  # to store the traceback path

        max_score = 0  # initial maximum score in DP table
        # Calculate DP table and mark pointers
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                score_diagonal = score[i - 1][j - 1] + self.match_score(seq1[i - 1], seq2[j - 1])
                score_up = score[i][j - 1] + self.gap_penalty
                score_left = score[i - 1][j] + self.gap_penalty
                score[i][j] = max(0, score_left, score_up, score_diagonal)
                if score[i][j] == 0:
                    pointer[i][j] = 0  # 0 means end of the path
                if score[i][j] == score_left:
                    pointer[i][j] = 1  # 1 means trace up
                if score[i][j] == score_up:
                    pointer[i][j] = 2  # 2 means trace left
                if score[i][j] == score_diagonal:
                    pointer[i][j] = 3  # 3 means trace diagonal
                if score[i][j] >= max_score:
                    max_i = i
                    max_j = j
                    max_score = score[i][j];

        align1 = []
        align2 = []  # initial sequences

        i, j = max_i, max_j  # indices of path starting point

        # traceback, follow pointers
        while pointer[i][j] != 0:
            if pointer[i][j] == 3:
                align1.append(seq1[i - 1])
                align2.append(seq2[j - 1])
                i -= 1
                j -= 1
            elif pointer[i][j] == 2:
                align1.append(None)
                align2.append(seq2[j - 1])
                j -= 1
            elif pointer[i][j] == 1:
                align1.append(seq1[i - 1])
                align2.append(None)
                i -= 1

        return self.finalize(align1, align2)

    def score(self, field1, field2):
        if (
            isinstance(field1, str) and
            isinstance(field2, str) and
            field1 == field2
        ):
            return self.k1
        elif (field1 == self.placeholder or field2 == self.placeholder):
            return self.k2

        return 0


    def distance(self, fields1, fields2, max_dist=None):
        if not( isinstance(fields1, list) and isinstance(fields2, list)):
            raise TypeError('Fields must be a list')

        max_len = max(len(fields1), len(fields2))
        min_len = min(len(fields1), len(fields2))

        total=0
        for i in range(min_len):
            total += 1.0 * self.score(fields1[i],fields2[i]) / max_len

        return 1 - total

    def scanInput( self ):
        for content in self.contents:
            content = re.sub('[0-9]*\.[0-9]*\.[0-9]*\.[0-9]*' , '<ip>', content)

            tokens = re.split(self.delimiters, content.strip())
            found = False
            for i in range(len(self.clusters)):
                [representative, count, all] = self.clusters[i]
                score = self.distance ( representative, tokens, 0.01)
                if score < float(self.m):
                    self.clusters[i][1] += 1
                    pattern = self.create_pattern(tokens, representative)
                    self.clusters[i][0] = pattern
                    found = True
                    break

            if not found:
                self.clusters.append([tokens, 1, []])

        sum = 0
        self.clusters.sort( key = lambda x: x[1])
        index = 0
        for cluster in self.clusters:
            patternStr = ' '.join(map(str, cluster[0]))
            self.listout.append({'frequency': repr(cluster[1]), 'pattern': repr(patternStr)})
            sum += cluster[1]
            index += 1



    def transform(self, records):
        listinp = list(records)
        for record in listinp :
            self.contents.append(record['_raw'])
        self.scanInput()
        return self.listout #self.contents

if __name__ == "__main__":
            dispatch(testpython, sys.argv, sys.stdin, sys.stdout, __name__)
