#fighting engine
import random, messages, time, threading

def messager(message="", name=None, fo=None):
	"""Add the fo and player along with the message you send through this"""
	if fo:
		fo = fo.descs.name
	if name:
		name = name.descs.self_name
	messages.add_message(message.format(name, fo))

def xp_adder(name, hit):
	"""Checks the type and adds it to the player's skill"""
	st = name.stats
	a = name.weapon.current_attack.type
	str = 0
	deff = 0
	att = 0
	if a == "balanced":
		att = 0.133
		str = 0.133
		deff = 0.133
	elif a == "strength":
		str = 0.4
	elif a == "defense":
		deff = 0.4
	elif a == "attack":
		att = 0.4
	elif a == "magic":
		magic = 0.4
	elif a == "ranged":
		ranged = 0.4
	st.strength.xp_add(str*hit)
	st.attack.xp_add(att*hit)
	st.defense.xp_add(deff*hit)
	st.hp.xp_add(0.133*hit)

def did_hit(name, fo):
	"""It checks fo's defense and sees if name's attack is high enough to hit."""
	a = name.stats.attack.boness(name.weapon.stats.ac + name.weapon.current_attack.ac)
	d = fo.stats.defense.boness(name.defense_boness())
	if random.uniform(name.stats.attack.mod_level,a) > d:
		return True
	else:
		return False

def hp_subtractor(name, fo):
	h = name.stats.strength.boness(name.weapon.stats.str + name.weapon.current_attack.str)
	h -= fo.armor.armor_defense
	h = random.uniform(1,h)
	if h > name.weapon.max_hit:
		h = name.weapon.max_hit
	h = int(round(h))
	messager("%s: %s" % (h, name.weapon.current_attack.message), name=name, fo=fo)
	fo.stats.hp.current_hp -= h
	if not "mob" in name.flags:
		xp_adder(name, h)


def special_events(name, fo):
	"""This is where stuff like poison goes"""
	pass

def death_checker(name, fo):
	if name.stats.hp.current_hp <= 0:
		if "player" in name.flags:
			messages.add_message("You have died, killed by %s!" % fo.descs.name)
		return True
	elif fo.stats.hp.current_hp <= 0:
		if "player" in name.flags:
			messages.add_message("You have died, killed by %s!" % fo.descs.name)
		return True
	else:
		return False

def attacker(name, fo):
	"""Runs the equasions for combat"""
	name.weapon.attack_choice(name)
	if death_checker(name, fo):
		return True
	if did_hit(name, fo) == True:
		h = hp_subtractor(name, fo)
		if death_checker(name, fo):
			return True
	else:
		messager("0: %s missed" % name.descs.name)
	special_events(name, fo)
	if death_checker(name, fo):
		return True
	time.sleep(name.weapon.current_attack.speed)
	if death_checker(name, fo):
		return True
	else:
		return False

def main(player, fo):
	play = False
	while not play:
		play = attacker(player, fo)
		time.sleep(0.05)

def combat(p, b):
	t = threading.Thread(target=initer, args=(p, b))
	t.start()

def initer(p, b):
	mob_thread = threading.Thread(target=main, args=(b, p))
	player_thread = threading.Thread(target=main, args=(p, b))
	mob_thread.start()
	player_thread.start()
	mob_thread.join()
	player_thread.join()
#	return "completed"


if __name__ == ('__main__'):
	import bear, player, threading
	b = bear.Bear(1)
	p = player.Person()
	def main(player, fo):
		play = False
		while not play:
			play = attacker(player, fo)
			time.sleep(0.5)

	mob_thread = threading.Thread(target=main, args=(b, p))
	player_thread = threading.Thread(target=main, args=(p, b))
	mob_thread.start()
	player_thread.start()
#	for m in messages.message_list:
#		print m

#	mob_thread.join()
#	player_thread.join()

