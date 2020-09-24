# Домашка № 5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.

from random import randint

shit = open('Domashka5_5_shitalka.txt', 'w', encoding='utf-8')
a = []
while True:
    a.append(randint(1, 100))
    if len(a) > 10:
        break

shit.writelines(" ".join(map(str, a)))

print("Случайный набор чисел: " + " ".join(map(str, a)))
print("Сумма случайных чисел: " + str(sum(a)))
