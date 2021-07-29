# 5. Реализовать формирование списка, используя функцию range() и возможности генератора.
# В список должны войти четные числа от 100 до 1000 (включая границы).
# Необходимо получить результат вычисления произведения всех элементов списка.
# Подсказка: использовать функцию reduce().
from functools import reduce

my_list = range(99, 1001)
out_list = [number for number in my_list[1:] if number % 2 == 0]


def reducer_func(el_prev, el):  # el_prev — предшествующий элемент # el — текущий элемент
    return el_prev * el


print(reduce(reducer_func, list(out_list)))
