#Bibliotecas importadas
import sys
import telnetlib
from time import sleep

#Informações para Acesso via Telnet
with open('/home/dev_net/My_Projects/Arquivos_Json/Lab_Automacao.txt','r') as arquivo:

    hosts = arquivo.readlines()
    arquivo.close()

nLinhas1 = len(hosts)-1
linhaAtual = 0
ultimaLInha = 0

while ultimaLInha != nLinhas1:

    lido = False
    
    while lido == False :

        for i in range(ultimaLInha,nLinhas1):

            if hosts[i].startswith("Host"):
                hosts[i] = hosts[i].replace("Host","")
                hosts[i] = hosts[i].replace("=","")
                hosts[i] = hosts[i].replace("\n","")
                hosts[i] = hosts[i].lstrip()
                HOST = hosts[i]

            if hosts[i].startswith("user"):
                hosts[i] = hosts[i].replace("user","")
                hosts[i] = hosts[i].replace("=","")
                hosts[i] = hosts[i].replace("\n","")
                hosts[i] = hosts[i].lstrip()
                user = hosts[i]

            if hosts[i].startswith("password"):
                hosts[i] = hosts[i].replace("password","")
                hosts[i] = hosts[i].replace("=","")
                hosts[i] = hosts[i].replace("\n","")
                hosts[i] = hosts[i].lstrip()
                password = hosts[i]
                ultimaLInha = i+1
                lido = True
                break
    linhaAtual = linhaAtual+1

    tn = telnetlib.Telnet(HOST)

    tn.read_until(b"Username: ")
    tn.write(user.encode('ascii') + b"\n")
    if password:
        tn.read_until(b"Password: ")
        tn.write(password.encode('ascii') + b"\n")

    #Comando 1
    """
    tn.write(b"configure terminal\n")
    tn.write(b"router ospf 1\n")
    aux = bytes(("router-id "+str(linhaAtual)+"."+str(linhaAtual)+"."+str(linhaAtual)+"."+str(linhaAtual)+"\n"),encoding='utf-8')
    tn.write(aux)
    tn.write(b"exit\n")
    tn.write(b"interface fastethernet 0/0\n")
    tn.write(b"ip ospf 1 area 0\n")
    tn.write(b"exit\n")
    for i in range (1,10):
        aux = bytes(("interface loopback "+str(i)+"\n"),encoding='utf-8')
        tn.write(aux)
        aux = bytes(("ip address "+str(linhaAtual)+"."+str(linhaAtual)+"."+str(i)+".1"+" 255.255.255.0\n"),encoding='utf-8')
        tn.write(aux)
        tn.write(b"ip ospf 1 area 0\n")
        tn.write(b"exit\n")
        sleep(0.5)
    tn.write(b"end\n")
    sleep(0.5)
    tn.write(b"exit\n")
    """

    #Comando 2
    
    tn.write(b"configure terminal\n")
    tn.write(b"crypto key generate rsa \n")
    tn.write(b"2048\n")
    tn.write(b"end \n")
    sleep(0.5)
    tn.write(b"exit")
    
    
    
    

