import pygame, globals
from time import sleep

pygame.mixer.pre_init(22050,-16, 2, 400)
pygame.mixer.init()

mix = pygame.mixer

sound = pygame.mixer.Sound
#the sound effects
menu_change = sound("sounds/menu_change.ogg")
menu_back = sound("sounds/menu_back.ogg")
menu_forward = sound("sounds/menu_forward.ogg")

def menu_sound(kname):
	"""checks the key name and plays the right sound for that key."""
	if kname in ["up", "down"]:
		menu_change.play()
	elif kname == "return":
		menu_forward.play()
	elif kname in ["escape", "left"]:
		menu_back.play()
