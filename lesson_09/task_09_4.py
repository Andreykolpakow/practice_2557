# 4. Реализуйте базовый класс Car.
# у класса должны быть следующие атрибуты: speed, color, name, is_police(булево). А также методы:
# go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда);
# опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
# добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля;
# для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60 (TownCar)
# и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
#
# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
# Вызовите методы и покажите результат.

class Car():
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print('Машина поехала')
    def stop(self):
        print('Машина остановилась')
    def turn(self, direction):
        print(f'{self.name} повернул(а) {direction.lower()}')
    def show_speed(self):
        print(f'Текущая скорость {self.speed} км/ч')

class TownCar(Car):
    def show_speed(self):
        msg = (f'Текущая скорость {self.speed} км/ч' if self.speed <= 60 else f'Скорость {self.speed} '
                                                                              f'км/ч выше разрешённой')
        print(msg)

class SportCar(Car):
    # def __init__(self, speed, color, name, is_police):
    #     super().__init__(speed, color, name, is_police)
    def show_police(self):
        if self.is_police:
            print('Это полицейская машина')


class WorkCar(Car):
    def show_speed(self):
        msg = (f'Текущая скорость {self.speed} км/ч' if self.speed <= 40 else f'Скорость {self.speed} '
                                                                              f'км/ч выше разрешённой')
        print(msg)

class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)
        if not self.is_police:
            print('Это не полицейская машина')


a = TownCar(70, 'yellow', 'легковушка', False)
a.show_speed()
b = WorkCar(40, 'grey', 'мусоровоз', False)
b.turn('Влево')
print(b.name)
p = PoliceCar(100, 'white-blue', 'Cop', False)
print(p.color)
s = SportCar(150, 'Red', 'Hooligan', True)

s.show_police()