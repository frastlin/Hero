#runs the threading for the attacks
import keyconfig, menus, player as p2, fighter, bear
from tests import pygametest as p

player = p2.Person()
player.stats.attack.mod_level = 4
fo = bear.Bear(1)

current_screen = "fight"

def game_player(play):
	"""basicly runs everything"""
	if play[0] == "current_screen":
		global current_screen
		current_screen = play[1]
	elif play[0] == "attack_choice":
		player.weapon.current_attack = play[1]

	return play


def main():
	p.screen("Fight test")
	play = ('', '')
	while play:
		n = p.key()
		if n[0] == "escape":
			play = False
		elif n[0] in ["[", "]", "x", "h"]:
			play = keyconfig.key_defaults(key=n[0], mod=n[1], player=player, fo=fo)
		elif n[0] == "tab":
			play = keyconfig.tabber(current_screen)
		elif n[1] in [4097, 4353, 4354, 4098] and n[0] == "space":
			player.stats.hp.current_hp = 10
			fo.stats.hp.current_hp = 7
		elif n[0] == "space":
			fighter.combat(player, fo)
		elif current_screen == "fight":
			play = menus.menu(key_pressed=n[0], options=player.weapon.acts)
		if play == None:
			play = ('', '')
		game_player(play)


main()
