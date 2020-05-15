import re
import os
def openfinder(a):
    with open(a,"r") as f:
        return re.findall(r'[a-zA-Z0-9\-\_]+',str(f.read()))

def getList():
    return os.listdir(".")

def getPy(a):
    return list(filter(lambda x:x[-3:]==".py",list(filter(lambda x:len(x)>3,(a)))))

def pyList(a):
    return {x:openfinder(x) for x in a}

def findBase(a,b):
    return [x for x in a if x in b]

def findCommon(a):
    b=list(a.keys())
    c={b[x]:b[x+1:] for x in range(len(b)-1)}
    d={x:{y:findBase(a[x],a[y]) for y in c[x]} for x in c.keys()}
    return d

def findRelational(a):
    b={x:{y:a[x][y] for y in a[x].keys() if len(a[x][y])>0} for x in a.keys()}
    c={(x,y):a[x][y] for x in a.keys() for y in a[x].keys()}
    return c

g=getList()
e=getPy(g)
p=pyList(e)
f=findCommon(p)
r=findRelational(f)
print(r)
