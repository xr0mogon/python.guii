"""
2. Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина).
-Значения данных атрибутов должны передаваться при создании экземпляра класса.????
-Атрибуты сделать защищенными.
-Определить метод расчета массы асфальта, необходимого для покрытия всего дорожного полотна.
-Использовать формулу: длина * ширина * масса асфальта для покрытия одного кв метра дороги асфальтом,
толщиной в 1 см * число см толщины полотна.
Проверить работу метода.
Например: 20м * 5000м * 25кг * 5см = 12500 т
"""


class Road:
    _length = None  # m
    _width = None   # m
    weight = 25     # kg
    thickness = 5   # cm

    def __init__(self, _width, _length, weight, thickness):
        self._width = _width
        self._length = _length
        self.weight = weight
        self.thickness = thickness
        print(f'Created {Road.__name__}')

    def mass_method(self):  # количество смеси, необходимой для укладки 1 кв. м покрытия.
        return self.weight * (self.thickness / 100)

    def road_surface(self):
        return self._width * self._length * self.mass_method()


r = Road(20, 5000, 25, 5)
print(f'Need: {int(r.road_surface())} ton for the building')
