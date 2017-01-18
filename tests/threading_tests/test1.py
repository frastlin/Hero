"""
#appending stuff to strings much faster
s = "Hello world!"

print s

l = ["john", "fred", "lucy", "I like cake!"]

s = " ".join(l)

print s
"""
"""
#This is about as fast as map and the first thing with the tupal can be iterated through as needed. the other way of writing a for loop is just much smaller to write..

f = ["tom", "jane", "mark", "dan"]

newlist = (s.upper() for s in f)
print newlist.next()
c = [a.upper() for a in newlist]
print c
"""
"""
#Dots are slow!
#if I can create functions for them, life will be much faster!

firstlist = ["j", "a", "s", "one", "r"]

upper = str.upper

newlist = []

append = newlist.append

for word in firstlist:
	append(upper(word))

print newlist
"""
