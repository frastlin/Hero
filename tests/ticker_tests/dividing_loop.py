import random, time, pygame

#print 6 % 2 == 0

def tick(t):
	"""This has a bug to where the clock starts with a number it ended with for a second and that triggers a true."""
	if time.clock() % t <= 0.05:
#		print time.clock()
		return True

while True:
	if tick(1):
		print "Yep"
	time.sleep(0.05)
