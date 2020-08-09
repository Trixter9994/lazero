# this is nothing.
from getFromPickleR import returnListR
# now what to do?
# check if works.
import rewire

r=returnListR()
# we have two shits in all.
print(r)
# print([type(r1) for r1 in r])
r0=rewire.unpacker(r[0])
print(r0)
# i think training a neural network is not as easy as managing our datasets.
# but this is tricky because we do not know where is the thing?