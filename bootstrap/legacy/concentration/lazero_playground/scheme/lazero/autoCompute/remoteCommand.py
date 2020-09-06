import zmq
port ="5570"
context=zmq.Context()
socket=context.socket(zmq.PAIR)
socket.connect("tcp://127.0.0.1:%s" % port)

socket.send_pyobj("pyautogui.write('hello world')")
