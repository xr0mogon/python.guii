"""3. Реализовать программу работы с органическими клетками. Необходимо создать класс Клетка.
В его конструкторе инициализировать параметр, соответствующий количеству клеток (целое число).
В классе должны быть реализованы методы перегрузки арифметических операторов:
сложение (__add__()), вычитание (__sub__()), умножение (__mul__()), деление (__truediv__()).
количества ячеек этих двух клеток.
В классе необходимо реализовать метод make_order(), принимающий экземпляр класса и количество ячеек в ряду.
"""


class Cell:
    def __init__(self, num):
        self.num = num

    def __add__(self, other):
        """Перегружаем сложение"""
        return Cell(self.num + other.num)

    def __sub__(self, other):
        """Перегружаем вычитание"""
        if self.num > other.num:
            return Cell(self.num - other.num)
        print(f"{self.num} - {other.num}: вычитание невозможно")
        return Cell(self.num - other.num)

    def __mul__(self, other):
        """Перегружаем умножение"""
        return Cell(self.num * other.num)

    def __truediv__(self, other):
        """Перегружаем целочисленное деление"""
        return Cell(self.num // other.num)

    # def make_order(self, param):
    #     return(('*' * param) + '\n') * (self.num // param) + '*' * (self.num % param)

    def make_order(self, row):
        rows = self.num // row  # узнаём количество строк
        remainder = self.num % row  # узнаём остаток последней строки
        return '\n'.join(['*' * row] * rows + (['*' * remainder]))

    def __str__(self):
        return f"Клетка состоит из {self.num} ячеек \n"


c_1 = Cell(12)
# print(c_1.make_order(5))
c_2 = Cell(15)
# print(c_2.make_order(3))
c_3 = c_1*c_2
# print(c_2.make_order(4))

print(c_1 + c_2)
print(c_1 - c_2)
print(c_2 - c_1)
print(c_2 - c_2)
print(c_1 * c_2)
print(c_1 / c_2)
# print((c_1 * c_2).make_order(23))


