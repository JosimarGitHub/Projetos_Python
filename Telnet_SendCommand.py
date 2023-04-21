#Bibliotecas importadas
import sys
import telnetlib

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

    #Comando
    
    tn.write(b"configure terminal\n")
    tn.write(b"interface loopback 54\n")
    tn.write(b"ip address 54.52.52.54 255.255.255.255\n")
    tn.write(b"end\n\n")
    time = 0
    for delay in range(10000000):
       time = time+1
    tn.write(b"exit\n")

    """tn.write(b"crypto key generate rsa \n")
    tn.write(b"2048 \n")
    tn.write(b"end \n")
    tn.write(b"exit")"""

    """tn.write(b"Reload\n")
    flag = 0
    for delay in range(1000):
        flag = flag+1
    tn.write(b"\n")
    for delay in range(1000):
        flag = flag+1
    tn.write(b"yes\n")
    for delay in range(1000):
        flag = flag+1"""
    
    
    

