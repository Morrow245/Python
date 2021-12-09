def gen1():
    a = int(input('Введите стартовое число: '))
    from itertools import islice
    from itertools import count

    for i in islice(count(a), 10):
        print(i)
gen1()

def gen2():
    my_list = [25, 31, None, 'abrakadabra']

    from itertools import islice
    from itertools import cycle

    for el in islice(cycle(my_list), 10):
        print(el)
gen2()