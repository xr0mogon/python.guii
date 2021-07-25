# 2. Реализовать функцию, принимающую несколько параметров,
# описывающих данные пользователя: имя, фамилия, год рождения, город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы.
# Реализовать вывод данных о пользователе одной строкой.
# name = input('Введите ваше имя: ')
# surname = input('Введите вашу фамилию: ')
# year = input('Введите ваш год рождния: ')
# city = input('Введите ваш город проживания: ')
# email = input('Введите ваш email: ')
# phone = input('Введите ваш номер телефона: ')

name = input('Введите ваше имя: ')
surname = input('Введите вашу фамилию: ')
year = input('Введите ваш год рождния: ')
city = input('Введите ваш город проживания: ')
email = input('Введите ваш email: ')
phone = input('Введите ваш номер телефона: ')

def user_param(name, surname, year, city, email, phone):
    print(f'Данные пользователя: {name}, {surname}, {year}, {city}, {email}, {phone}')


user_param(name=name, surname=surname, year=year, city=city, email=email, phone=phone)
