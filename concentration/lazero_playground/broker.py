import sys
import time
import utl
import zmq

# well, the client can always be listening.
# nuts.
class Broker(object):
    def __init__(self, ctl,xsub_port, xpub_port):
        self.xsub_socket, self.xpub_socket = utl.get_broker(ctl,
            xsub_port, xpub_port)
        self.poller = zmq.Poller()
        self.poller.register(socket=self.xpub_socket, flags=zmq.POLLIN)
        self.poller.register(socket=self.xsub_socket, flags=zmq.POLLIN)
        self.buffer = {}
# whatever.
    def update_buffer(self, msg):
        topic = msg.split(',')[0]
        if topic in self.buffer:
            self.buffer[topic].append(msg)
        else:
            self.buffer.update({topic: [msg]})

    def handler(self):
        while True:
          # you can do it later.
          # what the fuck?
            events = dict(self.poller.poll(1000))
            # events from publishers
            if self.xsub_socket in events:
                msg = self.xsub_socket.recv_string()
                self.xpub_socket.send_string(msg)
                print('[Broker] Forwarded message: %s' % msg)
                self.update_buffer(msg)
            # events from subscribers
            if self.xpub_socket in events:
                topic = ''.join(list(self.xpub_socket.recv_string())[1:])
                if topic in self.buffer:
                   	# send history messages
                    [self.xpub_socket.send_string(item)
                     for item in self.buffer[topic]]
                else:
                    self.xsub_socket.send_string(topic)

# you are nuts.
if __name__ == '__main__':
	# The 1st argument is XSub port number, the 2nd is XPub port number
  # what if we have dots?
    broker = Broker(sys.argv[1], sys.argv[2], sys.argv[3])
    # number or something?
    # what the fuck?
    # we will get shit.
    broker.handler()
# called the trading strategy.
# i have seen shit.