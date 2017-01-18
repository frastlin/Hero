import pygametest as p, time, threading, random



def funk2():
	"""Is the function you should be able to run  without stopping the other threads"""
	p.speak("You pressed the space bar!")

class Tr(object):
	def __init__(self):
		self.fos = 3
		self.number = 0
		self.lost = False

	def start_threads(self):
		l = []
		for s in range(self.fos):
			l.append(threading.Thread(target=self.funk1, args=(random.choice(["nimu", "john", "frank", "fredric", "johanis", "enrica", "liana", "jef", "rocko", "lolla", "sarah", "ruth"]), 5)))
		for j in l:
			j.start()
		self.fos += 1
		p.speak("Now the foes are up to %s!" % self.fos)
	def funk1(self, name="fred", level=0):
		"""Is the function each one of the threads runs"""
		if self.dead():
			return True
		while self.number < 10:
			self.number += 1
			p.speak("I am %s and this is the number now: %s" % (name, self.number))
			time.sleep(random.randint(1,5))
		if self.dead():
			return True
	def dead(self):
		if self.number >= 10:
			if self.lost == False:
				self.lost = True
				p.speak("You lost! try again!!!!!")
				self.number = 0
				self.fos = 3
			return True
		else:
			return False


def main():
	k = Tr()
	global number
	p.screen()
	play = True
	while play:
		n = p.key2()
		if n[0] == "escape":
			play = False
		elif n[0] == "space":
			funk2()
		elif n[0] == "down":
			k.number -= 1
		elif n[0] == "s":
			p.speak("the number is: %s" % k.number)
		elif n[0] == "g":
			p.speak("There are currently %s foes" % k.fos)
		elif n[0] == "return":
			p.speak("starting threads")
			t5 = threading.Thread(target=k.start_threads)
			t5.start()

main()
