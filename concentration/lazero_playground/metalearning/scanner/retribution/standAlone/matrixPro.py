import numpy

def Linkage(a):
    b,c=len(a),len(a[0])
    if type(a)==type([]):
    # print(b,c)
    # be the first. extract identity matrix and its length.
    # repetation can be visualized as multiple identity matrices mixed together.
    # add tolerance for omition
    # you can switch the major direction.
    # -l, l-1 avaliable.
        return [a[f][f%c:c]+a[f][-c:-c+f%c] for f in range(b)]
    else:
        return Linkage(a.tolist())

def ReverseLink(a):
    b,c=len(a),len(a[0])
    return [a[f][(-f)%c:c]+a[f][-c:-c+(-f)%c] for f in range(b)]

def Maxima(a):
    b=max([sum([int(a[c][d]) for c in range(len(a))]) for d in range(len(a[0]))])
    i=(len(a)+0.1)/(b+0.1)
    if i<1.2 and i>0.8:
        return True
    else:
        return False
    # really? this will skim many nice patterns.
    # better use an exponental approach.
    # from one to two.
    # (1+1/n)^n -> e

def prep(a,b):
    b0=[Linkage,ReverseLink][b]
    return numpy.array(b0(a.tolist() if type(a)!=type([]) else a)).transpose((1,0))

def generalize(a,b):
    # this is for identical comparation
    a0=prep(a,b)
    l=len(a0)
    # skip trivial first column.
    return [a0[r+1] for r in range(int(l/2+1 if l%2==0 else (l+1)/2)-1)]
# index is e, e+a=c, a is the beginning point
