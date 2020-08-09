import zmq
import random
import sys
import time

port = "5556"
context = zmq.Context()
socket = context.socket(zmq.PAIR)
socket.connect("tcp://127.0.0.7:%s" % port)
#while True:
#        msg = socket.recv()
#        print msg
# performing one-shot.
#        socket.send("client message to server1")
def send_string(a):
    #socket.send_string("client message to server2")
    socket.send_string(a)
#        time.sleep(1)
# asshole.
