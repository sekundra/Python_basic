# Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.

from num2words import num2words

file_name_input = 'file_4.txt'
with open(file_name_input, "r", encoding='UTF-8') as file_to_read:
    content = file_to_read.read()
    string_list = [str_el for str_el in content.split('\n') if len(str_el) > 0]
    print(f'File content:\n{content}')
    list_of_list = [emp.split(' ') for emp in string_list]
    clean_list = []
    for string in list_of_list:
        clean_list.append([el for el in string if len(el) > 0])
new_list = [[num2words(el[2], lang='ru').capitalize(), el[1], el[2]] for el in clean_list]
file_name_output = 'file_4_o.txt'
with open(file_name_output, "w", encoding='UTF-8') as file_to_write:
    string_list = [' '.join(new_list[i]) for i in range(len(new_list))]
    file_to_write.write('\n'.join(string_list) + '\n')
