# 7. Создать (не программно) текстовый файл,
# в котором каждая строка должна содержать данные о фирме: название, форма собственности, выручка, издержки.
# Пример строки файла: firm_1 ООО 10000 5000.
# Необходимо построчно прочитать файл,

# вычислить прибыль каждой компании, прибыль = выручка - издержки
# а также СРеднюю ПРибыль. ср_пр = сумма всех пр компаний, делённой на их количество

# Если фирма получила убытки, в расчет средней прибыли ее не включать.
# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями,
# а также словарь со средней прибылью. Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].

# Итоговый список сохранить в виде json-объекта в соответствующий файл.
# Пример json-объекта:
# [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
# Подсказка: использовать менеджеры контекста.

import json

with open('practice_5.7.txt', 'r', encoding='utf-8') as f_obj:
    data = (f_obj.readlines())  # читаем файл и записываем в список data
new_data = []  # новый список для создания списка со списками

for i in data:  # цикл записи элемента из файла в конец списка
    new_data.append(i.split())
print(new_data, 'колич элементов', len(new_data), type(new_data), 'new data')
my_dict = {}  # пустой словарь

average_profit = 0  # средняя прибыль
n = 0  # счетчик количествафирм для порсчета среднего дохода
for el in new_data:
    profit = 0

    if int(el[2]) > int(el[3]):
        n += 1
        # print('el', el[2], type(el[2]))
        profit += (int(el[2]) - int(el[3]))  # прибыль = выручка - издержки
        # print(el[2], '-', el[3], '=', profit)
        # print(average_profit, '+', profit)
        average_profit += profit
        # print(average_profit)
    else:
        profit = (int(el[2]) - int(el[3]))  # 'фирма получила убытки'

    my_dict[el[0]] = profit
    # print('profit', profit)
print(my_dict)
average = int(average_profit/n)

d = dict.fromkeys(['average_profit'], average)
print('средняя прибыль', n, 'фирм =', average, 'тугриков')

j_list = [my_dict, d]
print('j_list:', j_list)

with open('new_json_5.7.json', 'w') as file:
    json.dump(j_list, file)

# with open('new_json_5.7.json', 'r') as read_file:
#     data = json.load(read_file)
# print(data)

