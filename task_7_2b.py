#!/usr/bin/env python3

from sys import argv

in_file = argv[1]
out_file = argv[2]

ignore = ["duplex", "alias", "configuration"]

with open (in_file) as f, open (out_file, "w") as out:
    for line in f:
        if not line.startswith('!') and not (set(line.split()) & set(ignore)):
            out.write(line)