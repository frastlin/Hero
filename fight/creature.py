#All the different classes players and mobs can use for descriptions, classes, attacks and whatnot.
import stats, iteration


class Descriptions(object):
	def __init__(self, name="quackers", short_desc=None, long_desc=None):
		self.name = name
		self.self_name = "your"
		self.short_desc = short_desc
		self.long_desc = self.long_desc_default(long_desc)
	def long_desc_default(self, l_d):
		"""checks if the long description is none and if it is, makes it the short_desc"""
		if l_d:
			return l_d
		else:
			return self.short_desc

class Stats(object):
	"""Lists the stats and keeps track of them. if you supply an argument, the stat will be that level."""
	def __init__(self, strength=1, attack=1, defense=1, hp=1, all_level=0):
		if all_level:
			strength = all_level
			attack = all_level
			defense = all_level
			hp = all_level

		self.strength = stats.Strength(level=strength, name="Strength")
		self.attack = stats.Attack(level=attack, name="Attack")
		self.defense = stats.Defense(level=defense, name="Defense")
		self.hp = stats.Hp(level=hp, name="Hit points")


class Body_basic(object):
	def __init__(self, body={'head': None, 'feet': None, 'right hand': None, 'left hand': None}, hands=['left hand', 'right hand']):
		"""hands are used for english pirpuses and weapon pirpuses. OrderedDict makes what ever order is put at start, the order the dict is in when it is listed."""
		from collections import OrderedDict
		self.body = OrderedDict(body)
		self.hands = hands

	def wearing(self):
		"""prints out a nice message with all items wearing unless there is nothing which then it says 'nothing'"""
		s = ""
		for k in self.body:
			if self.body[k]:
				s += "\n%s: %s" % (k, self.body[k].name)
		if s:
			return "You are wearing" + s
		else:
			return "You are wearing:\nNothing!"

if __name__ == ("__main__"):
	class w(object):
		def __init__(self, name="fred"):
			self.name = name

	d = w()
	b = w("zooloo")
	c = w("nagashon")

	a = Body_basic()

	a.body["left hand"] = b
	a.body["right hand"] = c
	a.body["torso"] = d

	print "This is a big green bear"
	print a.wearing()
