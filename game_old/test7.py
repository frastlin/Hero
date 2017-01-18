class z(object):
	def __init__(self, name):
		self.name = name

y = z("yes").name
n = z("no").name
m = z("maybe")
p = z("perhaps").name

#l = [y, n, m, p]


l = ["yes", "no", "maybe", "perhaps"]
j = list(l)
j.pop(1)
print l
print "and j"
print j

#l.pop(l.index("maybe"))
#print l



#for j in l:
#	if "maybe" not in j:
#		l.remove(j)
#
##print l
#
#f = """
#this
#is a very
#long poem!
#"""
##print f.split("\n")
#
#l = ['yellow', 'red', 'orange']
#l2 = ['green', 'silver', 'gold']
#
#
#if 'orange' and 'red' in l:
#	print l
#else:
#	print "no"