# Реализовать два небольших скрипта:
# а) итератор, генерирующий целые числа, начиная с указанного,
# б) итератор, повторяющий элементы некоторого списка, определенного заранее.
# Подсказка: использовать функцию count() и cycle() модуля itertools.
# Обратите внимание, что создаваемый цикл не должен быть бесконечным. Необходимо предусмотреть условие его завершения.
# Например, в первом задании выводим целые числа, начиная с 3, а при достижении числа 10 завершаем цикл.
# Во втором также необходимо предусмотреть условие, при котором повторение элементов списка будет прекращено.

from itertools import count, cycle

print('Integer generator')
n_start, n_end = map(int,
                     list(input("Enter integer for first and last element of generator space separated:").split(' ')))
for el in count(n_start):
    if el > n_end:
        break
    else:
        print(el)
print('List copy generator')
num_col = int(input('Enter number of list generations:'))
input_list = [1, 2, 56, 'dfg', True, '']
print(f'List to generate: {input_list}')
i = 0
for el in cycle(input_list):
    if i > num_col * len(input_list) - 1:
        break
    else:
        print(el)
        i += 1
