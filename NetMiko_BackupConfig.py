#!/usr/bin/env python

from netmiko import ConnectHandler

iosv_l2_s1 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.1.19',
    'username': 'admin',
    'password': '0459',
}

iosv_l2_s2 = {
    'device_type': 'cisco_ios',
    'ip': '10.43.5.253',
    'username': 'Bauducco',
    'password': 'P@ndurat0',
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

all_devices = [iosv_l2_s1]#,iosv_l2_s2]#,iosv_l2_s3,iosv_l2_s4,iosv_l2_s5,iosv_l2_s6,iosv_l2_s7]
hosts = []
n = 0
for devices in all_devices:
    net_connect = ConnectHandler(**devices)
    output = net_connect.send_command('sh run | s hostname')
    output = output.replace('hostname ',"")
    hosts.append(output)
    
for devices in all_devices:   
    with open(hosts[n]+'.txt', 'w') as arquivo:
         net_connect = ConnectHandler(**devices)
         output = net_connect.send_command('show run')
         arquivo.write(output)
         arquivo.close()
         n = n+1
