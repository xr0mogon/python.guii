# 5.Запросите у пользователя значения выручки и издержек фирмы.
# Определите, с каким финансовым результатом работает фирма
# (прибыль — выручка больше издержек, или убыток — издержки больше выручки).
# Выведите соответствующее сообщение. Если фирма отработала с прибылью,
# вычислите рентабельность выручки (соотношение прибыли к выручке).
# Далее запросите численность сотрудников фирмы и определите прибыль фирмы в расчете на одного сотрудника.

# value1 > value2 #Прибыль
# value2 > value1 #убыток

value1 = int(input('Введите значения выручки: '))
value2 = int(input('Введите значение издержек: '))

if value1 > value2:
    print('выручка больше издержек')
    print(f'рентабельность выручки: {value1 / value2}')
    pers = int(input('введите численность сотрудников фирмы: '))
    print(f'прибыль в расчете на одного сотрудника составила: {(value1 - value2) / pers}')
else:
    value2 > value1
    print('издержка больше выручки')

