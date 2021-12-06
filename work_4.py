def my_func(x, y):
#     return x ** y
# print(my_func(7, 4))
    if(y == 1):
        return(x)
    if(y != 1):
        return(x * my_func(x, y - 1))
# x = int(input('Введите число:'))
# y = int(input('Введите его степень:'))
x = 7
y = 4
print(my_func(x, y))