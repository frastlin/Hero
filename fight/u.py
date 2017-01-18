#utility functions for the combat system
import random, globals, settings

def hper(level):
	hp = level*1.3
	if hp <=10:
		return 10
	else:
		return hp

def attacker(level):
	ac = level * 0.8
	return ac + 9

def strer(level):
	r = random.uniform(0.4, 0.6)
	return r * level

def defenser(level):
	return 0.5 * level

def change_attacks(attack=None):
	"""changes the globals.current_attack to the argument, if there is no argument, then it just talks the current_attack"""
	if attack:
		globals.current_attack = attack
	if settings.speak_attacks == True:
		spk(attack)

def speeder(attack_speed):
	"""Higher the number, faster the weapon is. You can do a range as well"""
	max = 10.5
	if attack_speed > 10:
		attack_speed = 10
	max -= attack_speed
	max /= 2
	max = random.uniform(-0.05*max, 0.05*max)+max
	return max
