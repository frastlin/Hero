import pygame

#the background sounds
mus = pygame.mixer.music


def background(piece):
	"""plays the background music on a loop"""
	if mus.get_busy():
		mus.fadeout(1500)
	if not piece:
		return None
	pygame.mixer.music.load("sounds/" + piece)
	pygame.mixer.music.play(-1)
