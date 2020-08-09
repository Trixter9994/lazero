from core4 import matchNeighbor
from simpleStorage import storeAList
# now you can make a local database.
#    k=chr(k0)
v={chr(k0):matchNeighbor(chr(k0)) for k0 in range(ord("a"),1+ord("z"))}
print(v)
storeAList(v)

