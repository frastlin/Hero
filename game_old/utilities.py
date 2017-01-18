

def popper(name, where):
	"""Is for lists of objects, this refferences them by name so one can get rid of an object by using the name argument. Name is the 	name of the object and where is the list of the object. make where equal popper"""
	l = []
	for f in where:
		l.append(f.name)
	if name in l:
		where.pop(l.index(name))
	return where

