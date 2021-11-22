# Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
# Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.


def my_division(num_1, den_1):
    """Возвращает результат деления num_1 на den_1"""
    try:
        num_1 / den_1
    except ZeroDivisionError:
        return 'Деление на ноль! Результат деления: бесконечность'
    else:
        return f'Результат: {num_1 / den_1}'


while True:
    try:
        num = int(input('Введите числитель:'))
    except ValueError:
        print('Введите число!')
    else:
        break

while True:
    try:
        den = int(input('Введите знаменатель:'))
    except ValueError:
        print('Введите число!')
    else:
        break
print(my_division(num, den))
