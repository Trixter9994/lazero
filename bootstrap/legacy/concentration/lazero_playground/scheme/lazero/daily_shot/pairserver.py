import zmq
import random
import sys
import time

port = "5556"
context = zmq.Context()
socket = context.socket(zmq.PAIR)
socket.bind("tcp://127.0.0.7:%s" % port)
while True:
#        socket.send_string("Server message to client3")
# what the fuck is this?
        msg = socket.recv_string()
        # will it stuck?
        print (msg)
        # this is fuck.
#        time.sleep(1)
