import zmq

port = "5560"
context = zmq.Context()
socket = context.socket(zmq.PUB)
socket.bind("tcp://127.0.0.7:%s" % port)
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
# this is shit.
# what the fuck?
# can we just do it once?
# why is it so damn shitty fucked?
# this is fuck.
nazi=[1,2,3,4]
# def jerk(nazi):
socket.send_pyobj(nazi)
