#using the lock function.
#lock will freaze a thread, I'm not sure if it freazes everything though.


import time, thread

def myfunction(string, sleeptime, lock, *args):
	while 1:
		#entering critical section
		lock.acquire()
		print string, " now sleeping after lock acquired for ",sleeptime
		time.sleep(sleeptime)
		print string, " now releasing lock and then sleeping again"
		lock.release()
	#exiting critical section
#	time.sleep(sleeptime) #why?

if __name__ == '__main__':
	lock = thread.allocate_lock()
	thread.start_new_thread(myfunction, ("thread no:1", 2, lock))
	thread.start_new_thread(myfunction, ("thread no:2", 2, lock))

	while 1:pass
