import pygame, menus
from pygame.locals import *
from accessible_output import speech

spk = speech.Speaker().output

spk("loading sounds")

pygame.init()
screen = pygame.display.set_mode((680, 440))
pygame.display.set_caption("sounds")
pygame.mouse.set_visible(0)

#We need the inits to run the mixer, the pre_init is there if we want defaults changed
#pygame.mixer.pre_init(44100, -16, 2, 1024)
pygame.mixer.init()

#loading the sound into the music object and loading sound into the mixer object
pygame.mixer.music.load("sounds\desert.ogg")
sound = pygame.mixer.Sound("sounds/desert.ogg")
#mixer object takes a long time

def play_sound(name, l):
	"""fades out and starts audio using the music class. press space to change the sound."""
	if name == "return":
		pygame.mixer.music.play(-1)
	elif name == "s":
		pygame.mixer.music.fadeout(1500)
	elif name == "space":
		f = menus.menu("pick a sound", l)
		if f != None:
			pygame.mixer.music.load("sounds/" + l[f])

def mixer_menu(name, l):
	"""plays sound using the mixer class, sound is the class instance and we call atributes to play and stop. Press space to change the sound."""
	global sound
	if name == "return":
		sound.play(-1)
	elif name == "s":
		sound.fadeout(1500)
	elif name == "space":
		f = menus.menu("pick a sound", l)
		if f != None:
			sound = pygame.mixer.Sound("sounds/" + l[f])

def main():
	spk("loaded sounds")
	spk("music")
	"""put new sounds into this list and menus.py has the command for loop, so name is just a lazy way to get what key is pressed because we already have menus called."""
	l = ["desert.ogg", "start.ogg"]
	scene = "music"
	while scene:
		name = menus.name()
		if name == "escape":
			scene = False
		elif name == "m":
			scene = "music"
			pygame.mixer.stop()
			spk("music")
		elif name == "a":
			pygame.mixer.music.stop()
			spk("mixer")
			scene = "mixer"
		elif scene == "music":
			play_sound(name, l)
		elif scene == "mixer":
			mixer_menu(name, l)

main()
