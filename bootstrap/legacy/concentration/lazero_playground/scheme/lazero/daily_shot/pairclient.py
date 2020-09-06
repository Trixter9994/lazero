import zmq
import random
import sys
import time
# there is no way you can do this.
# it is exclusive, and cannot have multiple subscribers.
# how about try that thing out?
# just a test.
# launch the thing first in subroutine, and then just sit and enjoy.
# old school like things.
# one for one?
port = "5556"
context = zmq.Context()
socket = context.socket(zmq.PAIR)
socket.connect("tcp://127.0.0.7:%s" % port)
#while True:
#        msg = socket.recv()
#        print msg
# performing one-shot.
#        socket.send("client message to server1")
socket.send_string("client message to server2")
#        time.sleep(1)
# asshole.
