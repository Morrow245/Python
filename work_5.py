class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        f'Запуск отрисовки.'

class Pen(Stationery):
    def draw(self):
        return f'Запуск 1 инструмента - {self.title}'
class Pencil(Stationery):
    def draw(self):
        return f'Запуск 2 инструмента - {self.title}'
class Handle(Stationery):
    def draw(self):
        return f'Запуск 3 инструмента - {self.title}'

pen = Pen("ручка")
pencil = Pencil("карандаш")
handle = Handle("маркер")
print(pen.draw())
print(pencil.draw())
print(handle.draw())