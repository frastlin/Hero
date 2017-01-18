import pygame
from time import sleep
from pygame.locals import *
from accessible_output import speech

spk = speech.Speaker().output

pygame.init()

screen = pygame.display.set_mode((680, 440))
pygame.display.set_caption("menu with sounds")
pygame.mouse.set_visible(0)


pygame.mixer.pre_init(22050,-16, 2, 400)
pygame.mixer.init()

mixer = pygame.mixer

sound = pygame.mixer.Sound
#the sound effects
fast = sound("sounds/swing1.ogg")
slow = sound("sounds/swing2.ogg")

mixer.set_reserved(0)

s = mixer.Channel(0)

#s.play(fast)

def pan(num, s):
	global spk
	l = 0.5
	r = 0.5
	l += num*0.05
	r -= num*0.05
#	spk("%s, %s" % (l, r))
	s.set_volume(l, r)

def main(name, s, sname, x):
	global spk
	if name == "escape":
		return "quit"
	elif name in ["return", "space"]:
		s.play(sname)
		return x
	elif name in ["up",]:
		if x < 10:
			x += 1
			pan(x, s)
			return x
		else:
			return x
	elif name in ["down"]:
		if x > -10:
			x -= 1
			pan(x, s)
			return x
		else:
			return x
	elif name == "f":
		return 0
	else:
		return x



play = 0
name = pygame.key.name

while play != "quit":
	sname = slow
	for event in pygame.event.get():
		if event.type == KEYDOWN:
			play = main(name(event.key), s, sname, play)

