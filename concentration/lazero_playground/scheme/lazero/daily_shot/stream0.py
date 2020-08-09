import time
import zmq
from zmq.devices.basedevice import ProcessDevice
import multiprocessing

# what is this fuck all about?

# fuck?
if __name__ == "__main__":
    # pass"
    multiprocessing.freeze_support()
    frontend_port = 5559
    backend_port = 5560
    # number_of_workers = 2
    # what the fuck?
    streamerdevice = ProcessDevice(zmq.STREAMER, zmq.PUB, zmq.SUB)
    # d0 = dir(streamerdevice)
    """['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__',
'__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_in_binds', '_in_connects', '_in_sockopts', '_launch_class', '_out_binds', '_out_connects',
'_out_sockopts', '_random_addrs', '_reserve_random_port', '_setup_sockets', 'bind_in', 'bind_in_to_random_port', 'bind_out', 'bind_out_to_random_port', 'connect_in', 'connect_out', 'context_factory', 'daemon', 'device_type', 'done', 'in_type', 'join', 'launcher', 'out_type', 'run', 'run_device', 'setsockopt_in', 'setsockopt_out', 'start']"""
    # print(d0)
    streamerdevice.bind_in("tcp://127.0.0.9:%d" % frontend_port)
    streamerdevice.bind_out("tcp://127.0.0.9:%d" % backend_port)
    # print(streamerdevice._out_sockopts)
    # we have got shit.
    # streamerdevice.setsockopt_string(zmq.IDENTITY, 'PUB')
    # streamerdevice.setsockopt_out(zmq.IDENTITY, 'SUB')
    streamerdevice.start()
    # this is fucked up.
    # fucking shit.
    while True:
      # I am dead.
      # denied? what the fuck?
        time.sleep(1)
