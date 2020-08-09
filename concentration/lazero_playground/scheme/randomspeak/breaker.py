import sys
import time
import utl
import zmq

# well, the client can always be listening.
class Broker(object):
    def __init__(self, ctl,xsub_port, xpub_port):
        self.xsub_socket, self.xpub_socket = utl.get_broker(ctl,
            xsub_port, xpub_port)
        self.poller = zmq.Poller()
        self.poller.register(socket=self.xpub_socket, flags=zmq.POLLIN)
        self.poller.register(socket=self.xsub_socket, flags=zmq.POLLIN)
        # self.buffer = {}
# whatever.
    # def update_buffer(self, msg):
    #     topic = msg.split(',')[0]
    #     if topic in self.buffer:
    #         self.buffer[topic].append(msg)
    #     else:
    #         self.buffer.update({topic: [msg]})
    def handler(self):
        while True:
          # you can do it later.
          # what the fuck?
            events = dict(self.poller.poll(1000))
            # events from publishers
            # do the tornado stuff?
            # what the heck?
            # can you receive anything?
            if self.xsub_socket in events:
                msg = self.xsub_socket.recv_pyobj()
                self.xpub_socket.send_pyobj(msg)
                print('[Broker] Forwarded message: ',msg)
                # self.update_buffer(msg)
                # what the fuck?
                # do we need buffer over here?
                # caution for buffer overflow!
            # events from subscribers
            # if self.xpub_socket in events:
            #   # must be string.
            #     topic = ''.join(list(self.xpub_socket.recv_pyobj())[1:])
            #     if topic in self.buffer:
            #        	# send history messages
            #         [self.xpub_socket.send_pyobj(item)
            #          for item in self.buffer[topic]]
            #     else:
            #         self.xsub_socket.send_pyobj(topic)


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