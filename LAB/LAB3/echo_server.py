import socket
import datetime


adresa_servera = ('localhost', 12345)

echo_server = socket.socket()
echo_server.bind(adresa_servera)
echo_server.listen(5)

datum_vrijeme = datetime.datetime.now()

print('Server pokrenut u:')
print(datetime.datetime.now())
print('Cekam klijenta na: {} port {}'.format(*adresa_servera))

echo_server.listen(1)
conn, addr = echo_server.accept()
print("Klijent spojen: " + str(addr))

while True:
    data = conn.recv(1024).decode()
    if not data:
        break
    print("primljeno od klijenta: " + str(data))
    print("saljem nazad: " + str(data))
    conn.send(data.encode())

    conn.close()


while True:
    data = conn.recv(1024)
    if not data:
        break
    conn.sendall(data)
conn.close()
