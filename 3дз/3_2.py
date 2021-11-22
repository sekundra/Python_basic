# Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
# имя, фамилия, год рождения, город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы.
# Реализовать вывод данных о пользователе одной строкой.


def my_user(**kwargs):
    """Gets user details and print in one string"""
    for key in kwargs:
        print(key, kwargs[key], sep=': ', end=', ')
    return kwargs


u_name = input('Enter user first name:')
u_last_name = input('Enter user last name:')
u_year = input('Enter user birth year:')
u_city = input('Enter user city of residence:')
u_email = input('Enter user e-mail:')
u_phone = input('Enter user phone:')
my_user(first_name=u_name, last_name=u_last_name, year=u_year, city=u_city, email=u_email, phone=u_phone)
