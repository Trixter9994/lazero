from utl import get_publisher
import time
#sigma=0.005
#sigma=0.007
sigma=0.01
# value may be reconfigured.
# you can do the redundancy check.
# meaning you can send it twice?
# it is not stable.
g = get_publisher("127.0.0.7", "3000")
# while True:
# for x in range(20):
    # g.send_string("xxxxxx")
g.send_string("xxxxxx")
def broadcast(x):
    time.sleep(sigma)
# you get shit.
    g.send_string(x)
# only one received.
# first shit will be dropped.
# it cannot have one-shot like shit.
# this is shit.
# pussy.
# why not use that thing?
# first is for checking.
# this is fuck.
    # what the fuck?
    # g.send_string("Hello World")
# this will never work!
# i have got shit!
# what the fuck?
# i used to think that my fucking computer is hyperactive.
# it was overclocked.
# fucking language server.
# what the fuck are you doing?
# i need to kill you.
