import globals, events
from accessible_output import speech
spk = speech.Speaker().output

def add_remove(item, add=None, takeout=None):
	if add:
		map(item.flags.append, add)
	if takeout:
		map(item.flags.remove, takeout)

def take(play, item):
	try:
		getattr(events, item.name.replace(" ", ""))(play, item)
	except AttributeError:
		spk("You take %s" % item.name)
		if 'use' in item.flags:
			item.flags.append('useWith')
		elif 'hold' in item.flags:
			item.append('wield')
		elif 'wearable' in item.flags:
			item.flags.append('wear')
		add_remove(item, ['drop'], ['take'])
		globals.inv.append(item)
		play.items.remove(item)
		globals.number = 0

def drop(play, item):
	spk("You drop %s" % item.name)
	if 'useWith' in item.flags:
		item.flags.remove('useWith')
	elif 'wield' in item.flags:
		item.flags.remove('wield')
	elif 'wear' in item.flags:
		item.flags.remove('wear')
	add_remove(item, ['take'], ['drop'])
	play.items.append(item)
	globals.inv.remove(item)
	globals.number = 0


def look(play, item):
	spk(item.long_desc)

def useWith(play, item):
	if globals.inv == []:
		spk("Use it on what? You don't have anything!")
	else:
		globals.number2 = 0
		globals.screen = "use_menu"

def enter(play, item):
	"""First in the try statement, checks if there is a function in events.py with the same name as the item. If not it says you enter*. It then returns the tupal which is the location the item takes them."""
	try:
		return getattr(events, item.name.replace(" ", ""))(play, item)
	except AttributeError:
		spk("you enter %s" % item.name)
		globals.number = 0
		return item.location


def sorter(l):
	q = []
	for m in l:
		if m in ("take", "drop", "use", "useWith", "wear", "hold"):
			pass
		elif m in q:
			return m
		else:
			q.append(m)

def use2(play, item1, item2):
	l = item1.flags + item2.flags
	f = sorter(l)
	if item1 == item2:
		spk("You can't use an item on itself")
		globals.screen = "use_menu"
	elif f:
		globals.number = 0
		return getattr(events, f)(play, item1, item2)
	else:
		spk("nothing seems to happen")

def read(play, item):
	name = item.name.replace(" ", "")
	try:
		getattr(events, item.name.replace(" ", ""))(play, item)
	except AttributeError:
		pass
	spk("You start reading %s" % item.name)
	events.reader(item.name)

def lookiner(item):
	"""This is a complex function and is the same as lookoner. first we get the items in the container. Then we list them for the user. then the user choses what item they want and then when they hit enter, the item's options come up. So basicly you are looking at the item's menu that is inside the container. The eval function is just there because I don't know how to get vars() into the global namespace so I can grab read or whatnot."""
	from menus import menu
	l = []
	for n in item.items:
		l.append(n.name)
		i = menu(item.items[0].name, l)
	if i != None:
		f = item.items[i]
		f.add_options(item)
		r = f.option_list()
		o = menu(r[0], r)
		if o == None:
			spk("You stop looking at the items in %s" % item.name)
		elif r[o] == 'take':
			spk("you remove %s from %s" % (f.name, item.name))
			take(item, f)
		else:
			eval(f.options.get(r[o]))(play, f)
	else:
		spk("You stop looking at the items in %s" % item.name)

def LookIn(play, item):
	"""Is the same as LookOn. Look to see if there are items in the item's items attribute."""
	spk("You look in %s and find" % item.name)
	if item.items != []:
		lookiner(item)
	else:
		spk("Nothing")

def lookoner(play, item):
	"""This is a complex function and is the same as lookiner. first we get the items in the container. Then we list them for the user. then the user choses what item they want and then when they hit enter, the item's options come up. So basicly you are looking at the item's menu that is inside the container. The eval function is just there because I don't know how to get vars() into the global namespace so I can grab read or whatnot."""
	from menus import menu
	l = []
	for n in item.items:
		l.append(n.name)
		i = menu(item.items[0].name, l)
	if i != None:
		f = item.items[i]
		f.add_options(item)
		r = f.option_list()
		o = menu(r[0], r)
		if o == None:
			spk("You stop looking at the items on %s" % item.name)
		elif r[o] == 'take':
			spk("you remove %s from %s" % (f.name, item.name))
			take(item, f)
		else:
			eval(f.options.get(r[o]))(play, f)
	else:
		spk("You stop looking at the items on %s" % item.name)

def LookOn(play, item):
	"""is the same as LookIn. Check if items are in the container and if there are, bring up the menu listing them."""
	spk("You start perusing the items on %s" % item.name)
	if item.items != []:
		lookoner(play, item)
	else:
		spk("Nothing")

