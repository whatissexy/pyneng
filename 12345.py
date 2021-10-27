#!/usr/bin/env python3

try:
    2/0
except (ZeroDivisionError):
    print('Нельзя делить на ноль!')

#raise ValueError("При выполнении команды возникла ошибка")