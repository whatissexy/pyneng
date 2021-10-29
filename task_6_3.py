#!/usr/bin/env python3

trunk_template = [
    "switchport trunk encapsulation dot1q",
    "switchport mode trunk",
    "switchport trunk allowed vlan",
]

trunk = {"0/1": ["add", "10", "20"], "0/2": ["only", "11", "30"], "0/4": ["del", "17"]}

'''for if_name, vlans in trunk.items():
    print('interface FastEthernet' + if_name)
    for command in trunk_template:
        if command.endswith('allowed vlan'):
            #vals = trunk[if_name]
            for item in trunk.values():
                if item[0] == 'add':
                    print(f' {command} {item[0]} {item[1]}, {item[2]}')
                    #break
                elif item[0] == 'only':
                    print(f' {command} {item[1]}, {item[2]}')
                    #break
                elif item[0] == 'del':
                    print(f' {command} remove {item[1]}')
                    #break
            else:
                break
            #print(vals)
        else:
            print(f' {command}')'''

for intf, value in trunk.items():
    print(f"interface FastEthernet {intf}")
    for command in trunk_template:
        if command.endswith("allowed vlan"):
            action = value[0]
            vlans = ",".join(value[1:])

            if action == "add":
                print(f" {command} add {vlans}")
            elif action == "only":
                print(f" {command} {vlans}")
            elif action == "del":
                print(f" {command} remove {vlans}")
        else:
            print(f" {command}")