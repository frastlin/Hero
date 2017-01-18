import sword, creature, armor as a
from game import globals

class Person(object):
	descs = creature.Descriptions(name="You", short_desc="You are here")
	stats = creature.Stats()
	inv = globals.inv
	body = globals.equ
	flags = ['player']
	armor = a.Arm(body=body)
	weapon = sword.Sword()
	fight_sounds = "sounds/grunt.ogg"
	def defense_boness(self):
		"""If for some reason I choose to add extra defense somewhere, this is where it would go."""
		return 0

