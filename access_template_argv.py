#!/usr/bin/env python3

#from sys import argv

#interface = argv[1]
#vlan = argv[2]

interface = input('Enter interface type and number: ')
vlan = input('Enter VLAN number: ')

access_template = ['switchport mode access',
'switchport access vlan {}',
'switchport nonegotiate',
'spanning-tree portfast',
'spanning-tree bpduguard enable']

#print('interface {}'.format(interface))
#print('\n'.join(access_template).format(vlan))

print('\n' + '-' * 30)
print('interface {}'.format(interface))
print('\n'.join(access_template).format(vlan))