# Домашка №4,5,6. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. А также класс
# «Оргтехника», который будет базовым для классов-наследников. Эти классы — конкретные типы оргтехники (принтер,
# сканер, ксерокс). В базовом классе определить параметры, общие для приведенных типов. В классах-наследниках
# реализовать параметры, уникальные для каждого типа оргтехники.
# 5. Продолжить работу над первым заданием.
# Разработать методы, отвечающие за приём оргтехники на склад и передачу в определенное подразделение компании. Для
# хранения данных о наименовании и количестве единиц оргтехники, а также других данных, можно использовать любую
# подходящую структуру, например словарь.
# 6. Продолжить работу над вторым заданием. Реализуйте механизм валидации
# вводимых пользователем данных. Например, для указания количества принтеров, отправленных на склад,
# нельзя использовать строковый тип данных. Подсказка: постарайтесь по возможности реализовать в проекте «Склад
# оргтехники» максимум возможностей, изученных на уроках по ООП.
class Stock:

    def __init__(self, q1, q2, q3):
        self.printers = {"HP": q1, "Epson": q2, "Canon": q3}
        self.scaners = {"Plustek": q1, "Fujitsu": q2, "Avision": q3}
        self.mfus = {"Xerox": q1}

    @staticmethod
    def get_printer(self):
        return f"Текущее количество принтеров на складе {self.printers}"

    @staticmethod
    def get_scaner(self):
        return f"Текущее количество сканеров на складе {self.scaners}"

    @staticmethod
    def get_mfu(self):
        return f"Текущее количество ксероксов на складе {self.mfus}"


class Org:
    def __init__(self, p1, p2, p3):
        self.printer = {"HP": p1, "Epson": p2, "Canon": p3}
        self.scaner = {"Plustek": p1, "Fujitsu": p2, "Avision": p3}
        self.mfus = {"Xerox": p1}

    @staticmethod
    def get_price_printer(self):
        i = int(input("Введите 1 если хотите посмотреть цену принтера HP, 2 - Epson, 3 - Canon ")) - 1
        if i == 0:
            return f"Цена принтера HP {self.printer.get('HP')}"
        if i == 1:
            return f"Цена принтера Epson {self.printer.get('Epson')}"
        if i == 2:
            return f"Цена принтера Canon {self.printer.get('Canon')}"

    @staticmethod
    def get_price_scaner(self):
        i = int(input("Введите 1 если хотите посмотреть цену сканера Plustek, 2 - Fujitsu, 3 - Avision ")) - 1
        if i == 0:
            return f"Цена сканера Plustek {self.scaner.get('Plustek')}"
        if i == 1:
            return f"Цена сканера Fujitsu {self.scaner.get('Fujitsu')}"
        if i == 2:
            return f"Цена сканера Avision {self.scaner.get('Avision')}"

    @staticmethod
    def get_price_mfu(self):
        i = int(input("Введите 1 если хотите посмотреть цену ксерокса Xerox, 2 - если не хотите ")) - 1
        if i == 0:
            return f"Цена ксерокса {self.mfus.get('Xerox')}"
        if i == 1:
            return f"Не хотите, не надо"


class Printer(Stock):

    @classmethod
    def to_print(cls):
        return f"Распечатываю - полностью рабочий аппарат!"


class Scan(Stock):

    @classmethod
    def to_scan(cls):
        return f"Сканирую - полностью рабочий аппарат!"


class Mfu(Stock):

    @classmethod
    def to_copy(cls):
        return f"Копирую - полностью рабочий аппарат!"


p = [50, 25, 10]
s = [19, 18, 17]
m = [5]
new_p = Printer(p[0], p[1], p[2])
new_s = Scan(s[0], s[1], s[2])
new_m = Mfu(m[0], None, None)
print("Кладовщик! У нас партия товаров оргтехники! Надо раскидать по складу!")
print(Stock.get_printer(new_p))
p[0] += int(input("Сколько привезли новых принтеров HP ? "))
p[1] += int(input("Сколько привезли новых принтеров Epson ? "))
new_p = Printer(p[0], p[1], p[2])
print(Stock.get_printer(new_p))
print(Stock.get_scaner(new_s))
s[0] += int(input("Сколько привезли новых сканеров Plustek ? "))
s[1] += int(input("Сколько привезли новых сканеров Fujitsu ? "))
new_s = Scan(s[0], s[1], s[2])
print(Stock.get_scaner(new_s))
print(Stock.get_mfu(new_m))
m[0] += int(input("Сколько привезли новых ксероксов Xerox ? "))
new_m = Mfu(m[0], None, None)
print(Stock.get_mfu(new_m))
print("----------------------------------------")
print("Кладовщик ты свободен можешь идти домой!")
p1 = {"HP": 12500, "Epson": 13500, "Canon": 14500}
p2 = {"Plustek": 5000, "Fujitsu": 6000, "Avision": 7000}
p3 = {"Xerox": 33000}
p1_price = Org(p1.get('HP'), p1.get('Epson'), p1.get('Canon'))
p2_price = Org(p2.get('Plustek'), p2.get('Fujitsu'), p2.get('Avision'))
p3_price = Org(p3.get('Xerox'), None, None)
to_print = Printer
to_scan = Scan
to_copy = Mfu
print("--------------------------------------------")
print("ДОБРО ПОЖАЛОВАТЬ В НАШ МАГАЗИН ОРГТЕХНИКИ!!!")
print("--------------------------------------------")
user_p = input("Хотите купить Принтер нажмите - 1, Сканер - 2, Ксерокс - 3 ")
while not user_p.isnumeric():
    user_p = input("Хотите купить Принтер нажмите - 1, Сканер - 2, Ксерокс - 3 ")
if user_p == '1':
    print(f"{Org.get_price_printer(p1_price)} рублей |..{to_print.to_print()}")
    user_b = input("Хотите купить ? нажмите Y - если да ").lower()
    if user_b == 'y':
        print("Поздравляю с покупкой принтера !")
    print("Вы вышли из магазина без покупки!")
if user_p == '2':
    print(f"{Org.get_price_scaner(p2_price)} рублей |..{to_scan.to_scan()}")
    user_b = input("Хотите купить ? нажмите Y - если да ").lower()
    if user_b == 'y':
        print("Поздравляю с покупкой сканера !")
    print("Вы вышли из магазина без покупки!")
if user_p == '3':
    print(f"{Org.get_price_mfu(p3_price)} рублей |..{to_copy.to_copy()}")
    user_b = input("Хотите купить ? нажмите Y - если да ").lower()
    if user_b == 'y':
        print("Поздравляю с покупкой ксерокса !")
    print("Вы вышли из магазина без покупки!")
