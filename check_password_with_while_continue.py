#!/usr/bin/env python3

username = input('Введите имя пользователя: ')
password = input('Введите пароль для пользователя: ')

password_set = False
while not password_set:
    if len(password) < 8:
        print('Пароль слишком короткий!')
    elif username in password:
        print('Пароль содержит имя пользователя')
    else:
        print('Пароль для пользователя {} установлен!'.format(username))
        password_set = True

        continue
    password = input('Введите пароль для пользователя {} еще раз: '.format(username))