#!/usr/bin/env python3

output = "\n{:<20} {}" * 5

with open('ospf.txt') as f:
    for line in f:
        res = line.replace(',', '').replace('[', '').replace(']', '').split()
        print (output.format('Prefix', res[1],
                            'AD/Metric', res[2],
                            'Next-Hop', res[4],
                            'Last Update', res[5],
                            'Outbound Interface', res[6]))