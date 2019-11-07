from PatternGenerator import PatternPlaceholder
from Variable import Variable


CRED = '\33[31m'
CYELLOW = '\33[33m'
CEND = '\033[0m'


class Output():
    def __init__(self, options):
        self.options = options

    def out(self, clusters):
        if len(clusters) == 0:
            return

        if self.options.get('sorted') == 'desc':
            clusters = sorted(clusters, lambda x, y: y[1] - x[1])
        if self.options.get('sorted') == 'asc':
            clusters = sorted(clusters, lambda x, y: x[1] - y[1])

        if self.options.get('number_align') is True:
            width = max([len(str(c[1])) for c in clusters])
        else:
            width = 0

        for [fields, count, pattern] in clusters:
            output = []
            # Note: the length of "fields" can be different with the length of
            # "pattern", this is because with a large max_dist config, many
            # different lines are put into the same cluster, thus the pattern
            # is not accurate. For cases like this, just print the fields.
            if len(fields) != len(pattern):
                output = fields
            else:
                for i in xrange(len(fields)):
                    field = fields[i]
                    if isinstance(pattern[i], PatternPlaceholder):
                        placeholder = self.options.get('pattern_placeholder')
                        if placeholder is None:
                            value = field
                        else:
                            value = placeholder
                        if self.options.get('highlight_patterns') is True:
                            value = CRED + value + CEND
                        output.append(value)
                    elif isinstance(pattern[i], Variable):
                        if self.options.get('mask_variables') is True:
                            value = str(field)
                        else:
                            value = field.name
                        if self.options.get('highlight_varibales') is True:
                            value = CYELLOW + value + CEND
                        output.append(value)
                    else:
                        output.append(field)
            print('%s %s' % (str(count).rjust(width), ' '.join(output)))
