# -- coding: utf-8 --
#echo_server.py
import socket
import datetime
from local_machine_info import print_machine_info
 
print (datetime.datetime.now())
print_machine_info()
 
host = socket.gethostname()
port = 12345
 
echo_server = socket.socket()       # TCP socket
echo_server.bind((host,port))
echo_server.listen(5)
 
print ("Cekam klijente...")
#conn, addr = echo_server.accept()          # Prihvaćanje konekcije kada se klijent spoji
#print "Spojen: ", addr
 
while True:
    conn, addr = echo_server.accept()
    print ("Spojen: ", addr)
    data = conn.recv(1024)      # Prihvaćanje podataka od klijenta
    if not data: break          # ako nema podataka izađi
    if data == 'aspira':
        conn.sendall("Molimo unesite drugi tekst; aspira unos nije podrzan")
    else:
        conn.sendall(data)          # Vrati primljene podatke klijentu