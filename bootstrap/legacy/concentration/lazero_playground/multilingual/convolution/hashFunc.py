import numpy as np
import itertools
import operator
def testFunc(a):
#    a0=[False,False,False,False]
    # code struct number character
    if a in '|^%$#@!+=:;{}<>/\\`':
        return 0
    elif a in '[]()&-+*,?.\'"~ ':
        return 1
    elif a in '0123456789':
        return 2
    else:
        return 3
    # know nothing about the char yet.

def fuckYou(a):
    c=[0,0,0,0]
    b=[testFunc(r) for r in a]
    for r in range(4):
        if (1+len(b))/(0.1+b.count(r))<(5-(0.1+r)/2) or ((1+len(b))/(b.count(r)+0.1)<(7-(0.1+r)/2) and (len(b)+0.1)>(12-(r+0.1)/2)):
            c[r]+=1
    return c

def least_common(lst):
    return min(set(lst), key=lst.count)

def most_common(L):
  # get an iterable of (item, iterable) pairs
  SL = sorted((x, i) for i, x in enumerate(L))
  # print 'SL:', SL
  groups = itertools.groupby(SL, key=operator.itemgetter(0))
  # auxiliary function to get "quality" for an item
  def _auxfun(g):
    item, iterable = g
    count = 0
    min_index = len(L)
    for _, where in iterable:
      count += 1
      min_index = min(min_index, where)
    # print 'item %r, count %r, minind %r' % (item, count, min_index)
    return count, -min_index
  # pick the highest-count/earliest item
  return max(groups, key=_auxfun)[0]

def hashYou(a):
    # i decide to make words into numerical shits.
    # if not doing so my brain will get fucked.
    # first is length.
    # next is alphabet average.
    # third is standard deviation.
    b=len(a)
    e=[ord(k) for k in a]
    c=sum(e)/b
    d=np.std(e)
    # check for type!
    f=list(set(e))
    h=len(f)
    g=sum(f)/len(e)
    i=np.std(f)
    j,k=most_common(e),least_common(e)
    l,m=e[0],e[-1]
    return b,c,d,h,g,i,j,k,l,m
