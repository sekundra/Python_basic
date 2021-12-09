# Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
# Проверьте его работу на данных, вводимых пользователем. При вводе пользователем нуля в качестве делителя программа
# должна корректно обработать эту ситуацию и не завершиться с ошибкой.


class ZeroDivision(Exception):
    def __init__(self, txt):
        self.txt = txt


num_1, num_2 = tuple(map(float, input("Enter tow numbers for division pace separated:").split(' ')))
try:
    if num_2 == 0:
        raise ZeroDivision('Division by zero impossible')
except ZeroDivision as err:
    print(err)
else:
    print(f"Division result is {num_1/num_2}")
