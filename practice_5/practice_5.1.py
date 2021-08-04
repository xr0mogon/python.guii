# 1. Создать программно файл в текстовом формате,
# записать в него построчно данные, вводимые пользователем.
# Об окончании ввода данных свидетельствует пустая строка.

#####
# out_f = open("out_file.txt", "w")
# str_list = ['stroka_1\n', 'stroka_2\n', 'stroka_3\n']
# out_f.writelines(str_list)
# out_f.close()

#####
f_name = input('Название файла: ')
f = open(f_name, 'w')
print(f'{f.name}')
while True:
    s = input('Нажмите "Enter" для выхода из записи или введите текст: ')
    if not s: break
    f.write(s + '\n')
f.close()
print(f'Запись закрыта? {f.closed}')

# import os
# os.remove('123')
# os.remove('out_file.txt')
