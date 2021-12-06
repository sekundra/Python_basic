# Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()),
# который должен принимать данные (список списков) для формирования матрицы.
# Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
# Примеры матриц вы найдете в методичке.
# Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
# Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов класса Matrix
# (двух матриц). Результатом сложения должна быть новая матрица.
# Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки первой матрицы складываем
# с первым элементом первой строки второй матрицы и т.д.


class Matrix:
    # конструктор класса
    def __init__(self, matrix):
        self.matrix = matrix

    # методы класса
    def __str__(self):
        return '\n'.join([' '.join(map(str, el)) for el in self.matrix])

    def __add__(self, other):
        sum_matrix = []
        for i in range(len(self.matrix)):
            line = []
            for j in range(len(self.matrix[i])):
                line.append(self.matrix[i][j] + other.matrix[i][j])
            sum_matrix.append(line)
        return Matrix(sum_matrix)


matrix_1 = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(f'First matrix:\n{matrix_1}')
matrix_2 = Matrix([[4, 0, 1], [2, 5, 9], [0, 0, 9]])
print(f'\nSecond matrix:\n{matrix_2}')
print(f'\nSum matrix sum:\n{matrix_1 + matrix_2}')
