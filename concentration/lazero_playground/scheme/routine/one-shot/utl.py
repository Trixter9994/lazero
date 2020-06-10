import zmq


def get_publisher(address, port):
    context = zmq.Context()
    socket = context.socket(zmq.PUB)
    connect_addr = 'tcp://%s:%s' % (address, port)
    socket.connect(connect_addr)
    return socket


def get_subscriber(address, port, topics):
	# Subscriber can register one more topics once
    context = zmq.Context()
    socket = context.socket(zmq.SUB)
    connect_addr = 'tcp://%s:%s' % (address, port)
    socket.connect(connect_addr)
    if isinstance(topics, str):
        socket.subscribe(topics)
    elif isinstance(topics, list):
        [socket.subscribe(topic) for topic in topics]
    return socket

# pub -> xsub
def get_broker(ctl,xsub_port, xpub_port):
    # shared_address=ctl
    # shit. it works like fuck.
    # fucking shit.
    # this is all fucked up.
    context = zmq.Context()
# the direction is wrong.
    xsub_socket = context.socket(zmq.XSUB)
    xsub_addr = 'tcp://'+ctl+':%s' % xsub_port
    xsub_socket.bind(xsub_addr)
    # make xsub receive any message
    # what the fuck?
    # what the fuck?
    xsub_socket.send(b'\x01')

    xpub_addr = 'tcp://'+ctl+':%s' % xpub_port
    xpub_socket = context.socket(zmq.XPUB)
    xpub_socket.bind(xpub_addr)
    # make xpub receive verbose messages
    xpub_socket.setsockopt(zmq.XPUB_VERBOSE, 1)

    # zmq.proxy(xsub_socket, xpub_socket)
    return xsub_socket, xpub_socket
