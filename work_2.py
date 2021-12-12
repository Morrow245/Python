with open('f2.txt', 'r') as f:
    cont = f.read()
    print(f'Содержимое файла: \n{cont}')
    f.seek(0)
    lines = f.readlines()
    print(f'Колличество строк: {len(lines)}')
    f.seek(0)
    for i in range(len(lines)):
        line = f.readline()
        words = line.split()
        print(f'Колличество слов в {i + 1} строке: {len(words)}')