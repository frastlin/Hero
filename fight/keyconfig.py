#Has the default keyconfigs for health, past messages and whatnot.
import messages

#xp_check uses this and it needs you to type python -m fight.keyconfig to run it.
from game import menus
from accessible_output import speech
spk = speech.Speaker().output

def key_defaults(key, mod=None, player=None, fo=None):
	"""Checks key and does the action that goes with the key."""
	if key in ["[", "]"]:
		r_messages(key, mod)
	elif key == "h".lower():
		hitpoint_check(mod, player, fo)
	elif key == "x":
		xp_check(player)

def level_list(p):
	"""Returns a double list of all the skills in a name level level: you need xp before level level"""
	l = [[], []]
	for k, v in p.stats.__dict__.items():
		l[0].append("%s level %s: you need %s xp before you reach level %s" % (k, v.level, v.tnl(), v.level+1))
		l[1].append("%s has %s total xp" % (k, v.xp))
	return l

def xp_check(player):
	"""Calls a menu and puts the list from level_list into it."""
	try:
		l = level_list(player)
		print len(l[0])
		menus.speak_menu("xp menu", options=l)
	except AttributeError:
		spk("You don't currently have any levels that have xp")

def hitpoint_check(mod, player, fo):
	if mod in [4097, 4353, 4354, 4098]:
		try:
			spk("%s HP %s" % (fo.stats.hp.current_hp, fo.descs.name))
		except AttributeError:
			spk("There is no fo now")
	else:
		try:
			spk("%s out of %s hp you have" % (player.stats.hp.current_hp, player.stats.hp.level))
		except AttributeError:
			spk("You don't have any HP currently")

def r_messages(k, mod):
	if messages.location_in_list < 0:
		messages.location_in_list = 0
	if mod in [4416, 4160]:
		if k == '[':
			messages.location_in_list = 0
		elif k == ']' and len(messages.message_list) - 1 > 0:
			messages.location_in_list = len(messages.message_list) - 1
	else:
		if k == '[' and messages.location_in_list > 0:
			messages.location_in_list -= 1
		elif k == ']' and messages.location_in_list < len(messages.message_list)-1:
			messages.location_in_list += 1
	if messages.message_list == []:
		spk("The message log is blank")
	else:
		spk(messages.message_list[messages.location_in_list])

def tabber(screen):
	"""Changes the screens"""
	if screen == "fight":
		return ("current_screen", "game")
	elif screen == "game":
		return ("current_screen", "fight")


if __name__ == ('__main__'):
	import pygame
	from pygame.locals import *
	pygame.init()
	screen = pygame.display.set_mode((640, 480))
	pygame.display.set_caption('pygame keyboard test')
	pygame.mouse.set_visible(0)

	import bear
	b = bear.Bear(1)

	map(messages.message_list.append, ['You swing your staff at the bear, causing lots of dammage!', 'Your health is low!', 'You are almost dead!'])
	messages.length_in_list = 2
	play = True
	while play:
		for event in pygame.event.get():
			if event.type == KEYDOWN and event.key == K_ESCAPE:
				play = False
			elif event.type == KEYDOWN:
				if pygame.key.name(event.key) == "space":
					spk(messages.message_list)
				key_defaults(key=pygame.key.name(event.key), mod=pygame.key.get_mods(), player=b)
#				spk(pygame.key.get_mods())

"""
keys:
h = your hp
shift h = mob hp
left and right bracket are scroll through message_list
ctrl + left and right bracket is move to start or end of message_list
x checks on xp and levels
"""
