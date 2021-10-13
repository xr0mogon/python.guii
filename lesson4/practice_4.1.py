# 1. Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
# В расчете необходимо использовать формулу: (выработка в часах * ставка в час) + премия.
# Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.

from sys import argv

if len(argv) == 4:
    name_script, output, rate, bonus = argv
    print(f'(выработка в часах * ставка в час) + премия = {int(output) * int(rate) + int(bonus)}')
else:
    try:
        output = int(input('выработка: '))
        rate = int(input('ставка: '))
        bonus = int(input('премия: '))
        print(f"(выработка в часах*ставка в час)+премия ={int(input(output)) * int(input(rate)) + int(input(bonus))}")
    except ValueError:
        print('only numbers!')
