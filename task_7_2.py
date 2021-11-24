#!/usr/bin/env python3

with open('ospf.txt') as f:
    for line in f:
        prefix = line.split()[1]
        AD = line.split()[2].replace('[', '').replace(']', '')
        next_hop = line.split()[4].replace(',','')
        update = line.split()[5].replace(',','')
        outbound_if = line.split()[6]
        print(f'''{'Prefix':<20} {prefix:<20}
{'AD/Metric':<20} {AD:<20}
{'Next-Hop':<20} {next_hop:<20}
{'Last update':<20} {update:<20}
{'Outbound Interface':<20} {outbound_if:<20}
        ''')