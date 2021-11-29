list = ('none', 'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Ser', 'Oct', 'Nov', 'Dec')
n = int(input('Введите порядковый номер месяца:'))
s = list[n]
my_dict = {'Jan': 1, 'Feb': 2, 'Mar': 3, 'Apr': 4, 'May': 5, 'Jun': 6, 'Jul': 7, 'Aug': 8, 'Ser': 9, 'Oct': 10, 'Nov': 11, 'Dec': 12}
a = my_dict[s]
if a == 1:
    print('Winter')
elif a == 2:
    print('Winter')
elif a == 12:
    print('Winter')
elif a == 3:
    print('Sping')
elif a == 4:
    print('Sping')
elif a == 5:
    print('Sping')
elif a == 6:
    print('Summer')
elif a == 7:
    print('Summer')
elif a == 8:
    print('Summer')
elif a == 9:
    print('Autumn')
elif a == 10:
    print('Autumn')
elif a == 11:
    print('Autumn')
else:
    print ('Error')
