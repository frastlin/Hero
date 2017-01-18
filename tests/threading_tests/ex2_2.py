

import time
from threading import Thread

class MyThread(Thread):

	def __init__(self, bignum):
		Thread.__init__(self)
		self.bignum = bignum

	def run(self):
		for l in range(10):
			for k in range(self.bignum):
				res=0
				for i in range(self.bignum):
					res += 1

def myadd_nothread(bignum):
	for l in range(10):
		for k in range(bignum):
			res = 0
			for i in range(bignum):
				res += 1

	for l in range(10):
		for k in range(bignum):
			res = 0
			for i in range(bignum):
				res += 1

def thread_test(bignum):
	#we create 2 objects for the two threads

	thr1 = MyThread(bignum)
	thr2 = MyThread(bignum)
	thr1.start()
	thr2.start()
	thr1.join()
	thr2.join()

def test():
	bignum = 1000

	#let us test the threading part
	starttime = time.clock()
	thread_test(bignum)
	stoptime = time.clock()
	print "running two threads took %.3f seconds" % (stoptime-starttime)

	#now we will run without threads:
	starttime = time.clock()
	myadd_nothread(bignum)
	stoptime = time.clock()

	print "running without threads took %.3f seconds" % (starttime -stoptime)

if __name__ == '__main__':
	test()
	profile.run('test()')
