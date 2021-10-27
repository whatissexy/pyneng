#!/usr/bin/env python3

username = input('Введите имя пользователя: ')
password = input('Введите пароль для пользователя: ')

while True:
    if len(password) < 8:
        print('Пароль слишком короткий!')
    elif username in password:
        print('Пароль содержит имя пользователя')
    else:
        print('Пароль для пользователя {} установлен!'.format(username))
        break
    password = input('Введите пароль для пользователя {} еще раз: '.format(username))