import time, random

class Creature(object):
	def __init__(self):
		self.ctime = 0
		self.name = "fred"
	def fight(self):
		"""waits for a second, then punches till death triggers"""
		if self.death():
			return 0
		if self.ctime < 1:
			self.ctime += 0.05
		else:
			self.ctime = 0
			self.hit()
	def death(self):
		pass
	def hit(self):
		if random.randint(0,2):
			h = random.randint(1,5)
			print "%s swings his club and hits for %s damage!" % (self.name, h)
			return h
		else:
			print "%s swings his club at the air!" % self.name
			return 0



b = Creature()

while True:
	b.fight()
	time.sleep(0.05)
