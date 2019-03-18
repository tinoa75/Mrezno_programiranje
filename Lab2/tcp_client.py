
import socket

client_socket = socket.socket()
host = socket.gethostname()
port = 9999 

client_socket.connect(('localhost',port))
print client_socket.recv(1024)
client_socket.close()