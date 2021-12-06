def number(a, b):
    try:
        n = a / b
        return n
    except ZeroDivisionError:
        return 'Деление на ноль'
    except ValueError:
        return 'Введите другое число'
print( number(int(input('Введите значение x:')), int(input('Введите значение y:'))))