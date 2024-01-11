import timeit
import time

def test1():
    l = []
    for i in range(1000):
        l = l + [i]

t1 = timeit.timeit(stmt="test1()",setup='',number=1000,globals=globals())
t2 = timeit.timeit(stmt="test1()",setup='from __main__ import test1',number=1000)

print(t1)
print(t2)