import pygame, audio
from pygame.locals import *
from accessible_output import speech
spk = speech.Speaker().output

def name(state=KEYDOWN):
	"""checks the pygame event queue and returns any key that are in the state. By default the state is if the key is pressed down. 	It returns the name of the key as a string"""
	for event in pygame.event.get():
		if event.type == state:
			return pygame.key.name(event.key)

def scroll(current_value, max_value, keys, name):
	"""Is called by menu and just makes sure that when the person scrolls it loops rather than going out of range. don't call this 	function, it really doesn't do anything."""
	max_value -= 1
	if name == keys[0]:
		current_value -= 1
	elif name == keys[1]:
		current_value += 1
	if current_value < 0:
		current_value = max_value
	elif current_value > max_value:
		current_value = 0
	return current_value

def menu(title, options=["yes", "no"], current_value=0, keys=['up', 'down'], state=KEYDOWN):
	"""This is the function you import. title is what you want the menu to say when opened. options is the list of choices the player 	hears spoken to them. keys are the two keys used to scroll through the menu, put them in a list, by default they are the up 	and down arrow keys. State is what you want the state of the key to be when the menu scrolls and when players choose an 	option. By default it is keydown."""
	spk(title)
	while True:
		name1 = name(state)
		audio.menu_sound(name1)
		if name1 == "escape":
			return None
		elif name1 in keys:
			current_value = scroll(current_value, len(options), keys, name1)
			spk(options[current_value])
		elif name1 == "return":
			return current_value

def muted_menu(title, options=["yes", "no"], current_value=0, keys=['up', 'down'], state=KEYDOWN):
	"""This is the function you import. title is what you want the menu to say when opened. options is the list of choices the player 	hears spoken to them. keys are the two keys used to scroll through the menu, put them in a list, by default they are the up 	and down arrow keys. State is what you want the state of the key to be when the menu scrolls and when players choose an 	option. By default it is keydown."""
	spk(title)
	while True:
		name1 = name(state)
		if name1 == "escape":
			audio.menu_sound(name1)
			return None
		elif name1 in keys:
			current_value = scroll(current_value, len(options), keys, name1)
			spk(options[current_value])
		elif name1 == "return":
			audio.menu_sound(name1)
			return current_value

def speak_menu(title, options=["yes", "no"], current_value=0, keys=['up', 'down'], state=KEYDOWN):
	"""This takes a double list options[[], []]. The first list is what shows, the second list is what is said when they hit return. 	This is the function you import. title is what you want the menu to say when opened. options is the list of choices the 	player 	hears spoken to them. keys are the two keys used to scroll through the menu, put them in a list, by default they 	are the up and down arrow keys. State is what you want the state of the key to be when the menu scrolls and when 	players choose an option. By default it is keydown."""
	spk(title)
	while True:
		name1 = name(state)
		audio.menu_sound(name1)
		if name1 == "escape":
			return None
		elif name1 in keys:
			current_value = scroll(current_value, len(options[0]), keys, name1)
			spk(options[0][current_value])
		elif name1 == "return":
			spk(options[1][current_value])
