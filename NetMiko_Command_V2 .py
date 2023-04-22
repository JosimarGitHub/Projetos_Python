#!/usr/bin/env python

from netmiko import ConnectHandler
import json
import csv

with open("/home/dev_net/My_Projects/Arquivos_Json/LAB_AUTOMACAO.json", encoding='ascii') as arquivo:
    all_devices = json.load(arquivo)

with open('/home/dev_net/My_Projects/Arquivos_Json/comands.txt','r') as arquivo:
    
    config_commands = arquivo.read().split('\n')

nLinhas1 = len(config_commands)
del(config_commands[nLinhas1 - 1])

for devices in all_devices:
    net_connect = ConnectHandler(**devices)
    output = net_connect.send_config_set(config_commands)
    print (output)
    output = net_connect.send_config_set('do write') 
    print (output)
    """
    for n in range(10,60,10):
        config_commands = ['interface loopback'+str(n),'ip address '+str(n)+'.'+str(n)+'.'+str(n)+'.'+str(n)+' 255.255.255.255']
        output = net_connect.send_config_set(config_commands)
        print (output)
        """
#NÃO USAR COMANDO "end" , do XXXXX, write, comandos fora do configure terminal       
     

