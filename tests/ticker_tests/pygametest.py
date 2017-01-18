import pygame
from pygame.locals import *
from accessible_output import speech
spk = speech.Speaker().output
pygame.init()

def screen(title="test script"):
	"""initalizes the screen"""
	screen = pygame.display.set_mode((640, 480))
	pygame.display.set_caption(title)
	pygame.mouse.set_visible(0)

def key2(state="KEYDOWN"):
	"""Waits till there is an event before returning it."""
	if type == "KEYUP".lower():
		state = 3
	else:
		state = 2
	t = True
	while t:
		event = pygame.event.wait()
		if event.type == state:
			t = False
	return (pygame.key.name(event.key), pygame.key.get_mods())
#	else:
#		return ('', '')

def key(state="KEYDOWN"):
	"""returns the name of the key and any mods in a tupal. The two states are 'KEYDOWN and KEYUP'"""
	for event in pygame.event.get():
		if event.type == KEYDOWN and state == "KEYDOWN":
			return (pygame.key.name(event.key), pygame.key.get_mods())
		elif event.type == KEYUP and type == "KEYUP":
			return (pygame.key.name(event.key), pygame.key.get_mods())
	return ['', '']

def speak(text=""):
	"""speaks the text that is passed"""
	spk(text)

def rest(time=0):
	"""rests and sleeps"""
	pygame.time.wait(time)

if __name__ == ('__main__'):
	def main():
		screen(title="testing pygame pass module")
		f = True
		while f:
			a = key()
			if a[0] == "space":
				speak("It worked!")
			elif a[0] == "up":
				speak("climbing up the latter!")
			elif a[0] == "escape":
				f = False

	screen()
	a = True
	while a:
		z = key2()
		if z[0] == "escape":
			a = False
		elif z[0] == "return":
			speak(z[1])
