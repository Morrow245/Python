import sys
result = 0
while True:
    i = input('Введите чиcла через пробел: ')
    print('Для завешения введите #')
    tokens = i.split(' ')
    for i in tokens:
        try:
            s = float(i)
            result += s
        except:
            if i == 'q':
                print(f'Сумма чисел равна {result}. ')
                exit(0)
            else:
                print(f'Сумма чисел равна {result}. Программа завешена', file=sys.stderr)
                exit(1)
    print(result)
