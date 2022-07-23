# 1. Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()), который
# должен принимать данные (список списков) для формирования матрицы.
# Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
# Примеры матриц: 3 на 2, 3 на 3, 2 на 4.
# | 31 22 |
# | 37 43 |
# | 51 86 |
#
# | 3 5 32 |
# | 2 4 6 |
# | -1 64 -8 |
#
# | 3 5 8 3 |
# | 8 3 7 1 |
# Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
# Далее реализовать перегрузку метода __add__() для сложения двух объектов класса Matrix (двух матриц).
# Результатом сложения должна быть новая матрица.
# Подсказка: сложение элементов матриц выполнять поэлементно. Первый элемент первой строки первой
# матрицы складываем с первым элементом первой строки второй матрицы и пр.

class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        res_string = ''
        # res_string = '\n'.join(map(str, self.matrix)) # Выводит списки в квадратных скобках

        for line in self.matrix:
            res_string += '| ' + ' '.join(map(str, line)) + ' |\n'
        return res_string

    def __add__(self, other):# Добавил проверку на матрицы равного размера
        len_param = len(self.matrix[0])
        flag = True
        if len(self.matrix) != len(other.matrix):
            flag = False

        if flag:
            for i in range(len(self.matrix)):
                if len(self.matrix[i]) != len_param or len(other.matrix[i]) != len_param:
                    flag = False
                    break

        if flag:
            self.matrix = [[num_1 + num_2 for num_1, num_2 in zip(row_1, row_2)]
                           for row_1, row_2 in zip(self.matrix, other.matrix)]
            return Matrix(self.matrix)
        else:
            return 'Складывать можно только матрицы одинакового размера!'


m1 = Matrix([[31, 22], [37, 43], [51, 86]])
m2 = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
m3 = Matrix([[3, 5, 32], [2, 4, 6], [-1, 64, -8]])
m4 = Matrix([[3, 5, 8, 3], [8, 3, 7, 1]])

print(m1)
print(m2)
print(m3)
print(m4)

print('Результат сложения одинаковых матриц:')
print(m2 + m3)
print('При попытке сложения матриц разного размера выводится сообщение:\n', m2 + m1)