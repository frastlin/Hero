from accessible_output import speech
spk = speech.Speaker().output

message_list = []
read_messages = True
location_in_list = len(message_list)-1

def add_message(message):
	"""adds messages to the list (may wish to have several lists)"""
	global message_list
	message_list.append(message)
	if len(message_list) > 100:
		message_list.pop[0]
	if read_messages:
		spk(message)
