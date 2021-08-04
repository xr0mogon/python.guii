"""
3. Реализовать базовый класс Worker (работник), в котором определить атрибуты:
name, surname, position (должность), income (доход).
Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы:
оклад и премия, например, {"wage": wage, "bonus": bonus}.
Создать класс Position (должность) на базе класса Worker.
В классе Position реализовать методы
получения полного имени сотрудника (get_full_name)
и дохода с учетом премии (get_total_income).
Проверить работу примера на реальных данных
(создать экземпляры класса Position, передать данные, проверить значения атрибутов, вызвать методы экземпляров)
"""


class Worker:

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'wage': wage, 'bonus': bonus}
        print('print', self.name, self.surname, self.position, self._income)


class Position(Worker):

    def get_full_name(self):
        return f'Full name: {self.name, self.surname}.'

    def get_position(self):
        return self.position

    def get_total_income(self):
        return self._income.get('wage') + (self._income.get('bonus'))


Alex = Position('Alexey', 'Nikitenko', 'Data_scientist', 160000, 50000)
print(Alex.get_full_name())
print(Alex.position)
print(Alex.get_total_income())
