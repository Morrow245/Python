dict = {'One' : 'Один', 'Two' : 'Два', 'Three' : 'Три', 'Four' : 'Четыре'}
new_file = []
with open("f4.txt", "r", encoding='utf-8') as f:
    for i in f:
        i = i.split(' ', 1)
        new_file.append(dict[i[0]] + '  ' + i[1])
with open('f4_new.txt', 'r+', encoding='utf-8') as f2:
    f2.writelines(new_file)
    f2.seek(0)
    cont2 = f2.read()
    print(cont2)