import messages

def player_death(player, fo):
	"""Is the player's death"""
	

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
