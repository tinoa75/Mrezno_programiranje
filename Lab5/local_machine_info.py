import socket


def print_machine_info():

    host_name = socket.gethostname()
    ip_address = socket.gethostbyname('localhost')

    print("------------------------------")
    print("Program se izvodi na racunalu:")
    print("Host name:' %s" % host_name)
    print("IP address: %s" % ip_address)
    print("------------------------------")

if __name__ == '__main__':

    print_machine_info()
