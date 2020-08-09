# this is the type-less version checker.
# shall we use other shits?
# just put it here. avoid canonical reference.
# import re
# WTF?

def flattern(a):
    return [x for y in a for x in y]

def flatternII(a):
    v=[x for x in a if type(x)==type([])]
    if v==[]:
        return a
    else:
        return [x for x in a if x not in v]+flatternII(flattern(v))

def flatternIII(a):
    v=[x for x in a if type(x)==type([])]
    if v==[]:
        return [a]
    else:
        return [[x for x in a if x not in v]]+flatternIII(flattern(v))

def base(a):
    return [None if type(y)!=type([]) else base(y) for y in a]

def purifier(a):
    return "".join(list(filter((lambda x: x in "[]"),str(base(a)))))

def shaper(a):
    return eval(purifier(a).replace("][","],["))

def baseII(a):
    v=[x for x in a if type(x)==type([])]
    if v==[]:
        return [(len(a),0)]
    # this is frustrating.
    else:
        return [(len(a),len(v))]+baseII(flattern(v))
    # scanner? incline detector?
    # use flattern func.

# extract all sublists.
# how about index? that is better.
def baseIII(a,b=[]):
    return [tuple(b+[x]) if type(a[x]) != type([]) else baseIII(a[x],b+[x]) for x in range(len(a))]

def baseIV(a):
    return flatternII(baseIII(a))

def baseV(a):
    return flatternIII(baseIII(a))

def extractor(a,b):
    c=a[b[0]]
    return c if len(b)==1 else extractor(c,b[1:])

def baseVI(a):
    r0=baseV(a)
    r=(lambda x:list(set(list(map((lambda y: y[:-1]),x)))))
    return [r0,list(map(r,r0[1:]))]
