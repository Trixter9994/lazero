#from continuality import moveOn as mO
import continuality
# prime numbers.
def basicTrans(a,b):
    # b is frequency.
    # a is a filled matrix.
    # need default filling. currently False.
    # linear or multidimension?
    return [[a[int(r*b+l)] for r in range(int(len(a)/b))] for l in range(b)]

# better use general method to fix this.
# both structure and dimension.
# assume all are formal matricies.
# we shall never loop this back.

def extractor(a):
    if type(a)==type([]):
        return extractor(a[0])
    else:
        return a

def flatternII(a):
    if a!=[]:
        r0=(lambda x: 0 if type(x[0])!=type([]) else r0(x[0])+1)
        r=r0(a)
        if r!=0:
    # the only matter is the dimension.
            def r1(x):
                e=[]
                for b in x:
                    if b!=[]:
                        for a in b:
                            e.append(a)
                return e
            r2=(lambda x,y: r1(x) if y==1 else r2(r1(x),y-1))
            r3=r2(a,r)
            return r3
        else:
            return a
    else:
        # shall never trigger this.
        return a

def flattern(a):
    if type(a)==type([]):
        r0=(lambda x: 0 if type(x[0])!=type([]) else r0(x[0])+1)
        r=r0(a)
        if r!=0:
    # the only matter is the dimension.
    # test if it contains True?
            r1=(lambda x: [a for b in x for a in b])
            r2=(lambda x,y: r1(x) if y==1 else r2(r1(x),y-1))
            r3=r2(a,r)
            return ((True in r3) if r3[0] in [True, False] else True)
        else:
            return ((True in a) if a[0] in [True,False] else True)
    else:
        return a
#    l=len(r0(a))

def flatternIII(a):
    if type(a)==type([]):
        r0=(lambda x: 0 if type(x[0])!=type([]) else r0(x[0])+1)
        r=r0(a)
        if r!=0:
    # the only matter is the dimension.
    # test if it contains True?
            r1=(lambda x: [a for b in x for a in b])
            r2=(lambda x,y: r1(x) if y==1 else r2(r1(x),y-1))
            r3=r2(a,r)
            return ((True in r3) if type(r3[0]) == type(True) else True)
        else:
            return ((True in a) if type(a[0]) == type(True) else True)
    else:
        return a
#    l=len(r0(a))

def limiterII(a,b,c):
    # this sucks.
    # how about use testers?
    # to get local shits out. grouped by periods.
    # return all possible periods. select by density?
    l=len(a)
    f=[[],list(range(l))[2:]]
    if flattern(a):
        for l0 in range(l):
            if flattern(a[l0]):
                if len(f[0])<b and len(f[1])!=0:
                    m=0
                    lm=len(f[1])
                    for lv in range(lm if lm<c else c):
                        if len(f[0])<b and len(f[1])!=0:
                            l1=f[1][m]
                            # test for flattern list.
                            if l0+l1<len(a):
                                if a[l0]==a[l0+l1]:
                                    f[0].append(f[1].pop(m))
                                else:
                                    if m<len(f[1])-1:
                                        m+=1
                                    else:
                                        break
                            else:
                                break
                        else:
                            return f[0]
                # use set. use amount control. use presets 0 & 1?
                else:
                    return f[0]
    return f[0]

def limiter(a,b):
    # this sucks.
    # return all possible periods. select by density?
    l=len(a)
    f=[[],list(range(l))[2:]]
    if flattern(a):
        for l0 in range(l):
            if flattern(a[l0]):
                if len(f[0])<b and len(f[1])!=0:
                    m=0
                    for lv in range(len(f[1])):
                        if len(f[0])<b and len(f[1])!=0:
                            l1=f[1][m]
                            # test for flattern list.
                            if l0+l1<len(a):
                                if a[l0]==a[l0+l1]:
                                    f[0].append(f[1].pop(m))
                                else:
                                    if m<len(f[1])-1:
                                        m+=1
                                    else:
                                        break
                            else:
                                break
                        else:
                            return f[0]
                # use set. use amount control. use presets 0 & 1?
                else:
                    return f[0]
    return f[0]

def fillOut(a):
    # make exact copy of it.
    # default is False.
    # use r0 to define.
    if type(a)==type([]):
        a0=a[0]
        if type(a0)!=type([]):
            if type(a0)==type(False):
                return False
            elif type(a0)==type(0):
                return 0
            else:
                return a0
        else:
            r0=(lambda x: [len(x)] if type(x[0])!=type([]) else r0(x[0])+[len(x)])
            r1=(lambda y:[fillOut(extractor(a0)) for y0 in range(y[-1])] if len(y)==1 else [r1(y[:-1]) for y0 in range(y[-1])])
            return r1(r0(a0))
    else:
        return fillOut([a])
    # reversed dimension sequence. best for reconstruction.

def fillMatrix(a,b):
#    return a+[fillOut(a[-1]) for x in range(len(a)%b)]
    return a+[fillOut(a) for x in range((b-len(a)%b)%b)]

def nonVerbal(a,b):
    # shall we use a function wrapper?
    # avaliable for 1.
    return basicTrans(fillMatrix(a,b),b)

def wrapper(f,a):
    # direct frequency.
    # here is limiter.
    return [nonVerbal(f,x) for x in limiterII(f,a,10)]
# caution.

def fixMe(a,b,c):
    # oh shit.
    return [a,[continuality.moveOn(a,x+1,c) for x in range(b)]]
# notice that we have empty sets.
# following shall be possible periods? no it is about scope. so we have 3 lists as one.

def wrapperII(f,a):
    # this is bad. without copier for 2-d arrays.
    # now we have it.
#    a=wrapper(f)
# a^2
# this is obviously wrong.
# test for individual segments.
# bad idea to combine the fucking shit as one.
    return [[[fixMe(c,3,3) for c in b],[[fixMe(r0,3,3) for r0 in r] for r in wrapper(b,a)]] for b in wrapper(f,a)]
# detect subpattern.
# use density, standard deviation.
# better use some sample first.