# Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел.
# У пользователя необходимо запрашивать новый элемент рейтинга.
# Если в рейтинге существуют элементы с одинаковыми значениями,
# то новый элемент с тем же значением должен разместиться после них.
ratingList = [9, 7, 3, 2, 1]
finalList = ratingList.copy()
ans = 'Y'
while ans == 'Y':
    ratingList = finalList.copy()
    newRate = int(input('Введите новый рейтинг:'))
    if newRate <= finalList[-1]:
        finalList.append(newRate)
    else:
        for i in range(len(finalList)):
            if newRate > finalList[i]:
                finalList.insert(i, newRate)
                break
    print(f'Изначальный список {ratingList}')
    print(f'Финальный список {finalList}')
    ans = input('Хотите продолжить? (Y/N)').upper()


