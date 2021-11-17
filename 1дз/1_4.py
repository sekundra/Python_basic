# Пользователь вводит целое положительное число. Найдите самую большую цифру в числе.
# Для решения используйте цикл while и арифметические операции.
n = int(input("Введите целое положительное число:"))
maxNum = 0
restN = n
while restN // 10 > 0:
    if maxNum < restN % 10:
        maxNum = restN % 10
    restN = restN // 10
if maxNum < restN:
    maxNum = restN
print(f'Самая большая цифра в {n}: {maxNum}')