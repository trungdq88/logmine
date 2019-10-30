from MapReduce import MapReduce

class He():
    def __init__(self, factor):
        self.factor = factor

    def m(self, x):
        return [(1, x * factor)]


    def r(self, x):
        return sum(x[1])

h = He(2)

mapper = MapReduce(h.m, h.r)
x = mapper([1, 2, 3, 4])
print(x)

