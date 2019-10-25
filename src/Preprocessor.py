import re
from Variable import Variable


class Preprocessor():
    def __init__(self, variables=[]):
        self.variables = map(
            lambda (name, regex): (name, re.compile(regex)),
            variables
        )

    def process(self, fields):
        result = []

        if len(self.variables) == 0:
            return fields

        for (name, regex) in self.variables:
            for field in fields:
                if re.match(regex, field):
                    result.append(Variable(name))
                else:
                    result.append(field)
        return result
