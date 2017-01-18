import pygame
from pygame.locals import *
from accessible_output import speech

spk = speech.Speaker().output

pygame.mixer.pre_init(22050,-16, 2, 484)
pygame.init()

screen = pygame.display.set_mode((680, 440))
pygame.display.set_caption("menu with sounds")
pygame.mouse.set_visible(0)

pygame.mixer.init()


sound_menu_change = pygame.mixer.Sound("sounds/menu_change.ogg")
sound_menu_forward = pygame.mixer.Sound("sounds/menu_forward.ogg")
#sound_menu_back = pygame.mixer.Sound("sounds/menu_back.ogg")

name = pygame.key.name

play = True

def arrows(kname):
	global sound_menu_change
	if kname in ["up", "down"]:
		sound_menu_change.play()
		spk(kname)
	elif kname == "return":
		sound_menu_forward.play()
		spk(kname)
	elif kname == "backspace":
		sound_menu_back = pygame.mixer.Sound("sounds/menu_back.ogg")
		sound_menu_back.play()
		spk(kname)

while play:
	for event in pygame.event.get():
		if event.type == KEYDOWN and name(event.key) == "escape":
			play = False
		elif event.type == KEYDOWN:
			arrows(name(event.key))

pygame.quit()
