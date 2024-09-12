# Домашка №2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль. Проверьте его работу на
# данных, вводимых пользователем. При вводе пользователем нуля в качестве делителя программа должна корректно
# обработать эту ситуацию и не завершиться с ошибкой.

class DelZero:
    def __init__(self, num_1, num_2):
        self.num_1 = num_1
        self.num_2 = num_2

    @staticmethod
    def divide(num_1, num_2):
        try:
            return f"Результат деления {num_1 / num_2}"
        except ZeroDivisionError:
            return f"Нельзя делить на ноль!"


n1 = input("Введите первую цифру ")
while not n1.isnumeric():
    n1 = input("Введите первую цифру ")
n2 = input("Введите на какую цифру мы будем делить ? ")
while not n2.isnumeric():
    n2 = input("Введите на какую цифру мы будем делить ? ")
div = DelZero(int(n1), int(n2))
print(div.divide(int(n1), int(n2)))
