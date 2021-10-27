#!/usr/bin/env python3

mac = ["aabb:cc80:7000", "aabb:dd80:7340", "aabb:ee80:7000", "aabb:ff80:7000"]
result = []

for cisco_addr in mac:
    result.append(cisco_addr.replace(':','.'))

print(result)