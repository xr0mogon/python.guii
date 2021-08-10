"""
2. Реализовать проект расчета суммарного расхода ткани на производство одежды.
Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название.
К типам одежды в этом проекте относятся пальто и костюм.
У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма).
Это могут быть обычные числа: V и H, соответственно.
Для определения расхода ткани по каждому типу одежды использовать формулы:
для пальто (V/6.5 + 0.5), для костюма (2 * H + 0.3). Проверить работу этих методов на реальных данных.
Реализовать общий подсчет расхода ткани.
Проверить на практике полученные на этом уроке знания: реализовать абстрактные классы для основных классов проекта,
проверить на практике работу декоратора @property.
"""

from abc import ABC, abstractmethod


class Clothes(ABC):
    def __init__(self, param):
        self.param = param

    @abstractmethod
    def get_consumption(self):
        """Подсчёт материала"""
        pass

    @property
    def set_param(self):
        """ Узнать размер """
        return self.param

    @set_param.setter
    def set_param(self, param):
        """ Установить новый размер """
        self.param = param


class Coat(Clothes):
    def get_consumption(self):
        return round(self.param / 6.5 + 0.5, 2)

    @property
    def H(self):
        return self.param

    @H.setter
    def H(self, param):
        self.param = param

    def __str__(self):
        return f"Для пошива пальто {self.param} размера " \
               f"требуется {self.get_consumption()} кв.м. ткани"


class Suit(Clothes):
    def get_consumption(self):
        return round(self.param * 2 + 0.3, 2)

    @property
    def V(self):
        return self.param

    @V.setter
    def V(self, param):
        self.param = param

    def __str__(self):
        return f"Для пошива костюма на рост {self.param} " \
               f"требуется {self.get_consumption()} кв.м. ткани"


coat = Coat(54)
print(coat)
coat.H = 45
print(coat)

suit = Suit(1.83)
print(suit)
suit.V = 1.72
print(suit)
