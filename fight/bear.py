#This will create the bear class
import creature, claws, armor

class Bear(object):
	def __init__(self, level=5):
		self.level = self.level_check(level)
		self.descs = creature.Descriptions(name="The Bear", short_desc="A Big black bear is here")
		self.stats = creature.Stats(all_level=level)
		self.flags = ['mob']
		self.b = creature.Body_basic({"right paw and left paw": claws.Claw()}, hands=["right paw and left paw"])
		self.armor = armor.Arm(body=self.b)
		self.weapon = self.b.body["right paw and left paw"]
		fight_sounds = {"groul": "sounds/groul.ogg"}

	def defense_boness(self):
		"""If for some reason I choose to add extra defense somewhere, this is where it would go."""
		return 0

	def level_check(self, level):
		"""If I choose to give the bear a level as an easy default this checks for it and adds."""
		if level > 1:
			self.stats = creature.Stats(strength=level, attack=level, defense=level, hp=level)
		return level


if __name__ == ("__main__"):
	b = Bear()
	print b.descs.long_desc
	print b.stats.strength.level
	b.f = "Hi, I'm F!"
	print b.f
	print b.weapon.name


#latvian and astonian
