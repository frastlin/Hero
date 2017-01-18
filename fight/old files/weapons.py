#weapons!

class Weapon(object):
	def __init__(self, name, short_desc, min_level, weapon_options=["slash", "stab", "defend"], min_damage=0, ac=0, str=0, special=None):
		self.name = name
		self.short_desc = short_desc
		self.long_desc = short_desc
		self.weapon_options = weapon_options
		self.min_damage = min_damage
		self.max_damage = min_damage *1.6
		self.ac = ac
		self.str = str
		self.special = special
		flags = ["weapon"]
	def mattack_chooser(self):
		a = random.choice(self.weapon_options)
		
		spk(attacks.astr.get(attack_name, "No attack named %s" % attack_name).format(self.name "your foe!", "its"))



weapon_list = {
"sword1": Weapon("The Sword of Night", "A darker than night sword sucks the light from around it", 5),

"claws": Weapons("Razer Sharp Claws", "These vishous claws look like they could do some serious damage!", 5, ["swipe", "eviserate", "slash"]),

}


