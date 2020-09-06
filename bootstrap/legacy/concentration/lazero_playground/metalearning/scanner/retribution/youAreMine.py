# youAreMine
# use the abstraction.
# never mind. you can be anything.
# this is the thing waiting for abstraction.
import abstraction
import re
# do you believe in the power of cognition and knowledge?
def hexTest(a):
    try:
        b=int("0x"+a,0)
        return True
    except:
        return False

def relativityFuck(a,b):
    a0=re.findall(r'\w+',a)
    assert hexTest(a0[0])
    return [a0[0],[a0[a0.index(b):]]]

# unspeakable relationship? fuck!

def generalFuck(a,b):
    return [relativityFuck(a0,b) for a0 in a]
# fuck my computer is gonna blow. full of shitty useless pictures. fuck me!
def organize(a,b):
    a0=[[],[]]
    for a1 in a:
        # print(a1)
        if b(a1[1]):
            a0[0].append(a1)
        else:
            a0[1].append(a1)
    return a0

def simpleClass(a,b):
    l=len(b)
    for n in range(l):
        if b[n] in a:
            return n
    return l
# get the number?

def indexGetter(a,b):
    b0=[[] for x in range(len(b)+1)]
    for a0 in range(len(a)):
        y=a[a0]
        b0[simpleClass(y,b)].append([a0,y])
    return b0
        # the last classification is for freaks.
        # multiple freaks?
def simpleFlat(a):
    return [x for y in a for x in y]

def getFucked(v):
    a=list(reversed(sorted(v,key=(lambda x:len(x)))))
    # done with the same length.
    a0,a1=a[0],a[1]
    a2=abstraction.filterOut(a0,a1) # but that None function is useful somehow. we have to admit that.
    # filter out those with too many None.
    # print(a2)
    am=list(reversed(sorted([list(map((lambda y:abstraction.linearFilter(y,x)),a)) for x in a2],key=(lambda z: len(simpleFlat(z))))))
    # print(am)
    # classification?
    # get few lines worked.
    return am
# get the filter. or use random instead. both will reach the target.
# select themost popular one.
# the count. flattern the shit.
# fuck it. just want the shit.
# most common case.
# [1,2] with [1,2,3] -> [True,True,None] -> None
# higher level conclusion.
# if Result is None, what would happens?
# does it exists?
# print(a)
# [1,None],[None,1](only internal 0),[None,0],[None,None]
# how to deal with non-fixed length? sequence could get rearranged.
# how to conclude next level? most based on abstraction. (or example?)
# a[0] with [1,None] -> [True,False,False,False,False]
# a[0] with [None,1] -> [False,True,False,True,False]
# a[0] with [None,None] -> [True,True,True,True,True]
# a[0] with [None,0] -> [False,False,True,False,True]
# you could also get None.
# --------------------------------
# how to create higher level abstraction?
# a[1] with [1,None] -> [True,False,False,False,False]
# a[1] with [None,1] -> [False,False,False,False,False]
# a[1] with [None,None] -> [True,True,True,True,True]
# a[1] with [None,0] -> [False,True,True,True,True]
# Error is important. What is Error? Result -> None