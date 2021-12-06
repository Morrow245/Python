def my_func(a, b, c):
    n = [a, b, c]
    total = []
    max_1 = max(n)
    total.append(max_1)
    n.remove(max_1)
    max_2 = max(n)
    total.append(max_2)
    n.remove(max_2)
    print(sum(total))
my_func(9, 50, 80)