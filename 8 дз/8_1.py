# Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
# В рамках класса реализовать два метода. Первый, с декоратором @classmethod, должен извлекать число, месяц, год и
# преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и
# года (например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных данных.


class Date:
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year

    @classmethod
    def date_parse(cls, date):
        list_dt = date.split('-')
        try:
            list_dt = list(map(int, list_dt))
        except ValueError:
            return 'Input date incorrect, day, month and year must be int type'
        else:
            day, month, year = list_dt
            if cls.date_val(*list_dt):
                return cls.date_val(*list_dt)
            else:
                return cls(day, month, year)

    @staticmethod
    def date_val(day, month, year):
        if day < 0 or day > 31:
            return f'day {day} is not valid calendar date'
        if month < 0 or month > 12:
            return f'month {month} is not valid calendar month'
        if year < 0:
            return f'year {year} is not valid calendar year'


date_str = input("Enter date in format 'dd-mm-yyyy':")
date = Date.date_parse(date_str)
try:
    print(f'Result date is {date.day}.{date.month}.{date.year}')
except AttributeError:
    print(date)
