import pygame, scenes
from accessible_output import speech
from pygame.locals import *
spk = speech.Speaker().output

pygame.init()
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("Key test and other stuff")
pygame.mouse.set_visible(0)

class Opk(object):
	def __init__(self):
		self.name = "radish"

def name_change(name):
	scenes.name = name


def main():
	play = True

	input = pygame.event.get()
	name = pygame.key.name
	while play:
		for event in pygame.event.get():
			if(event.type == KEYDOWN) and (event.key == K_ESCAPE):
				spk(name(event.key))
				play = False
			elif event.type == KEYDOWN and name(event.key) == "up":
				name_change("Pie")
				spk(scenes.name)
			elif event.type == KEYDOWN and name(event.key) == "down":
				scenes.name = "Salid"
				spk(scenes.name)
			elif event.type == KEYDOWN and name(event.key) == "left":
				scenes.name = "Orange!!!"
				spk(scenes.name)
			elif event.type == KEYDOWN and name(event.key) == "space":
				spk(scenes.name)
	
	pygame.quit()
