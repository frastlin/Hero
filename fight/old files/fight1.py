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

def main(name, s, play):
	if name == "escape":
		return "quit"
	elif name =="d":
		return "slow"


def engine():
	s = mixer.Channel(0)
	play = 0
	name = pygame.key.name
	speed = "fast"

	while play != "quit":
		for event in pygame.event.get():
			if event.type == KEYDOWN:
				play = main(name(event.key), s, play)
		if play ==  speed:
			speed = "fast"
		elif play == "slow":
			speed = "slow"

