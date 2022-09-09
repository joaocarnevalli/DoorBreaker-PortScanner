## PortScanner - CP 5 - FIAP ##

import socket
import ipaddress
import sys
from tracemalloc import start
import pyfiglet
import time
from concurrent.futures import ThreadPoolExecutor
from time import sleep
from datetime import date


web = ["web", "website", "site"]
ip = ["ip"]
positivo = ["sim", "s", "Sim", "yes", "Yes", "y"]
negativo = ["nao", "não", "n", "Não", "Nao", "no", "No"]
passs = False
passs1 = False
specify = False
relatorio = False
pergunta = False
validate = False
today = date.today()
todaydate = today.strftime("%b-%d-%Y")
# Função de slowprint (Efeito de escrever)
def slowprint(a):
    for c in a+ '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(1./10)


# Função de fastprint (Efeito de escrever)
def fastprint(a):
    for c in a+ '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(1./10000)


# Scan Function
def test_port_number(host, port):
    # Criação do socket
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        # Setando um timeout
        sock.settimeout(3)
        try:
            # Tentativa de conexão
            sock.connect((host, port))
            
            # Conexão estabelecida (Porta aberta)
            return True

        except:
            # Ignorar o erro
            return False

sleep(0.7)
print(pyfiglet.figlet_format(" Door Breaker"))
sleep(0.66554)
fastprint("<------------------------------------------------------------->")


# Multithread Scan
def port_scan(host, ports):
    global count
    t = time.localtime()
    currenttime = time.strftime("%H:%M:%S", t)
    print(f"<------------------------------------------------------------------>")
    print(f"         {todaydate} - {currenttime} - Scanning the host {host}\n")
    with open(r"C:/Users/joaos/Documentos/TESTE/relatorioPORTAS.txt", "a") as fp:
        fp.write(f"<------------------------------------------------------------------>\n         {todaydate} - {currenttime} - Scanning the host {host}\n")
    with ThreadPoolExecutor(len(ports)) as executor:
        resultado = executor.map(test_port_number, [host]*len(ports), ports)
        for port,portopen in zip(ports,resultado):
            if portopen:
                try:
                    print(f'> {port} open - {socket.getservbyport(port)}')
                    with open(r"C:/Users/joaos/Documentos/TESTE/relatorioPORTAS.txt", "a") as fp:
                        fp.write(f'> {port} open - {socket.getservbyport(port)}\n')
                except:
                    continue
            else:
                count = count + 1


# Inicio do programa
while True:
    while True:
        try:
            if passs == True:
                break
            if pergunta == False:
                while True:
                    try:
                        fastprint("Want to scan a website or an ip?")
                        ask = str(input(" > ")).lower()
                        if ask in web or ask in ip:
                            break
                        else:
                            fastprint("\n\nType IP or WEB!\n\n")
                    except ValueError:
                        fastprint("\n\nType something\n\n")


## Gerar o relatorio
            if relatorio == False:
                while True:
                    try:
                        fastprint("At the end of the procedure, would you like to generate a report?")
                        askrelat = str(input(" > ")).lower()                        
                        if askrelat in positivo:
                            with open(r"C:/Users/joaos/Documentos/TESTE/relatorioPORTAS.txt", "w") as fp:
                                relatorio = True
                                break
                        elif askrelat in negativo:
                            break
                        else:
                            print("\n\nType YES or NO!\n\n")                        
                    except ValueError:
                        print("\n\nType something!\n\n")


# Input URL target
            if ask in web:
                while True:
                    try:
                        fastprint("URL Target: ")
                        target = input(" > ")
                        if len(target) <= 8:
                            fastprint("Type something!")
                        elif len(target) <= 0:
                            fastprint("Type something!")
                        elif target.isdigit():
                            fastprint("Please enter a valid URL!")
                        else:
                            passs = True
                            break
                    except ValueError:
                        fastprint("Type something!")


## Input IP target
            elif ask in ip:
                while True:
                    try:
                        fastprint("IP Target: ")
                        target = input(" > ")
# Validando se o targer é um IP valido
                        try:
                            ip = ipaddress.ip_address(target)
                            validate = True
                        except ValueError:
                            validate = False
                        if len(target) <= 0:
                            fastprint("Type something!")
                        elif validate == False:
                            fastprint("Please enter a valid IP!")
                        else:
                            passs = True
                            break
                    except ValueError:
                        fastprint("Type something!")
            else:
                fastprint("Please enter a valid value!")
        except ValueError:
            fastprint("Please enter a valid value!")


# Pergunta especificação de range
    while True:
        try:
            if passs1 == True:
                break
            fastprint("Want to specify the port range? ")
            ask = str(input(" > ")).lower()
            if ask in positivo:
                while True:
                    try:
                        fastprint("Start port: ")
                        startport = int(input(" > "))
                        if startport <= 0:
                            fastprint("Type something!")
                        elif startport > 65536:
                            fastprint("65536 is the maximum port!")
                        else:
                            passs1 = True
                        fastprint("Stop port: ")
                        stopport = int(input(" > "))
                        if stopport <= 0:
                            fastprint("Type Something")
                        elif startport > 65536:
                            fastprint("65536 is the maximum port!")
                        if stopport < startport:
                            fastprint("type end port smaller than start port")
                        else:
                            passs1 = True
                            specify = True
                            break
                    except ValueError:
                        fastprint("Type YES or NO!")
            elif ask in negativo:
                passs1 = True
                break
        except ValueError:
            fastprint("Type YES or NO!")


# range definido pelo usuario.
    if specify == True:
        count = 0
        start_time = time.time()
        port_scan(target, range(startport, stopport))
        t = time.localtime()
        currenttime = time.strftime("%H:%M:%S", t)
        with open(r"C:/Users/joaos/Documentos/TESTE/relatorioPORTAS.txt", "a") as fp:
            fp.write("\n> Not shown: {} closed ports\n         {} - {} - Elapsed time: {:.2f} seconds\n<------------------------------------------------------------------>\n".format(count, todaydate, currenttime, time.time() - start_time))
            fp.close()
        print("\n> Not shown: {} closed ports\n         {} - {} - Elapsed time: {:.2f} seconds\n<------------------------------------------------------------------>\n".format(count, todaydate, currenttime, time.time() - start_time))
        break


# Scan nas principais portas definidas pelo IANA
    if specify == False:
        count = 0
        ports = range(1024)
        host = target
        start_time = time.time()
        port_scan(host, ports)
        t = time.localtime()
        currenttime = time.strftime("%H:%M:%S", t)
        with open(r"C:/Users/joaos/Documentos/TESTE/relatorioPORTAS.txt", "a") as fp:
            fp.write("\n> Not shown: {} closed ports\n         {} - {} - Elapsed time: {:.2f} seconds\n<------------------------------------------------------------------>\n".format(count, todaydate, currenttime, time.time() - start_time))
            fp.close()
        print("\n> Not shown: {} closed ports\n         {} - {} - Elapsed time: {:.2f} seconds\n<------------------------------------------------------------------>\n".format(count, todaydate, currenttime, time.time() - start_time))
        break
