# Домашка №5. Реализовать класс Stationery (канцелярская принадлежность). Определить в нем атрибут title (название) и
# метод draw (отрисовка). Метод выводит сообщение “Запуск отрисовки.” Создать три дочерних класса Pen (ручка),
# Pencil (карандаш), Handle (маркер). В каждом из классов реализовать переопределение метода draw. Для каждого из
# классов методы должен выводить уникальное сообщение. Создать экземпляры классов и проверить, что выведет описанный
# метод для каждого экземпляра.
import time
import random
import string

class Stationery:

    def __init__(self, title):
        self.title = title

    def draw(self):
        return f"Запуск отрисовки"


class Pen(Stationery):
    def draw(self):
        return f"Ну и каракули! {''.join(random.sample(string.ascii_lowercase,10))}"


class Pencil(Stationery):
    def draw(self):
        return f"Уже получше! {''.join(random.sample(string.ascii_lowercase,15))}"


class Handle(Stationery):
    def draw(self):
        return f"Маркером самое то! {''.join(random.sample(string.ascii_lowercase,25))}"


a = Pen("\033[31m{}".format("Пишем красной ручкой"))
b = Pencil("\033[37m{}".format("Пишем карандашом"))
c = Handle("\033[34m{}".format("Пишем синим маркером"))
s = Stationery("Учимся писать английские буквы!")
print(s.title)
o = [s.draw(), a.title, a.draw(), b.title, b.draw(), c.title, c.draw()]

i = 0
while True:
    time.sleep(1)
    print(o[i])
    time.sleep(1)
    i += 1
    if i == 7:
        time.sleep(1)
        print("\n\033[0mУроки рисования завершились!")
        break
