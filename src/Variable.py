class Variable():
    def __init__(self, value):
        self.value = value

    def __eq__(self, other):
        return self.value == other.value

    def __repr__(self):
        return "'%s'" % self.value

    def __str__(self):
        return self.value
