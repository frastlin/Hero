import globals, Items, scenes, random, utilities
from accessible_output import speech
spk = speech.Speaker().output

def torch(play, i1, i2):
	spk("You wrap the cloth around the stick, creating a stick with a cloth around it")
	map(globals.inv.remove, [i1, i2])
	globals.inv.append(Items.torch)

def house(play, item):
	x = random.choice([
"You move away some vines and try to get a good grip on the splintery door. You brace yourself and yank. The door gives with some protest and you manage to squeeze through.",
"You manage to get a grip on the door and pull. The door slips and you get a huge sliver in your thumb. The door slides shut and you curse the gods. You grip with your other hand and this time you stick your foot in the door before it slips out of your grasp again and squeeze through into the dark room.",
"You look around for some kind of catch to put into the door. You see a short stick and try to get a grip on the door. You keep trying to nudge the old thing, but every time you think you have a grip, it slips. You put down the stick and use both hands. You manage to get it open enough for your foot to fit, but as you turn around to grab the stick, the door somehow slips over your foot and closes again. You look goggle eyed at the door and slowly reach out your index finger to poke it, just to make sure it is still real. You get a sliver in response. You grip the door with both hands and yank it open. Before it closes you dash in.",
"You tug on the door, but don't really feel like trying to pull it open. You walk around the house to the window. You hoist yourself up to the sill and clamber through.",
"You tug on the door for about two minutes with no effect. You suddenly get a fantastic idea. You grasp some vines and start to climb up to the roof. You hoist yourself over the lip and lay on your belly panting from the effort. You put your hands down to hoist yourself up and get about six splinters in your left palm. You wince but keep going on your mission. You cautiously make your way over to the chimney and clear the vines and leaves away. You grin to yourself and put both legs in and drop. ***** SPLAT! *****",
"You reach out your right hand to get a grip on the door to enter. As you touch the wood a very sharp splinter jumps out of the wood and stabs your hand. You yank your hand back and look at the splinter. The splinter stairs back at you with a smug expression. You start to think that you are going crazy and yank out the splinter. You reach out with your left hand and another splinter impales itself on your hand. You let out a yelp of surprise. The second splinter seems to let out an evil chuckle. You quickly yank it out of your hand and decide you are really going over the edge. You think to yourself that if splinters are already laughing at you, what worse could happen? You get in your most wizard-like pose and in a deep and sonorous  voice you say: \"Open says me.\" The door smoothly swings open. Not wanting to look dumb in this clearly fantasy world, you walk into the house."
])
	spk(x)
	return item.location

def reader(name):
	"""There is an import of the menus module and then there"""
	from menus import muted_menu
	texts = {
	'the poem': """
There once was in time long past
ledgends of a heavenly lass
So fair was she in face and heart
that kingdoms trembled at her fart.
one day it came to pass at mid-summer's eve
that Fegar Lionhart, most respected in the land,
asked her hand to charush and keep.
and with a distracted air his love did speak:
'Yeah dude... forget it bro.'
For one whole minute the cort failed to blink
where those words came from nobody could think.
The king sent for wise men and scollars of the past,
but nowhere was a 'dude' or 'bro' ever seen.
When she was asked about what those words did mean, the beauty replied:
'Yo Face!'
till on one stormy night an old man she did meet.
he called her a babe, a homy in disguise
they talked about totes and fabs and besties all night.
The next day they were gon, no trace but this letter if letter it was, full of strange words
'chillaxin with Gpa @ the cabin'
even werse than before.
The king did proclaim that there never was a girl
who talked of strange things never heard of in the world.
Soon the land forgot the beauty they knew,
but one man was left who said he would find
and vanquish the two.
He studdied the sword, spells and prayers
and soon he was head of the wizards and thought he could do
what the king never thought could be done
find the unknown girl he once did lose.
So he traveled and searched till he found this house.
There he did meet his beauty, but much to his dismay
she yelled words he never could say
'bugger off!'
He thought she was addled
and kindly he said:
'thou art my wife by law and by right
so come along now or I'll stop being nice.'
She screamed and fot with tooth and nale but sir Lionhart
with bareley a thought
placed her under a magic sleepping guard 
It was at this point
when all hope was lost
the old man did come and change the fate of our beauty's next night.
The man grinned,
showing two rows of white teeth
and he chanted
these words no wizard would speak:
'you're as sharp as they're made,
but as dumb as a spade
you shine so brightly
you'll melt in the day
you'll hang on the wall
and will never fall
till one comes and saves the made.'
With an implosion of space and a strange look on his face
 the hero did shrink and fall on the ground with an audible plink.
The old man grabbed the hilt and placed it by the door
and stuck it inside where the blade only would be touched by the night.
The beauty she lay
asleep and cold
no matter what he did the old man couldn't make
the beauty awake.
She was under a spell
from ledgends of old
waiting for a hero to break the hold
of her ageless sleep.
and the sword of knight
that no longer did breathe,
hung on the wall
awating the hero to be
The old man took the beauty and hid her away
safe behind a monster
that only wisdom could beat
Thus sleeps the beauty
of ledgends passed
awaiting the hero who
will come at last
"""
}
	text = texts.get(name).split("\n")
	muted_menu(name, text)

def thepoem(play, item):
	if not globals.sword_in_house:
		play.items.append(Items.sword)
		globals.sword_in_house = True
	else:
		spk("The sword seems to stair balefully down at you")

def TheSwordofNight(play, item):
	l = []
	for n in globals.inv + globals.equ:
		l.append(n.name)
	if 'The Lit Torch' in l:
		spk("You carefully lift the sword of night from over the door.")
		globals.number = 0
		globals.inv.append(item)
		play.items.remove(item)
		item.flags.remove('take')
		item.flags.append('wield')
	else:
		spk("You reach up to take the black sword down, but as your hand gets within 2 inches of the sword, they lose all feeling. You yank your hand back and slap them against your legs. The life slowly returns to your fingers. Perhaps the sword doesn't want to socialize just yet.")

def ACaveEntrance(play, item):
	l = []
	for j in globals.inv + globals.equ:
		l.append(j.name)
	if "The Sword of Night" in l and "The Lit Torch" in l:
		spk("You brandish the sword of night in your right hand and the blazing torch in your left and confadently plunge into the dark cave.")
		return item.locations
	elif 'The Sword of Night' in l:
		spk("It would be rather silly to enter a dark cave without any way to see where you are going. Where did the torch go?")
	elif 'The Lit Torch' in l:
		spk("Although the torch makes seeing much easier, if there was a dragon or some creature hiding in there, the torch is little protection.")
	else:
		spk("OOH, not a good idea. With no way to see or defend yourself, venturing down into an unknown dark cave is not very smart!")

def oil(play, i1, i2):
	spk("You dip the cloth that is on the end of the stick into the oil. You hold it there until it is completely soaked then remove it. Now you have an unlit torch!")
	globals.inv = utilities.popper("A Stick With a Cloth Around It", globals.inv)
	globals.inv.append(Items.UnlitTorch)

def fire(play, i1, i2):
	"""if you do l = globals.inv what ever you do to l will happen to globals.inv, so list(globals.inv) makes a copy of globals.inv for l 	to use."""
	l = utilities.popper("The Unlit Torch", list(globals.inv))
	if l != globals.inv:
		globals.inv = l
		spk("You get a fantastic idea! You hold the torch between your legs, grab the flint in your right hand and the lamp in your left and with tramendous force, bring the 2 together.")
		spk("The glass cover flighs off and the steel top breaks off. You grab the steel bar that is left in the frame and pull it out. You then position the steel so it is pointing down at the cloth. You angle the flint so it will shoot the sparks into the torch. You smack the steel with the flint and BAM!")
		spk("*****")
		spk("You've got fire!")
		utilities.popper("An Old Lamp", globals.inv)
		utilities.popper("A Piece of Sharp Flint", globals.inv)
		globals.inv.append(Items.lit_torch)
	else:
		spk("You bang the flint on the top of the lamp in a basic rhythm and start singing your favorite bar song at the top of your lungs. You sing so hard and so Intensely, sparks start shooting off the lamp cover.")
