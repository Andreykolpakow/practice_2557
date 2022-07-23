# 3. Осуществить программу работы с органическими клетками, состоящими из ячеек. Необходимо
# создать класс «Клетка». В его конструкторе инициализировать параметр, соответствующий
# количеству ячеек клетки (целое число). В классе должны быть реализованы методы перегрузки
# арифметических операторов: сложение (__add__()), вычитание (__sub__()), умножение (__mul__()),
# деление (__floordiv__, __truediv__()). Эти методы должны применяться только к клеткам и выполнять
# увеличение, уменьшение, умножение и округление до целого числа деления клеток, соответственно.
# Сложение. Объединение двух клеток. При этом число ячеек общей клетки должно равняться сумме
# ячеек исходных двух клеток.
# Вычитание. Участвуют две клетки. Операцию необходимо выполнять, только если разность количества
# ячеек двух клеток больше нуля, иначе выводить соответствующее сообщение.
# Умножение. Создаётся общая клетка из двух. Число ячеек общей клетки — произведение количества
# ячеек этих двух клеток.
# Деление. Создаётся общая клетка из двух. Число ячеек общей клетки определяется как целочисленное
# деление количества ячеек этих двух клеток.
# В классе необходимо реализовать метод make_order(), принимающий экземпляр класса и количество
# ячеек в ряду. Этот метод позволяет организовать ячейки по рядам.
# Метод должен возвращать строку вида *****\n*****\n*****..., где количество ячеек между \n равно
# переданному аргументу. Если ячеек на формирование ряда не хватает, то в последний ряд
# записываются все оставшиеся.
# Например, количество ячеек клетки равняется 12, а количество ячеек в ряду — 5. В этом случае
# метод make_order() вернёт строку: *****\n*****\n**.
# Или, количество ячеек клетки — 15, а количество ячеек в ряду равняется 5. Тогда
# метод make_order() вернёт строку: *****\n*****\n*****.

class Cell():
    def __init__(self, amount: int):
        self.amount = amount

    def __add__(self, other):
        self.amount += other.amount
        return self#.amount + other.amount

    def __sub__(self, other):
        if self.amount > other.amount:
            self.amount -= other.amount
            return self
        else:
            print('Вычитаемая клетка больше или равна уменьшаемой')
            return self

    def __mul__(self, other):
        self.amount *= other.amount
        return self

    def __floordiv__(self, other):
        self.amount //= other.amount
        return self

    def __truediv__(self, other):
        return self.__floordiv__(other)

    def make_order(self, n):
        # res_str = ''
        res_str = ('*' * n + '\n') * (self.amount // n)
        res_str += f'*' * (self.amount % n)
        return res_str if self.amount % n else res_str[:-1]
        #Удаляет лишний \n в конце строки, если количество ячеек в клетке кратно количеству ячеек в ряду


c1 = Cell(10)
c2 = Cell(3)
print('c1.amount: ', c1.amount, '', '\nc2.amount: ', c2.amount)
print('c1 + c2: ', (c1 + c2).amount)
print('c1 * c2: ', (c1 * c2).amount)
print('c1 - c2: ', (c1 - c2).amount)
print('c2 - c1: ', (c2 - c1).amount)
print('c1 / c2: ', (c1 / c2).amount)
print('c1.make_order(5):', '\n' + c1.make_order(5))