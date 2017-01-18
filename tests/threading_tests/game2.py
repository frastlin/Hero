import threading, random, pygametest

class Creature(object):
	def __init__(self, name="fred", hp=10, flags=[]):
		self.name = name
		self.hp = hp
		self.flags = flags
		self.d = False

	def hit(self, fo):
		if self.death_check(fo):
			return True
		n = random.randint(1,3)
		fo.hp -= n
		pygametest.speak("%s hits %s for %s damage!" % (self.name, fo.name, n))
		if self.death_check(fo):
			return True
		pygametest.rest(random.randint(1000,4000))
		return self.death_check(fo)

	def death_check(self, fo):
		self.mydeath()
		if self.hp <= 0 or fo.hp <= 0:
			return True
		else:
			return False

	def mydeath(self):
		if self.hp <= 0 and "mob" in self.flags:
			pygametest.speak("%s has died" % self.name)
		elif self.hp <= 0 and "player" in self.flags:
			pygametest.speak("You have died!")
		self.d = True

class Keyboard(object):
	def __init__(self):
		self.scene = scene

def threader(player, fo):
	pl = threading.Thread(target=mob_main, args=(player, fo))
	m = threading.Thread(target=mob_main, args=(fo, player))
	pl.daemon = True
	m.daemon = True
	pl.start()
	m.start()
	pygametest.speak("exeting the activating thread.")

def mob_main(name, fo):
	play = False
	while not play:
		play = name.hit(fo)
	pygametest.speak("%s has finished" % name)

def keyboard_default(play, key):
	if n[0] == "escape":
		return False
	elif n[0] == "h":
		if n[1] in [4097, 4353, 4354, 4098]:
			p.speak("%s has %s hp out of 10" % (fo.name, fo.hp))
		else:
			p.speak("You have %s/10 hp" % name.hp)
		return play
	elif n[0] == "space" and n[1] in [4097, 4353, 4354, 4098]:
		play = ("heal", play[1])
	elif n[0] == "1":
		p.speak("This is the screen %s" % screen)
	elif n[0] == "g":
		p.speak(threading.enumerate())
	return play

def screen_changer(play, n):
	if play[1] == "rest":
		if n[0] == "return":
			p.speak("starting the battle")
			return ("fight_start", "fight")

def player_main(name, fo):
	p = pygametest
	p.screen("fighter")
	play = (True, "rest")
	while play:
		n = p.key2()
		play2 = keyboard_default(play, n)
		play3 = screen_changer(play, n)
		l = [play2, play3]

if __name__ == '__main__':
	pl = Creature(name="queen", flags="player")
	m = Creature(name="mob", flags=['mob'])
	player_main(pl, m)
