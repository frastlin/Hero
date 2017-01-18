class Item(object):
	def __init__(self, name, short_desc, long_desc=None, flags=[], location=None, size=0):
		if long_desc == None:
			long_desc = short_desc
		self.name = name
		self.short_desc = short_desc
		self.long_desc = long_desc
		self.location = location
		self.size = size
		self.flags = flags
		self.options = {}
		self.items = []
	def add(self, where, *what):
		"""Pass in the name of the list you would like to append items to in quotes 'flags' and then the items you would like in the
		list. getattr just changes the string into an attribute. so getattr(self, "flags") (or in this case where), becomes self.flags.
		Where is the list's name. The map function goes through all the items after the name of the list and appends them to the
		list you named with where
		"""
		where = getattr(self, where)
		map(where.append, what)
	def option_list(self):
		l = []
		map(l.append, self.options)
		return l
	def add_options(self, play):
		self.options = {}
		self.options['examine'] = 'look'
		for f in self.flags:
			if f in ("take", "drop", "useWith", "read", "LookIn", "LookOn", "enter"):
				self.options[f] = f


stick = Item('a stick', 'A stick is laying on the ground.',
"This long, dry stick covered in loose, sluffing bark looks like it would burn very well.",
['take', 'use', 'torch'])

house = Item('house', 'A small, old cabin with its door open is here.', 'This cabin is very cwaint and homy looking.',
['enter'], (42, 42))

door1 = Item('the door', 'an old wooden door hangs from a couple rusty hinges to the south.', "Time has not been good to this kind old door. The constant exposure to the weather with no break has made the outside half become a bed of splinters. The two hinges holding the door up look like they were very well made at one point in time, but now they are just covered in rust. The bar has fallen off and there is no way of latching the door anymore. The only thing keeping it shut is the rusty hinges.",
['enter'], (0, 0))

cloth = Item("a piece of cloth", "A dry piece of cloth is here",
"This cloth looks like it would be great for soacking up a wet mess",
['take', 'use', 'torch'])

torch = Item("A Stick With a Cloth Around It", "a stick with a cloth wrapped around it is here", "There is a stick and a piece of cloth. They are placed together so that the cloth is wrapped around one end of the rather long and stirdy stick. It is kind of reminiscent of a torch...",
['useWith', 'drop', 'oil'])

poem = Item("the poem", "Some papers resting on the table", "There looks to be quite a lot of text on this newly looking paper.",
["read"])

table = Item('The Spotless Table', "A stirdy, clean table rests against the north wall", 'Contrarry to what one would think, this stirdy oak table is completely dust free. The top even shimmers. There are some papers on top of the table as well that are not yellowed with age.',
['container', 'LookOn'], None, 1)
table.add('items', poem)

sword = Item('The Sword of Night', "A beyond black sword hanging over the door sucks the light from out of the room", "Ouch! It hurts to look at the sword! Just how it hurts to look at something that is too bright, it hurts to look at this sword because it is too dark. Night is definitely this swords dominion.",
['take', 'hold'])

lit_torch = Item("The Lit Torch", "A torch is burning brightly here", "Fire! This torch is really burning bright! Who knew a piece of cloth and some oil on a stick could become something so... so... hott!",
['wield'])

flint = Item("A Piece of Sharp Flint", "Some jaggid rocks are laying on the ground", "Looking at this rock, it becomes clear why humans first started using stone to cut. The edge on this rock is unbelievably sharp. It could probably cut stake like butter.",
['take', 'use', 'fire'])

lamp = Item("An Old Lamp", "An old lamp is mostly barried under the sand", "There is a steel frame around the oil chamber and the glass cover where a wick used to be. There is some oil left, but the wick has gone on vacation. You slighly rub the glass cover just to see what happens...",
['oil', 'take', 'use', 'fire'])

UnlitTorch = Item("The Unlit Torch", "A torch drenched in oil is here", "The orriginal cloth and stick pairing could be called a torch, but nothing screems \"Light me!\" like this torch. Dripping with oil, the cloth on this stick looks like it was built for a spark.",
['drop', 'useWith', 'fire'])

cave = Item("A Cave Entrance", "The dark mouth to a cave can be seen behind some old masonry", "Some weathered and cracked steps lead into the dark mouth of the cave. This probably means it didn't used to be a cave, but time has destroyed all but the barest remains of what could have been a cellar or dungeon of some kind. One thing is for sure, it is as dark as it could possibly be past the first few steps.",
['enter'], (2, 1))

tree = Item("The Tree", "A large seeder tree Dominates this area of the woods", "The trunk of this large seeder tree  is about 5 feet wide in Diameter, attesting to its not unconsiderable age. There are a couple broken branches though that have gotten stuck among their fellows instead of falling to the ground.",
['LookIn', 'search'], None, 1)
tree.add('items', stick)
