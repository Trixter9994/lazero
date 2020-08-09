# the server accepts inputs.
# as animal, there isn't much we can move.
import zmq
import pyautogui
import traceback
# make it debuggable?
# what keystroke?
# just typing. see if this works.
# check random commands!
port = "5570"
context=zmq.Context()
socket=context.socket(zmq.PAIR)
socket.bind("tcp://127.0.0.1:%s" % port)
while True:
    try:
        msg = socket.recv_pyobj()
    # send a list instead? two things?
        assert type(msg)==str
        exec(msg)
    except:
        e = traceback.format_exc()
        print(e)
    # just a string.
