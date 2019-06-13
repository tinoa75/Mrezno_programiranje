from __future__ import print_function
import multiprocessing
import socket
import sys
import datetime
from local_machine_info import print_machine_info


if __name__ == '__main__':
    
	datum = datetime.datetime.now()
	print(datum)
	print_machine_info()
