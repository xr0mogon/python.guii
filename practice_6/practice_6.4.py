'''
4. Реализуйте базовый класс Car.
у класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
А также методы:
go, stop, turn(direction),
которые должны сообщать, что машина поехала, остановилась, повернула (куда);
опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля;
для классов TownCar и WorkCar переопределите метод show_speed.
При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
'''


class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        if not self.is_police:
            return f'{self.name} car started moving'
        else:
            return f'patrol car {self.name} started moving'

    def stop(self):
        return f'{self.name} stopped'

    def turn(self, direction):
        return f'{self.name} turn {direction}'

    def show_speed(self):
        return 'speed: ', self.speed


class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed > 60:
            return f'{self.name} speed {self.speed} need to reduce speed!'
        else:
            return f'{self.name} speed {self.speed} you are good driver'


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed > 40:
            return f'{self.name} speed {self.speed}, you need to reduce speed!'
        else:
            return f'{self.name} speed {self.speed} he observes the rules'


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed > 60:
            return f'{self.name} speed {self.speed}! emergency situation. contact with dispatcher!'
        else:
            return f'{self.name} speed {self.speed} overwatch in normal mode'


bmw = PoliceCar(100, 'white', 'BMW', True)
lada1 = WorkCar(30, 'Green', 'vesta', False)
lada2 = WorkCar(70, 'Pink', 'Lada', True)
infiniti = TownCar(140, 'Grey', 'Infiniti', False)
hyundai = WorkCar(70, 'Yellow', 'hyundai', False)
print(f'{infiniti.show_speed()}, {infiniti.turn("left")}.')
print(f'{bmw.go()}, {bmw.turn("left")}, {bmw.show_speed()}')
print(f'{lada2.turn("right")}. {lada2.stop()} and blocked the road. {lada2.name} help {bmw.name} '
      f'to stop {infiniti.name}! \n'
      f'{lada2.name} color is {lada2.color}!! {lada2.name} is a police car too? {lada2.is_police}')
print(f'{infiniti.stop()} with {bmw.name} and got a fine!')
# print(f'{lada1.show_speed()}')
# print(f'{hyundai.go()}. His car color is{hyundai.color}. He {hyundai.turn("right")} and take a man on board.\n '
#       f'{hyundai.name} is he policeman? {hyundai.is_police} he is a taxi driver')
# print(bmw.show_speed())
# print(lada1.show_speed())
# print(lada2.is_police)
# print(infinity.show_speed())
