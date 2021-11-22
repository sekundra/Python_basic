# Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
# Напишите решения через list и через dict.
month = int(input('Введите номер месяца от 1 до 12:'))
# через list
listMonths = [(12, 1, 2), (3, 4, 5), (6, 7, 8), (9, 10, 11)]
listSeasons = ['Зима', 'Весна', 'Лето', 'Осень']
season = ''
for i in range(len(listMonths)):
    for el in listMonths[i]:
        if el == month:
            season = listSeasons[i]
            break

print(f'Через list {season}')

# через dict
dictMonths = {1: 'Зима', 2: 'Зима', 3: 'Весна', 4: 'Весна', 5: 'Весна', 6: 'Лето', 7: 'Лето', 8: 'Лето', 9: 'Осень',
              10: 'Осень', 11: 'Осень', 12: 'Зима'}
print(f'Через dict {dictMonths[month]}')
