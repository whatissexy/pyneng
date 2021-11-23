#!/usr/bin/env python3

with open('ospf.txt') as f:
    for line in f:
        prefix = line.split()[1]
        AD = line.split()[2]
        next_hop = line.split()[4].replace(',','')
        update = line.split()[5].replace(',','')
        outbound_if = line.split()[6]
        print(f"Prefix {prefix}")