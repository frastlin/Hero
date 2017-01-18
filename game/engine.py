#Run the main loop
import pyglet
from pyglet.window import key as k
clk = pyglet.clock.get_default()
from speech import speak as spk

window = pyglet.window.Window(caption="Hero")


def talker(item, text="Nothing"):
	spk(text)


def on_key_press(key, mods):
	if key == k.SPACE:
		spk("Hello world")
	elif key == k.A:
		spk("Event added")
		clk.schedule_once(talker, 2, "Hello I'm a clock")
	elif key == k.UP:
		spk("Going")
		clk.schedule_interval(talker, 1, "Walking")

window.push_handlers(on_key_press)


@window.event
def on_key_release(key, mods):
	if key == k.UP:
		clk.unschedule(talker)


pyglet.app.run()