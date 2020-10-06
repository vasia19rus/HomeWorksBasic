# Домашка №1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата
# «день-месяц-год». В рамках класса реализовать два метода. Первый, с декоратором @classmethod, должен извлекать
# число, месяц, год и преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod, должен проводить
# валидацию числа, месяца и года (например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных
# данных.

class Data:
    def __init__(self, day_month_year):
        self.day_month_year = day_month_year

    @classmethod
    def extract(cls, day_month_year):
        my_date = []

        for i in day_month_year.split('-'):
            my_date.append(i)

        return [int(my_date[0]), int(my_date[1]), int(my_date[2])]

    @staticmethod
    def valid(day, month, year):
        mon1 = [1, 3, 5, 7, 8, 10, 12]
        mon2 = [1, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
        # Здесь мы учитываем, что 31 число бывает только по определенным месяцам!
        if day == 31 and month in mon1 and 0 <= year <= 2020:
            return f'Вы ввели правильный формат даты {day}.{month}.{year}'
        elif 1 <= day <= 28 and month == 2 and 0 <= year <= 2020:  # Февраль проверяем на наличие 28 числа!
            return f'Вы ввели правильный формат даты {day}.{month}.{year}'
        elif 1 <= day <= 30 and month in mon2 and 0 <= year <= 2020:
            return f'Вы ввели правильный формат даты {day}.{month}.{year}'  # Тут проверяем остальные месяца!
        else:
            return f'Вы ввели неправильный формат даты {day}.{month}.{year}'
        # На самом деле еще надо проверять високосный год на 29 февраля! Наверно это следующий уровень скилла=)

    def __str__(self):
        return f'Текущая дата {Data.extract(self.day_month_year)[0]}.' \
               f'{Data.extract(self.day_month_year)[1]}.' \
               f'{Data.extract(self.day_month_year)[2]}'


Day = Data('04-10-2020')
print(Day)
print("Проверим дату на корректность! ")
d = input("Введите день ")
while not d.isnumeric():
    d = input("Введите день ")
m = input("Введите месяц ")
while not m.isnumeric():
    m = input("Введите месяц ")
y = input("Введите год ")
while not y.isnumeric():
    y = input("Введите год ")
print(Day.valid(int(d), int(m), int(y)))

print(f"Катастрофа с башнями близнецами случилась {Day.extract('11-01-2001')[0]}."
      f"{Day.extract('11-01-2001')[1]}."
      f"{Day.extract('11-01-2001')[2]}")
