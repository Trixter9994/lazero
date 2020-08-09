# get the range with packages.
# import unicodeblocks
# this is the semantic unicode project. Crucial for today's understanding.
# unicode_charnames.
# how the heck can we do that?
from iterme import getFucked
def openShit(a):
    with open("layout_improved/"+a,"r") as f:
        return f.read().split("\n")
# really? today's different?
def checker(a):
    return "Copyright © 1991-2019 Unicode, Inc. All rights reserved." in a
def rollOver(a,b):
    a0,b0=[],[]
    for a1 in a:
        if b(a1):
            if b0!=[]:
                a0.append(b0)
            b0=[]
        else:
            b0.append(a1)
    if b0!=[]:
        a0.append(b0)
    return a0
def slicer(a,x):
    f=[]
    for a0 in a:
        try:
            f.append(a0[x])
        except IndexError:
            f.append(None)
    return f
def sliceX(a,x):
    f=[]
    for a0 in a:
        try:
            f.append(a0[x[0]:x[1]])
        except IndexError:
            f.append(None)
    return f
# def getAfter(a,b)
s=rollOver(openShit("U0B80.txt"),checker)
s0=s[1]
# print(s0)
s1=getFucked(s0)
for x in s1:
    print(x) # how to get shit?
    # I mean those txt files? get a piece of shit first.
# shall there be the character?
# number 2 has the chart.
# for s0 in s:
#     # print(s0)
#     print(slicer(s0,4))