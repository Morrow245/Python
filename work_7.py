from itertools import count
from math import factorial
def fgen():
    for el in count(1):
        yield factorial(el)

gen = fgen()
n = 0
for elem in gen:
    if n < 6:
        print(elem)
        n += 1
    else:
        break