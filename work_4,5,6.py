class OfficeEquipment:

    def __init__(self, name, price, quantity, number_of_lists=None):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.numb = number_of_lists
        self.my_store_full = []
        self.my_store = []
        self.items = {'Модель устройства': self.name, 'Цена за единицу': self.price, 'Количество': self.quantity}

    def income(self):
        try:
            name = input(f'Введите наименование: ')
            price = int(input(f'Введите цену за единицу: '))
            quantity = int(input(f'Введите количество: '))
            item = {'Модель устройства': name, 'Цена за единицу': price, 'Количество': quantity}
            # self.items.update(item)
            # print(self.items)
            self.items.update(item)
            self.my_store.append(self.items)
            print(f'Текущий список -\n {self.my_store}')
        except ValueError:
            return f'Недопустимое значение!'

        print(f'Для выхода - Q, продолжение - Enter')
        q = input(f'---> ')
        if q == 'Q' or q == 'q':
            self.my_store_full.append(self.my_store)
            print(f'Весь склад -\n {self.my_store_full}')
            return f'Выход'
        else:
            return OfficeEquipment.income(self)

class Printer(OfficeEquipment):
    def to_print(self):
        return f'to print smth {self.numb} times'


class Scanner(OfficeEquipment):
    def to_scan(self):
        return f'to scan smth {self.numb} times'


class Copier(OfficeEquipment):
    def to_copier(self):
        return f'to copier smth  {self.numb} times'


unit_1 = Printer('hp', 2000, 5, 10)
unit_2 = Scanner('Canon', 1200, 5, 10)
unit_3 = Copier('Xerox', 1500, 1, 15)
print(unit_1.income())
print(unit_2.income())
print(unit_3.income())
print(unit_1.to_print())
print(unit_3.to_copier())