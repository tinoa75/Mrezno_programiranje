
import socket
import datetime
from local_machine_info import print_machine_info

adresa_servera = ('localhost', 12345)

client_socket = socket.socket()

client_socket.connect(adresa_servera)

print(print_machine_info())
print(datetime.datetime.now())

print('Molim vas upisite tekst za slanje serveru:')
poruka = input(" -> ")

while poruka != 'aspira':
    client_socket.send(poruka.encode())
    data = client_socket.recv(1024).decode()
    print('Odgovor servera: ' + data.decode())
    client_socket.close()
