with open('f_py.txt', 'w+') as my_f:
    text= input('Введите текст:')
    while text:
        my_f.writelines(f'{text}\n')
        text = input('Введите тест: ')
        if not text:
            break
    my_f.seek(0)
    content = my_f.read()
    print(content)