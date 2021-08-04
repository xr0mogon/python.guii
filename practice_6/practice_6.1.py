"""1.
Создать класс TrafficLight (светофор).
-определить у него один атрибут color (цвет) и метод running (запуск);
-атрибут реализовать как приватный;
-в рамках метода реализовать переключение светофора в режимы: красный, жёлтый, зелёный;
-продолжительность первого состояния (красный) сост. 7 секунд, второго (жёлтый) — 2 секунды, третьего (зелёный) —
на ваше усмотрение;
-переключение между режимами должно осуществляться только в указанном порядке (красный, жёлтый, зелёный);
-проверить работу примера, создав экземпляр и вызвав описанный метод.

**Задачу можно усложнить, реализовав проверку порядка режимов.
  При его нарушении выводить соответствующее сообщение и завершать скрипт.
"""

from time import sleep

class TrafficLight:

    __color = ['red', 'yellow', 'green']  # Private атрибуты  класса

    def __init__(self):
        self.__color = ['red', 'yellow', 'green']
        # self.__color = ['yellow', 'red', 'green']  # для проверки порядка режимов
        # self.__color = ['green', 'red', 'yellow']


    def running(self): # методы класса
        print("Запускаем светофор с атрибутами:", self.__color)
        num_color = 0
        r = 0
        temp = []
        etalon = ('red', 'yellow', 'green')

        for tmp in self.__color:  # записываем световой режим который поступил
            temp.append(tmp)

        for i in range(3):  # проходим по индексам self.__color
            print(self.__color[num_color], 'light')
            if tuple(temp) == etalon:
                pass
                # print('проверка порядка режимов', temp, '=', etalon)
            else:  # При его нарушении выводить соответствующее сообщение
                print('программа не может быть выполнена! '
                      'эталон', etalon, '!= поступившему световому запросу', tuple(self.__color))
                break  # И завершать скрипт

            if num_color == 0:
                r = int(7)
            elif num_color == 1:
                r = int(2)
            elif num_color == 2:
                r = int(10)

            for el in range(r):  # Секундомер
                print(f'\r{r - el}', end='')
                sleep(1)
            print(end='\n')
            num_color += 1


start = TrafficLight()
start.running()
