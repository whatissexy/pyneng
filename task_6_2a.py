#!/usr/bin/env python3

ip_addr = input('Введите IP адрес: ').split('.')

for octet in ip_addr:
    if int(octet) and int(octet) in range(0, 255):
        print('PASS ' + octet)
    else: print('FAIL ' + octet)



'''octet = int(ip_addr.split('.')[0])
if octet in range(1,223):
    print('unicast')
elif octet in range(224,239):
    print('multicast')
elif ip_addr == '255.255.255.255':
    print('local broadcast')
elif ip_addr == '0.0.0.0':
    print('unassigned')
else:
    print('unused')'''