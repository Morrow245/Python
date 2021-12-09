def salary_1():
    try:
        time = float(input('Выработка в часах:'))
        salary = float(input('Ставка в час:'))
        bonus = float(input('Премия:'))
        result = time * salary + bonus
        print(f'Заработная плата сотрудника {result}')
    except ValueError:
        return print('Введите числовое значение')
salary_1()