# 3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
# и возвращает сумму наибольших двух аргументов.

def my_func():
    new_list = []
    for i in range(3):
        new_list.append(input(f'Введите {i+1} элемент списка: '))
    new_list.sort()
    print(new_list)
    print(f'Сумма сумму наибольших двух аргументов: {int(new_list[1]) + int(new_list[2])}')

my_func()
