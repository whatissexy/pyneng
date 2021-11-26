#!/usr/bin/env python3

output = "{:<10} {:<20} {:<10}\n"
temp_list = list()

with open('CAM_table.txt') as f:
    for line in f:
        if len(line.rstrip()):
            res = line.split()
            if len(res) and res[0].isdigit() and res[1].split('.')[0].isalnum() and len(res[1].split('.')) == 3:
                temp_list.append([int(res[0]), res[1], res[3]])
    for vlan, mac, intf in sorted(temp_list):
        #print(f'{vlan:<10} {mac:<20} {intf:<10}')
        print(output.format(vlan, mac, intf).rstrip())