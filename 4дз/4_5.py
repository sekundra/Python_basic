# Реализовать формирование списка, используя функцию range() и возможности генератора.
# В список должны войти четные числа от 100 до 1000 (включая границы).
# Необходимо получить результат вычисления произведения всех элементов списка.
# Подсказка: использовать функцию reduce().

from functools import reduce


def my_product(num_1, num_2):
    """Get two numbers, return product of the tow"""
    return num_1 * num_2


gen_list = [num for num in range(100, 1001) if num % 2 == 0]
print(f'Первые 10 эелементов списка: {gen_list[0:10]} \nПоследние 10 элементов списка: {gen_list[-10:]}')
print(f'Произведение элементов списка: {reduce(my_product, gen_list)}')
