# Домашка №2. Реализовать проект расчета суммарного расхода ткани на производство одежды. Основная сущность (класс)
# этого проекта — одежда, которая может иметь определенное название. К типам одежды в этом проекте относятся пальто и
# костюм. У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма). Это могут быть обычные
# числа: V и H, соответственно. Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто
# (V/6.5 + 0.5), для костюма (2 * H + 0.3). Проверить работу этих методов на реальных данных. Реализовать общий
# подсчет расхода ткани. Проверить на практике полученные на этом уроке знания: реализовать абстрактные классы для
# основных классов проекта, проверить на практике работу декоратора @property.

class Clothing:

    def __init__(self, title, get_size, get_height):
        self.title = title
        self.get_size = get_size
        self.get_height = get_height

    def size(self):
        return self.get_size/6.5 + 0.5

    def height(self):
        return 2 * self.get_height + 0.3

    @property
    def get_full(self):
        return str(f'Общий подсчёт расхода ткани {float("{0:.2f}".format((self.size()) + (self.height())))}')


class Coat(Clothing):

    def __str__(self):
        return f'Расчёт расхода ткани для Пальто - {float("{0:.2f}".format(self.size()))}'


class Suit(Clothing):

    def __str__(self):
        return f'Расчёт расхода ткани для Костюма - {float("{0:.2f}".format(self.height()))}'


p = int(input("Введите ваш размер для Пальто "))
s = int(input("Введите ваш рост для Костюма "))
a = Coat("Coat", p, s)
b = Suit("Suit", p, s)
c = Clothing("Cloth", p, s)
print(a)
print(b)
print(c.get_full)
