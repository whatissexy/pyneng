#!/usr/bin/env python3

import time
import datetime

while True:
    try:
        vlan_num = int(input('Введите номер vlan: '))
    except ValueError:
        print('Введен некорректный номер vlan, повторите попытку!')
        time.sleep(1)
        continue
    else:
        break

output = "{:<10} {:<20} {:<10}\n"
temp_list = list()

with open('CAM_table.txt') as f:
    for line in f:
        if len(line.rstrip()):
            res = line.split()
            if res[0].isdigit() and res[1].split('.')[0].isalnum() and len(res[1].split('.')) == 3 and int(res[0]) == vlan_num:
                temp_list.append([int(res[0]), res[1], res[3]])
    for vlan, mac, intf in sorted(temp_list):
        #print(f'{vlan:<10} {mac:<20} {intf:<10}')
        print(output.format(vlan, mac, intf).rstrip())

print(datetime.datetime.now().strftime("\n%d.%m.%Y %H:%M:%S"))