# Программа принимает действительное положительное число x и целое отрицательное число y.
# Необходимо выполнить возведение числа x в степень y. Задание необходимо реализовать в виде функции my_func(x, y).
# При решении задания необходимо обойтись без встроенной функции возведения числа в степень.


def my_func(x, y):
    """Gets positive x and negative integer y, returns x times  """
    product = 1
    for i in range(1, -y + 1):
        product *= 1/x
        i += 1
    return product


while True:
    x_inp = input('Enter real positive x:')
    try:
        x_inp = float(x_inp)
    except ValueError:
        print('x is not a real number!')
    else:
        if x_inp < 0:
            print('x is not positive!')
        else:
            break
while True:
    y_inp = input('Enter negative integer y:')
    try:
        y_inp = int(y_inp)
    except ValueError:
        print('y is not an integer number!')
    else:
        if y_inp >= 0:
            print('y is not negative!')
        else:
            break
print(f'{x_inp} times {y_inp} = {my_func(x_inp, y_inp)}')
