from getFromPickleR import returnListF
import random # this is fuck.
# mother fucker we have a recoverable data format?
# do we need to compare between documents?
# yes.
# the fucking shit! we are eating shit right now!
# now the visual elements are ready. from the traditional contextual view.
import youAreMine
import matrixPro
import niche
import re
import lunaticKMeans
import statistics
import numpy as np
import readLikeHuman
def vary(a,b):
    if a>=b:
        return 1-b/a
    else:
        return vary(b,a)

def intTest(a):
    try:
        b=int(a)
        return True
    except:
        return False

def hexTest(a):
    try:
        b=int("0x"+a,0)
        return True
    except:
        return False

def hasNumber(a):
    r=list(map((lambda x: str(x)),list(range(10))))
    for a0 in a:
        if a0 in r:
            return True
            # break
    return False

def hasHex(a):
    r=list(map((lambda x: str(x)),list(range(10))))+[*"abcdefABCDEF"]
    for a0 in a:
        if a0 in r:
            return True
            # break
    return False

def numberIdentity(a):
    b,c,d="0123456789","abcdef","ABCDEF"
    if a in b:
        return 0
    elif a in c:
        return 1
    elif a in d:
        return 2
    else:
        return 3

def nonsense(a,b,c):
    # c is the sum of the length of all possible compliment sets.
    # a is bigger than b?
    if len(a)>=len(b):
        if type(a[0])!=int:
            l=(lambda y: list(map((lambda x: int("0x"+x,0)),y)))
            a0,b0=l(a),l(b)
        else:
            a0,b0=a,b
        m=False
        for b1 in b0:
            for c0 in range(1,1+c):
                if m==True:
                    break
                for k in [-1,1]:
                    b2=b1+c0*k
                    if b2 in a0:
                        m=True
                        break
        return m
    else:
        return nonsense(b,a,c)

def numberPurity(a):
    # by continuality, by case, by many other shits?
    return [numberIdentity(b) for b in a] # check if there is anything inside?
    # check the purity of each fucking number.
    # nothing is like deadbeef.
    # check for continuality?

def devil(a):
    b=int(len(a[0])*random.random())
    return [a[0].pop(b),a[1].pop(b)]

def rollOver(a):
    b0=len(a[0])
    return [[a[0][b],a[1][b]] for b in range(b0)]

def backUp(a):
    # this way it is deep enough.
    return [[x0 for x0 in x] for x in a]

def tripleTest(a,b):
    r=(lambda x: list(map((lambda y: y[1]),x[1])))
    r0=[len(a[0])==len(b[0]),len(a[1])==len(b[1]),r(a)==r(b)]
    # print(r0)
    return r0

def doubleTest(a,b):
    r=(lambda x: list(map((lambda y: y[1]),x[1])))
    r0=[len(a[1])==len(b[1]),r(a)==r(b)]
    print(r0)
    # check relative relationships?
    return r0

def tyson(a):
    b,c=devil(a), devil(a)
    # print(b[0],c[0])
    return [b,tripleTest(b,c)]

def MC(a):
    return max(set(a),key=a.count)

def killSquad(a):
    f=None
    while True:
        d=tyson(a)
        # print(d)
        if d[1]==[True for x in range(3)]:
            f=d[0]
            break
    return f

def checkShared(a,b):
    s=[[],[],[]]
    for a0 in range(len(a[0])):
        if a[0][a0] in b[0]:
            # if doubleTest([a[0][a0],a[1][a0]],[b[0][a0],b[1][a0]])==[True for x in range(2)]:
            s[0].append(a[0][a0])
            s[1].append(a[1][a0])
            s[2].append(b[1][a0])
    return s

def batchFilter(a,b):
    # b as a sample.
    x=list(filter((lambda y: tripleTest(b,y)==[True for z in range(3)]),rollOver(a)))
    return x

def formFilter(a):
    a0=list(filter((lambda x: x[0]),a))
    print(a0)
    # possibility filter is necessary. it needs to be applied.
# check only for relationships?
# type detector?

def hoax(y):
    return statistics.mean(list(map((lambda x: int("0x"+x,0)),y)))

def typeFilter(a,b):
    return list(filter((lambda x:b(x[0])),a))

def retrieveIndex(a,b):
    return [index for index, item in enumerate(a) if b(item)]
# mean sum? set theory? shape recognition? later on.
# print(r0[0])
# c=checkShared(r,r0)
# print(c[0]
def getDomain(r):
    # print(r)
    r1=r[0]
    # print(r1)
    r2=retrieveIndex(r1,hexTest)
    # print(r2)
    index=[int("0x"+r1[x],0) for x in r2]
    # print(index)
    k0=lunaticKMeans.mainShit(index)
    # print(k0)
    # check indices.
    # get the most common shit?
    k2=MC(k0)
    # print(k0)
    k1=[r2[m] for m in range(len(r2)) if k0[m]==k2]
    # shape detector? double center?
    v=[r[0][y] for y in k1]
    x0=[r[1][y] for y in k1]
    x1=list(map((lambda x: len(x)),x0))
    x2=list(set(x1))
    x3=[[v[y] for y in range(len(x0)) if x1[y]==x2[z]] for z in range(len(x2))]
    # are they next to each other?
    # print(x3)
    x4=list(reversed(list(sorted(x3,key=(lambda x: len(x))))))
    # determine by rule of filling.
    # print(x4)
    x5=list(map((lambda x:len(x)),x4))
    x6=sum(x5[1:])
    x7=[nonsense(x4[0],x4[z],x6) for z in range(1,len(x4))]
    x8=[True]+x7
    x9=[x4[y] for y in range(len(x8)) if x8[y]]
    # fuck it...
    # print(x9)
    x10=x9[1:]
    # appear in tne same line or in the same column?
    # print(x10)
    sD=[]
    for y in x10:
        sE=[[],[]] # common things?
        for z in y:
            kv=r1.index(z)
            kz=np.array(r[1][kv]).transpose(1,0).tolist()
            sE[0]=sE[0]+kz[0]
            sE[1]=sE[1]+kz[1]
            # print(kv,kz)
        sV=(lambda y: list(filter((lambda x: y.count(x)>1),y)))
        sZ=list(map((lambda x:sV(x)),sE))
        sD+=sZ[0]
    sD=list(set(sD))
    return sD
    # print(sE,sZ)

def shudder(a,b):
    a0=(lambda x: re.findall(r'\w+',x))
    a1,b0=a0(a),a0(b)
    for b1 in a1:
        if b1 in b0:
            return True
    return False

def chaos(a,b,c):
    return [[c(a0,b0) for a0 in a] for b0 in b]

def stupid(a):
    s=[]
    for a0 in range(len(a)):
        for b0 in range(len(a[0])):
            if a[a0][b0]:
                s.append([a0,b0])
    return s

def demo():
    r,r0=returnListF(0),returnListF(1)
    s=getDomain(r)
    s0=getDomain(r0)
    # get the fuck.
    # print(s,s0)
    e,e0=readLikeHuman.Meta(0),readLikeHuman.Meta(1)
    e1=e.getCustomLines(s,True)
    # e3=len(e0.content)
    # print(e3)
    e2=e0.getCustomLines(s0,True)
    c0=chaos(e1,e2,shudder)
    s0=stupid(c0)
    # print(s0)
    f0=[[e1[y[0]],e2[y[1]]] for y in s0]
    return f0
    # share the same lineIndex.

def bitch(a,b):

    if len(a)<len(b):
        return False
    else:
        b0=niche.Method0(a.lower(),b.lower())
        # print(b0)
        b1=np.array(matrixPro.Linkage(b0)).transpose(1,0).tolist()
        for b2 in b1:
            if sum(b2)/len(b2)==1:
                return True
        return False

# simply from the original shit.
def getRange(x):
    r=returnListF(x)
    # use the matrix?
    r0=r[0]
    rx="range"
    # print(r[0])
    f,f0,l,l0=0,0,len(r0),[]
    for i in range(l):
        y=r0[i]
        # print(y)
        if bitch(y,rx):
            f=i
            break
    # print(r0[f])
    # fucker is here. fuck you. every fucking single fucking one. fuck you fucking asshole.
    for i in range(f+1,l):
        y=r0[i]
        if f0<2:
            if hexTest(y):
                l0.append(y)
                f0+=1
        else:
            break
    return l0
# IsHex -> InRange
# The order? No Error Order. Tweak it around? Use it as a whole?
# let the computer know numbers first.
# no fucking need for pure textual analyzation. in this way you can get fucked.
# in this sick format no one can fucking tell where it is coming from.
def inRange(a,b):
    if hexTest(a):
        a0=(lambda x: int('0x'+x,0))
        a1,b0=a0(a),list(map(a0,b))
        if a1>=b0[0] and a1<=b0[1]:
            return True
        return False
    return False

def hasInfo(a,b):
    if len(a)<len(b)+2:
        return False
    else:
        return True

def bizarre(a,x):
    return hexTest(re.findall(r'\w+',a)[0])

r=returnListF(0)
r0,r2=r[1],readLikeHuman.Meta(0).content
g=getRange(0)
print(g)
gx=(lambda x:int("0x"+x[1],0)-int("0x"+x[0],0)+1)
# get unified rule?
# abstract model?
f=[r0[i] for i in range(len(r0)) if inRange(r[0][i],g)]
y0=youAreMine.getFucked(f) # randomly select those numbers.
# get index only? Make the function?
# random is a good thing.
gh=(lambda x: list(map((lambda y:y[0]),x)))
fc=(lambda x: list(filter((lambda y:len(re.findall("\w*",y))>3),x)))
g0=[]
for z in range(len(y0[0])):
    y1=gh(y0[0][z])
    # print(y1,y2)
    g0+=fc([r2[fx] for fx in y1])
g1=list(map((lambda x:re.findall(r'\w*',x)),g0))
# select by frequency?
# filter out those useless words.
# print(g1)
g2=youAreMine.simpleFlat(g1)
g3=list(reversed(sorted(list(set(g2)),key=g2.count)))
g4=list(filter((lambda x: len(x)>1),g3[0:10]))
g5=youAreMine.indexGetter(r2,g4)
g6=g5[0]
g7=youAreMine.organize(g6,(lambda x:bizarre(x,g4[0])))
# get from existing shit.
# avoid the return and many more shits.
g8=list(map((lambda x:x[1]),g7[0]))
g9=youAreMine.generalFuck(g8,g4[0])
g10=list(set(list(map((lambda x:x[0]),g9))))
# the correct shit? may have reserved shits?
# a large number of shit just went missing!
print(g9,len(g10),gx(g))
# use beautifulsoup to solve this motherfucking problem.
# you want the unicode table, it is just fine. but to tell you the truth, it does not worth that much effort.
# you just put things together, the depth can be talked later on.
# it is not about how fucking smart that you can accomplish some fucking foolish bullshit. It is about the fucking mechanism, the fucking integrity as a whole.
# fucking put it altogether! don't you have to collect a bunch of building blocks before you fucking start to build shits?
# you want to do fun stuff over image parsing? that is wrong.
# warning multiple shit can happen. in other space may encounter problems.
# pussy.
# print(g7)
# filter out useless pricks.
# print(g6)
# this is a chain. once have the first thing, the next thing is ingored.
# calculate the visibility of each fucking characher?
    # print(f0)
    # only one HEX -> more than HEX.
# get the pattern is the first priority.
# the prediction chain model.
# the binary classification?
# randomly select few shits.
# common pattern spotter?
# print(f)
# print(getRage(0))
# print(readLikeHuman.Meta(0).name)
# only has the beginning.
# you could get these shit from the filename?
# identical connection versus not identical connection?
# print(f0)
# print(c0)
# print(e1)
# print(e2)
# have same words?
# so what is the word?
# internal processor?
# fuck you!
# x8=[x4[0]]+[x4[y+1] for y in range(len(x4)-1) if x7[y]]
# print(x8)
# use the nextTo method?
# random and uncertainty.
# get the shit?
# check the structure, determine the similarity via shape.
# check possible ranges. are they next to each other?
# only read first few lines?
# is this learned stuff or pricky shits?
# check the shared elements.
# check the format?
# I want hex only? I only want hex within the range.
# ain't go your way cunts.
# k=killSquad(r)
# print(k)
# b=batchFilter(r,k)
# # print(b[0][0])
# c=typeFilter(b,hexTest)
# print(c)
# check those things first? record their indexes.
# numberRecognition?
# just apply it as filters. do it now.
# select those next to range. do not force me to do the stuff?
# we can lead it to do something alike.
# first check the fuck. then detect alike shits.
# r0=backUp(r)
# print(len(r[0])==len(r[1]))
# print(len(r0[0]))
# d=devil(r)
# learn that shit!
# # make things unretrievable? how? one fucking way out?
# print(d)
# print(len(r0[0]))
# random select?
# # exactly the thing.
# randomly select things?
# fuck me? regex with other shits?
# group these metaCharacters.
# mixed with period analysis? oh fucking come on. we are gonna die if you fucking insist on that shit.
# shape alike? position alike?
