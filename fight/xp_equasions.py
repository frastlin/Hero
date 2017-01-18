import math


class Xp(object):
	"""A much more accurate equasion for equating xp"""
	def equate(self, xp):
		return math.floor(xp + 300 * (2 ** (xp / 7.0)))
 
	def level_to_xp(self, level):
		return math.floor(sum((self.equate(lvl) for lvl in xrange(1, level))) / 4)
 
	def xp_to_level(self, xp):
		level = 1
		while self.level_to_xp(level) < xp:
			level += 1
		return level

 
def xp_counter(level=0):
	points = 0
	for l in range(1, level):
		diff = int(l + 300 * math.pow(2, float(l)/7))
		points += diff/4
	return points


def xp_test(level=0):
	t = 75
	for l in range(level):
		t *= 1.10409


class L(object):
	def __init__(self, level=0):
		self.level = level
		self.xp = 0
	def tnl(self, extra_level=1):
		le = xp_counter(self.level + extra_level)
		le -= self.xp
		return le

if __name__ == ('__main__'):
	x = L()
	rs = Xp()
	print Xp().level_to_xp(15)
	print Xp().xp_to_level(3000)
