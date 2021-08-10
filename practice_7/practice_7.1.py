"""
1. Реализовать класс Matrix (матрица).
Обеспечить перегрузку конструктора класса (метод __init__()),
который должен принимать данные (список списков) для формирования матрицы.
Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.

Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов класса Matrix(двух матриц).
 Результатом сложения должна быть новая матрица.
Подсказка: сложение элементов матриц выполнять поэлементно —
первый элемент первой строки первой матрицы складываем с первым элементом первой строки второй матрицы и т.д.

"""


class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        return '\n'.join('\t'.join(map(str, row)) for row in self.matrix)

    def __add__(self, other):
        result_list = []
        if len(self.matrix) != len(other.matrix):
            print("Invalid matrix size")
        n = 0
        for row in zip(self.matrix, other.matrix):
            if len(self.matrix[n]) != len(other.matrix[n]):
                raise ValueError("Invalid matrix size")
            else:
                n += 1
            print(row, type(row))
            result_list.append([sum([j, k]) for j, k in zip(*row)])
        return Matrix(result_list)


matrix1 = Matrix([[1, 2, 3, 4], [6, 7, 8, 9], [11, 12, 13, 14]])
matrix2 = Matrix([[1, 2, 3, 4], [6, 7, 8, 9], [11, 12, 13, 14]])
print(matrix1 + matrix2)
