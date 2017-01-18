from Items import *

class Room(object):
	"""Description and exits of a room are here from this class"""
	def __init__(self, name, coord, description="This is a room", background=None):
		self.name = name
		self.coord = coord
		self.description = description
		self.background = background
		self.items = []
		look = Item('look', 'Look around', description)
		self.items.insert(0, look)
		self.exits = []
	def add_exits(self, *exits):
		"""put in exits to this and the for-loop will pull the coord from the exit and append it to exits."""
		for e in exits:
			self.exits.append(e.coord)
	def add(self, where, *what):
		"""See items.py for description, but where is the name of the list and what are the list items"""
		where = getattr(self, where)
		map(where.append, what)

start = Room('start', (0, 0), "Grass and trees are all around and there is a little house nessled behind some over-grown shrubbery.", "start.ogg")

house1 = Room('house', (42, 42), "You stand in a dimly lit room. A table is against the north wall and a bed is along the west wall. The door is to the south and a window is to the east.", 'house.ogg')

lake = Room('lake', (0, 1), "A rectangular lake streches to the north farther than the eye can see. The forest is to the west and a sandy beech goes on to the east. A collection of really sharp and jaggid rocks litters the shore.", "lake.ogg")

forest = Room('trees', (1, 0), "Tall trees have grown quite close together here. The forest continues off to the north and some broken masonry can be seen to the west.", "forest.ogg")

desert = Room('desert', (0, -1), "Hot air presses down upon the sunbaked sand and the ground is littered with small succulents.The little house is to the north and far to the north west you see a dark spot that may be trees.", "desert.ogg")

ruins = Room('ruins', (2, 0), "A few sad looking moss-covered pillers poke up out of what looks like the remains of a once grand building. There is a dark hole that leads under the ruins. The trees are all around and one adventurace tree has taken root in the old stone.", "ruins.ogg")

cave1 = Room('cave', (2, 1), "This room is very dark and the musty smell of some creature wafts in from farther on. Rusty chains litter the floor and a few iron bars still mark where there used to be cells. Cold air wafts in from the opening up the stairs to the south.", "cave.ogg")

lair = Room('lair', (2, 2), "The smell of inhabitation is really strong here. There is a buzzing from above and a little bit of light shines down. A long rope is attached to an old ring in the floor and there are crude stone steps leading up. There is a smoothe rock slab to the east and a case made of glass and gold to the north west.", "lair.ogg")

start.add_exits(lake, desert, forest)
lake.add_exits(start)
desert.add_exits(start)
forest.add_exits(start, ruins)
ruins.add_exits(forest)
cave1.add_exits(lair, ruins)
lair.add_exits(cave1)

start.add('items', house)
house1.add('items', door1, table)
forest.add('items', tree)
ruins.add('items', cave)
lake.add('items', flint)
desert.add('items', lamp, cloth)

rooms = {
(0, 0): start,
(0, 1): lake,
(1, 0): forest,
(0, -1): desert,
(2, 0): ruins,
(2, 1): cave1,
(2, 2): lair,
(42, 42): house1
}
