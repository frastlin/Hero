#our imports, numpy is required for pygame.sndarray to run and math is used for the sin and pi functions
import pygame, numpy, math

def sound_creator(duration=1.0, frequency=440, left=0.5, right=0.5, sr=44100, bits=16):
	#initialize the pygame's mixer module with default values.
	pygame.mixer.init(frequency = sample_rate, size = -bits, channels = 2)

	#This gives a number of samples in our file. Don't try to print this number, it is really big! I'm not sure why the "round" function 	#is there
	n_samples = int(round(duration*sample_rate))

	#This is creating our lovely array. I'm not sure what all of it means, but the n_samples is the amount of items in our list (That 	#really big number that we got above!) and the 2 there means that we are wanting 2 channels. I don't know what the other 	#number is.
	buf = numpy.zeros((n_samples, 2), dtype = numpy.int16)

	#This is making sure our intijure buffer formats are inbetween -1 and 1, it is making sure we don't have a clipping sound
	max_sample = 2**(bits - 1) - 1

	#Now we are appending samples to the array we made above. I'm not sure why we didn't just do this with "buffer = [[], []]" 	#above, but what ever! 
	for i in xrange(n_samples):

		#This is where we create the type of wave it is.
		#t is the time we have in seconds
		t = i/float(sr)

#This is appending the wave type numbers to the first array which on 2 channels is the left
		buf[i][0] = int(round(max_sample*left*math.sin(2*math.pi*frequency*t)))
		#Now we are doing the same to the second array which is the right
		buf[i][1] = int(round(max_sample*right*math.sin(2*math.pi*frequency*t)))

		# Now we are creating the sound through pygame's sndarray module
	sound = pygame.sndarray.make_sound(buf)

	#Now we are returning a sound that is the same as a sound object in the mixer module
	return sound

#This will only run if you run this module, it is a nice example that will play quietly in the left speaker
if __name__ == ('__main__'):
	#Change these values to suit your needs
	duration = 1.0 #in seconds
	sample_rate = 44100
	bits = 16
	frequency = 440
	left = 0.1
	right = 0.03

	#Sound is a tipical sound file like "bird.ogg"
	sound = sound_creator(duration, frequency, left, right, sample_rate, bits)
	sound.play()

	#If you don't wait the program will exit. If you wait the duration of the sound you will get some popping when the sound is 	#done. That is why I'm waiting 1.5 seconds, rather than 1.
	pygame.time.wait(1500)
	pygame.mixer.quit()