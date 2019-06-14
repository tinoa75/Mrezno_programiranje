from multiprocessing import Process, Queue
import random

import datetime
from local_machine_info import print_machine_info
if __name__ == '__main__':
    
	datum = datetime.datetime.now()
	print(datum)
	print_machine_info()

def rand_num():
    num = random.random()
    print ("\n %f" % num)

if __name__ == "__main__":
    queue = Queue()

    processes = [Process(target=rand_num, args=()) for x in range(4)] 
    
    for p in processes:
        p.start()

    for p in processes: 
        p.join()