import zmq
import subprocess
# really nigga?

port = "5556"
context = zmq.Context()
socket = context.socket(zmq.PAIR)
socket.bind("tcp://127.0.0.7:%s" % port)
while True:
#        socket.send_string("Server message to client3")
# what the fuck is this?
        msg = socket.recv_string()
        # will it stuck?
        # what the heck?
        ms = subprocess.check_output([msg], stderr=subprocess.STDOUT)
        # it does not work.
        print (type(ms))
        print (ms)
# what is that?
        # this is not good.
        # shall.use sync method.
        # this is fuck.
#        time.sleep(1)
