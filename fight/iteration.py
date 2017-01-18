
def classes(class_name):
	"""Returns a dict from the classes arguments"""
	d = {}
	for k, v in class_name.__dict__.items():
		if not (k.startswith('__') and k.endswith('__')):
			d[k] = v
	return d

if __name__ == ("__main__"):
	class C(object):
		a = 2
		b = "B"
		c = "C"
		d = 5

	cl = C
	class_dict = classes(cl)
	for k,v in class_dict.items():
		print "%s: %s" % (k, v)
	print class_dict.items()

