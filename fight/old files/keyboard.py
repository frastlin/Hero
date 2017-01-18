#This is a little app that will tell the names of the keys and works with modifier keys. see the keyboard1 function

import pygame, beep
from pygame.locals import *
from accessible_output import speech

spk = speech.Speaker().output

pygame.init()
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption('pygame keyboard test')
pygame.mouse.set_visible(0)


def keyboard1():
	name = pygame.key.name
	for event in pygame.event.get():
#for quitting the app
		if event.type == KEYDOWN and event.key == K_ESCAPE:
			return "quit"
#testing if the applications key is pressed.
		elif event.type == KEYDOWN and name(event.key) == "menu":
			sound1 = beep.sound_creator(0.05)
			sound1.play()
			spk("You hit the menu key!")
#pygame.key.get_mods() returns a number. For example, left shift is 1. mod keys like ctrl+shift have their own number. 
		mod = pygame.key.get_mods()
		spk(mod)
#checks if left shift is held down alone.
		if mod == 4097:
			spk("You did it! a mod is down!")
#just says the name of the key.
		if event.type == KEYDOWN:
			spk(name(event.key))

def main():
	running = True
	while running:
		f = keyboard1()
		if f == "quit":
			running = False
	pygame.time.wait(5)

if __name__ == '__main__':
	main()

