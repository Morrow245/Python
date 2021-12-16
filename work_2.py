class Road():
    _length: int
    _width: int

    def __init__(self, _length, _width, mass, thickness):  # конструктор для приема переменных экземпляров
        self._length = _length
        self._width = _width
        self.thickness = thickness
        self.mass = mass

    def massa(self):
        return (self._length * self._width * self.mass * (self.thickness / 100)) * 0.1


m = Road(20, 5000, 25, 5)  # экземпляр
print(f'Масса асфальта: {m.massa()} тонн')


# если при создании экземпляра передаются только длина и ширина
class Road():
    _length: int
    _width: int

    def __init__(self, _length, _width):  # конструктор для приема переменных экземпляров
        self._length = _length
        self._width = _width

    def massa(self):
        mass = 25
        thickness = 5
        return (self._length * self._width * mass * (thickness / 100)) * 0.1


m = Road(20, 5000)  # экземпляр
print(f'Масса асфальта: {m.massa()} тонн')