"""
so basicly, a decorator is a way to pass an unrun function into a class or function without having it run first.
it looks like:
@function_that_needs_to_run_with_another_function_passed_in_as_an_argument
def function_that_is_passed():
	print "Stuff that runs"

then it runs when the program happens, but if it is a class, it will look like the function without the ().
"""


class Z(object):
	def __init__(self, f):
		self.f = f
		self.x = 0
	def crackers(self, xx):
		print "This is in the function and this is xx: %s" % xx
		self.x = xx

h = Z("walk")

@h.crackers
def zook():
	print "Jump"


h.x()

print h.x
