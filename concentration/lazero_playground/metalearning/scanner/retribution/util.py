import readLikeHuman
from simpleStorageR import storeAList
import metaStack
import random
from matrixPro import generalize
from backTrans import wrapperII
# shall we use tolist func?
# oh shit!
# randomly select the core?
# alert! max workload is fixed and therefore not negotiable.
# must select most notified shits for all.
s=readLikeHuman.Meta(0)
s0=s.Meta0()
s0v2=s.Meta0v2().tolist()
# notice that this is the matrix.
# first let's analyze this sequence.
m=metaStack.Meta([4,2])
# generalize is a wrong choice.
# we shall take half of all matricies.
s1=len(s0)
#s0m=Linkage(list(s0v2))
#print(Linkage(s0v2))

#f=generalize(s0v2,0)
# the first column is definitely meaningless for identical matricies.

#print(f)

f=list(map((lambda x:wrapperII(x.tolist(),5)),generalize(s0v2,0)))

storeAList(f)

# the meaning of the matrix?
#print(f)

# the fucking scale?
# function needed
