import time, random

class Ticker(object):
	def __init__(self, tick=0.6, framerate=60):
		self.tick = tick
#		self.clock = time.clock
		self.playing = True
		self.functions = []
		self.framerate = 1.0/framerate

	def wait(self, wait_time=0, name="g"):
		try:
			self.dict1[name] += self.framerate
		except AttributeError:
			self.dict1 = {}
			self.dict1[name] = self.framerate
		finally:
			if self.dict1[name] >= wait_time:
				return True

	def main_loop(self):
		while self.playing:
			[x() for x in self.functions]
			time.sleep(self.framerate)

a = Ticker()

def hello():
	if a.wait(1, "fred"):
		print "hello world"
		a.functions.remove(hello)

a.functions.append(hello)


a.main_loop()

#class t(object):
#	def __init__(self):
#		self.framerate = 0.016666
#
#	def add(self, wait_time=0, name="g"):
#		try:
#			self.dict1[name] += self.framerate
#		except AttributeError:
#			self.dict1 = {}
#			self.dict1[name] = self.framerate
#		finally:
#			if self.dict1[name] >= wait_time:
#				return True
#
#c = t()
#f = False
#while not f:
#	f = c.add(1, "fred")
#	time.sleep(c.framerate)
#
#print "done"
#
#
##a = Ticker()
##a.functions.append(hello)
#
#