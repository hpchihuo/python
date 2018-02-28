from multiprocessing import Process, Queue 
import os, time, random

def write(q):
	print('Process to write %s'% os.getpid())
	for value in ['A', 'B', 'C']:
		print('Put %s to queue...'%value)
		q.put(value)
		time.sleep(random.random())

def read(q):
	print('Process to read: %s'% os.getpid())
	while True:
		value = q.get(True)
		print('Get %s from queue.'% value)

if __name__ == '__main__':
	#父进程创建Queue，并传给各个只进程
	q = Queue()
	pw = Process(target=write, args=(q,))
	pr = Process(target=read, args=(q,))
	#启动子进程
	pw.start()
	pr.start()
	pw.join()
	pr.terminate()
