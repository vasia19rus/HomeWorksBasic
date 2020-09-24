# Домашка № 2. Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить подсчет количества
# строк, количества слов в каждой строке.

let_it_be = open('Domashka5_2_let it be.txt', 'r')
a = let_it_be.read()
print(f"Содержимое текста:\n{a}")
let_it_be.seek(0)
b = let_it_be.readlines()
print(f"\nКоличество строк в файле:\n{len(b)}\n")
i = 0
while i < len(b):
    spl = (b[i].split())
    print("Количество слов в " + str(i + 1) + " строке " + str(len(spl)))
    i += 1
let_it_be.close()
