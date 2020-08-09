def basicTrans(a,b):
    # b is frequency.
    # a is a filled matrix.
    # need default filling. currently False.
    # linear or multidimension?
    return [[a[int(r*b+l)] for r in range(int(len(a)/b))] for l in range(b)]

# better use general method to fix this.
# both structure and dimension.
# assume all are formal matricies.

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
            r1=(lambda x: [a for b in x for a in b])
            r2=(lambda x,y: r1(x) if y==1 else r2(r1(x),y-1))
            r3=r2(a,r)
            return (True in r3)
        else:
            return (True in a)
    else:
        return a
#    l=len(r0(a))

def limiter(a,b):
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

def wrapper(f,a):
    # direct frequency.
    return [nonVerbal(f,x) for x in limiter(f,a)]
# caution.

def wrapperII(f,a):
    # this is bad. without copier for 2-d arrays.
    # now we have it.
#    a=wrapper(f)
# a^2
    return [[b]+wrapper(b,a) for b in wrapper(f,a)]
# detect subpattern.
# use density, standard deviation.
# better use some sample first.
