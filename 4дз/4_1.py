# Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
# В расчете необходимо использовать формулу: (выработка в часах * ставка в час) + премия.
# Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.
from sys import argv

name, res_per_hour, pay_per_hour, bonus = argv

print(f'Зарплата: {float(res_per_hour) * float(pay_per_hour) + float(bonus)}')
