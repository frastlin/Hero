import pygame
from accessible_output import speech
from pygame.locals import *

spk = speech.Speaker().output

pygame.init()
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("Map")
pygame.mouse.set_visible(0)

play = True
name = pygame.key.name

while play:
	for event in pygame.event.get():
		if(event.type == KEYDOWN) and (event.key == K_ESCAPE):
			play = False
		elif event.type == KEYDOWN:
			spk(name(event.key))

pygame.quit()