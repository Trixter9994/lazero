from bs4 import BeautifulSoup
import numpy as np
# 0-316. this is the range.
from f0 import getCode, getElimination
import niche
import matrixPro
import re

def chainedGroup(a,b):
    r=[[],[]]
    for x in a:
        r[int(not b(x))].append(x)
    if len(r[0])>0 and len(r[1])>0:
        return r[0]+[r[1]]
    else:
        return a

def splitMe(a,b):
    r,r0=[],[]
    for a0 in a:
        if b(a0):
            if r0!=[]:
                r.append(r0)
                r0=[]
            r.append(a0)
        else:
            r0.append(a0)
    if r0!=[]:
        r.append(r0)
    return r

def groupMe(a,b):
    # this is linear version of the game. -> recursive grouping -> recursive sorting?
    # b is the lambda function which can determine each fucking shit.
    r=[[],[]]
    for x in a:
        r[int(not b(x))].append(x)
    if len(r[0])>0 and len(r[1])>0:
        return r
    else:
        return a

def remedyGroup(a,b):
    r,r0=[[],[]],False
    for x in a:
        if not r0:
            r0=b(x)
        r[int(r0)].append(x)
    return r

# shall we simplify this?

def checkNoSub(a):
    for x in a:
        if type(x)==list:
            return False
    return True

def maxGroup(a,b):
    if type(a)!=list:
        return a
    elif checkNoSub(a):
        return groupMe(a,b)
    else:
        return [maxGroup(x,b) for x in a]

def maxSplit(a,b):
    if type(a)!=list:
        return a
    elif checkNoSub(a):
        return splitMe(a,b)
    else:
        return [maxSplit(x,b) for x in a]

def maxChain(a,b):
    if type(a)!=list:
        return a
    elif checkNoSub(a):
        return chainedGroup(a,b)
    else:
        return [maxChain(x,b) for x in a]

def sortMe(a,b):
    return list(sorted(a,key=b))

def maxSort(a,b):
    if type(a)!=list:
        return a
    elif checkNoSub(a):
        return sortMe(a,b)
    else:
        return [maxSort(x,b) for x in a]

def inRange(a,b):
    if hexTest(a):
        a0=(lambda x: int('0x'+x,0))
        a1,b0=a0(a),list(map(a0,b))
        if a1>=b0[0] and a1<=b0[1]:
            return True
        return False
    return False

def hexTest(a):
    try:
        b=int("0x"+a,0)
        return True
    except:
        return False

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

def getRange(x_v):
    # r=x
    # use the matrix?
    r0=list(filter((lambda x: len(x)>1),re.findall(r'\w*',x_v)))
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

def styleMap(x):
    return {a[0]:a[1] for a in x}

def chartDetect(a):
    for g4 in a:
    # print(styleMap(list(map((lambda x: x.split(":")),list(filter((lambda x: len(x)>0),g4.attrs["style"].split(";")))))))
        s0=g4('span')
        for s1 in s0:
            sn=float(styleMap(list(map((lambda x: x.split(":")),list(filter((lambda x: len(x)>0),s1.attrs["style"].split(";"))))))["font-size"][:-2])
            if sn>15:
                return True
    return False

def checkBold(g4):
    p=styleMap(list(map((lambda x: x.split(":")),list(filter((lambda x: len(x)>0),g4.attrs["style"].split(";"))))))
    s=g4('b')
    if len(s)>0:
        s0=s[0]('span')
        for s1 in s0:
            sn=float(styleMap(list(map((lambda x: x.split(":")),list(filter((lambda x: len(x)>0),s1.attrs["style"].split(";"))))))["font-size"][:-2])
            if sn<10:
                return True
    return False

def checkAnother(g4):
    try:
        s0=g4('span')
        for s1 in s0:
            sn=styleMap(list(map((lambda x: x.split(":")),list(filter((lambda x: len(x)>0),s1.attrs["style"].split(";"))))))
            if sn['font-family']=="ArialNarrow,sans-serif" and sn['font-size']=="9pt":
                return True
        return False
    except:
        return False

def getBold(a):
    v,v1=[],[]
    for g4 in a:
        p=styleMap(list(map((lambda x: x.split(":")),list(filter((lambda x: len(x)>0),g4.attrs["style"].split(";"))))))
        s=g4('b')
        if len(s)>0:
            s0=s[0]('span')
            for s1 in s0:
                sn=float(styleMap(list(map((lambda x: x.split(":")),list(filter((lambda x: len(x)>0),s1.attrs["style"].split(";"))))))["font-size"][:-2])
                if sn<10:
                    v.append([p,sn])
        else:
            s0=g4('span')
            for s1 in s0:
                sn=styleMap(list(map((lambda x: x.split(":")),list(filter((lambda x: len(x)>0),s1.attrs["style"].split(";"))))))
                if sn['font-family']=="ArialNarrow,sans-serif" and sn['font-size']=="9pt":
                    v1.append([p,sn])
                #font-family:ArialNarrow,sans-serif;font-size:9pt;
    return v,v1

def inNewRange(a,b):
    return (a>=b[0] and a<=b[1])

def hotFix(a):
    return int(5*(a//5))

def getStyleCode(a,b):
    f=[["top","left","font-size"],["margin","padding"]]
    f0=[x for y in f for x in y]
    a0=styleMap(list(map((lambda x: x.split(":")),list(filter((lambda x: len(x)>0),a.attrs["style"].split(";"))))))[b]
    if b in f0:
        if b in f[0]:
            return hotFix(float(a0[:-2]))
        else:
            return hotFix(float(a0))
    else:
        return a0

def getLine(g4):
    if not chartDetect(g4):
        g8=list(g4)
        g5=list(sorted(list(set(list(map((lambda y:int(styleMap(list(map((lambda x: x.split(":")),list(filter((lambda x: len(x)>0),y.attrs["style"].split(";"))))))["top"][:-2])),g4))))))
        # print(g5)
        g6=[g5[0]+1,g5[-1]-1]
        g7=groupMe(g8,(lambda x: inNewRange(getStyleCode(x,"top"),g6)))
        # print(g7)
        # print(g7[1])
        g9=g7[0]
        g10=getBold(g9)
        g11=list(sorted(list(set(list(map((lambda x: int(x[0]["left"][:-2])),g10[1]))))))
        if len(g11)==2:
            g13,g14=g11[1]-1,(g11[1]-g11[0]+10)
            g12=maxSort(groupMe(g9,(lambda x: getStyleCode(x,"left")<g13)),(lambda x: g14*getStyleCode(x,"top")+getStyleCode(x,"left")))
            # two pages.
            # if do it at once, then we will have no issue.
            # let the computer create its code later.
            return g12[0]+g12[1]
        else:
            return maxSort(g9,(lambda x:250*getStyleCode(x,"top")+getStyleCode(x,"left")))
    else:
        g8=list(g4)
        g5=list(sorted(list(set(list(map((lambda y:int(styleMap(list(map((lambda x: x.split(":")),list(filter((lambda x: len(x)>0),y.attrs["style"].split(";"))))))["top"][:-2])),g4))))))
        # print(g5)
        g6=[g5[0]+1,g5[-1]-1]
        g7=groupMe(g8,(lambda x: inNewRange(getStyleCode(x,"top"),g6)))
        # print(g7)
        # print(g7[1])
        g9=g7[0]
        g10=getBold(g9)
        g11=list(sorted(list(set(list(map((lambda x: int(x[0]["left"][:-2])),g10[1]))))))
        if len(g11)==1:
            g13,g14=g11[0]-1,250
            g12=maxSort(groupMe(g9,(lambda x: getStyleCode(x,"left")<g13)),(lambda x: g14*getStyleCode(x,"top")+getStyleCode(x,"left")))
            # two pages.
            # if do it at once, then we will have no issue.
            # let the computer create its code later.
            if chartDetect(g12[0]) and (not chartDetect(g12[1])):
                return g12[1]
            elif chartDetect(g12[1]) and (not chartDetect(g12[0])):
                return g12[0]
            else:
                return []
        else:
            return []

def fullCapital(a):
    python=list(map((lambda x: chr(x)),list(range(ord("A"),1+ord("Z")))))
    l=[int(r in python) for r in list(".".join(re.findall("r'\w*",a)))]
    return sum(l)==len(l)

# def proc(x):
#     x0,x1,x2="=",[],[]
#     # first get the name for god sake.
#     # consider the break as end of capital, initial marks. group these things as sentences.
#     for y in x:
#         y0=
#         # get the mode? previous sentence mode?
#         if

def getName(a):
    # if not the first
    if not fullCapital(a[0].text):
        return [[a[0]],a[1:]]
    elif fullCapital(a[1].text):
        return [[a[0]],a[1:]]
    else:
        g=getName(a[1:])
        return [[*g[0],a[0]],g[1]]

def loveIsGone(a,a0):
    g,g0=False,[]
    for x in a:
        if not g:
            g=a0(x)
            if g:
                g0.append(x)
        else:
            g0.append(x)
    return g0

def HeadDetect(a):
    a0=list(a('span'))
    if len(a0)==1:
        if a0[0].text[0]=="=":
            return True
        else:
            return False
    else:
        f=a[0].text
        f0="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        if len(f)==1 and f not in f0+f0.lower()+"0123456789 ":
            return True
        else:
            return False

def scanIndex(a):
    return [HeadDetect(x) for x in a]

def processMe(a):
    p,p0,p1=scanIndex(a),[],[]
    for x in range(len(p)):
        if p[x]:
            if p0!=[]:
                p1.append(p0)
            p0=[a[x]]
        else:
            p0.append(a[x])
    p1.append(p0)
    return p1

# number of span.
g=getCode(0)
g0=getElimination(0)
b=BeautifulSoup(g,features="lxml")
# get
# print(g0)
g1=getRange(g0[1])
# print(g1)
g2=b("div")[1:]
fn=[]
for x in range(len(g2)):
    g3=g2[x]("p")
    fn+=getLine(g3)
# print(fn)
fx=maxSplit(splitMe(fn,checkBold),checkAnother)
rk=fx[1][4] # get to know this shit.
# reorder this thing.
g0=loveIsGone(rk,(lambda x: len(x.text)>1))
# print(g0)
g1=remedyGroup(g0,(lambda x:len(x('span'))>1))
# the name is in the first group.
g2=getName(g1[0])
g3=processMe(g2[1])
# print(g2[0][0].text)
# has translation.
# print(g3)
# print(g1)
# with prefix, FULL CAPITAL, with equal sign?
# shall be processed separatedly.
    # print(len(fx))
# print(g15)
# print(g12[0])
# print(g12)
# the satisfactory mechanism is not loaded yet. and thus we shall delay developing it.
# print(g10)
# g10=list(sorted(list(set(list(map((lambda y:int(styleMap(list(map((lambda x: x.split(":")),list(filter((lambda x: len(x)>0),y.attrs["style"].split(";"))))))["left"][:-2])),g4))))))
# print(g10)
# A FINITE WORKFLOW.
# SORT AND GROUP AT THE SAME TIME.
# extract those top things?
# print(list(sorted(list(g4),key=(lambda y:float(styleMap(list(map((lambda x: x.split(":")),list(filter((lambda x: len(x)>0),y.attrs["style"].split(";"))))))["top"][:-2])))))
# get the content that shall be filtered out.
# f=getBold(g4)
# rework on the thing.
# g5=list(filter((lambda y: float(styleMap(list(map((lambda x: x.split(":")),list(filter((lambda x: len(x)>0),y.attrs["style"].split(";"))))))["top"]),list(g4))))
# get content out.
# print(chartDetect(g3),chartDetect(g4))

# any partial charts? there must be something unknown.
# randomly group things together?
# check if any font is greater than 15.

        # print(styleMap(list(map((lambda x: x.split(":")),s1.attrs["style"].split(";")))))
    # multiple span warning.
    # print(g4('span')[0])
    # print(styleMap(list(map((lambda x: x.split(":")),g4.attrs["style"].split(";")))))
# print("--------------------------------")
# for g4 in g3:
#     print(g4)
# how to tell?
# print(len(g2))