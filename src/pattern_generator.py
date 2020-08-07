from .vendor.alignment import water


class PatternPlaceholder(str):
    pass


class PatternGenerator():
    def __init__(self, placeholder='---'):
        self.placeholder = placeholder

    def create_pattern(self, a, b):
        if len(a) == 0 and len(b) == 0:
            return []
        (a, b) = water(a, b)
        new = []
        for i in range(len(a)):
            if a[i] == b[i]:
                new.append(a[i])
            else:
                new.append(PatternPlaceholder(self.placeholder))
        return new
