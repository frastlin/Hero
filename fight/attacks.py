import random

class A(object):
	def __init__(self, type=None, speed=3.1211, sound=None, message=None, str_boness=0, ac_boness=0, default=True):
		self.type = type
		self.speed = speed
		self.sound = sound
		self.message = message
		self.str = str_boness
		self.ac = ac_boness
		self.default = default
		if default:
			self. default_type(type)

	def default_type(self, t):
		"""If default is checked, a default type will be generated and if type=None, a random type will be chosen"""
		if t == None:
			self.typer()
		elif t == "strength":
			self.typer(speed=5, str=7, ac=-2)
		elif t == "attack":
			self.typer(speed=2, ac=5, str=0)
		elif t == "defense":
			self.typer(speed=3, str=0, ac=0)
		elif t == "balanced":
			self.typer(speed=3, str=2, ac=2)

	def typer(self, speed=random.randint(1,5), ac=random.randint(1,7), str=random.randint(1,7)):
		if self.speed == 3.1211:
			self.speed = speed
		if self.str == 0:
			self.str = str
		if self.ac == 0:
			self.ac = ac

if __name__ == ('__main__'):
	st = A(type="strength")
	print st.speed
	print st.ac
	print st.str
