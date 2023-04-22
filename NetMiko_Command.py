#!/usr/bin/env python

from netmiko import ConnectHandler

iosv_l2_s1 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.44.10',
    'username': 'cisco',
    'password': 'cisco',
}

iosv_l2_s2 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.44.11',
    'username': 'cisco',
    'password': 'cisco',
}

iosv_l2_s3 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.44.12',
    'username': 'cisco',
    'password': 'cisco',
}

iosv_l2_s4 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.44.13',
    'username': 'cisco',
    'password': 'cisco',
}

iosv_l2_s5 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.44.14',
    'username': 'cisco',
    'password': 'cisco',
}

iosv_l2_s6 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.44.15',
    'username': 'cisco',
    'password': 'cisco',
}

iosv_l2_s7 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.44.16',
    'username': 'cisco',
    'password': 'cisco',
}

iosv_l2_s8 = {
    'device_type': 'cisco_xe',
    'ip': '192.168.44.17',
    'username': 'cisco',
    'password': 'cisco',
}

all_devices = [iosv_l2_s1,iosv_l2_s2,iosv_l2_s3,iosv_l2_s4,iosv_l2_s5,iosv_l2_s6,iosv_l2_s7,iosv_l2_s8]
n = 1
for devices in all_devices:
    net_connect = ConnectHandler(**devices)
    config_commands = ['interface loopback'+str(n),'ip address '+str(n)+'.'+str(n)+'.'+str(n)+'.'+str(n)+' 255.255.255.255']
    output = net_connect.send_config_set(config_commands)
    n=n+1
    print (output) 

