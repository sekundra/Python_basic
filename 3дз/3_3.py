# Реализовать функцию my_func(), которая принимает три позиционных аргумента,
# и возвращает сумму наибольших двух аргументов.


def my_func(*args):
    """Gets three numbers and returns sum of greatest two"""
    sum_max = sum(*args) - min(*args)
    return sum_max


while True:
    try:
        nums = tuple(map(float, input('Enter three numbers space separated:').split(' ')))
    except ValueError:
        print('Enter numbers!')
    else:
        break
print(f'Sum of the greatest two is {my_func(nums)}')


