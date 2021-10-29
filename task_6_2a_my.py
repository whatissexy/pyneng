#!/usr/bin/env python3

ip_addr = input('Введите IP адрес в формате XX.XX.XX.XX: ')
correct_ip = False

while correct_ip != True:
    if len(ip_addr.split('.')) == 4:
         for octet in ip_addr.split('.'):
            if (octet.isdigit() and int(octet) in range(256)):
                correct_ip = True
            else:
                ip_addr = input('Введите корректный IP адрес в формате XX.XX.XX.XX: ')
                break
    else:
        ip_addr = input('Введите корректный IP адрес в формате XX.XX.XX.XX: ')

octet = int(ip_addr.split('.')[0])
if octet in range(1,223):
    print('unicast')
elif octet in range(224,239):
    print('multicast')
elif ip_addr == '255.255.255.255':
    print('local broadcast')
elif ip_addr == '0.0.0.0':
    print('unassigned')
else:
    print('unused')