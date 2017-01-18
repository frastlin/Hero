import pygame, random, ticker
pygame.init()

fps = 30
fpsClock = pygame.time.Clock()
c = ticker.Scheduler(0.001)

play = True

class Creature:
	def __init__(self, name, hp=10):
		self.name = name
		self.hp = hp
		self.did_hit = True
		self.alive = True

	def attack(self, fo):
		"""Will check if either it or fo are dead and if so, will call death, else it will swing"""
		if self.hp <= 0:
			self.death()
		elif fo.hp > 0 and self.did_hit:
			c.schedule(self.hit, random.uniform(1.0,3.0), fo=fo)
			self.did_hit = False

	def hit(self, fo):
		"""Takes hp from fo"""
		hit = random.randint(1,3)
		if self.hp > 0:
			fo.hp -= hit
			self.did_hit = True
			print("%s swings his club and hits a %s on %s" % (self.name, hit, fo.name))


	def death(self):
		print("%s is dead!" % self.name)
		self.alive = False



b = Creature("Bear")
f = Creature(name="Frog")

while play:
	if f.alive:
		f.attack(b)
	if b.alive:
		b.attack(f)
	c.tick(fpsClock.tick(fps))

