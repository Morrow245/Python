class Car:
    name: str
    color: str
    speed: int
    is_police: bool

    def __init__(self, name, color, speed, is_police):
        self.name = name
        self.color = color
        self.speed = speed
        self.is_police = is_police

    def go(self):
        return f'начал движение'

    def stop(self):
        return f'остановился'

    def tern_r(self):
        return f'повернул направо'

    def tern_l(self):
        return f'повернул налево'

    def show_speed(self):
        return self.speed

class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            return f'превысил скорость'
        else:
            return self.speed

class SportCar(Car):
    def sport_car(self):
        return f'- sport car.'

class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            return f'превысил скорость'
        else:
            return self.speed

class PoliceCar(Car):
    def ispolice(self):
        if self.is_police is True:
            return "- police car."

mazda = TownCar("Mazda", "Red", 80, False)
kamaz = WorkCar("Kamaz", "Orange", 30, False)
dooge = SportCar("Dooge", "Yellow", 120, False)
laga = PoliceCar("Police Car", "Black", 100, True)

print(f'Марка городского авто: {mazda.name}.\nЦвет рабочей машины: {kamaz.color}. \nСкорость спортивного авто: {dooge.speed}км/ч.\nЛада - полицейский автомобиль: {laga.is_police}.')
print(f'Dooge {dooge.sport_car()}\nDooge {dooge.go()} и {dooge.tern_l()}.')
print(f'Mazda {mazda.show_speed()} и {mazda.stop()}.')
print(f'Kamaz {kamaz.tern_r()} и его скорость составляет сейчас {kamaz.show_speed()}км/ч.')
print(f'Lada {laga.ispolice()}')