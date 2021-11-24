profit = float(input('Введите выручку фирмы:'))
costs = float(input('Введите издержки фирмы:'))
if profit > costs:
    input(f'Компания работает с пибылью. Выручка составила { profit - costs }')
    workers = int(input('Введите колличество сотудников'))
    print(f'пибыль на одного сотудника { profit / workers }')
elif profit == costs:
    print('Фирма работает в ноль')
else:
    print('Фирма работает в убыток')