#!/usr/bin/env python3

device_name = input('Enter device name (r1/r2/sw1): ').lower()

london_co = {
"r1": {
        "location": "21 New Globe Walk",
        "vendor": "Cisco",
        "model": "4451",
        "ios": "15.4",
        "ip": "10.255.0.1"
      },
"r2": {
        "location": "21 New Globe Walk",
        "vendor": "Cisco",
        "model": "4451",
        "ios": "15.4",
        "ip": "10.255.0.2"
      },
"sw1": {
        "location": "21 New Globe Walk",
        "vendor": "Cisco",
        "model": "3850",
        "ios": "3.6.XE",
        "ip": "10.255.0.101",
        "vlans": "10,20,30",
        "routing": True
       }
}

parameter = input('Enter  parameter name ' + str(list(london_co[device_name].keys())) + ' : ').lower()

print(london_co[device_name].get(parameter, 'Такого параметра нет!'))