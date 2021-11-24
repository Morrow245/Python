n = int(input('Введите число:'))
Max = n % 10
while n >= 1:
    n = n // 10
    if n % 10 > Max:
        Max = n % 10
    if n > 9:
        continue
    else:
        print('Максимальная цифра', Max)
        break
