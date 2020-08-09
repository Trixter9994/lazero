from bs4 import BeautifulSoup
from simpleStorage import storeList
def soup(a):
    return BeautifulSoup(a)

def openShit(b):
    f=""
    with open(b,"r") as fuck:
        f=fuck.read()
    return f

def openList(b):
    return list(filter((lambda x:x!=""),openShit(b).split("\n")))

def shit(x):
    return list(map((lambda x:x[1:]),(list(filter((lambda x: x[1:3]=="op" and "?" not in x),[a["href"] for a in soup(openShit(x)).find_all(name="a",attrs={"class":"d-inline-block"},recursive=True)])))))
# fuck you.

#d=[list(filter((lambda x:x!=[]),[shit(c) for c in b])) for b in [openList(a) for a in openList("trauma.log")]]
# this is not the worst part.
fuckYou=(lambda x:[y for z in x for y in z])
d=[shit(x) for x in openList("glossary.log")]
#print(d)
storeList(list(set(fuckYou(d))))
#e=[[shit(c) for c ]]
#print(len(d))
