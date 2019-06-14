import multiprocessing as mp

import datetime
from local_machine_info import print_machine_info
if __name__ == '__main__':
    
	datum = datetime.datetime.now()
	print(datum)
	print_machine_info()



def my_func(x):
	print(x**x) #x na x

def main():
	pool = mp.Pool(mp.cpu_count())
	result = pool.map(my_func, [4,2,3])
	
if __name__ == "__main__":
	main()