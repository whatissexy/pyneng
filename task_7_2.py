#!/usr/bin/env python3

from sys import argv

filename = argv[1]

with open (filename) as f:
    for line in f:
        if not line.startswith('!'):
            print(line.rstrip())
