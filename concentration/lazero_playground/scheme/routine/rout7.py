import zmq
# import time

# this is fucked.
# all fucked up.
# i need the one-shot thing.
port = "5560"
context = zmq.Context()
socket = context.socket(zmq.PUB)
socket.bind("tcp://127.0.0.7:%s" % port)
# must have that fucking connection?
# well, try it later.
# man this is shit.
# nothing is like that.
# this sucks.
# why it is in use?
# check it?
# command line is too long.
# fucking shit.
# we need to build our fucking server.
# this shit will never work.
# it is shit.


def jerk(nazi):
    socket.send_pyobj(nazi)
