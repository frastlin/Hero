#Instances of each of the skill class. I can modify different things to happen each class.
import xp_equasions, messages

class Stat(object):
	"""Is what every skill has. Define the skills below"""
	def __init__(self, level=1, name="Default skill"):
		self.level = level
		self.name = name
		self.mod_level = level
		self.xp = 0
		self.next_level = self.nl()
	def boness(self, extra_level=0):
		return 0
	def nl(self):
		"""Calculates the amount needed for the next level and makes next_level equal that amount, it is the big 			number"""
		if self.level == 0:
			self.next_level = 75
		else:
			self.next_level = xp_equasions.Xp().level_to_xp(self.level+1)
		return self.next_level
	def tnl(self, levelto=0):
		"""Call this with no arguments to get how much xp it is to the next level. add arguments to know how much xp it 		is to that level"""
		if not levelto:
			return self.next_level - self.xp
			print self.next_level
		else:
			return xp_equasions.Xp().level_to_xp(self.level+1) - self.xp
	def xp_add(self, xp=0):
		"""is basicly a leveler and is what should be called to add xp."""
		if xp == 0:
			return None
		else:
			self.xp += xp
		if self.xp >= self.next_level:
			l = xp_equasions.Xp().xp_to_level(self.xp) - self.level
			if l > 0:
				if l == 1:
					s = "You have gained a level in {1}!"
				elif l > 1:
					s = "You have gained {0} levels in {1}!"
				self.level += l
				self.next_level = self.nl()
				s = s.format(l, self.name)
				print s
				messages.add_message(s)
				return s



class Strength(Stat):
	def boness(self, extra_level=0):
		"""gives bonesses for each level and returns the boness"""
		return (self.level + extra_level) * 2.5

class Attack(Stat):
	def boness(self, extra_level=0):
		ac = (self.level + extra_level) * 0.8
		return ac + 9

class Defense(Stat):
	def boness(self, extra_level=0):
		deff = (self.level + extra_level) * 0.8
		return deff + 9

class Hp(Stat):
	def __init__(self, level=10, name="Hit Points"):
		Stat.__init__(self)
		self.level = level
		self.current_hp = level
		self.name = name
	def hit(self, dam):
		"""Removes or adds hp depending on what kind of argument is passed"""
		self.current_hp-=dam
		if self.current_hp <= 0:
			return False
		else:
			return True


if __name__ == ("__main__"):

	print "Here is strength default level: %s" % Strength().level
	s = Strength(level=5, name="strength")
	s.xp += 9
	d = Defense()
	print "Strength's xp is: %s and defense's xp is: %s" % (s.xp, d.xp)
	print "strength's modified level from the __init__ level is: %s" % s.level
	h = Hp(name="Hit points")
	print "Here is HP: " + str(h.level)
	at = Attack()
	print at.boness(2)
	print s.boness(2)
	print "You need %s xp before you reach level %s in strength" % (s.tnl(), s.level+1)
	print "You need %s xp before you reach level %s in hp" % (h.tnl(), h.level+1)
	print("adding 50 xp to hp:")
	h.xp_add(50)
	print("Now you are level %s in hp and need %s xp to advance in hp" % (h.level, h.tnl()))
	print("Adding 2000 xp to hp")
	h.xp_add(2000)
	print "You now are level %s with %s xp in hp" % (h.level, h.xp)
	print("now you need %s xp to advance in hp" % h.tnl())
	s.xp_add(4000)
	print h.nl()