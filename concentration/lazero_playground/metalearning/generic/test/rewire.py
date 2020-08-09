import backTrans
import continuality
import random
import numpy as np
# fucking grammar tree? huh? you bitch!
# to fix all shits.
# do we need randomness test for single units?
# be converted into different periodSegments.
# Haskell sucks.
# mental calculus.

# class identifier:
    # # for reconstruction.
    # def __init__(self,a,b,c):
    #     self.a = a
    #     self.b = b
    #     self.c = c
    # def period(self):
    #     return self.a
    # def scale(self):
    #     return self.b
    # def content(self):
    #     return self.c

class periodSegment:
    def __init__(self,a,b,c,d,e):
        self.a=a
        self.b=b
        self.c=c
        # on which level of abstraction.
        self.d=d
        self.e=e
        # method declarator.
        # not those shits that are reachable.
        # type examinator?
        # the function to detect repetition?
        # single local range.
        # do we need tolerance here?
        # no. normally no
    def period(self):
        return self.a
    def scale(self):
        return self.b
        # scan if there are same shits? remove conflicts.
    def content(self):
        return self.c
    def level(self):
        return self.d
    def comprehension(self):
        # it could be none.
        return self.e

# metaExtractor -> metaRanker

def typeChecker(a):
    return type(a)==type(periodSegment)
# matrix -> todo-list

def conflictSolver(a,b,c):
    if c == 0:
        r=(lambda x: x[1]-x[0])
        # if False delete the second one.
        if a == b:
            # random return one.
            return [1,0][int((random.random()*2)>1)]
        else:
            l, m = r(a), r(b)
            if l > m:
                return 1
            elif l == m:
                return int(not a[0]>b[0])
            else:
                return 0
    else:
        return conflictSolver(b,a,0)

def prelude(a,b):
    a0, b0= set(a), continuality.Faith([set([b0]) for b0 in b]).set()
    return sum([int(b1.issubset(a0)) for b1 in b0])>0

# has conflict or not.
# check if the target is None or something else?

def conflictDetector(a,b):
    if prelude(a,b):
        return True
    # use set operation? no!
    else:
        # these are no-conflict patterns.
        return not sum([sum([int(a0>b0) for a0 in a]) for b0 in b]) in [0,4]
    # must be pure.

def conflictDetectorII(a,b):
    # use set operation? no!
    if prelude(a,b):
        return 2
    else:
        x, v = sum([sum([int(a0>b0) for a0 in a]) for b0 in b]), [0,4]
        if x not in v:
            return 2
        else:
            return v.index(x)
        # must be pure.

def mixer(a):
    # a is length.
    m = a//2
    m1 = [[x for x in range(a-m)],[a-x-1 for x in range(m)]]
    m2 =[]
    for x in range(m):
        m2.append(m1[0][x])
        m2.append(m1[1][x])
    if 2*m == a:
        return m2
    else:
        return m2+[m1[0][-1]]

def examinator(a):
    x0, l=[[],[]], len(a)-1
    for x in range(l+1):
        if a[x]==2:
            if x<l:
                if a[x+1]==2:
                    x0[0].append(x)
            if x>0:
                if a[x-1]==2:
                    x0[1].append(x)
    return x0

def purifier(a,b):
    l, m = len(a), len(b)
    if abs(l-m)==(l+m):
        raise Exception
    # check the length? transform the matrix.
    if l>=m:
        r=[[None for l0 in range(l)] for m0 in range(m)]
        # this is the template matrix.
        for b0 in mixer(m):
            for a0 in range(l):
                f=r[b0][a0]
                if f==None:
                    a1, b1= a[a0], b[b0]
                    f0=conflictDetectorII(a1,b1)
                    r[b0][a0]=f0
                    if f0 ==0:
                        for r1 in range(m-1-b0):
                            if r[r1+1+b0][a0] == None:
                                r[r1+1+b0][a0]=0
                    elif f0 ==1:
                        for r1 in range(b0):
                            if r[b0-r1-1][a0] == None:
                                r[b0-r1-1][a0]=1
                    else:
                        pass
                        # deal with it later on.
            a0, a1=examinator(r[b0])
            for a2 in a0:
                for r1 in range(m-1-b0):
                    if r[r1+1+b0][a2] == None:
                        r[r1+1+b0][a2]=0
            for a2 in a1:
                for r1 in range(b0):
                    if r[b0-r1-1][a2] == None:
                        r[b0-r1-1][a2]=1
        return r
    else:
        # print(a,b)
        return np.array(purifier(b,a)).transpose(1,0).tolist()
    # basic linear rearranger.
    # count for occurance?
    # test if is a subset of current object, solve for conflicts.

def arranger(a):
    l=len(a)
    return [x for y in [[[a[a0],a[a1+a0+1]] for a1 in range(l-a0-1)] for a0 in range(l)] for x in y]

def ranker(a):
    return arranger(list(map((lambda x:x[0]),list(sorted([[a0,(lambda x: sum([y[1]-y[0] for y in x])/(1+len(x)))(a[a0])] for a0 in range(len(a))],key=(lambda x: -x[1]))))))

def extractor(a):
    # return candidates?
    return [x for y in [[[x,y] for x in range(len(a[0])) if a[y][x]==2] for y in range(len(a))] for x in y]

def popStar(a):
    return [a[x]-x for x in range(len(a))]

def dualProcess(a,b):
    r,s = [[],[]], 0
    for b0 in b:
        r[b0].append(a[s][b0])
        s+=1
    return list(map((lambda x:popStar(list(sorted(list(set(x)))))),r))
    # need rearrangement.

def withdraw(a,n):
    # this is for a single period portion.
    s=(lambda x,y,z,a,b: [x[y][a],x[z][b]])
    # return nothing? really?
    processPlan=ranker(a)
    # do not fuck with nothing!
    for p in processPlan:
        try:
            f, g = p
            p0=extractor(purifier(a[f],a[g]))
            # modify those things.
            # get execution list.
            p1=[conflictSolver(*s(a,f,g,*p2),n) for p2 in p0]
            p2, p3 = dualProcess(p0,p1)
            for p4 in p2:
                a[f].pop(p4)
            for p5 in p3:
                a[g].pop(p5)
        except:
            pass
        # get the results out.
        # simply pop it up.
    # inside one same scope we have multiple identifiers.
    # rank those shits with ranker.
    # generate a custom process plan for it.
    # safety twitch.
    return a

def form(a,f,i):
    # this is for another calculation.
    return list(map((lambda x: x*f+i),a))

def unify(a,f,n):
    return [x for y in withdraw([list(map((lambda x: form(x,f,i)),[x for y in withdraw(a[i],n) for x in y])) for i in range(len(a))],n) for x in y]
    # to get the frequency?
    # this sucks.
    # sounds like a bunch of pop and bangs.

def unity(a,f,n):
    # matrix transformation
    # now, time for reconstruction.
    # may use withdraw.
    return withdraw([unify([a[y][x] for y in range(len(a))],f,n) for x in range(5)],n)

def transverse(a,n):
    # now what?
    return [[a0[0] for a0 in a], *list(map((lambda x: withdraw(x,n)),np.array([a0[1] for a0 in a]).transpose(1,0).tolist()))]

def universe(a,n):
    t=transverse(a,n)
    # print(t)
    return [[t[0][r],[t[s+1][r] for s in range(5)]] for r in range(len(t[0]))]

def popChecker(a,b):
    return len([x for x in a if x != b])>0

def integrityII(a,b,c,d,e):
    # what is your dimension? 3?
    # for 5 kinds of scale.
    # scale -> repetition matrix -> exact location
    return list(filter((lambda x:x!=[]),list(filter((lambda y: list(filter((lambda z: z[1]-z[0]>d),y))), continuality.moveOnII(a,b,c,e)))))

def integrity(a,b):
    # b for periods.
    # test if fits?
    # do you think that this fuck is gonna work?
    # can we ever find hidden pattern here?
    # it is not equivalent to periodic test.
    # it is only a subset of it.
    return list(filter((lambda x:x!=[]),list(filter((lambda y: list(filter((lambda z: z[1]-z[0]>0),y))), continuality.moveOn(a,b,0)))))
# test if on one fucking dimension it fits the need?
    # test this shit first?
    # no fucking tolerance?
    # it could be nothing in it.

def firstOrderII(a,b,c,d):
    # b -> rangeLenthFilter
    # c -> tolerance
    # 4d. 4-1=3.
    return [integrityII(a,b0+1,c,b,d) for b0 in range(5)]

def firstOrder(a):
    # select possible periods?
    # you require 5 dimensions.
    return [integrity(a,b+1) for b in range(5)]
    # make sure the length of this list is 5.
    # or simply keep collecting.
    # give out the dimension first.
    # five levels of abstraction?
    # check and rearrange the whole list.
    # unionfy the marks.
# now it is the time to collect those shits using existing knowledge?
# adjacent periods! how the fuck can I collect those shits?
# periods-tolerance
# frequency-key-element

def naiveFunc(a):
    return a

def soapFunc(a):
    return [a.period(),a.scope(),a.level()]

def checkMate(a):
    if typeChecker(a):
        return soapFunc(a)
    else:
        # to never use that shit!
        return a

def frequencyTest(a,b,s):
    # first extract all possible frequencies.
    # need to pass the fucking test? yes.
    # do not use the limiter?
    # b for frequency number limiter.
    # fixed frequency?
    # the method to return period, scale.
    c, candidates = (lambda x: backTrans.nonVerbal(a,x)), list(range(len(a)))[1:]
    d, r2 = 0, []
    for r in candidates:
        r0=c(r)
        # test this shit first.
        # the function is integrated.
        r1=list(map((lambda x:firstOrderII(x,0,0,checkMate)),r0))
        # no fucking tolerance please?
        # here is the filter.
        if popChecker(r1,[[],[],[],[],[]]) and d<b:
            d+=1
            # r1 could be 5d. 5-2=3.
            # r2 could be 2d.
            # not all are such kind of shit?
            # we need a high level frequency checker.
            # firstOrder needs adjustment.
            # avoid excessive calculation.
            # here we have different shits to deal with! multiple scopes! must be separated.
            r2.append([r,unity(r1,r,s)])
        else:
            pass
        # detect frequency avaliability.
        # [] -> [[],[],[],[],[]]
        # return all avaliable shits.
    # starting from frequency 1.
    # if it has that kind of shit then we will move on.
    return r2
    # use the output.
    # time to end this shit.
    # trying to group this shit.
    # minimum frequency is prior than any other shits.
    # have tolerance -> have no tolerance.

def metaExtractor(a):
    # scale starts from 1.
    f=(lambda x: [y for z in x for y in z])
    return f(f([[[[[a0[0],a1+1],a2] for a2 in a0[1][a1]] for a1 in range(5)] for a0 in a]))
    # need metaRanker here.
    # problem is clearly at the frequency level.

def popCheckerII(a,b):
    # 0 for scope oriented.
    l,f,x0= len(a), (lambda x,y: (x[0]!=y[0] and x[1]!=y[1])), 0
    for x in range(l):
        if x0<len(a)-1:
            m,n=a[x0],a[x0+1]
            # print(m,n)
            if f(m[0],n[0]):
                # no fucking conflict?
                # print("there")
                v,w=m[1],n[1]
                if conflictDetector(v,w):
                    # print("here")
                    # no fucking conflict?
                    if conflictSolver(v,w,b):
                        a.pop(x0+1)
                        # which one to pop?
                        # prefer local frequencies?
                        # 0 for global frequencies.
                    else:
                        a.pop(x0)
                else:
                    x0+=1
            else:
                x0+=1
        else:
            break
    return a

def popCheckerIII(a,b):
    c=popCheckerII(a,b)
    d=popCheckerII(c,b)
    # internal error.
    if c == d:
        return c
    else:
        return popCheckerII(d,b)

def metaRanker(a,b):
    a0, a2=popCheckerIII(list(sorted(metaExtractor(a),key=(lambda x: x[1][0]))),b), 0
    # small things first?
    # rearrange that a0! hold on!
    # print(a0)
    for a1 in range(len(a0)):
        e, f = a0[a1][1]
        # time that one needs to pop from the spot.
        # simply replace the shit first?
        h=f-e
        a0[a1][1]=[e-a2,h]
        a2+=h
    # print(a0)
    return a0

# pop -> replace
# collect afterwards.
def kingPoper(a,b,c,d):
    # fuck?
    for b0 in b:
        e,f,g,h,i=*b0[0],*b0[1],[]
        try:
            for b1 in range(h):
                try:
                    i.append(a.pop(g))
                except:
                    break
            # print("here")
            # does not have limitations?
            try:
                i.append(a[g])
            except:
                pass
        except:
            pass
        try:
            try:
                a[g]=periodSegment(e,f,i,c,d)
            except:
                a[g-1]=periodSegment(e,f,i,c,d)
        except:
            a[g-2]=periodSegment(e,f,i,c,d)
    return a

# still prefer frequency than scope? they are all the same.

def wrapUpOnce(a,b,c,d):
    # c is the level of abstraction.
    backUp=[a0 for a0 in a]
    # is it the same?
    # here is the error.
    f0=frequencyTest(a,b,d)
    # for each item inside the func do that fuck.
    # print(f0)
    u=universe(f0,d)
    # duplicate checker inside the metaRanker.
    # this universe is not stable enough.
    # print(u)
    f=metaRanker(u,d)
    # use another thing. different period, different treatments.
    # print(f)
    # b is number of frequencies.
    # must declare the type.
    # print(f)
    if f!=[]:
        k=kingPoper(backUp,f,c,checkMate)
        # here is the error.
        # print(k)
        return k
        # what is this signal?
    return False

def metaWrapper(a,b,c,e,d=[]):
    # c is for number of abstraction.
    if c==0:
        return d
    else:
        try:
            # run till the last error.
            backUp=[a0 for a0 in a]
            w=wrapUpOnce(a,b,len(d),e)
            # we now have multi-frequency error.
            if w:
                return metaWrapper(w,b,c-1,e,d+[w])
            else:
                return d
        except:
            return d

# it could become much better I thought.
# inspired by that pricky pop function
# better have backup before the action.
def metaWrapperII(a,b,c):
    # fuck me!
    return metaWrapper(a,b,1000000000000000000000,c)
        # use this universe to generate a workList.
        # check if it works?
        # return universe()
        # assume all are done?
        # across different frequencies.
        # do what?
        # multiple frequency determination?
        # better without tolerance?
        # use the wrapper? how?
        # create the object and insert it into the fucking list!
        # first thing first.
        # use a purification function.
    # make sure there is result.
    # b is abstractionLevelMarker.
# always use the first one? use first frequencyTestResult?