# 5. Создать (программно) текстовый файл,
# записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.

f_obj = open("practice_5.5.txt", 'w+', encoding='utf-8')
# line = input('Введите цифры через пробел: ')
line = '1 2 3 4 5'
# print(type(line))
f_obj.writelines(line)
f_obj.close()

with open('practice_5.5.txt', 'rt', encoding='utf-8') as f_obj:
    sum = 0
    list_obj = f_obj.readlines()
    list_obj = list_obj[0].split()
    for data in list_obj:
        sum += int(data)
    print('Сумма чисел из файла =', sum)
