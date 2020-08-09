def basicTrans(a,b):
    # b is frequency.
    # a is a filled matrix.
    # need default filling. currently False.
    # linear or multidimension?
    return [[a[int(r*b+l)] for r in range(int(len(a)/b))]for l in range(b)]

# better use general method to fix this.
# both structure and dimension.
# assume all are formal matricies.

def fillOut(a):
    # make exact copy of it.
    # default is False.
    # use r0 to define.
    a0=a[0]
    if type(a0)!=type([]):
        return False
    else:
        r0=(lambda x: [len(x)] if type(x[0])!=type([]) else r0(x[0])+[len(x)])
        r1=(lambda y:[False for y0 in range(y[-1])] if len(y)==1 else [r1(y[:-1]) for y0 in range(y[-1])])
        return r1(r0(a0))
    # reversed dimension sequence. best for reconstruction.

def fillMatrix(a,b):
#    return a+[fillOut(a[-1]) for x in range(len(a)%b)]
    return a+[fillOut(a) for x in range((b-len(a)%b)%b)]

def nonVerbal(a,b):
    # shall we use a function wrapper?
    return basicTrans(fillMatrix(a,b),b)

def wrapper(f):
    return [nonVerbal(f,x+2) for x in range(len(f)-2)]

def wrapperII(f):
    # this is bad. without copier for 2-d arrays.
    # now we have it.
#    a=wrapper(f)
    return [[b]+wrapper(b) for b in wrapper(f)]
# detect subpattern.
# use density, standard deviation.
# better use some sample first.