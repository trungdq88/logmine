from Variable import Variable


class LineScorer():
    def __init__(self, k1, k2):
        self.k1 = k1  # k1 if x=y and both are fixed value
        self.k2 = k2  # k2 if x=y and both are variable
        self.early_returned = False

    def distance(self, fields1, fields2, max_dist=None):
        if not (isinstance(fields1, list) and isinstance(fields2, list)):
            raise TypeError('Fields must be a list')

        max_len = max(len(fields1), len(fields2))
        min_len = min(len(fields1), len(fields2))

        total = 0
        for i in range(min_len):
            total += 1.0 * self.score(fields1[i], fields2[i]) / max_len

            # Early abandon
            if max_dist is not None and (1 - total) < max_dist:
                self.early_returned = True
                return (1 - total)

        self.early_returned = False
        return 1 - total

    def score(self, field1, field2):
        if (
            isinstance(field1, str) and
            isinstance(field2, str) and
            field1 == field2
        ):
            return self.k1

        if (
            isinstance(field1, Variable) and
            isinstance(field2, Variable) and
            field1 == field2
        ):
            return self.k2

        return 0
