from getFromPickleR import returnListF
# we need a verifier and sql injector.
# first, remove nonprelude elements.
import sqlite3
# test transferring tags and prelude.
from bs4 import BeautifulSoup
# import re
import transformer
import copy
import re
import numpy as np
import niche
import matrixPro

def eatShit(a):
    return (a if a[-1]!="\n" else a[:-1])

def constructMe(a):
    return "".join(["["+str(x)+"]" for x in a])

def getMe(a):
    # number of <> are they even? are they >=4?
    # print(a)
    a1=a[1:].split(" ")[0]
    return BeautifulSoup(a,features="lxml")(a1)[0]

def getTest(a):
    a0,a1=a.count("<"),a.count(">")
    if a0>1:
        if a0==a1:
            if (a0//2)*2==a0:
                return True
    return False

def checkHealth(a):
    if type(a) is str:
        return getTest(a)
    return False

def getReady(a):
    csdn=copy.copy(a)
    # a is the shallow copy.
    # shall we dance?
    b=list(filter((lambda x:checkHealth(transformer.extractor(csdn,x))),transformer.baseIV(a)))
    # use the eval function.
    # fuck.
    for c in b:
        # time to hack.
        # next time use exec() instead of eval().
        d="csdn"+constructMe(c)
        exec(d+"=getMe("+d+")")
    return csdn

def CH(a):
    return [a, type(a)]

def nothing(a):
    csdn=copy.copy(a)
    return list(map((lambda x:CH(transformer.extractor(csdn,x))),transformer.baseIV(a)))

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

def hexTest(a):
    try:
        b=int("0x"+a,0)
        return True
    except:
        return False

def realTest(a):
    a0,a1="0123456789","abcdefghijklmnopqrstuvwxyz"
    a2=a1.upper()
    for x in a0+a1+a2:
        if x in a:
            return True
    return False

r=returnListF(247)
r0=getReady(r)
print(r0) # structure is maintained. WE SHALL GET THE TITLE SOMEHOW.
# remove the traliing newline sign. \r\n?
# so what the hell am i doing? am i just fucking around?
# Now just every fucking thing has fucking name now.
r1=list(map((lambda x:eatShit(x)),r0[0]))
r2,r3=list(filter((lambda x: realTest(x)),re.findall(r'\w*',r1[0]))),getRange(r1[1]) # make the range out.
print(r2,r3)
r4=" ".join(r2) # we need to search for nonstandard blank characters.
# get all type of notices.
# how the heck can we have the name out?
# in fact, the biggest problem of code refacturing is the codec.
# fucking blank spaces will ruin the whole shit.
# i am sorry but this just will not work.