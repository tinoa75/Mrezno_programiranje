#port_skener

import socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
import datetime
import nmap

from local_machine_info import print_machine_info
 
print (datetime.datetime.now())
print_machine_info()

nmScan = nmap.PortScanner()


target = input("Upisite IP adresu koju cemo skenirati: ")

nmScan.scan('127.0.0.1', '12340-12350')

def scanner(port):
    try:
        sock.connect((target, port))
        return True
    except:
        return False

for portNumber in range(12340,12350):
    print("Scanning port", portNumber)
if scanner(portNumber):
    print('[*] Port', portNumber, '/tcp','is open')