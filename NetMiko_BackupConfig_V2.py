#!/usr/bin/env python

from netmiko import ConnectHandler
import json

with open("/home/dev_net/My_Projects/Arquivos_Json/LAB_AUTOMACAO.json", encoding='utf-8') as arquivo:
    all_devices = json.load(arquivo)

hosts = []
n = 0
for devices in all_devices:
    net_connect = ConnectHandler(**devices)
    output = net_connect.send_command('sh run | s hostname')
    output = output.replace('hostname ',"")
    hosts.append(output)
    
for devices in all_devices:   
    with open('/home/dev_net/My_Projects/Arquivos_Backup/'+hosts[n]+'.txt', 'w') as arquivo:
         net_connect = ConnectHandler(**devices)
         output = net_connect.send_command('show run')
         arquivo.write(output)
         arquivo.close()
         n = n+1
