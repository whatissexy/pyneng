#!/usr/bin/env python3

ip_addr = input('Enter network prefix or host IP address (XX.XX.XX.XX/XX): ')

subnet = ip_addr.split('/')[0].split('.')
mask = int(ip_addr.split('/')[-1])

ip_bin = str('{:08b}'.format(int(subnet[0])) + '{:08b}'.format(int(subnet[1])) + '{:08b}'.format(int(subnet[2])) + '{:08b}'.format(int(subnet[3])))
net_addr_bin = ip_bin[0:mask] + '0'*(32-mask)
mask_full = '1' * mask + '0' * (32-mask)

print(
'\nNetwork:' +
    '\n{:<8} {:<8} {:<8} {:<8}'.format(int(net_addr_bin[0:8], 2), int(net_addr_bin[8:16], 2), int(net_addr_bin[16:24], 2), int(net_addr_bin[24:32], 2)) +
    '\n{:<8} {:<8} {:<8} {:<8}'.format(net_addr_bin[0:8], net_addr_bin[8:16], net_addr_bin[16:24], net_addr_bin[24:32]) +
    '\n'
    )
print(
'Mask\n' +
    '/' + '{:<8}'.format(mask) + '\n' +
    '{:<8} {:<8} {:<8} {:<8}'.format(int(mask_full[0:8], 2), int(mask_full[8:16], 2), int(mask_full[16:24], 2), int(mask_full[24:32], 2)) + '\n' +
    '{:<8} {:<8} {:<8} {:<8}'.format(mask_full[0:8], mask_full[8:16], mask_full[16:24], mask_full[24:32]) + '\n'
    )
print(
'Number of hosts via Network\n' +
    '{:<8} '.format(2 ** (32-mask) - 2)
    )