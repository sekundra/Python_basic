# Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет
# и наличие лекционных, практических и лабораторных занятий по этому предмету и их количество.
# Важно, чтобы для каждого предмета не обязательно были все типы занятий.
# Сформировать словарь, содержащий название предмета и общее количество занятий по нему. Вывести словарь на экран.
# Примеры строк файла:
# Информатика: 100(л) 50(пр) 20(лаб).
# Физика: 30(л) — 10(лаб)
# Физкультура: — 30(пр) —
#
# Пример словаря:
# {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}

file_name = 'file_6.txt'
with open(file_name, "r", encoding='UTF-8') as file_to_read:
    content = file_to_read.read()
    string_list = [str_el.split(' ') for str_el in content.split('\n') if len(str_el) > 0]
    dict_clean = {string_list[i][0][:-1]: [el for el in string_list[i] if len(string_list[i]) > 0
                                           and string_list[i].index(el) > 0] for i in range(len(string_list))}
    dict_with_sum = {}
    for key in dict_clean.keys():
        dict_with_sum[key] = [el for el in [''.join(filter(str.isdigit, dict_clean[key][i]))
                                            for i in range(len(dict_clean[key]))] if len(el) > 0]
        dict_with_sum[key] = sum(map(float, dict_with_sum.get(key)))
print(f'File content:\n{content}')
print(f'Dictionary with sum by discipline:\n{dict_with_sum}')
