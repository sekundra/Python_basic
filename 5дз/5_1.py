#  Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
#  Об окончании ввода данных свидетельствует пустая строка.

with open("my_file.txt", "w", encoding='UTF-8') as file_to_write:
    while True:
        my_string = input('Enter string to write. To stop writing enter empty string:')
        if len(my_string) == 0:
            break
        else:
            file_to_write.write(f'{my_string}\n')
