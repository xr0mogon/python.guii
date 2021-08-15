"""
1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
В рамках класса реализовать два метода.

Первый, с декоратором @classmethod, должен извлекать число, месяц, год и преобразовывать их тип к типу «Число».

Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).

Проверить работу полученной структуры на реальных данных.
"""


class Number(int):
    def __str__(self):
        return f"{self:02}"


class Date:
    attributes = ('day', 'month', 'year')

    def __init__(self, date: str, /):
        parts = date.split('-')
        if not self.validation(*parts):
            raise ValueError(f'{date} invalid date format')

        self.day, self.month, self.year = self.transform(parts)

    def __iter__(self):
        for el in self.attributes:
            yield self.__getattribute__(el)

    # @classmethod, должен извлекать число, месяц, год и преобразовывать их тип к типу «Число».
    @classmethod
    def transform(cls, date):  # List[Number]
        Number = []
        for i in date:
            Number.append(i)
        return Number

    # @staticmethod, должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12)
    @staticmethod
    def validation(*date):  # bool
        try:
            day, month, year = [int(x) for x in date]

        except TypeError:
            return False

        return all([1 <= day <= 31, 1 <= month <= 12, 1970 <= year <= 2021])

    def __str__(self):
        return f"Date '{'-'.join([str(s) for s in self])}' is ok"


for date in ('11-08-2021', '01-12-2020', '31-12-1969', '29-08-2022'):
    try:
        print(Date(date))
    except ValueError as e:
        print(e)
