import zmq
# import random
# import sys
import time

port = "5556"
context = zmq.Context()
socket = context.socket(zmq.PAIR)
socket.connect("tcp://fc00::%s" % port)
t0, t1 = 0, 0
while True:
  # what the heck?
    msg = socket.recv_string()
    # print msg
    # how to broadcast without shit?
    # check it.
    # does not have messages.
    # should we use async?
    t1 = time.time()
    print(msg, t1-t0)
    socket.send_string("client message to server1")
    socket.send_string("client message to server2")
    time.sleep(1)
    t0 = time.time()
