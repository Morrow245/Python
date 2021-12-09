list_1 = [el for el in range(100, 1000) if el % 2 == 0]
print(list_1)
from functools import reduce
def my_func(el_p, el):
    return el_p * el
print(reduce(my_func, list_1))