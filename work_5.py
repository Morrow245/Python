n = int(input('Введите число:'))
my_list = [7, 4, 3, 2]
a = my_list.count(n)
for element in my_list:
    if a > 0:
        i = my_list.index(n)
        my_list.insert(i+a, n)
        break
    else:
        if n > element:
            j = my_list.index(element)
            my_list.insert(j, n)
            break
        elif n < my_list[len(my_list) - 1]:
            my_list.append(n)
print(my_list)