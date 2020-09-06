import zmq
# import random
# import sys
import time
# subroutine?
# port = "5556"
context = zmq.Context()
socket = context.socket(zmq.PAIR)
# what the fuck?
# print(dir(socket))
# so data are flowing everywhere.
# my hardware is only a start.
socket.IPV6 = True
socket.IPV4ONLY=False
# ok, so what?
# i need the computer be aware of time.
# also, communication.
# socket.bind("tcp://[fc00::]:2000")
socket.bind("tcp://[fe80::fb7:c6df:9d3a:3d7b]:5555")
# what the heck?
# never mind.
# socket.bind_to_random_port("tcp://fc00::/2000")
# socket.bind_to_random_port("tcp://3FFE:FFFF:7654:FEDA:1245:BA98:3210:4562")
# socket.bind("tcp://fc00::%s" % port)
t0, t1 = 0, 0
# shit. use ipv4 only?
while True:
  # who can send without care?
    # print(dir(socket))
    # make it scatter through the hardware.
    socket.send_string("Server message to client3")
    # bitcoin sucks.
    # it is only about crypt-currency.
    # not about global development and computer conscious.
    msg = socket.recv_string()
    # can we receive everything?
    # what the fuck is it anyway?
    # what the hell?
    # should we consider construct the global dynamic learning interface (GDLI)?
    # learning together is better than learning alone.
    # never mind, people still have their fucking choice.
    # making the machine into headache.
    # what the fuck?
    # it is stucked.
    t1=time.time()
    print (msg,t1-t0)
    # is it stuck?
    time.sleep(0.5)
    t0=time.time()
