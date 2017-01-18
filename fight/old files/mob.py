#creats mobs and under are the mobs
import u

class Monster(object):
	def __init__(self, name, short_desc, level):
		self.name = name
		self.short_desc = short_desc
		self.long_desc = short_desc
		self.level = level
		self.hp = u.hper(level)
		self.current_hp = self.hp
		self.str = level
		self.mstr = self.str
		self.attack = level
		self.mattack = self.attack
		self.defense = level
		self.mdefense = self.defense

		self.weapon = weapons.weapon_list["fists"]
		self.wearing = {'left': None, 'right': None}
		self.fo = None

bear = Monster("bear", "a bear", 6)

