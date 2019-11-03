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

        for field in fields:
            matched = False
            for (name, regex) in self.variables:
                if re.match(regex, field):
                    matched = Variable(name, field)
                    break

            if matched:
                result.append(matched)
            else:
                result.append(field)
        return result
