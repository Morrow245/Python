def summary():
    with open("f5.txt", "w+") as f:
        line = input('введите числа через пробел : ')
        f.writelines(line)
        num = line.split()
        print(sum(map(float, num)))
summary()