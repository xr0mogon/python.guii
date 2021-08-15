"""
2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
Проверьте его работу на данных, вводимых пользователем.
При вводе пользователем нуля в качестве делителя программа должна корректно обработать эту ситуацию
и не завершиться с ошибкой.
"""


class Zero_Division_Exception(Exception):
    text = "На ноль делить невозможно"

    def __str__(self):
        return self.text


class Division(float):
    def __truediv__(self, other):
        if other is not None and not other:
            raise Zero_Division_Exception
        else:
            return Division(float(self) / float(other))


while True:
    try:
        dividend, divider = map(Division, input("Введите делимое и делитель через пробел: ").split())
        print(dividend / divider)
    except Zero_Division_Exception as e:
        print(e)
    except ValueError as e:
        print(e)
        break
