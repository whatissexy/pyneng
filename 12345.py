#!/usr/bin/env python3

'''try:
    2/0
except (ZeroDivisionError):
    print('Нельзя делить на ноль!')

#raise ValueError("При выполнении команды возникла ошибка")'''

trunk = {"0/1": ["add", "10", "20"], "0/2": ["only", "11", "30"], "0/4": ["del", "17"]}

for item in trunk.values():
    #print(','.join(item))
    print(item.pop(0))

#print(','.join(trunk.values()))