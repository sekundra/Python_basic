# Реализовать функцию int_func(), принимающую слово из маленьких латинских букв и возвращающую его же,
# но с прописной первой буквой. Например, print(int_func(‘text’)) -> Text.
# Продолжить работу над заданием. В программу должна попадать строка из слов, разделенных пробелом.
# Каждое слово состоит из латинских букв в нижнем регистре. Сделать вывод исходной строки,
# но каждое слово должно начинаться с заглавной буквы. Необходимо использовать написанную ранее функцию int_func().


def int_func(word_in):
    """Gets word in small Latins, returns it with first capital letter"""
    false_flg = 0
    for element in word_in:
        if ord(element) > 122 or ord(element) < 97:
            false_flg = 1
            break
    if false_flg == 0 and len(word_in) > 0:
        word_out = word_in[0].upper() + word_in[1:]
    else:
        word_out = ''
    return word_out


my_string = input('Enter words in small Latin letters space separated, finish with Enter:').split(' ')
string_list = []
for word in my_string:
    string_list.append(int_func(word))
fin_string = ' '.join(string_list)
print(fin_string) if len(fin_string.replace(' ', '')) > 0 else \
    print('There is not a single word of small letters in input string')
