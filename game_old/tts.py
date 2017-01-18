import pyttsx

engine = pyttsx.init()

#for basic speech
spk = engine.say
spk("Hello world")
spk("Main menu")

engine.runAndWait()

#for changing the speech rate

rate = engine.getProperty('rate')
engine.setProperty('rate', rate+50)
engine.say("The big brown fox had a lovely box")
engine.runAndWait

#for changing volume
volume = engine.getProperty('volume')
engine.setProperty('volume', volume-0.25)
engine.say("The big brown fox got quieter")
engine.runAndWait()


#for changing voices, this script just says something in all voices installed
voices = engine.getProperty('voices')

for voice in voices:
	engine.setProperty('voice', voice.id)
	engine.say("The quick brown fox jumped over the log")

engine.runAndWait()