#!/usr/bin/env python

from netmiko import ConnectHandler

iosv_l2 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.44.108',
    'username': 'cisco',
    'password': 'cisco',
}

with open('Ry.txt') as f:
    lines = f.read().splitlines()
print (lines)

net_connect = ConnectHandler(**iosv_l2)
output = net_connect.send_config_set(lines)
print (output)


