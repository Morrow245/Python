def int_func(s):
#     return s.title()
# print(int_func('snow'))
    a = s.split()
    for i in a:
        print(chr(ord(i[0]) - 32) + i[1:], end=' ')
print(int_func('hello world'))