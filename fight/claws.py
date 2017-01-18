import random, attacks, other_stats
from accessible_output import speech
spk = speech.Speaker().output


class Claw(object):
	def __init__(self):
		self.name = "Sharp Claws (two handed)"
		self.type = "weapon"
		self.level = 5
		self.flags = ["two-handed"]
		self.stats = other_stats.Weapon_stats()
		self.max_hit = self.level*1.6
		self.acts = {"swipe": attacks.A(speed=3, type="attack", sound="sounds/hit2.ogg", message="The bear swipes its claws across your chest, leaving bloody gashes", str_boness=1, ac_boness=4), "rake": attacks.A(speed=2, sound=random.choice(["sounds/hit3.ogg", "sounds/hit.ogg"]), message="The bear slowly pulls its claws through your skin", str_boness=8, type="strength")}
		self.current_attack = self.acts['swipe']
	def extra_boness(self, fo):
		return 0
	def attack_choice(self, name):
		"""Checks if it is a mob or player asking for the attack and chooses attacks accordingly."""
		if 'mob' in name.flags:
			self.current_attack = self.acts[random.choice(self.acts.keys())]
		return self.current_attack


if __name__ == ("__main__"):
	b = Claw()

	print b.acts["swipe"].str_boness
	print "Changing"
	b.acts["swipe"].str_boness = 9
	print b.acts['swipe'].str_boness
	print b.acts["swipe"].message
	#spk("test o yeah!")
	print "Here is the attack: %s" % Claw().attack_choice(['mob'])
