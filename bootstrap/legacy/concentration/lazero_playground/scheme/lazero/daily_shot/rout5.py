import zmq
import time
# import inspect
# import signal
from threading import Thread
import functools
# you can learn, you can also give up.

def timeout(timeout):
    def deco(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            res = [Exception('function [%s] timeout [%s seconds] exceeded!' % (
                func.__name__, timeout))]

            def newFunc():
                try:
                    res[0] = func(*args, **kwargs)
                except Exception as e:
                  # this is funny.
                    res[0] = e
            t = Thread(target=newFunc)
            t.daemon = True
            try:
                t.start()
                t.join(timeout)
            except Exception as je:
                print('error starting thread')
                raise je
            ret = res[0]
            if isinstance(ret, BaseException):
                raise ret
            return ret
        return wrapper
    return deco


# we need to resimulate the simulation.
# which sucks.

# import sys
# import zmq


# def alarm_handler(signal, frame):
#   raise IOError("Timeout processing auth request")


# previous_alarm_handler = signal.signal(signal.SIGALRM, alarm_handler)
# this is fucked.
# what the fuck?
# how to enable the free talk?
# is the program stucked?
# you can even use this ipv6?
# what the fuck?
# all these fucking errors.
# screw you!
port = "5560"
# excuse me?
context = zmq.Context(io_threads=1)
# one thread only.
# is this good or bad?
# what the fuck?
# all of you, fucking sucks.
# that can be fucking great.
# you do not wrap this?
socket = context.socket(zmq.SUB)
# socket = context.socket(zmq.PUB)
socket.connect("tcp://127.0.0.9:%s" % port)
# why we have no shit?
# do we can only receive messages instead of programs?
# what the fuck do you mean?
# topicfilter=None
# socket.setsockopt_string(zmq.SUBSCRIBE, topicfilter)
socket.setsockopt_string(zmq.SUBSCRIBE, '')
# got listen to a bunch of shits?
# revision?
# shit.
# socket.subscribe('hello world')
# WTF?
# what the fuck?
# you know shit.
# k0 = socket.recv_string
# # what the fuck?
# kx = inspect.getargspec(k0)
# # k1 = [k0.__defaults__, k0.__code__.co_argument, k0.__code__.co_varnames]
# # print(k1)
# all shit.
# print(kx)
# you have shit!
# name only?
# socket.setsockopt(zmq.RCVTIMEO, 3)
# socket.RCVTIMEO = 3
# what the fuck?
# must wait?
# try it again.
# what the fuck is this?
# does this consume a lot of CPU and RAM?
# no, it is that one's business.
# stay up to date. trust me, we will have it rolling.
# what the hell?
# not having shit?
# how to subscribe all shits?
# no fucking verification?
# like python objects?
# what the fuck is it then?
# to pass a function?
# how the fuck?
# how to subscribe all shits?
# shit, this fucking works!
# subscribe to all shits.
# not getting out?
# what the fuck is this?
t0, t1 = 0, 0
# tt = dir(socket.recv_string())
# what the fuck?
while True:
  # fuck these people.
    # signal.alarm(3)
    # msg0 = timeout(timeout=3)(socket.recv_string)
    # msg = msg0()
    # print(dir(socket))
    msg=socket.recv_string()
    # fuck them all.
    # it does not work.
    # what is wrong?
    # we need osciliation here.
    # to do something over and over again.
    # it is working.
    # signal.alarm(0)
    # there is no timeout here.
    # so this program will gonna live forever without human interference?
    # what the fuck?
    # socket.sennd_string("")
    # what the fuck?
    # nothing here.
    # shit. address in use.
    # we need middleware.
    # fucking network.
    # all fucked up.
    # what the fuck?
    # shit.
    # it gets stucked.
    # we cannot let this happen.
    # or we can do something co change this shit.
    t1 = time.time()
    # no shit?
    # yes, there are no shit out there.
    print(msg)
    print(t1-t0)
    # socket.send_string("client message to server1")
    # socket.send_string("client message to server2")
    print("do we have timeout?")
    # time.sleep(1)
    # it is not sleeping, but it need to wait.
    # fuck. what about timeout?
    # what the fuck?
    # it stopped.
    # not working.
    # what the fuck!
    # maybe we shall send a hypervisor.
    t0 = time.time()
    # it is always sending.
    # never care about the shit.
