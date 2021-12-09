# Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число», реализуйте перегрузку
# методов сложения и умножения комплексных чисел. Проверьте работу проекта, создав экземпляры класса (комплексные числа)
# и выполнив сложение и умножение созданных экземпляров. Проверьте корректность полученного результата.


class ComplexNum:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __add__(self, other):
        return ComplexNum(self.a + other.a, self.b + other.b)

    def __mul__(self, other):
        return ComplexNum(self.a * other.a - self.b * other.b, self.a * other.b + self.b * other.a)

    def __str__(self):
        return f'{self.a} + {self.b}i'


a_complex = ComplexNum(1, 2)
b_complex = ComplexNum(4, 5)
print(f'a_complex = {a_complex}')
print(f'b_complex = {b_complex}')
print(f'Sum result: {a_complex + b_complex}')
print(f'Multiplication result: {a_complex * b_complex}')
