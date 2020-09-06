import zmq
import random
import time

lt0 = "127.0.0.7"

port = '5556'
pub_server_name = 'pub-server01'
# this is shit.
context = zmq.Context()
socket = context.socket(zmq.PUB)
socket.bind('tcp://'+lt0+':%s' % port)
# why not bind to an ip address?
while True:
    topic = random.randrange(9999, 10005)
    # this is great.
    messagedata = random.randrange(1, 215)-80
    print ('topic:%s messagedata:%s' % (topic, messagedata))
    socket.send_string('%d %d %s' % (topic, messagedata, pub_server_name))
    time.sleep(1)
