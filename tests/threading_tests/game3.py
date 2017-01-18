import threading


letter = []
event = threading.Event()
lock = threading.Lock()


def writing_function(name, text, e=None):
	global letter
	lock.acquire()
	letter.append("Dear Grandma, this is %s and %s" % (name, text))
	lock.release()
	if e:
		event.set()

def line_writing():
	global letter
	if event.wait():
		letter.append("\nxoxxo<3<3<3xxoxxoooo")
		event.clear()


def my_function(text):
	global letter
	letter.append("\n\nHey grandma, %s" % text)



me_thread = threading.Timer(2, my_function, ["I'm going crazy playing Castaways! Aprone has made the new map really really hard!"])
daddy_thread = threading.Thread(target=writing_function, args=("daddy", "I hate going to the pool. When I stick my leg into the water, I just can't stop thinking about all the little kids who have peed in the water"))
mommy_thread = threading.Thread(target=writing_function, args=("mommy", "I went to the pool today. It was so refreshing after a long day of work just to swim through the water.\nHope to see you soon\nMommy"))
brother_thread = threading.Thread(target=writing_function, args=("brother", "I just got a longbow in swamp and I've been running through sub 2, killing all the zombies TTYS!", True))
girlfriend_thread = threading.Thread(target=line_writing)

me_thread.start()
girlfriend_thread.start()
daddy_thread.start()
mommy_thread.start()
brother_thread.start()

import time, logging
logging.basicConfig(level=logging.DEBUG)
time.sleep(3)
for line in letter:
	logging.debug(line)

