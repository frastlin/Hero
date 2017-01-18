import attacks, other_stats, random, collections

class Sword(object):
	def __init__(self):
		self.name = "The sword of night"
		self.type = ["weapon", "blade"]
		self.level = 1
		self.flags = []
		self.stats = other_stats.Weapon_stats()
		self.max_hit = self.level*1.6
		self.acts = collections.OrderedDict()
		self.acts["slash"] = attacks.A(speed=3, type="attack", sound="sounds/hit2.ogg", message="You slash {1} with your sword")
		self.acts["stab"] = attacks.A(sound=random.choice(["sounds/hit3.ogg", "sounds/hit.ogg"]), message="You jab the pointy end of the Sword into {1}", type="strength")
		self.acts["defend"] = attacks.A(type="defense", message="You try and fend off attacks while managing to get in a swipe of your own.", sound="hit.ogg")
		self.current_attack = self.acts['slash']
	def extra_boness(self, fo):
		return 0

	def attack_choice(self, name):
		"""Checks if it is a mob or player asking for the attack and chooses attacks accordingly."""
		if 'mob' in name.flags:
			self.current_attack = self.acts[random.choice(self.acts.keys())]
		return self.current_attack

