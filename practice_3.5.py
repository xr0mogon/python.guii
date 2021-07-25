# 5. Программа запрашивает у пользователя строку чисел, разделенных пробелом.
# При нажатии Enter должна выводиться сумма чисел.
# Пользователь может продолжить ввод чисел, разделенных пробелом и снова нажать Enter.
# Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме.
# Но если вместо числа вводится специальный символ, выполнение программы завершается.
# Если специальный символ введен после нескольких чисел,
# то вначале нужно добавить сумму этих чисел к полученной ранее сумме и после этого завершить программу.
"""сделать ввод в цикле и посчитать сумму, проверять, если ввод == спец.символу то break"""


# def my_sum ():
#     sum_res = 0
#     ex = False
#     while ex == False:
#         number = input('Input numbers or Q for quit - ').split()
#
#         res = 0
#         for el in range(len(number)):
#             if number[el] == 'q' or number[el] == 'Q':
#                 ex = True
#                 break
#             else:
#                 res = res + int(number[el])
#         sum_res = sum_res + res
#         print(f'Current sum is {sum_res}')
#     print(f'Your final sum is {sum_res}')
#
#
# my_sum()


def my_sum():
    s = 0
    while True:
        try:
            print('Для выхода из программы введите: "Q/q" ')
            my_list = input('Для выполнения программы введите число или несколько чисел через пробел: ').split(' ')
            if my_list[-1] == 'q' or my_list[-1] == 'Q':  # проверка на спецсимвол
                my_list = my_list[0:len(my_list) - 1]
                print(f'Сумма чисел списка {my_list} и {s} = {sum(list(map(int, my_list))) + s}'
                      f'\nСложение выполнено и программа завершена!')
                break
            else:
                for element in map(int, my_list):
                    # каждый введённый элемент в нашем списке складывается с пердыдущим
                    # print(f'{element} + {s} = {n+s}')  # наглядный пример действия сложения
                    s += element  # и складывается с общим значением
                print(f'Сумма = {s}')
        except Exception as e:
            print('ВНИМАНИЕ! Не соблюдены условия ввода: ', e)
            break  # тут
'''
если не останавливать программу "# тут" и продолжать ввод, то она продолжает складывать числа,
а после возвращения в начало цикла сумма введенных значений остаётся в переменной s и складывается уже с
новыми вводимыми числами
как пофиксить пока не додумался ¯\_(ツ)_/¯ 
и так с этой програмой боролся более суток  。゜゜(´Ｏ) ゜゜。

'''

my_sum()

# while my_string[-1] != 'q':  # взятие первого элемента С КОНЦА строки
#     if len(my_string) <= 1:
#         num = num + (list(map(int, my_string)))
#         print(num)
#     else:
#         my_string = my_string[0:len(my_string)-1]
#         print(sum(list(map(int, my_string))))


# while True:
#     my_string = input('Запрос ввода: ').split(' ')
#     for n in list(map(int, my_string)):  # Запрос ввода + делим по пробелам
#          print(my_string)
#          s += n
#          print(my_string)
# s = 0


# try:
#     while True:
#         for n in map(int, input().split()):
#             s += n
#     print(s)
# except:
#     print('123')

# for n in list1:  # Запрос ввода + делим по пробелам
# s += n
# print(s)
# print(sum(list(map(int(first_string)))))
# else first_string = list_1:


#
# print(first_string[5])  # возвращает элемент с индексом 5
#
# print(len(first_string))
# print(type(first_string), first_string)

#
# s = 0
# #
# while True:
#     for n in map(int, input('Запрос ввода: ').split()):  # Запрос ввода + делим по пробелам
#         print(map)
#         s += n
#     print(s)
#     print((map))

# print(len(s))
# if n == 'q':
#     break


# while True:
#     list = input('')
#     list = list.split(' ')
#     n = 0
#     while n < len(list):
#         try:
#             list[n] = int(list[n])
#         except ValueError:
#             break
#         n = n + 1
#     result = 0
#     for c in list:
#         result = result + c  # Считаем все
#     print(result)  # Выводим результат


#
# while 1:
#     i = input(">>>")#Запрос ввода
#     i = i.split(" ")#Делим по пробелам
#     a = 0
#     while a<len(i):
#         try:
#             i[a] = int(i[a])#строки в числа
#         except ValueError:
#             print("Value Error")#при ошибке пишем ошибку и останавливаем цикл
#             break
#         a = a + 1
#     z = 0#Переменная с результатом
#     for c in i:
#         z = z + c#Считаем все
#     print(z)#Выводим результат


# numbers = []
# while True:
#     #numbers = input('Введите числа: ')#
#     numbers.append(input(f'Введите число: '))
#     if numbers == 'q':
#         break
#     print((sum(map(int, numbers.split(' ')))))

#
# def func
#     new_list = []
#     for i in range(3):
#         new_list.append(input(f'Введите {i+1} элемент списка: '))
#     new_list.sort()
#     print(new_list)

# data1 = list('fdghzsdgszd')
# print(sum(data1))
#


# summ = (input('Введите числа через пробел: ').split())

# print(summ)
