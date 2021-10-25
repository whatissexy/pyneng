#!/usr/bin/env python3

access_template = [
    "switchport mode access",
    "switchport access vlan {}",
    "switchport nonegotiate",
    "spanning-tree portfast",
    "spanning-tree bpduguard enable",
]

trunk_template = [
    "switchport trunk encapsulation dot1q",
    "switchport mode trunk",
    "switchport trunk allowed vlan {}",
]

#access_template.append("Введите номер VLAN: ")
#trunk_template.append("Введите разрешенные VLANы: ")

template = {"access": access_template, "trunk": trunk_template}
question = {"access": "Введите номер VLAN: ", "trunk": "Введите разрешенные VLANы: "}

mode = input("Введите режим работы интерфейса (access/trunk): ")
interface = input("Введите тип и номер интерфейса: ")

vlans = input(question[mode])
#vlans = input(template[mode][-1])

#access_template.remove("Введите номер VLAN: ")
#trunk_template.remove("Введите разрешенные VLANы: ")

print(f"interface {interface}")
#print("\n".join(template[mode]).format(vlans))
print('\n'.join(template[mode]).format(vlans))