# Создать текстовый файл (не программно), сохранить в нем несколько строк,
# выполнить подсчет количества строк, количества слов в каждой строке - словами считаем то, что разделено пробелами.

file_name = 'file_2.txt'
with open(file_name, "r", encoding='UTF-8') as file_to_read:
    content = file_to_read.read()
    string_list = [str_el for str_el in content.split('\n') if len(str_el) > 0]
    string_num = len(string_list)
    print(f'File content:\n{content}')
    print(f'Number of strings in file: {string_num}')
    for string, i in zip(string_list, range(len(string_list))):
        string_clean = [word for word in string.split(' ') if len(word) > 0]
        print(f'{i + 1} row contains {len(string_clean)} words')
