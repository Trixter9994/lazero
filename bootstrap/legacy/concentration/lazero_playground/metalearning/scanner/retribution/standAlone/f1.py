def openIndex(a):
    r=None
    with open("index.log","r") as f:
        r=list(filter((lambda x:len(x)>1),f.read().split("\n")))
    return r[a]

def checkMax(a,b=1,c=0):
    m=int(b+c)
    try:
        a(m)
        return checkMax(a,int(b*2),int(c))
    except:
        if int(b)!=1:
            return checkMax(a,1,int(b/2+c))
        else:
            return int(c)
        # indicate the last avaliable value.

def checkMe():
    return checkMax(openIndex)

def getCode(a):
    p=(lambda x: "/".join(["../../../../multilingual/rockstar/unicode-standard/retribution/toJerk",x,x+".html"]))
    s,s0=p(openIndex(a)),None
    with open(s,"r") as f:
        s0=f.read() # raw data.
    return s0

def getElimination(a):
    p=(lambda x: "/".join(["../../../../multilingual/rockstar/unicode-standard/retribution/",x+".txt"]))
    s,s0=p(openIndex(a)),[]
    with open(s,"r") as f:
        s0.append(f.readline())
        s0.append(f.readline()) # first two lines? only in a group.
    return s0
# remember we are training our left hand, not training nothing out of nothing.
# alpnazero is just trained out of alphago, not nothing out of nothing.
# so use every fucking intelligence that you have to build this evil shit.