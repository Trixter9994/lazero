import zmq
import time

# this is fucked.
# all fucked up.
port = "5560"
context = zmq.Context()
socket = context.socket(zmq.PUB)
socket.bind("tcp://127.0.0.7:%s" % port)
t0, t1 = 0, 0
while True:
    # msg = socket.recv_string()
    # socket.sennd_string("")
    # t1 = time.time()
    # WTF?
    # print(msg)
    # print(t1-t0)
    socket.send_pyobj([1,2,3,4])
    # socket.send_string("client message to server1")
    print(t1 - t0)
    # port is not the issue.
    # socket.send_string("client message to server2")
    # well,we have it.
    # this sucks.
    t1 = time.time()
    time.sleep(1)
    t0 = time.time()
    # it is always sending.
    # never care about the shit.
    # what the fuck is going on?