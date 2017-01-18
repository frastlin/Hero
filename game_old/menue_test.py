#pygame junk, ignore, it just brings up a black window
import pygame
from accessible_output import speech
from pygame.locals import *

spk = speech.Speaker().output

pygame.init()
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("menue example")
pygame.mouse.set_visible(0)
#spk is the same as print
#All these global variables will be in many different files
play = True
x = 0
y = 0
screen = "start"

#These two lists are really classes with menus for each option
start_menu = [
'look around',
'a stick is here',
'a tree is blowing in the wind'
]

second_menu = [
'take',
'use'
]

#Here is where the crazyness begins:

def list_viewer(name, number, x):
	"""cicles through the numbers in a list. number is the length of the list, x is the current number of the list and name is the up or down arrows."""
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

def menus(play, name):
	"""The major function in the script. It checks if the key was pressed, and if so, checks what menu is up and changes what the number of the menues are. It also speeks the menu options"""
	global screen, x, y, start_menu, second_menu
	if screen == "start" and name in ("up", "down"):
		x = list_viewer(name, len(start_menu), x)
		spk(start_menu[x])
	elif screen == "start" and name in ("return", "right"):
		screen = "second"
		spk("Options menu")
	elif screen == "second" and name in ("up", "down"):
		y = list_viewer(name, len(second_menu), y)
		spk(second_menu[y])
	elif screen == "second" and name == "left":
		screen = "start"
		spk(start_menu[x])
		y = 0

def key_input(play):
	"""Filters out all the unwanted key presses"""
	for event in pygame.event.get():
		if event.type == KEYDOWN and pygame.key.name(event.key) == "escape":
			return False
		elif event.type == KEYDOWN:
			menus(play, pygame.key.name(event.key))
	return True

def main():
	"""The while loop that keeps the game running."""
	global play
	while play:
		play = key_input(play)
	pygame.quit()

main()
