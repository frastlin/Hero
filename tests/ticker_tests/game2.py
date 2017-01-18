# fight against a creature
import sys, ticker, pygametest, random, pygame
spk = pygametest.speak

c = ticker.Scheduler(0.001)
fps = 30
fpsClock = pygame.time.Clock()

class Creature:
	"""Create mobs and players"""

	def __init__(self, name, hp=10, strength=1, mob=True):
		self.name = name
		self.hp = hp
		self.strength = strength
		self.mob = mob

		#our operation variables
		self.attack_list = {}
		self.did_hit = True
		self.living = True

	def add_attack(self, name, pre_message, hit_message, strength, sounds={}):
		"""Call this to add an attack to the creature's attack list"""
		self.attack_list[name] = Attack(name, messages={"pre_message": pre_message, "hit_message": hit_message}, stats={"strength": strength}, sounds=sounds)

	def attacker(self, fo, key=None):
		"""Will attack the fo"""
		if self.hp > 0 and fo.hp > 0:
			if self.mob:
				self.mob_attack(fo)
			else:
				self.player_attack(key, fo)
		if self.hp <= 0:
			self.death()

	def mob_attack(self, fo):
		"""Does mob attacks"""
		if self.did_hit:
			a = self.attack_list[random.choice(self.attack_list.keys())]
			a.anounce("pre_message")
			c.schedule(self.hitter, a.speed(), attack=a, fo=fo)
			self.did_hit = False

	def player_attack(self, key, fo):
		"""Manages player attacks"""
		a = self.attack_list.get(key)
		if self.did_hit and a:
			a.anounce("pre_message")
			c.schedule(self.hitter, a.speed(), attack=a, fo=fo)
			self.did_hit = False

	def hitter(self, attack, fo):
		"""Does the attack at the end of the event"""
		if self.living and fo.living:
			h = attack.run()
			attack.anounce("hit_message", self.name, fo.name, h)
			fo.hp -= h
			self.did_hit = True

	def death(self):
		"""Is the death message"""
		spk("%s is dead!" % self.name)
		self.living = False

class Attack:
	"""Makes attacks"""
	def __init__(self, name, messages={}, stats={}, sounds={}):
		self.name = name
		self.messages = messages
		self.stats = stats
		self.sounds = sounds

		#operations:
		default_stats = {"min_speed": 1, "max_speed": 3, "strength": 1}
		[self.stats.update({i: default_stats[i]}) for i in default_stats if i not in self.stats]
		[self.stats.update({i: float(self.stats[i])}) for i in self.stats]
		[self.sounds.update({i: pygame.mixer.Sound(self.sounds[i])}) for i in self.sounds]

	def speed(self):
		"""Makes the speed random"""
		return(random.uniform(self.stats["min_speed"], self.stats["max_speed"]))

	def run(self):
		"""Calculates the damage"""
		return random.randint(1, self.stats['strength'])

	def anounce(self, message_name, *args):
		"""You pass a string of the message name and it will check both messages and sounds for that message"""
		message = self.messages.get(message_name)
		sound = self.sounds.get(message_name)
		if message:spk(message.format(*args))
		if sound:sound.play()




pygametest.screen("Fighter")
fighting = False
play = True
while play:
	k, m = pygametest.key()

	if k == "escape":
		pygame.quit()
		sys.exit()
	elif k == "space":
		fighting = True
		b = Creature("Bear")
		b.add_attack(name="slash", pre_message="The big black bear pulls his claw back for a massive swing", hit_message="The claws of the bear slam into {1}'s chest, doing {2} points of damage", strength=5, sounds={"hit_message": "sounds/hit.ogg", "pre_message": "sounds/groul.ogg"})
		p = Creature("You", mob =False)
		p.add_attack("1", "You pull your sword back to swing", "You slash your sword across {1}'s chest, leaving a bluddy gash causing {2} points of damage.", 5, sounds={"hit_message": "sounds/hit3.ogg"})

	if fighting:
		p.attacker(b, k)
		b.attacker(p)
		if not b.living or not p.living:
			fighting = False

	c.tick(fpsClock.tick(fps))
