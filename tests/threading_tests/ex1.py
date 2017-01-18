#is an example of very basic thread module. start_new_thread

import time, thread

def myfunction(string, sleeptime, *args):
	while 1:
		print string
		#sleep for a specified amount of time
		time.sleep(sleeptime)

if __name__ == ('__main__'):
	thread.start_new_thread(myfunction, ("thread no:1", 2))
	while 1:pass