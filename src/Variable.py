class Variable():
    def __init__(self, value, name=None):
        self.value = value
        self.name = name or value

    def __eq__(self, other):
        if isinstance(other, str):
            return self.value == other
        return self.value == other.value

    def __repr__(self):
        return "'%s'" % self.value

    def __str__(self):
        return self.value

    def __add__(self, other):
        return self.value + other

    def __radd__(self, other):
        return other + self.value
