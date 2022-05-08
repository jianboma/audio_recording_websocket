

import os, sys
from websocket_own.audio_websocket_server import WebsocketServer
import numpy as np
import wave

sampleDIR = 'recorded_samples'

# Called for every client connecting (after handshake)
def new_client(client, server):
	print("New client connected and was given id %d" % client['id'])
	server.send_message_to_all("Hey all, a new client has joined us")


# Called for every client disconnecting
def client_left(client, server):
	print("Client(%d) disconnected" % client['id'])


# Called when a client sends a message
# this is the function called when the server received data
def message_received(client, server, message):
    try:
        message_decoded = message.decode('utf8')
        print("Client(%d) said: %s" % (client['id'], message_decoded))
    except:
        message_decoded = np.frombuffer(message, np.int16)
        client['of'].writeframes(b''.join(message_decoded))
        client['handler'].send_message(f'Received data:  {len(message_decoded)} ')


PORT=9001
server = WebsocketServer(port = PORT)
server.set_fn_new_client(new_client)
server.set_fn_client_left(client_left)
server.set_fn_message_received(message_received)
server.run_forever()