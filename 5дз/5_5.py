# Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.

file_name = 'file_5.txt'
b = 0
while True:
    num_string = input('Enter numbers space separated:').split(' ')
    string_list = [num for num in num_string if len(num) > 0]
    num_list = []
    for el in string_list:
        try:
            float(el)
        except ValueError:
            pass
        else:
            num_list.append(el)
    if len(num_list) == 0:
        print('No numbers in input string, nothing to sum')
    else:
        break
with open(file_name, "w+", encoding='UTF-8') as file_to_write:
    file_to_write.write(' '.join(num_list) + '\n')
    file_to_write.seek(0)
    list_of_nums = [float(el.rstrip('\n')) for el in file_to_write.read().split(' ')]
    print(f'Sum of numbers in list is {sum(list_of_nums)}')
