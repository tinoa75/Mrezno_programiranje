# -- coding: utf-8 --
#echo_client.py
import socket
import datetime
from local_machine_info import print_machine_info
 
print (datetime.datetime.now())
print_machine_info()
 
host = socket.gethostname()
port = 12345
client_socket = socket.socket()     # TCP socket
 
client_socket.connect((host,port))
print ("Molim vas unesite tekst za slanje serveru")
text = raw_input("> ")
 
client_socket.sendall(text)
 
data = client_socket.recv(1024)     # Tekst koji je primljen od servera
 
print (data)
# Ispis podataka