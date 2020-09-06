import pickle
from lolita import fury
"""papi=""
with open("scavenger.pickle","rb") as _file:
    papi=pickle.load(_file)
    print (papi)
#fuck
papi0=""
with open("scavenger0.pickle","rb") as _file:
    papi0=pickle.load(_file)
    print (papi0)
"""

pap=""
with open("scavenger1.pickle","rb") as _file:
    pap=pickle.load(_file)
    print (pap)

joker=(lambda nope0:nope0[:-1] if nope0[-1]=="\n" else nope0)
joke=(lambda nope0: list(filter((lambda x:x!=""),nope0)))

nope=""
with open("core.log","r") as tits:
    nope=tits.read()

with open(joker(nope)+"alphabets.txt","r") as dickhead:
    shit=dickhead.read().split("\n")
    shit0=joker(joke(shit))
    fuckme=[]
    for m in range(len(pap)):
        fuckme.append([])
    for r,k in enumerate(shit0):
        for r0,k0 in enumerate(pap):
            for r1,k1 in enumerate(k0):
                redis=fury(k1,k)
                if redis==True:
                    fuckme[r0].append([r,r1])
                else:
                    pass
    print(fuckme)
#    print(shit0)
