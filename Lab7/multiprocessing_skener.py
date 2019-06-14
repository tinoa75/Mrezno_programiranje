from __future__ import print_function
from multiprocessing import Pool

import multiprocessing
import socket
import sys
import datetime
from local_machine_info import print_machine_info

def host_to_ip(host):
    print("[+] Resolving", host)
    return socket.gethostbyname(host)


def scan(target):
    target_ip, port = target

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(2)

    try:
        sock.connect((target_ip, port))
        sock.close()

        return port, True
    except (socket.timeout, socket.error):
        return port, False

if __name__ == '__main__':

	host = raw_input("Unesite adresu hosta koju zelite testirati: ")
	print("Unesite od kojeg do kojeg porta zelite napraviti skeniranje")
	start = raw_input("Pocetni port: ")
	end = raw_input("Zavrsni port: ")

	if not host.replace(".", "").isdigit():
		host = host_to_ip(host)
		print("[+] Scanning", host)

		ports = range(int(start), int(end)+1)
		scanlist = [(host, port) for port in ports]

		pool = Pool(multiprocessing.cpu_count()*2)
		
		for port, status in pool.imap(scan, scanlist):
			if status:
				print("[!]", port, "is open")
		print("[+] Finished scanning", host)