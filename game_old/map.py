import pygame, scenes, globals, menus, actions, audio, background_sound
from accessible_output import speech
from pygame.locals import *
from time import sleep

spk = speech.Speaker().output

pygame.init()
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("Hero")
pygame.mouse.set_visible(0)

def move(play, name):
	"""Checks the coord of the current room and checks where the player wants to go and removes or adds one to the x or y 	number. x is the first number going left and right, y is the second number going up and down. The return value is a get call to 	the list of rooms and their location in scenes.py. That dict is called rooms."""
	coord = play.coord
	x = coord[0]
	y = coord[1]
	if name == "l" or name == "return":
		globals.screen = "look"
		spk("look menue")
		spk("look around")
	elif name in ("I", "i"):
		spk("In your inventory you have:")
		if globals.inv == []:
			spk("Nothing")
			spk(play.description)
		else:
			globals.screen = "inv"
	elif name == "up":
		y += 1
	elif name == "down":
		y -= 1
	elif name == "right":
		x -= 1
	elif name == "left":
		x += 1
	if (x, y) in play.exits:
		return scenes.rooms.get((x, y))
	else:
		return play

def item_list(name, x, number):
	number -= 1
	if name == "up":
		x -= 1
	elif name == "down":
		x += 1
	if x < 0:
		x = number
	elif x > number:
		x = 0
	return x

def item_menu(play, item, who, name):
	audio.menu_sound(name)
	l = item.option_list()
	if name in ("escape", "left"):
		globals.screen = who
		if who == "look":
			spk(item.short_desc)
		else:
			spk("inventory menu")
			spk(item.name)
	elif name in ("up", "down"):
		globals.number2 = item_list(name, globals.number2,
		len(l))
		spk(l[globals.number2])
	elif name in ("return", "right"):
		globals.screen = who
		r = getattr(actions, item.options.get(l[globals.number2]))(play, item)
		if who == "look" and not r:
			spk(play.items[globals.number].short_desc)
		elif who == "inv" and globals.inv == []:
			spk("You don't have anything left in your inventory")
			globals.screen = "go"
			spk(play.description)
		elif who == "inv":
#			spk(globals.inv[globals.number].name)
			pass
		return r

def use_menu(play):
	l = globals.inv + play.items
	l1 = []
	for m in l:
		if 'useWith' in m.flags or 'useOn' in m.flags:
			l1.append(m)
	list = []
	for i in l1:
		list.append(i.name)
	num = menus.menu("Use with what?", list)
	if num == None:
		globals.screen = "inv"
		spk("inventory menu")
		spk(globals.inv[globals.number].name)
	else:
		globals.screen = "inv"
		return actions.use2(play, globals.inv[globals.number], l[num])

def inv_menu(play, name):
	audio.menu_sound(name)

	globals.number2 = 0
	if globals.inv == []:
		spk("You don't have anything in your inventory")
		spk(play.description)
		globals.screen = "go"
	elif name == "escape":
		spk("Exeting inventory")
		globals.screen = "go"
		spk(play.description)
	elif name in ("up", "down"):
		globals.number = item_list(name, globals.number, len(globals.inv))
		spk(globals.inv[globals.number].name)
	elif name == "return" or name == "right":
		globals.screen = "item_menu_inv"
		globals.inv[globals.number].add_options(play)
		spk("options")
		spk(globals.inv[globals.number].option_list()[0])

def look_menue(play, name):
	audio.menu_sound(name)
	globals.number2 = 0
	if not play.items:
		spk("There is nothing interesting here")
	elif name == "escape":
		spk("exiting look menue")
		globals.screen = "go"
		globals.number = 0
	elif name == "up" or name == "down":
		globals.number = item_list(name, globals.number, len(play.items))
		spk(play.items[globals.number].short_desc)
	elif name == "return" or name == "right":
		if globals.number == 0:
			spk("You take in everything around you")
			spk(play.description)
			spk("look around")
		else:
			globals.screen = "item_menu_look"
			play.items[globals.number].add_options(play)
			spk("options")
			spk(play.items[globals.number].option_list()[0])

def keyboard_input(play):
	screen = globals.screen
	name = pygame.key.name
	for event in pygame.event.get():
		if(event.type == KEYDOWN) and (event.key == K_ESCAPE) and screen == "go":
			return "quit"
		elif (event.type == KEYDOWN) and screen == "go":
			return move(play, name(event.key))
		elif (event.type == KEYDOWN) and screen == "look":
			return look_menue(play, name(event.key))
		elif event.type == KEYDOWN and screen == "item_menu_look":
			return item_menu(play, play.items[globals.number], "look", name(event.key))
		elif event.type == KEYDOWN and screen == "item_menu_inv":
			return item_menu(play, globals.inv
			[globals.number], "inv", name(event.key))
		elif event.type == KEYDOWN and screen == "inv":
			return inv_menu(play, name(event.key))
		elif screen == "use_menu":
			return use_menu(play)

def main():
	play = scenes.start
	background_sound.background(play.background)
	globals.play = play
	spk(play.description)
	while play:
		sleep(0.05)
		play2 = keyboard_input(play)
		if play2 == "quit":
			play = False
		elif play == play2 or not play2:
			pass
		elif play != play2:
			if play2 in scenes.rooms:
				play2 = scenes.rooms.get(play2)
			background_sound.background(play2.background)
			globals.play = play2
			sleep(0.5)
			spk(play2.description)
			play = play2
	pygame.quit()

main()