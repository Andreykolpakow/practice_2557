# 2. Реализовать проект расчёта суммарного расхода ткани на производство одежды. Основная
# сущность (класс) этого проекта — одежда, которая может иметь определённое название. К типам
# одежды в этом проекте относятся пальто и костюм. У этих типов одежды существуют параметры:
# размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и H, соответственно.
# Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5),
# для костюма(2*H + 0.3). Проверить работу этих методов на реальных данных.
# Выполнить общий подсчёт расхода ткани. Проверить на практике полученные на этом уроке знания.
# Реализовать абстрактные классы для основных классов проекта и проверить работу декоратора @property.

from abc import ABC, abstractmethod
#
class Dress(ABC):
    names = ['Пальто', 'Костюм']
    def __init__(self, name, amount):
        self.name = name
        self.amount = amount

    @abstractmethod
    def calculate(self):
        if self.name not in self.names:
            print(str(self.name))
            print('Нет такого вида продукции')
            exit(1)


class Coat(Dress):
    def __init__(self, name, size, amount):
        self.size = size
        super().__init__(name, amount)

    @property
    def calculate(self):
        super().calculate()
        return round((self.size / 6.5 + 0.5) * self.amount, 2)



class Suit(Dress):
    def __init__(self, name, growth, amount):
        super().__init__(name, amount)
        self.growth = growth

    @property
    def calculate(self):
        super().calculate()
        return round((self.growth * 2 / 100 + 0.3) * self.amount, 2)

x = Coat('Куртка', 42, 1)
c48 = Coat('Пальто', 48, 10)
s170 = Suit('Костюм', 170, 5)
print(f'На 10 пальто 48-го размера и 5 костюмов 170-го роста надо {c48.calculate + s170.calculate} метров '
      f'ткани')
x.calculate