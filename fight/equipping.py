#not dealing with this for the current game, the speaking thing works, you pass arguments as braces into the dict of the equip function. the class is on the second part of the module, search for class.
#checks all kinds of stuff to equip items, equiper is the master function.
#equiper(item={}, bod={}, hands=[]):

def spker(k, item, bod, hands):
	"""Speaks everything"""
	i = item[k]
	if k in bod:
		if bod[k]:
			if k in hands:
				spk("You remove %s from your %s" % (bod[k], k))
			else:
				spk("You remove %s from your %s" % (bod[k], k))
		if k in self.hands:
			spk("You hold %s in your %s" % (item[k], k))
		else:
			spk("You wear %s on your %s" % (item[k], k))



def equiper(item={}, bod={}, hands=[]):
	"""This runs to see if there is the body part in the list and if not returns a blank dict. If so, it returns the item and says what was worn and what was replaced. It also runs the flag checker"""
	k = item.keys()[0]


from accessible_output import speech
spk = speech.Speaker().output

d = {'i like': "I like candy", "the man": "The man ran", "dance": "Dance for me!"}

class C(object):
	def __init__(self, body={'head': None, 'feet': None, 'right hand': 'green', 'left hand': None}, hands=['left hand', 'right hand']):
		self.body = body
		self.hands = hands

	def equip(self, body_and_item={}):
		for k in body_and_item:
			if "two_handed" in flags

			it = equipping.equiper(item=body_and_item, bod=self.body, hands=self.hands)

a = C()
print a.body['feet']

a.equip({'left hand': 'red'})
