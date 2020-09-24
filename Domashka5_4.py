# Домашка № 4. Создать (не программно) текстовый файл со следующим содержимым: One — 1 Two — 2 Three — 3 Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные. При этом английские
# числительные должны заменяться на русские. Новый блок строк должен записываться в новый текстовый файл.

from googletrans import Translator

file_translate = Translator()
f = open('Domashka5_4_translate.txt', 'r')
contents = f.read()
print("Оригинальное содержимое файла\n" + str(contents))
result = file_translate.translate(contents, dest='ru')
print("Перевод на русский язык\n" + str(result.text))
print("\nnew_translate.txt - ищите его в папке в которой работаете")
with open('Domashka5_4_new_translate.txt', 'x') as f:
    f.write(result.text)
