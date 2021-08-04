# 4. Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.

rus = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
new_file = []
with open('practice_5.4.txt', 'r', encoding='utf-8') as file_obj_1:
    for el in file_obj_1:
        el = el.split(' ', 1)  # Split на первой запятой и разбиват только на 2 части.
        new_file.append(rus[el[0]] + ' ' + el[1])

with open('practice_5.4_new.txt', 'w', encoding='utf-8') as file_obj_2:
    file_obj_2.writelines(new_file)
