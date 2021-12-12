with open('f3.txt', 'rt', encoding = 'utf-8') as f:
    cont = f.readlines()
    f.seek(0)
    sal = []
    for i in range(len(cont)):
        line = f.readline()
        words = line.split()
        if float(words[1]) < 20000:
            print(words[0])
        sal.append(words[1])
    print(f'Средний доход сотудников: {sum(map(float, sal)) / len(sal)}')