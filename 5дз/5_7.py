# Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о
# фирме: название, форма собственности, выручка, издержки.
# Пример строки файла: firm_1 ООО 10000 5000.
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
# Если фирма получила убытки, в расчет средней прибыли ее не включать.
# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
# Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
# Итоговый список сохранить в виде json-объекта в соответствующий файл.
# Пример json-объекта:
# [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
#
# Подсказка: использовать менеджеры контекста.

import json

file_name_txt = 'file_7.txt'
file_name_json = 'file_77.json'
with open(file_name_txt, "r", encoding='UTF-8') as file_to_read:
    content = file_to_read.read()
    string_list = [str_el.split(' ') for str_el in content.split('\n') if len(str_el) > 0]
    for i in range(len(string_list)):
        string_list[i] = [float(string_list[i][j]) if j in (2, 3) else string_list[i][j]
                          for j in range(len(string_list[i]))]
    dict_profit = {string_list[i][0]: string_list[i][2] - string_list[i][3] for i in range(len(string_list))}
    avg_profit_list = [el for el in dict_profit.values() if el > 0]
    final_list = [dict_profit, {'average_profit': round(sum(avg_profit_list)/len(avg_profit_list), 3)}]
    print(f'List to write to json:\n{final_list}')
with open(file_name_json, "w", encoding='UTF-8') as file_to_write:
    json.dump(final_list, file_to_write, ensure_ascii=False)
