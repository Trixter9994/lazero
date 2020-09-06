from bs4 import BeautifulSoup
from simpleStorage import storeAList
def soup(a):
    return BeautifulSoup(a)

def openShit(b):
    f=""
    with open(b,"r") as fuck:
        f=fuck.read()
    return f

#def openList(b):
#    return list(filter((lambda x:x!=""),openShit(b).split("\n")))

def shit(x):
    return [a["href"] for a in soup(openShit(x)).find_all(name="a",attrs={"itemprop":"name codeRepository"},recursive=True)]
# fuck you.

#d=[list(filter((lambda x:x!=[]),[shit(c) for c in b])) for b in [openList(a) for a in openList("trauma.log")]]
d=[shit(x) for x in [str(b)+"_.log" for b in range(6)]]
print(d)
storeAList(d)
#e=[[shit(c) for c ]]
#print(len(d))
