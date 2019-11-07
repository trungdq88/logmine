import re
from Variable import Variable


class Preprocessor():
    def __init__(self, variables=[]):
        parsed_variables = []
        for variable in variables:
            parts = variable.split(':')
            if len(parts) <= 1:
                raise Exception('Invalid variable fortmat')
            name = parts[0]
            wrapped_regex = ':'.join(parts[1:])
            regex = wrapped_regex.split('/')[1]
            parsed_variables.append((name, regex))
        self.variables = map(
            lambda (name, regex): (name, re.compile(regex)),
            parsed_variables
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
