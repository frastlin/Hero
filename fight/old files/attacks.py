#These are all the attacks
import random

#the key is the name of the attack, then it goes kind of attack,
#0 is ac focus, 1 is str boness, 2 is shared boness 3 is defense boness and 4 is special
#then player hit message, player miss message, mob hit message, mob miss message
#in each message the numbers are [0] = weapon name, [1] equals creature name, [2] = jender
#you can create a list of hit or miss messages by using random.choice(["you swing your hand and it connects with a slap", "you #jiggle #your [0] and then throw it", "you dance"])

class Attack(object):
	def __init__(self, type=random.randint(1,3), player_hit=None, player_miss=None, mob_hit=None, mob_miss=None, speed=	0, extra_ac=0, extra_str=0):
		self.type = self.typer(type)
		self.player_hit = self.default_hit(player_hit)
		self.player_miss = self.default_miss(player_miss)
		self.mob_hit = self.default_hit(mob_hit)
		self.mob_miss = self.default_miss(mob_miss)
		self.speed = speed
		self.extra_ac = extra_ac
		self.extra_str = extra_str

	def typer(self, t):
		return "%s is type" % t

	def default_hit(self, message):
		if not message:
			return message
		else:
			return "[1] swing [0] and solidly connect"


astr = {

"swing": (0, "You swing [0], connecting horribly", "The swing you do of [0] fails", "The [0] swing at you and take out a nice chunk of skin", "The swing of [1] mannages to miss you completely"),

"slash": (1, "You swing {0} with a feral grin on your face", "you swing {0}, but miss", "{1} swipes {2} {0} at you", "{1} slashes {2} {0} at you, but misses you by inches"),

"stab": (2, "You bring {0} back and jab it forward in a lunge", "You bring {0} back and jab it forward in a lunge, but just miss", "{1} jabs {2} {0} at you, causing pane!", "{1} jabs {2} {0} forward, but just manages to miss you"),

"specialAttack1": (4, "You swing the sword at the chain that stretches up to the roof and slice it in 2.", "You try to cut the chain, but the bear manages to get in your way", None, None)
}

#def attacker(fighter, opponent, extra_str=0, extra_ac=0, flags=None):
#	str = fighter.str + extra_str

fr = Attack()
print fr.type
