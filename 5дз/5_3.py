# Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
# Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
# Выполнить подсчет средней величины дохода сотрудников.

file_name = 'file_3.txt'
with open(file_name, "r", encoding='UTF-8') as file_to_read:
    content = file_to_read.read()
    string_list = [str_el for str_el in content.split('\n') if len(str_el) > 0]
    print(f'File content:\n{content}')
    list_of_list = [emp.split(' ') for emp in string_list]
    clean_list = []
    for string in list_of_list:
        clean_list.append([el for el in string if len(el) > 0])
    low_sal = [name[0] for name in clean_list if float(name[1]) < 20_000]
    print(f'List of employees with salary < 20 000:{low_sal}')
    salary_list = list(map(float, [sal[1] for sal in clean_list]))
    print(salary_list)
    print(f'Average salary: {round(sum(salary_list)/len(salary_list), 3)}')
