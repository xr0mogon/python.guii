# 1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
#  Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.

def f_del(num1, num2):
    if num2 != 0:
        return num1 / num2
    else:
        while num2 == 0:
            print(f'на ноль делить нельзя! ')
            num2 = int(input('Введите делитель: '))
        return num1 / num2


num1 = int(input('Введите множитель: '))
num2 = int(input('Введите делитель: '))
print(f_del(num1, num2))

# my_func = lambda p_1, p_2: p_1 / p_2
# num1 = int(input('Введите множитель: '))
# num2 = int(input('Введите делитель: '))
# print(my_func(num1, num2))
