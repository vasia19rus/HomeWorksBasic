# Домашка 4. Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name,
# is_police (булево). А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала,
# остановилась, повернула (куда). Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. Добавьте
# в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля. Для классов TownCar и
# WorkCar переопределите метод show_speed. При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться
# сообщение о превышении скорости. Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к
# атрибутам, выведите результат. Выполните вызов методов и также покажите результат.
from random import randint
import time


class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        return f"{self.name} Поехал вперёд!"

    def stop(self):
        return f"{self.name} Остановился"

    def turn_left(self):
        return f"{self.name} Повернул налево"

    def turn_right(self):
        return f"{self.name} Повернул направо"

    def show_speed(self):
        return f"{self.name} едет со скоростью {self.speed}!"

    def col(self):
        return f"{self.name} цвет машины {self.color}"

    def police(self):
        if self.is_police is True:
            return f"{self.name} Полицейская машина!"
        else:
            return f"{self.name} Не из полиции"


class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed > 60:
            return f"{self.name} едет со скоростью {self.speed}! - Это превышение скорости!"
        else:
            return f"{self.name} едет со скоростью {self.speed}! - Это нормальная скорость!"


class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed > 40:
            return f"{self.name} едет со скоростью {self.speed}! - Это превышение скорости!"
        else:
            return f"{self.name} едет со скоростью {self.speed}! - Это нормальная скорость!"


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


f = SportCar(randint(90, 130), "Красный", "\033[31mFerrari", False)
n = TownCar(randint(50, 80), "Желтый", "\033[33mTiida", False)
k = WorkCar(randint(30, 50), "Зеленый", "\033[32mKamaz", False)
p = PoliceCar(randint(80, 120), "Синий", "\033[34mDodge", True)

a = [f.col(), f.go(), f.show_speed(), f.turn_right(), f.turn_left(), f.stop(), f.police()]
b = [n.col(), n.go(), n.show_speed(), n.turn_left(), n.turn_right(), n.stop(), n.police()]
c = [k.col(), k.go(), k.show_speed(), k.turn_right(), k.turn_left(), k.stop(), k.police()]
d = [p.col(), p.go(), p.show_speed(), p.turn_left(), p.turn_right(), p.stop(), p.police()]

i = 0
while True:
    print(a[i])
    time.sleep(1)
    print(b[i])
    time.sleep(1)
    print(c[i])
    time.sleep(1)
    print(d[i])
    time.sleep(1)
    i += 1
    if i == 7 and p.speed > f.speed:
        print("\033[0mУ Полицейской машины скорость быстрее Феррари! Спорткар попался!")
    if i == 7 and p.speed < f.speed:
        print("\033[0mУ Феррари скорость больше чем у полицейского! Копы упустили свой шанс")
    if i == 7:
        break
