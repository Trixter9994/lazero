import sys as os # fuck.
import copy
g="0123456789ABCDEF"
g0=['\ue230', '\ue231', '\ue232', '\ue233', '\ue234', '\ue235', '\ue236', '\ue237', '\ue238', '\ue239', '\ue241', '\ue242', '\ue243', '\ue244', '\ue245', '\ue246']
def openShit(a):
    with open(""+a,"r") as f:
        return f.read()
def writeShit(a,b):
    with open(""+a[:3]+"_again.txt","w+") as f:
        f.write(b)
def getShit(a):
    a0=copy.copy(a)
    for g1 in g0:
        a0=a0.replace(g1,g[g0.index(g1)])
    return a0
o=os.argv[1]
o0=openShit(o)
o1=writeShit(o,getShit(o0))
# the trust is important.