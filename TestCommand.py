#!/usr/bin/env python

from netmiko import ConnectHandler

iosv_l2 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.44.10',
    'username': 'cisco',
    'password': 'cisco',
}


net_connect = ConnectHandler(**iosv_l2)
output = net_connect.send_command('sh run | s hostname')
output = output.replace('hostname ',"")
print (output)
#n = 15
#config_commands = ['interface fastethernet 0/0 ', 'ip address 192.168.44.'+str(n)+' 255.255.255.0']
#output = net_connect.send_config_set(config_commands)
#print (output)

