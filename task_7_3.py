#!/usr/bin/env python3

output = "{:<10} {:<20} {:<10}\n"

with open('CAM_table.txt') as f:
    for line in f:
        if len(line.rstrip()):
            res = line.split()
            if res[0].isdigit():
                print (output.format(res[0], res[1], res[3]).rstrip())