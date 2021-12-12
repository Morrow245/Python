import json
profit = {}
pr = {}
prof = 0
prof_aver = 0
i = 0
with open('f7.txt', 'r') as file:
    for line in file:
        name, form_ownership, earning, damage = line.split()
        profit[name] = int(earning) - int(damage)
        if profit.setdefault(name) >= 0:
            prof = prof + profit.setdefault(name)
            i += 1
    if i != 0:
        prof_aver = prof / i
        print(f'Прибыль средняя - {prof_aver:.2f}')
    else:
        print(f'Компании работают в убыток')
    pr = {'average profit': round(prof_aver)}
    profit.update(pr)
    print(f'Прибыль компаний - {profit}')

with open('f7.json', 'w') as write_js:
    json.dump(profit, write_js)
    js_str = json.dumps(profit)
    print(f'Создан файл с расширением json с содержимым: \n'
          f'{js_str}')