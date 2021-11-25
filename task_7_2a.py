#!/usr/bin/env python3

#from sys import argv

filename = argv[1]
#filename = 'config_sw1.txt'
ignore = ["duplex", "alias", "configuration"]
findd = False
'''
with open (filename) as f:
    for line in f:
        if not line.startswith('!'):
            for ign in ignore:
                if ign in line:
                    findd = True
                    break
                else:
                    findd = False
            if not findd:
                print(line.rstrip())
                findd = False'''

with open (filename) as f:
    for line in f:
        if not line.startswith('!') and not (set(line.split()) & set(ignore)):
            print(line.rstrip())