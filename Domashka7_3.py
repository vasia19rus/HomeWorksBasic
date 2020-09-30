# Домашка №3. Реализовать программу работы с органическими клетками. Необходимо создать класс Клетка. В его
# конструкторе инициализировать параметр, соответствующий количеству клеток (целое число). В классе должны быть
# реализованы методы перегрузки арифметических операторов: сложение (__add__()), вычитание (__sub__()), умножение (
# __mul__()), деление (__truediv__()).Данные методы должны применяться только к клеткам и выполнять увеличение,
# уменьшение, умножение и обычное (не целочисленное) деление клеток, соответственно.
from random import randint
import math


class Cell:

    def __init__(self, cell):
        self.cell = cell

    def __add__(self, other):
        return f"Результат сложения двух клеток = {self.cell + other.cell}"

    def __sub__(self, other):
        if self.cell - other.cell > 0:
            return f"Результат вычитания двух клеток = {self.cell - other.cell}"
        else:
            return "Результат вычитания двух клеток меньше или равно 0"

    def __mul__(self, other):
        return f"Результат умножения двух клеток = {self.cell * other.cell}"

    def __truediv__(self, other):
        return f"Результат целочисленного деления двух клеток = {math.floor(self.cell / other.cell)}"

    def make_order(self, cells):
        row = ''
        for i in range(int(self.cell / cells)):
            row += f'{"*" * cells}\n'
        row += f'{"*" * (self.cell % cells)}'
        return row


a = randint(1, 10)
b = randint(1, 10)
c1 = Cell(a)
c2 = Cell(b)

print("Первая клетка " + str(a))
print("Вторая клетка " + str(b))
print(c1 + c2)
print(c1 - c2)
print(c1 * c2)
print(c1 / c2)
print()
print("Первая ячейка до 3 символов\n" + str(c1.make_order(3)))
print()
print("Вторая ячейка до 3 символов\n" + str(c2.make_order(3)))
