#The fight engine, time
import u, random
from accessible_output import speech

spk = speech.Speaker().output

#I need to make a dict in weapons that will grab what ever attacks that are passed in the init argument and connect them with those in the attacks_list module dict
#I need to figure out how to get the .format("name.weapon.name, name.name and whatnot and make it called when the messages are.
#need to create speed, perhaps add a cooldown. Also, need to add the selecter for the attack that is being done (swipe, stab...).

def does_hit(name, attack_name):
	"""Returns a true or false saying if the ac is enough for the target to hit"""
	attack_total = 0
	ac_total += name.weapon.ac
	ac_total += u.attacker(name.attack)
	attack_total += attack_name.extra_ac
	if ac_total >= random.randrange(1, 101):
		return True
	else:
		return False

def damage(name, attack_name):
	"""totals up the amount of damage the attack does"""
	h = name.mstr + attack_name.extra_str
	h += random.randint(0, name.weapon.max_damage)
	h = u.strer(h)
	if h < name.weapon.min_damage:
		return name.weapon.min_damage
	elif h > name.weapon.max_damage:
		return name.weapon.max_damage
	else:
		return h

def mob_attacker(name):
	"""Chooses the attack the mob does and then runs the equasions"""
	a = random.choice(name.weapon.weapon_options)
	if does_hit(name, a):
		total_dammage = dammage(name, a)
		total_damage -= u.defenser(name.fo.mdefense)
		name.fo.hp -= total_damage
		if settings.speaks_hits == True:
			spk("%s. %s" % (total_damage, name.name))
	time.sleep(u.speeder(a.speed))



def player_attacker(name):
	pass

def hit(name):
	"""Works out the hit (if any) the player or creature that is passed in does without defense"""
	if "player" in name.flags:
		player_attacker(name)
	else:
		mob_attacker(name)

def mob_fo_chooser(players, mobs):
	"""Randomly chooses a fo from the players list"""
	for m in mobs:
		m.fo = random.choice(players)

def main(players=[], mobs=[]):
	mob_fo_chooser(players, mobs)

#need to initiate threads with the below function
	hit(name)


if __name__ == ("__main__"):
	import mob
	b = mob.bear
	p = mob.Monster("Player", "This is a player", 9)
	mob_attacker(b)
