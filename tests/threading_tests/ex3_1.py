#don't run this, it goes crazy!


#let us profile some threads
import time
from threading import *

class itemQ(object):

	def __init__(self):
		self.count = 0

	def produce(self, num=1):
		self.count += num

	def consume(self):
		if self.count:self.count -= 1

	def isEmpty(self):
		return not self.count


class Producer(Thread):

	def __init__(self, condition, itemq, sleeptime=1):
		Thread.__init__(self)
		self.comd = condition
		self.itemq = itemq
		self.sleeptime = sleeptime

	def run(self):
		comd = self.comd
		itemq = self.itemq
		
		while 1:
			comd.acquire() #acquire the lock
			print currentThread(), "produced one item"
			itemq.produce()
		comd.notifyAll()
		comd.release()
		time.sleep(self.sleeptime)


class Consumer(Thread):

	def __init__(self, condition, itemq, sleeptime=2):
		Thread.__init__(self)
		self.comd = condition
		self.itemq = itemq
		self.sleeptime = sleeptime

	def run(self):
		comd = self.comd
		itemq = self.itemq
		
		while 1:
			time.sleep(self.sleeptime)
			comd.acquire() #acquire the lock

			while itemq.isEmpty():
				comd.wait()
				itemq.consume()
				print currentThread(), "Consumed one item"
				comd.release()

if __name__ == '__main__':
	
	q = itemQ()
	comd = Condition()

	pro = Producer(comd, q)

	cons1 = Consumer(comd, q, sleeptime=1)

	cons2 = Consumer(comd, q, sleeptime=1)

	pro.start()
	coms1.start()
	cons2.start()

	while 1:pass
