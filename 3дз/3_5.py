# Программа запрашивает у пользователя строку чисел, разделенных пробелом.
# При нажатии Enter должна выводиться сумма чисел.
# Пользователь может продолжить ввод чисел, разделенных пробелом и снова нажать Enter.
# Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме.
# Но если вместо числа вводится специальный символ, выполнение программы завершается.
# Если специальный символ введен после нескольких чисел,
# то вначале нужно добавить сумму этих чисел к полученной ранее сумме и после этого завершить программу.


def my_sum(list_str, summ):
    """Gets string of symbols before quit symbol, returns sum of numbers in it"""
    quit_flg = 0
    for num in list_str:
        if num.upper() == 'Q':
            quit_flg = 1
            break
        else:
            try:
                float(num)
            except ValueError:
                pass
            else:
                summ += float(num)
    if quit_flg == 1:
        print(f'Program is stopped, final sum is: {summ}')
    else:
        print(f'Sum of numbers is: {summ}')
    return quit_flg, summ


sum_m = 0
quit_flag = 0
while quit_flag == 0:
    string_inp = input('Enter numbers space separated, finish input with Enter,'
                       '\nto stop program enter \'q\':').split(' ')
    quit_flag, sum_m = my_sum(string_inp, sum_m)
