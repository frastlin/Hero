import pygame
from time import sleep
from pygame.locals import *
from accessible_output import speech

spk = speech.Speaker().output

pygame.init()

screen = pygame.display.set_mode((680, 440))
pygame.display.set_caption("menu with sounds")
pygame.mouse.set_visible(0)

def key_board(event, name, block):
	if event.type == KEYDOWN:
		name = name(event.key)
		if event.key == K_b:
			spk("b down")
			return "block"
		elif name == "up":
			spk("UP")
			return "up"
	elif event.type == KEYUP:
		if event.key == K_b:
			spk("B UP")
			return "blockup"
		sleep(0.5)

def main():
#	pygame.key.set_repeat(1)
	name = pygame.key.name
	play = 0
	block = False
	while play != "quit":
		for event in pygame.event.get():
			if event.type == KEYDOWN and event.key == K_ESCAPE:
				play = "quit"
			else:
				play = key_board(event, name, block)
		if play == "block":
			block = True
		elif play == "blockup":
			block = False
		if block == True and play == "up":
			spk("bam!")

main()
