# Создать список и заполнить его элементами различных типов данных.
# Реализовать скрипт проверки типа данных каждого элемента.
# Использовать функцию type() для проверки типа. Элементы списка можно не запрашивать у пользователя,
# а указать явно, в программе.
listFirst = [(1, 3), 'qwerty', 1, {0, 1, 1, 2, 2}, {'Name': 'Ivan', 'Age': 23}, True]
for element in listFirst:
    print(f'Эелемент списка {element} принадлежит классу {type(element)}')
