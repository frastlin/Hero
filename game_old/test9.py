"""
continue and break statements"""

print """
the break statement exits a loop before it runs the whole chain:
"""
for s in range(20):
	print "This is %d out of 20" % s
	if s == 4:
		print "OK, time to break!"
		break


print """
The continue statement skips over the poticular iteration of the loop so for\nexample:
"""
for f in range(20):
	if f == 2:
		print "Ha, got 2! You don't get it!"
		continue
	elif f == 4:
		print "Ha got 4 as well!"
		continue
	elif f == 6:
		print "OK, we're done"
		break
	else:
		print "I don't like this number"
		print "Here is %d out of 20" % f

print "Done with the loops"

"""
#The above loop can be done with an else statement, but if you don't want an else statement than use continue
for num in range(2, 10):
	if num %2 == 0:
		print "found an evin number", num
		continue
	print "Found a number", num

"""