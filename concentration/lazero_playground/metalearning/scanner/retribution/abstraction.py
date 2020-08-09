# mother fucker.
# common result -> example -> abstraction contains None.
import random
from continuality import Faith
# about list unpacking?
# import re
# sex: None
# length: None
# what about None versus None? -> Unknown versus arbitrary? -> False
# not too fucking bad using the fucking mupdf tool.
def spot(a,b):
    # a and b are indecomposable elements.
    # function may change.
    a0=list(set([a,b]))
    if None in a0:
        return False
    elif len(a0)==2:
        return False
    else:
        return True
    # if None then no need to compare.

def linearCompare(a,b):
    # of the same length?
    return [spot(a[y],b[y]) for y in range(len(a))]

def linearAbstract(a,b):
    # a for only one example. b for result.
    return [a[y] if b[y] else None for y in range(len(a))]

def wrapper(a,b):
    return linearAbstract(a,linearCompare(a,b))

# shared abstraction?
def calcPlan(a,b):
    return list(Faith([x for y in [[wrapper(a0,b0) for a0 in a] for b0 in b] for x in y]).set())

def filterOut(a,b):
    return list(filter((lambda x: x.count(None)!=2),calcPlan(a,b)))

def linearFilter(a,b):
    # b is single and a is a list?
    return [x for x in a if linearCompare(x,b)==linearCompare(b,b)]
# get the most common abstraction.
# how can we develop something greater than linearAbstract?
# use it again?
# Trinity: Example, Abstraction, Result.